import streamlit as st
import plotly.express as px
from data.trade_programs import TRADE_PROGRAMS

st.set_page_config(page_title="Trade Programs", page_icon="🎓")

def render_trade_programs():
    st.title("Trade Programs Directory")
    st.markdown("""
    Explore detailed information about various trade programs, including duration, 
    costs, and career prospects.
    """)

    # Program Selection
    selected_trade = st.selectbox(
        "Select a Trade Program",
        options=list(TRADE_PROGRAMS.keys())
    )

    # Display program details
    if selected_trade:
        program = TRADE_PROGRAMS[selected_trade]
        
        # Program Overview
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Program Overview")
            st.markdown(f"""
            **Description:** {program['description']}
            
            **Duration:** {program['duration']}
            
            **Average Salary:** ${program['avg_salary']:,}
            
            **Industry Growth:** {program['demand_growth']}
            
            **Certification:** {program['certification']}
            """)
            
        with col2:
            # Create salary comparison chart
            fig = px.bar(
                x=['National Average', f'{selected_trade} Average'],
                y=[45000, program['avg_salary']],
                title="Salary Comparison"
            )
            st.plotly_chart(fig)

        # Available Programs
        st.subheader("Available Training Programs")
        for prog in program['programs']:
            with st.expander(f"{prog['name']} - {prog['duration']}"):
                st.markdown(f"""
                * **Duration:** {prog['duration']}
                * **Cost:** ${prog['cost']:,}
                * **Format:** Full-time, hands-on training
                """)
                
                if st.button("Calculate ROI", key=f"roi_{prog['name']}"):
                    st.switch_page("pages/3_calculators.py")

        # Facility Images
        st.subheader("Training Facilities")
        facility_col1, facility_col2 = st.columns(2)
        with facility_col1:
            st.image("https://images.unsplash.com/photo-1664382953518-4a664ab8a8c9",
                     caption="Modern Training Equipment")
        with facility_col2:
            st.image("https://images.unsplash.com/photo-1664382951771-40432ecc81bd",
                     caption="Hands-on Learning Environment")

if __name__ == "__main__":
    render_trade_programs()
