import streamlit as st
from google import genai

# Set page config
st.set_page_config(page_title="Personalized Diet & Workout Planner", layout="wide")

# Initialize client
import os
api_key = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("❌ GOOGLE_API_KEY not configured. Please add it to Streamlit Secrets or environment variables.")
    st.stop()
client = genai.Client(api_key=api_key)
model_name = "models/gemini-2.5-pro"

# Custom function
def generate_recommendations(dietary_preferences, fitness_goals, lifestyle_factors, diet_restrictions, health_conditions, user_query):
    prompt = f"""
    can you provide personalized diet and workout recommendations based on the following information?
    for this user:
- Dietary Preferences: {dietary_preferences}
- Fitness Goals: {fitness_goals}
- Lifestyle Factors: {lifestyle_factors}
- Diet Restrictions: {diet_restrictions}
- Health Conditions: {health_conditions}
- User Query: {user_query}

based on the above user's dietary preferences, fitness goals, lifestyle factors, diet restrictions, health conditions, and user query, please provide personalized diet and workout recommendations that are tailored to the user's needs and goals.
    Diet Recommendations:RETURN LIST
    5 specific diet recommendations that align with the user's dietary preferences, fitness goals, lifestyle factors, diet restrictions, and health conditions. Each recommendation should include a brief description of the diet plan, its benefits, and how it can help the user achieve their fitness goals.

    workout Recommendations:RETURN LIST
    5 specific workout recommendations that align with the user's dietary preferences, fitness goals, lifestyle factors, diet restrictions, and health conditions. Each recommendation should include a brief description of the workout routine, its benefits, and how it can help the user achieve their fitness goals.
     
    Meal Plan:RETURN LIST
    5 breakfast ideas.

    5 dinner options

    Additional Tips:RETURN LIST
    5 additional tips for maintaining a healthy lifestyle and achieving fitness goals, considering the user's dietary
     """
    response = client.models.generate_content(
        model=model_name,
        contents=prompt
    )
    return response.text

# Title and description
st.title("🏋️ Personalized Diet & Workout Planner")
st.markdown("Get personalized recommendations based on your fitness goals and health conditions")

# Create form
with st.form("recommendation_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        dietary_preferences = st.text_input("Dietary Preferences", placeholder="e.g., vegetarian, keto")
        fitness_goals = st.text_input("Fitness Goals", placeholder="e.g., weight loss, muscle gain")
        lifestyle_factors = st.text_input("Lifestyle Factors", placeholder="e.g., sedentary, active")
    
    with col2:
        diet_restrictions = st.text_input("Diet Restrictions", placeholder="e.g., gluten-free, dairy-free")
        health_conditions = st.text_input("Health Conditions", placeholder="e.g., diabetes, heart disease")
    
    user_query = st.text_area("Your Query", placeholder="Ask your question here...", height=120)
    
    submitted = st.form_submit_button("Get Recommendations", use_container_width=True)

# Process form submission
if submitted:
    if not all([dietary_preferences, fitness_goals, lifestyle_factors, diet_restrictions, health_conditions, user_query]):
        st.error("Please fill in all fields")
    else:
        with st.spinner("🤖 Generating personalized recommendations..."):
            try:
                recommendations_text = generate_recommendations(
                    dietary_preferences, fitness_goals, lifestyle_factors, 
                    diet_restrictions, health_conditions, user_query
                )
                
                # Parse recommendations
                recommendations = {
                    "diet_types": [],
                    "workouts": [],
                    "breakfast": [],
                    "dinner": [],
                    "additional_tips": []
                }
                
                current_section = None
                for line in recommendations_text.splitlines():
                    if "Diet Recommendations:" in line:
                        current_section = 'diet_types'
                    elif "Workout Recommendations:" in line:
                        current_section = 'workouts'
                    elif "Meal Plan:" in line:
                        current_section = 'breakfast'
                    elif "dinner options" in line:
                        current_section = 'dinner'
                    elif "Additional Tips:" in line:
                        current_section = 'additional_tips'
                    elif line.strip() and current_section:
                        recommendations[current_section].append(line.strip())
                
                # Display results
                st.success("✅ Recommendations generated!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("🥗 Diet Recommendations")
                    for i, diet in enumerate(recommendations['diet_types'], 1):
                        st.write(f"**{i}. {diet}**")
                    
                    st.subheader("🍳 Breakfast Ideas")
                    for i, breakfast in enumerate(recommendations['breakfast'], 1):
                        st.write(f"**{i}. {breakfast}**")
                
                with col2:
                    st.subheader("💪 Workout Recommendations")
                    for i, workout in enumerate(recommendations['workouts'], 1):
                        st.write(f"**{i}. {workout}**")
                    
                    st.subheader("🍽️ Dinner Options")
                    for i, dinner in enumerate(recommendations['dinner'], 1):
                        st.write(f"**{i}. {dinner}**")
                
                st.subheader("💡 Additional Tips")
                for i, tip in enumerate(recommendations['additional_tips'], 1):
                    st.write(f"**{i}. {tip}**")
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
