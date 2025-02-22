import streamlit as st
from data.success_stories import SUCCESS_STORIES

st.set_page_config(page_title="Success Stories", page_icon="⭐")

def render_success_stories():
    st.title("Trade Professional Success Stories")
    st.markdown("""
    Read inspiring stories from professionals who have built successful careers in the trades.
    Learn about their journeys, challenges, and achievements.
    """)

    # Filter by trade
    selected_trade = st.selectbox(
        "Filter by Trade",
        options=["All"] + list(set(story["trade"] for story in SUCCESS_STORIES))
    )

    # Display stories
    for story in SUCCESS_STORIES:
        if selected_trade == "All" or selected_trade == story["trade"]:
            with st.container():
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.image(story["image"], width=200)
                
                with col2:
                    st.subheader(story["name"])
                    st.markdown(f"""
                    **Trade:** {story["trade"]}  
                    **Current Role:** {story["current_role"]}  
                    **Years of Experience:** {story["years_experience"]}
                    
                    {story["story"]}
                    """)
                
                st.markdown("---")

    # Call to Action
    st.markdown("""
    ## Start Your Success Story
    
    Ready to begin your journey in the trades? Take our career assessment to find 
    your perfect match.
    """)
    
    if st.button("Take Career Assessment"):
        st.switch_page("pages/1_career_assessment.py")

if __name__ == "__main__":
    render_success_stories()
