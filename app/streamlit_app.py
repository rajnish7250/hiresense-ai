#streamlit_app.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from controllers.resume_controller import ResumeController

st.set_page_config(page_title="HireSense AI", layout="wide")

controller = ResumeController()

st.title("HireSense AI")
st.subheader("AI-Powered Resume Analyzer")

col1, col2 = st.columns(2)

with col1:
    resume = st.text_area("📄 Paste Resume", height=300)

with col2:
    jd = st.text_area("💼 Paste Job Description", height=300)

if st.button("🚀 Analyze Resume"):

    result = controller.analyze_resume(resume, jd)

    if result.get("status") == "error":
        st.error(result.get("message"))

    else:
        # Score Section
        st.metric("Match Score", f"{result['match_score']}%")
        st.write(f"**Confidence:** {result['confidence']}")

        # Keywords Section
        col3, col4 = st.columns(2)

        with col3:
            st.subheader("✅ Matched Skills")
            st.write(result["matched_keywords"])

        with col4:
            st.subheader("❌ Missing Skills")
            st.write(result["missing_keywords"])

        # Feedback
        st.subheader("🧠 AI Feedback")
        st.text(result["llm_feedback"])
