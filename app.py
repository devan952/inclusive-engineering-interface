import streamlit as st
import io
import urllib.parse
from gtts import gTTS

st.set_page_config(
    page_title="Inclusive Engineering Interface",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Inclusive Engineering Interface")

st.subheader(
    "Smart, Safe and Multilingual Machine Assistance"
)

st.write(
    "A user-friendly interface that helps machine "
    "operators understand instructions and safety alerts."
)

st.divider()

# Language selection
language = st.selectbox(
    "🌐 Select Your Language",
    ["English", "தமிழ்", "हिन्दी"]
)

if language == "தமிழ்":
    st.header("வணக்கம்! வரவேற்கிறோம் 👋")
    st.write("இயந்திர வழிகாட்டி இணையதளத்திற்கு வரவேற்கிறோம்.")
    instruction_title = "இயந்திர வழிமுறைகள்"
    button_text = "வழிமுறைகளைப் பார்க்க"
else:
    st.header("Welcome, Machine Operator! 👋")
    st.write("Your smart machine assistance dashboard.")
    instruction_title = "Machine Instructions"
    button_text = "View Instructions"

st.divider()

# Dashboard
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Machine Status", "Ready")

with col2:
    st.metric("Safety Alerts", "0")

with col3:
    st.metric("Assistance", "Available")

st.divider()

st.subheader(f"📋 {instruction_title}")

machine = st.selectbox(
    "Choose a machine",
    ["Machine A", "Machine B", "Machine C"]
)

if st.button(button_text, use_container_width=True):
    st.info(f"Selected: {machine}")
    st.write("1. Check the machine before use.")
    st.write("2. Follow the approved safety instructions.")
    st.write("3. If an error occurs, stop and inform the supervisor.")

st.divider()

import io
from gtts import gTTS

st.subheader("🎙️ Voice Assistance")

if language == "தமிழ்":
    voice_text = "இயந்திரத்தை இயக்கும் முன் பாதுகாப்பு வழிமுறைகளை சரிபார்க்கவும்."
    voice_language = "ta"
else:
    voice_text = "Please check the safety instructions before operating the machine."
    voice_language = "en"

st.write(voice_text)

if st.button("🔊 Listen to Instructions"):
    try:
        audio = io.BytesIO()

        speech = gTTS(
            text=voice_text,
            lang=voice_language
        )

        speech.write_to_fp(audio)

        st.audio(audio.getvalue(), format="audio/mp3")

    except Exception as e:
        st.error(f"Voice error: {e}")
        # Machine Safety Alerts
st.header("🚨 Machine Safety Alerts")

machine_condition = st.selectbox(
    "Select Machine Condition",
    [
        "Normal Operation",
        "High Temperature",
        "Excessive Vibration",
        "Emergency Stop Required"
    ]
)

alert_language = st.selectbox(
    "Select Alert Language",
    ["English", "தமிழ்"]
)

if machine_condition == "Normal Operation":
    risk_level = "Low"
    alert_en = "Machine is operating normally."
    alert_ta = "இயந்திரம் இயல்பாக செயல்படுகிறது."

elif machine_condition == "High Temperature":
    risk_level = "High"
    alert_en = "Warning! High machine temperature. Stop and inspect safely."
    alert_ta = "எச்சரிக்கை! இயந்திரத்தின் வெப்பநிலை அதிகமாக உள்ளது. பாதுகாப்பாக நிறுத்தி பரிசோதிக்கவும்."

elif machine_condition == "Excessive Vibration":
    risk_level = "Medium"
    alert_en = "Warning! Excessive vibration detected. Inspect the machine safely."
    alert_ta = "எச்சரிக்கை! இயந்திரத்தில் அதிக அதிர்வு உள்ளது. பாதுகாப்பாக பரிசோதிக்கவும்."

else:
    risk_level = "High"
    alert_en = "Emergency! Follow the approved emergency shutdown procedure."
    alert_ta = "அவசரம்! அங்கீகரிக்கப்பட்ட அவசர நிறுத்த நடைமுறையைப் பின்பற்றவும்."

if risk_level == "Low":
    st.success("Risk Level: LOW")
elif risk_level == "Medium":
    st.warning("Risk Level: MEDIUM")
else:
    st.error("Risk Level: HIGH")

if alert_language == "தமிழ்":
    alert_message = alert_ta
else:
    alert_message = alert_en

st.write("*Safety Alert:*", alert_message)

if st.button("🔊 Listen to Safety Alert"):
    try:
        from gtts import gTTS
        import io

        lang_code = "ta" if alert_language == "தமிழ்" else "en"
        audio_buffer = io.BytesIO()

        tts = gTTS(text=alert_message, lang=lang_code)
        tts.write_to_fp(audio_buffer)

        audio_buffer.seek(0)
        st.audio(audio_buffer.getvalue(), format="audio/mp3")

    except Exception as e:
        st.error(f"Voice error: {e}")