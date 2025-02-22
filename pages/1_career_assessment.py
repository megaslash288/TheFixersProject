import streamlit as st
import plotly.express as px
from utils.assessment import ASSESSMENT_QUESTIONS, calculate_trade_match

st.set_page_config(page_title="Career Assessment", page_icon="📋")

def render_assessment():
    st.title("Trade Career Assessment")
    st.markdown("""
    Discover which trade career path might be the best fit for you. Answer these 
    questions honestly to get personalized recommendations.
    """)

    if "assessment_complete" not in st.session_state:
        st.session_state.assessment_complete = False

    answers = {}
    
    # Display questions
    for question in ASSESSMENT_QUESTIONS:
        answers[question["id"]] = st.slider(
            question["question"],
            min_value=question["min"],
            max_value=question["max"],
            value=3,
            help="Slide to rate from 1 (lowest) to 5 (highest)"
        )

    if st.button("Calculate Results"):
        results = calculate_trade_match(answers)
        st.session_state.assessment_results = results
        st.session_state.assessment_complete = True

    if st.session_state.assessment_complete:
        st.header("Your Results")
        
        # Create bar chart of results
        results_df = px.bar(
            x=list(st.session_state.assessment_results.keys()),
            y=list(st.session_state.assessment_results.values()),
            title="Trade Career Match Scores"
        )
        results_df.update_layout(
            xaxis_title="Trade",
            yaxis_title="Match Score (%)"
        )
        st.plotly_chart(results_df)

        # Display recommendations
        st.subheader("Recommended Next Steps")
        top_trade = max(st.session_state.assessment_results.items(), key=lambda x: x[1])[0]
        st.markdown(f"""
        Based on your responses, you show a strong aptitude for **{top_trade}**. 
        Here are your next steps:
        
        1. Explore the {top_trade} program details in our Trade Programs directory
        2. Calculate potential ROI for this career path
        3. Read success stories from professionals in this field
        """)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Explore Trade Programs"):
                st.switch_page("pages/2_trade_programs.py")
        with col2:
            if st.button("Calculate ROI"):
                st.switch_page("pages/3_calculators.py")

if __name__ == "__main__":
    render_assessment()
