import streamlit as st
import time
import requests
import json


# Title of the app
st.title("🎉 PCOS Health Check 🎉")
st.markdown("### A quick questionnaire to learn more about your health!")

api_url = "http://fastapi:8000/predict" 

countries = ['Madagascar', 'Vietnam', 'Somalia', 'Malawi', 'France', 'Rwanda', 'Tanzania', 'United States', 'Italy', 'Australia', 'India', 'Argentina', 'Morocco', 'Zambia', 'Romania', 'Sudan', 'Benin', 'Burkina Faso', 'Nepal', 'Mali', 'Malaysia', 'Chile', 'Mozambique', 'Ivory Coast', 'Taiwan', 'Nigeria', 'Zimbabwe', 'Uzbekistan', 'Germany', 'Indonesia', 'Egypt', 'Russia', 'Chad', 'Peru', 'Bangladesh', 'Iraq', 'Canada', 'Cameroon', 'Brazil', 'North Korea', 'Kazakhstan', 'Uganda', 'Guinea', 'Yemen', 'Saudi Arabia', 'South Korea', 'Afghanistan', 'Spain', 'Ghana', 'Guatemala', 'China', 'Japan', 'Pakistan', 'Kenya', 'Ethiopia', 'South Africa', 'Poland', 'Colombia', 'Burundi', 'Venezuela', 'Philippines', 'Ukraine', 'Ecuador', 'Sri Lanka', 'Cambodia', 'Niger', 'Thailand', 'Netherlands', 'Iran', 'Senegal', 'Turkey', 'United Kingdom', 'Syria', 'Algeria', 'Myanmar', 'Angola', 'Mexico']

# Progress bar for engagement
progress_bar = st.progress(0)

# Introduction
st.write("Welcome! Complete this short form to help us understand your health better. Let's start!")

