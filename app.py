import streamlit as st
import requests

# -----------------------------
# Streamlit Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="centered"
)

st.title("✈️ AI Travel Planner")
st.write("Generate a personalized travel itinerary using AI.")

# -----------------------------
# User Inputs
# -----------------------------
with st.sidebar:
    st.header("Travel Details")
    hf_token = st.text_input(
        "Enter your Hugging Face API Token",
        type="password"
    )
    destination = st.text_input("Destination")
    days = st.number_input(
        "Number of Days",
        min_value=1,max_value=30,
        value=3 
    )
    budget = st.selectbox(
        "Budget",
        ["Low", "Medium", "High"]
    )
    interests = st.multiselect(
        "Interests",
    [
        "Adventure",
        "Nature",
        "Historical Places",
        "Food",
        "Shopping",
        "Nightlife",
        "Culture",
        "Photography"
    ]
)

# -----------------------------
# Generate Travel Plan
# -----------------------------
if st.button("Generate Travel Plan"):

    if not hf_token:
        st.warning("Please enter your Hugging Face API Token.")
        st.stop()

    if not destination:
        st.warning("Please enter a destination.")
        st.stop()

    interest_text = ", ".join(interests) if interests else "General Tourism"

    prompt = f"""
Create a detailed {days}-day travel itinerary for {destination}.

Budget: {budget}

Interests: {interest_text}

Include:

1. Day-wise itinerary
2. Morning, Afternoon and Evening activities
3. Famous tourist attractions
4. Recommended local foods
5. Estimated daily expenses
6. Transportation suggestions
7. Travel tips
8. Total estimated budget

Format the response using Markdown headings and bullet points.
"""

    API_URL = "https://router.huggingface.co/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {hf_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "google/gemma-3-4b-it",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 1200,
        "temperature": 0.7
    }

    with st.spinner("Generating your travel itinerary..."):
        try:
            response = requests.post(
                API_URL,
                headers=headers,
                json=payload,
                timeout=120
            )

            if response.status_code == 200:
                result = response.json()
                plan = result["choices"][0]["message"]["content"]

                st.success("Travel Plan Generated Successfully!")
                st.subheader(f"{destination} Travel Plan")
                st.markdown(plan)

            else:
                st.error(f"Error {response.status_code}")
                st.code(response.text)

        except requests.exceptions.Timeout:
            st.error("Request timed out. Please try again.")

        except requests.exceptions.ConnectionError:
            st.error("Unable to connect to Hugging Face API.")

        except Exception as e:
            st.error(f"Unexpected Error:\n{e}")