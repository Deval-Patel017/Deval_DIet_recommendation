
import os
import openai
from openai_credentials import OPENAI_API_KEY
openai.api_key = "YOUR_OPENAI_API_KEY"
model_engine = "gpt-3.5-turbo-0125"
client = openai.OpenAI()

# Function to collect user inputs

def collect_user_inputs():
    print("Please provide some information about your lifestyle, eating habits, exercise routine, mental well-being, and any medical conditions you have.")
    try:
        lifestyle = input("Lifestyle: ")
        eating_habits = input("Eating habits: ")
        exercise_routine = input("Exercise routine: ")
        mental_wellbeing = input("Mental well-being: ")
        medical_conditions = input("Medical conditions: ")
        
        # Validate inputs (for example, check if any input is empty)
        if not all([lifestyle, eating_habits, exercise_routine, mental_wellbeing, medical_conditions]):
            raise ValueError("Please provide valid input for all fields.")

    except ValueError as e:
        print(f"Error: {e}")
        return collect_user_inputs()  # Retry input collection if there's an error

    user_inputs={
        "lifestyle": lifestyle,
        "eating_habits": eating_habits,
        "exercise_routine": exercise_routine,
        "mental_wellbeing": mental_wellbeing,
        "medical_conditions": medical_conditions
    }
    return user_inputs

# Function to process user inputs using the GPT-3 model
def process_user_inputs(user_inputs):
    # Use the GPT-3 model to analyze user inputs
    
    user_message = {
        "role": "user",
        "content": f"""Hello, assistant! I'd like to discuss my lifestyle and get some insights into my overall health.

    * My lifestyle is: {user_inputs['lifestyle']}
    * My eating habits are: {user_inputs['eating_habits']}
    * My exercise routine is: {user_inputs['exercise_routine']}
    * My mental well-being is: {user_inputs['mental_wellbeing']}
    * I have the following medical conditions (optional): {user_inputs['medical_conditions']}
    """
    }

    response = client.chat.completions.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "Hi there! I'm happy to help. Based on this information, here's some tips for your health..."},
            user_message,
        ],
        max_tokens=1500,  # Adjust as needed for response length
        n=1,
        stop=None,
        temperature=0.7,  # Adjust temperature for creativity vs. informativeness
    )
    analysis_results = response.choices[0].message.content
    return analysis_results

def generate_recommendations(analysis_results):
    # You can customize this function based on the analysis results
    recommendations = "Here are your personalized diet recommendations based on the analysis:\n"
    recommendations += analysis_results  # You may need to parse and format the analysis results here
    return recommendations

# Function to display recommendations to the user
def display_recommendations(recommendations):
    #print("Here are your personalized diet recommendations:")
    print(recommendations)

# Function to gather user feedback
def gather_feedback():
    feedback = input("Did you find these recommendations helpful? (Yes/No): ").lower()
    if feedback == "yes":
        print("Thank you for your feedback!")
    elif feedback == "no":
        print("We're sorry to hear that. Please provide more details so we can improve:")
        additional_feedback = input("Additional feedback: ")
        print("Thank you for your feedback. We will use this to improve our recommendations in the future.")

# Main function to orchestrate the entire process
def main():
    user_inputs = collect_user_inputs()
    analysis_results = process_user_inputs(user_inputs)
    recommendations = generate_recommendations(analysis_results)
    print(recommendations)
    display_recommendations(recommendations)
    gather_feedback()

if __name__ == "__main__":
    main()
