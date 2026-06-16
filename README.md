# Personalized Diet & Workout Planner

A web application that provides personalized diet and workout recommendations using Google's Gemini AI. Available in both Flask and Streamlit versions.

## Features

✨ **AI-Powered Recommendations**
- Personalized diet plans based on your preferences and restrictions
- Customized workout routines aligned with your fitness goals
- Meal planning suggestions (breakfast and dinner ideas)
- Health and lifestyle tips

🎯 **Easy to Use**
- Simple, intuitive form interface
- Multiple input options for flexibility
- Interactive modal displays (Flask) or expandable sections (Streamlit)

🚀 **Multiple Deployment Options**
- Local Flask development server
- Streamlit Cloud deployment
- GitHub repository ready for deployment

## Installation

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key (get it from [AI Studio](https://ai.google.dev/))

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/workout_project.git
   cd workout_project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API key**
   - Open `app.py` or `streamlit_app.py`
   - Replace `YOUR_API_KEY` with your Google Gemini API key
   - Or set it as an environment variable: `export GOOGLE_API_KEY=your_key_here`

## Usage

### Option 1: Flask (Web Version)

```bash
python app.py
```

Then open your browser and navigate to:
```
http://127.0.0.1:5001
```

### Option 2: Streamlit (Recommended for Cloud Deployment)

```bash
streamlit run streamlit_app.py
```

Streamlit will open automatically in your browser at `http://localhost:8501`

## Project Structure

```
workout_project/
├── app.py                 # Flask application
├── streamlit_app.py       # Streamlit application
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
├── README.md             # This file
├── templates/
│   └── index.html        # Flask HTML template
├── static/
│   └── style.css         # CSS styling
└── .env                  # Environment variables (not pushed to Git)
```

## Deployment

### Deploy to Streamlit Cloud (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository and file: `streamlit_app.py`
   - Click "Deploy"

3. **Add secrets** (in Streamlit Cloud dashboard)
   - Go to your app settings
   - Add secret: `GOOGLE_API_KEY = your_api_key_here`

### Deploy to Heroku (Flask)

1. **Create Procfile**
   ```
   web: gunicorn app:app
   ```

2. **Push to Heroku**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

## GitHub Setup

### First-time Setup

```bash
# Initialize git repository (if not cloned)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Add Personalized Diet & Workout Planner"

# Add remote repository
git remote add origin https://github.com/yourusername/workout_project.git

# Push to GitHub
git push -u origin main
```

### For future updates

```bash
git add .
git commit -m "Your commit message"
git push
```

## API Key Security

⚠️ **Important**: Never commit your API key to GitHub!

- API keys are already excluded in `.gitignore`
- Use environment variables for local development
- Use Streamlit Secrets for cloud deployment
- Use Heroku Config Vars for Heroku deployment

## Configuration

### Environment Variables

Create a `.env` file (not tracked by Git):

```
GOOGLE_API_KEY=your_api_key_here
```

Load in Python:
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
```

## Troubleshooting

### API Quota Exceeded
- Error: "You exceeded your current quota"
- Solution: Upgrade to a paid Google Cloud plan or wait for daily quota reset

### Model Not Found
- Error: "models/gemini-2.5-pro is not found"
- Solution: Check available models and update the model name in code

### Port Already in Use (Flask)
- Error: "Address already in use"
- Solution: Change port in `app.py`: `app.run(debug=True, port=5002)`

## Technologies Used

- **Backend**: Flask / Streamlit
- **AI**: Google Gemini API
- **Frontend**: HTML, CSS, JavaScript (Flask) / Streamlit UI
- **Database**: None (stateless application)

## Future Enhancements

- [ ] User authentication
- [ ] Save recommendations history
- [ ] Export recommendations as PDF
- [ ] Mobile app version
- [ ] Support for multiple languages
- [ ] Integration with fitness tracking apps
- [ ] Personalized progress tracking

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Create a GitHub Issue
3. Check [Google Gemini API Documentation](https://ai.google.dev/docs)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Made with ❤️ | Personalized Diet & Workout Planner**
