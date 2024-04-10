# Prompting the user for assessment
print("Please provide some information about your lifestyle, eating habits, exercise routine, mental well-being, and any medical conditions you have.")

# Collecting responses
lifestyle = input("Lifestyle: ")
eating_habits = input("Eating habits: ")
exercise_routine = input("Exercise routine: ")
mental_wellbeing = input("Mental well-being: ")
medical_conditions = input("Medical conditions: ")

# Storing the collected information
user_assessment = {
    "lifestyle": lifestyle,
    "eating_habits": eating_habits,
    "exercise_routine": exercise_routine,
    "mental_wellbeing": mental_wellbeing,
    "medical_conditions": medical_conditions
}

# Printing collected information
print("\nUser Assessment:")
for key, value in user_assessment.items():
    print(f"{key.capitalize()}: {value}")
