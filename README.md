✈️ AI Travel Planner

An AI-powered travel planning application built with Python and Streamlit.
The application generates a personalized day-wise travel itinerary based on the user's destination, trip duration, budget, and interests.

🚀 Features

- 🌍 Enter any travel destination
- 📅 Select the number of travel days
- 💰 Choose a budget level:
  - Low
  - Medium
  - High
- ❤️ Select travel interests such as:
  - Adventure
  - Nature
  - Historical Places
  - Food
  - Shopping
  - Nightlife
  - Culture
  - Photography
- 🤖 Generate a personalized itinerary using AI
- 🍽️ Get recommended local foods
- 🚗 Get transportation suggestions
- 💵 Get estimated daily and total travel expenses
- 💡 Receive useful travel tips
- 📝 Markdown-formatted travel plan

🛠️ Technologies Used

- Python
- Streamlit
- Requests
- Hugging Face Inference API
- Google Gemma 3 4B IT

⚙️ How It Works

1. The user enters a Hugging Face API token.
2. The user provides the destination and number of days.
3. The user selects a budget and travel interests.
4. The application creates an AI prompt using these inputs.
5. The prompt is sent to the Hugging Face Router API.
6. The Google Gemma 3 4B IT model generates the travel itinerary.
7. The generated itinerary is displayed in the Streamlit application.

📋 Generated Travel Plan Includes

The AI-generated travel plan contains:

- Day-wise itinerary
- Morning, afternoon, and evening activities
- Famous tourist attractions
- Recommended local foods
- Estimated daily expenses
- Transportation suggestions
- Travel tips
- Total estimated budget

📁 Project Structure

AI-Travel-Planner/
│
├── app.py
├── README.md
└── requirements.txt

💻 Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Go to the project folder:

cd AI-Travel-Planner

Install the required Python packages:

pip install streamlit requests

▶️ Run the Application

Start the Streamlit application using:

streamlit run app.py

The application will open in your browser.

🔑 Hugging Face API Token

This application requires a Hugging Face API token to generate the AI travel plan.

The token is entered directly into the application's password field and is used to authenticate requests to the Hugging Face API.

Do not upload or commit your API token to GitHub.

📌 Future Improvements

Possible improvements include:

- 🌤️ Real-time weather information
- 🗺️ Interactive maps
- 🏨 Hotel recommendations
- ✈️ Flight information
- 📍 Nearby attractions
- 📄 Export itinerary as PDF
- 💾 Save and download travel plans
- 🔐 Use Streamlit Secrets instead of entering the API token manually

👩‍💻 Author

J Sweety pun sofia

B.Tech – Artificial Intelligence & Data Science
