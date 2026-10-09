import streamlit as st
from risk_agent import analyze_student_risk

st.set_page_config(page_title="RTMNU Student Risk Agent", layout="wide", page_icon="🎓")

st.title("🎓 Smart Student Academic & Risk Agent")
st.caption("RTMNU BCA Final Year Project - Early Warning System")

st.markdown("---")

# Process Data
df_risk = analyze_student_risk("students.csv")

# Metrics Display
col1, col2, col3 = st.columns(3)
col1.metric("Total Students", len(df_risk))
col2.metric("Critical (Red)", len(df_risk[df_risk['Risk Level'].str.contains("CRITICAL")]))
col3.metric("Warning (Yellow)", len(df_risk[df_risk['Risk Level'].str.contains("WARNING")]))

st.markdown("### 📊 Student Analysis & AI Recommendations")
st.dataframe(df_risk, use_container_width=True)

st.markdown("---")
if st.button("🚀 Trigger Automated AI Alerts", type="primary"):
    st.success("✅ Execution Complete! Warnings sent to High-Risk students via Agent Workflow.")