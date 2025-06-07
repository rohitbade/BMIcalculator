import streamlit as st

# Title of the app
st.title("🧮 BMI Calculator")
st.subheader("Check your Body Mass Index and get health suggestions.")

# Inputs from user
name = st.text_input("Enter your name:")

height_cm = st.number_input("Enter your height (in centimeters):", min_value=50.0, max_value=250.0)
weight_kg = st.number_input("Enter your weight (in kilograms):", min_value=10.0, max_value=300.0)

# Calculate BMI only if valid inputs
if height_cm > 0 and weight_kg > 0:
    height_m = height_cm / 100  # Convert height to meters
    bmi = weight_kg / (height_m ** 2)
    bmi = round(bmi, 2)

    st.success(f"{name}, your BMI is: {bmi}")

    # Give suggestions based on BMI
    if bmi < 18.5:
        st.warning("You are underweight.")
        st.info("🍚 Suggestions:\n- Eat more calories.\n- Include protein-rich foods.\n- Weight training.\n- Consult a dietitian.")
    elif 18.5 <= bmi < 24.9:
        st.success("You are in a healthy weight range. Great job! 💪")
        st.info("🥗 Tips to maintain:\n- Continue balanced diet\n- Regular exercise\n- Stay hydrated")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
        st.info("🏃 Suggestions:\n- Reduce sugar and fried food\n- Increase cardio\n- Track calories\n- Stay active")
    else:
        st.error("You are obese.")
        st.info("⚠️ Strongly Recommended:\n- Seek medical advice\n- Adopt a structured weight loss plan\n- Daily workouts\n- Healthy food habits")

# Optional footer
st.markdown("---")
st.caption("Made with ❤️ by Rohit using Streamlit")

        print("❌ Please enter valid numbers for weight and height.")