# Form to collect data
with st.form("pcos_form"):
    st.header("Tell Us About Yourself")

    # Combine inputs into grouped sections for brevity
    col1, col2 = st.columns(2)

    # Column 1 inputs
    with col1:
        country = st.selectbox("🌍 Country",options=countries)
        age = st.number_input("🎂 Age", min_value=11, max_value=100, step=1)
        bmi = st.selectbox("⚖️ BMI Category", ["Underweight", "Normal", "Overweight", "Obese"])
        ethnicity = st.selectbox("🌏 Ethnicity", ["Hispanic", "Caucasian", "African", "Asian", "Other"])
        menstrual_regularity = st.selectbox("📅 Menstrual Regularity", ["Regular", "Irregular"])
        acne_severity = st.selectbox("🧴 Acne Severity", ["Mild", "Moderate", "Severe", "NA"])

    # Column 2 inputs
    with col2:
        hirsutism = st.selectbox("🧔 Excessive Hair Growth?", ["Yes", "No"])
        family_history_pcos = st.selectbox("👨‍👩‍👧‍👦 Family History of PCOS?", ["Yes", "No"])
        insulin_resistance = st.selectbox("🍬 Insulin Resistance?", ["Yes", "No"])
        lifestyle_score = st.slider("🏋️‍♀️ Lifestyle Score (1=Unhealthy, 10=Healthy)", 1, 10, 5)
        stress_levels = st.selectbox("😅 Stress Levels", ["Low", "Medium", "High"])
        socioeconomic_status = st.selectbox("💰 Socioeconomic Status", ["Low", "Middle", "High"])

    # Additional questions
    st.subheader("More About You")
    urban_rural = st.selectbox("🏙️ Living Area", ["Urban", "Rural"])
    awareness_pcos = st.selectbox("📚 Aware of PCOS?", ["Yes", "No"])
    fertility_concerns = st.selectbox("👶 Fertility Concerns?", ["Yes", "No"])
    # diagnosis = st.selectbox("🩺 Diagnosed with PCOS?", ["Yes", "No"])

    # Submit button
    submitted = st.form_submit_button("🚀 Submit Your Answers")

    if submitted:
        # Update progress bar
        for i in range(100):
            time.sleep(0.01)  # Simulate processing time
            progress_bar.progress(i + 1)

        # Collect data into a dictionary
        data = {
            "Country": country,
            "Age": age,
            "BMI": bmi,
            "Menstrual_Regularity": menstrual_regularity,
            "Hirsutism": hirsutism,
            "Acne_Severity": acne_severity,
            "Family_History_of_PCOS": family_history_pcos,
            "Insulin_Resistance": insulin_resistance,
            "Lifestyle_Score": lifestyle_score,
            "Stress_Levels": stress_levels,
            "Urban_Rural": urban_rural,
            "Socioeconomic_Status": socioeconomic_status,
            "Awareness_of_PCOS": awareness_pcos,
            "Fertility_Concerns": fertility_concerns,
            "Ethnicity": ethnicity,
            # "Diagnosis": diagnosis,
        }

        # Display results
        st.write("### 🎉 Thank you for completing the questionnaire! 🎉")

        
        try:
            response = requests.post(api_url,data=json.dumps(data),headers={'Content-Type':'application/json'})

            # Check for response status
            if response.status_code == 200:
                st.success("✅ Data successfully sent to the server!")
                server_response = response.json()
                prediction = server_response[0]["result"]
                st.write("### 📊 Analysis:")
                if prediction == "Yes":  # If the API says the person might have PCOS
                    st.error("⚠️ Based on your answers, there's a possibility you might have PCOS.")
                    st.markdown("""
                                    ### 🌟 **You Are Not Alone, and You Are Strong! 🌟**
                                    Finding out that you might have PCOS can feel overwhelming, but remember: **this is just the beginning of a journey to better health and well-being.** Here are some empowering truths to hold onto:

                                    1. **You Are Not Defined by PCOS:**  
                                    PCOS is a condition, not your identity. It’s something you *manage*, not something that defines who you are.

                                    2. **You Have Support:**  
                                    Millions of women worldwide face PCOS, and there’s a vast community of people, healthcare providers, and resources to guide you. You don’t have to navigate this alone.

                                    3. **Your Body Is Resilient:**  
                                    With the right lifestyle changes, medical support, and self-care, many women with PCOS go on to lead healthy, vibrant lives. Small steps—like eating nourishing foods, moving your body, and managing stress—can make a big difference.

                                    4. **You’re Taking the First Step:**  
                                    By seeking answers and completing this questionnaire, you’ve already shown courage and a desire to prioritize your health. That’s a powerful move toward understanding and empowerment.

                                    5. **Hope Is Ahead:**  
                                    Advances in medicine and holistic care mean there are more options than ever to manage PCOS symptoms and improve quality of life. Whether it’s regulating hormones, achieving fertility goals, or simply feeling better day-to-day—you *can* thrive.

                                    ### 💬 **Remember: Progress Over Perfection**  
                                    Take one step at a time. Celebrate small victories, and don’t hesitate to reach out to healthcare professionals or supportive communities for guidance.

                                    You are **strong**, you are **capable**, and you have the power to take control of your health. This isn’t the end of the story—it’s the start of a brighter, healthier chapter. 💖✨
                            """)

                else:  # If the API says the person is unlikely to have PCOS
                    st.success("🎉 Based on your answers, it's unlikely that you have PCOS!")
                    st.balloons()
                    st.markdown("""
                                ### 🌟 **Great News! 🌟**
                                It looks like you don’t show significant signs of PCOS based on this questionnaire. While this is reassuring, it’s always a good idea to maintain regular checkups with your healthcare provider and keep making healthy lifestyle choices.

                                1. **Celebrate Your Health:**  
                                Keep up the good work in taking care of your body and mind.

                                2. **Stay Informed:**  
                                Learning about PCOS and other health conditions is a proactive step towards overall well-being.

                                3. **Support Others:**  
                                If you know someone who might be struggling with PCOS or health challenges, you can share your knowledge and encouragement with them.

                                💬 **Your health is a journey, and you’re doing great! Keep going, stay positive, and know that you’re on the right track.** 💖✨
                    """)
            else:
                st.error(f"🚨 Failed to send data. Server responded with status code: {response.status_code}")
                st.write(response.text)
           
        except Exception as e:
            st.error(f"❌ An error occurred while sending data: {e}")

        st.write("🎈 Your responses have been saved. Thank you! 🎈")
btn = st.button("Reset Form")
if btn:
    st.rerun()       
        
        # Celebration
        
