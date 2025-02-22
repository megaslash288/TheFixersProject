import streamlit as st
import plotly.express as px
from data.career_paths import CAREER_PATHS

st.set_page_config(page_title="Career Pathways", page_icon="📈")

def render_career_pathways():
    st.title("Career Pathways")
    st.markdown("""
    Explore potential career progression paths in different trades. See how your career
    can grow over time with experience and additional certifications.
    """)

    selected_trade = st.selectbox(
        "Select a Trade",
        options=list(CAREER_PATHS.keys())
    )

    if selected_trade:
        path = CAREER_PATHS[selected_trade]
        
        # Create visualization of career progression
        levels = [p["level"] for p in path]
        salary_ranges = [p["salary"].split("-") for p in path]
        min_salaries = [int(r[0]) for r in salary_ranges]
        max_salaries = [int(r[1]) for r in salary_ranges]
        
        # Salary range visualization
        fig = px.line(
            x=levels,
            y=[(min_sal + max_sal) / 2 for min_sal, max_sal in zip(min_salaries, max_salaries)],
            error_y=[max_sal - ((min_sal + max_sal) / 2) for min_sal, max_sal in zip(min_salaries, max_salaries)],
            title=f"Career Progression in {selected_trade}",
            labels={"x": "Career Level", "y": "Salary Range ($)"}
        )
        st.plotly_chart(fig)

        # Detailed progression information
        st.subheader("Career Levels")
        for level in path:
            with st.expander(f"{level['level']} ({level['years']} years)"):
                st.markdown(f"""
                * **Experience Required:** {level['years']} years
                * **Salary Range:** ${level['salary']}
                """)

        # Educational requirements
        st.subheader("Educational Requirements")
        st.markdown(f"""
        ### Path to Success in {selected_trade}:
        1. Complete high school or equivalent
        2. Enroll in a trade school program
        3. Complete apprenticeship
        4. Obtain necessary certifications
        5. Gain experience and advance through levels
        """)

        # Call to Action
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Explore Trade Programs"):
                st.switch_page("pages/2_trade_programs.py")
        
        with col2:
            if st.button("Calculate Your ROI"):
                st.switch_page("pages/3_calculators.py")

if __name__ == "__main__":
    render_career_pathways()
