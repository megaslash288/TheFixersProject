import streamlit as st
from data.trade_programs import TRADE_PROGRAMS
import plotly.express as px
import BLS_Import

st.set_page_config(
    page_title="Trade Career Explorer",
    page_icon="🛠️",
    layout="wide"
)

def main():
    st.title("Trade Career Explorer 🛠️")
    
    # Hero section with image
    st.image("https://images.unsplash.com/photo-1454165804606-c3d57bc86b40", 
             caption="Explore Your Future in Skilled Trades")

    st.markdown("""
    ## Discover Your Path in Skilled Trades
    Explore rewarding career opportunities in the trades industry. Find the perfect 
    match for your skills and interests while learning about excellent earning potential 
    and job security.
    """)

    # Quick Stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Average Starting Salary", "$45,000")
    with col2:
        st.metric("Job Growth", "12%")
    with col3:
        st.metric("Programs Available", len(TRADE_PROGRAMS))

    # Featured Trades
    st.subheader("Featured Trade Programs")
    
    # Create three columns for featured trades
    cols = st.columns(3)
    
    for idx, (trade, details) in enumerate(list(TRADE_PROGRAMS.items())[:3]):
        with cols[idx]:
            st.markdown(f"### {trade}")
            st.markdown(f"**Average Salary:** ${details['avg_salary']:,}")
            #st.markdown(f"**Growth Rate:** {details['demand_growth']}")
            st.markdown(f"**Duration:** {details['duration']}")
            st.button(f"Learn More About {trade}", key=f"learn_more_{trade}")

    # Career Exploration Tools Section
    st.header("Career Exploration Tools")
    tool_col1, tool_col2 = st.columns(2)
    
    with tool_col1:
        st.markdown("### Career Assessment")
        st.markdown("Discover which trade aligns with your interests and skills.")
        if st.button("Take Assessment"):
            st.switch_page("pages/1_career_assessment.py")
            
    with tool_col2:
        st.markdown("### ROI Calculator")
        st.markdown("Compare the costs and benefits of different education paths.")
        if st.button("Calculate ROI"):
            st.switch_page("pages/3_calculators.py")

    # Success Stories Preview
    st.header("Success Stories")
    st.image("https://images.unsplash.com/photo-1617575521317-d2974f3b56d2",
             caption="Real Stories from Trade Professionals")
    if st.button("View All Success Stories"):
        st.switch_page("pages/4_success_stories.py")
    
    #generatecsv
   # BLS_Import.CreateCSV()

if __name__ == "__main__":
    main()
