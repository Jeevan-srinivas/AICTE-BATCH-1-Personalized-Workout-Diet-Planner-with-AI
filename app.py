from flask import Flask, render_template, request
from google import genai
import os

#setup API key
import os
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set")
client = genai.Client(api_key=api_key)

app= Flask(__name__)

#initialize model
model_name = "models/gemini-2.5-pro"

#custom function
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

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/recommendation", methods=["POST"])
def recommendation():
    if request.method == "POST":
        #collect form data
        dietary_preferences = request.form["dietary_preferences"]
        fitness_goals = request.form["fitness_goals"]
        lifestyle_factors = request.form["lifestyle_factors"]
        diet_restrictions = request.form["diet_restrictions"]
        health_conditions = request.form["health_conditions"]
        user_query = request.form["user_query"]


        #Generate recommendations using the model
        recommendations_text=generate_recommendations(
            dietary_preferences, fitness_goals, lifestyle_factors, diet_restrictions, health_conditions, user_query
            )

        recommendations = {
            "diet_types": [],
            "workouts": [],
            "breakfast": [],
            "dinner": [],
            "additional_tips": []
        }

        print('text:', recommendations_text)

        #split and map responses based on keywords
        current_section = None
        for line in recommendations_text.splitlines():
            if "Diet Recommendations:" in line:
                current_section='diet_types'
            elif "Workout Recommendations:" in line:
                current_section='workouts'
            elif "Meal Plan:" in line:
                current_section='breakfast'
            elif "dinner options" in line:
                current_section='dinner'
            elif "Additional Tips:" in line:
                current_section='additional_tips'
            elif line.strip() and current_section:
                recommendations[current_section].append(line.strip())
        
        print('dict:',recommendations)
        return render_template("index.html", recommendations=recommendations)
    
#python main
if __name__=="__main__":
    app.run(debug=True, port=5001)