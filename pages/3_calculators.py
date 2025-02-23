import streamlit as st
import plotly.express as px
from data.trade_programs import TRADE_PROGRAMS
from utils.calculators import calculate_roi, calculate_education_comparison

st.set_page_config(page_title="Cost & ROI Calculators", page_icon="🧮")

def render_calculators():
    st.title("Education Cost & ROI Calculators")

    tab1, tab2 = st.tabs(["ROI Calculator", "Education Cost Comparison"])

    with tab1:
        st.header("Trade Education ROI Calculator")

        # Input parameters
        selected_trade = st.selectbox(
            "Select Trade Program",
            options=list(TRADE_PROGRAMS.keys())
        )

        tuition_cost = st.number_input(
            "Enter Total Tuition Cost ($)",
            min_value=0,
            value=TRADE_PROGRAMS[selected_trade]["programs"][0]["cost"],
            step=1000
        )

        # Set the current salary to avg_salary of the selected trade
        current_salary = TRADE_PROGRAMS[selected_trade]["avg_salary"]
        st.metric("Current Annual Salary", f"${current_salary:,.2f}")

        years_to_calculate = st.slider(
            "Years to Calculate ROI",
            min_value=1,
            max_value=20,
            value=5
        )

        if st.button("Calculate ROI"):
            
            # Calculate ROI using the correct formula
            roi = calculate_roi(tuition_cost, current_salary, years_to_calculate)

            st.metric("Expected ROI", f"{roi:.1f}%")

            # Create ROI visualization
            years = list(range(years_to_calculate + 1))
            costs = [tuition_cost] + [0] * years_to_calculate
            earnings = [0] + [current_salary] * years_to_calculate
            cumulative_earnings = [sum(earnings[:i + 1]) - tuition_cost for i in range(len(years))]

            fig = px.line(
                x=years,
                y=cumulative_earnings,
                title="Cumulative Return on Investment",
                labels={"x": "Years", "y": "Cumulative Return ($)"}
            )
            st.plotly_chart(fig)

    with tab2:
        st.header("Trade School vs College Comparison")

        # Trade school selection
        selected_trade = st.selectbox(
            "Select Trade Program",
            options=list(TRADE_PROGRAMS.keys()),
            key="trade_comparison"
        )

        selected_program = st.selectbox(
            "Select Specific Program",
            options=[prog["name"] for prog in TRADE_PROGRAMS[selected_trade]["programs"]],
            key="program_comparison"
        )

        # College program details
        college_program = {
            "cost": st.number_input(
                "College Program Cost (4 years)",
                min_value=0,
                value=100000,
                step=5000
            )
        }

        program_details = next(
            prog for prog in TRADE_PROGRAMS[selected_trade]["programs"]
            if prog["name"] == selected_program
        )

        if st.button("Compare Costs"):
            comparison = calculate_education_comparison(program_details, college_program)

            # Create comparison visualization
            fig = px.bar(
                x=["Trade School", "College"],
                y=[comparison["trade"]["total"], comparison["college"]["total"]],
                title="Total Cost Comparison",
                labels={"x": "Education Path", "y": "Total Cost ($)"}
            )
            st.plotly_chart(fig)

            st.markdown(f"""
            ### Cost Breakdown

            **Trade School Total:** ${comparison["trade"]["total"]:,}
            * Tuition: ${comparison["trade"]["tuition"]:,}
            * Lost Wages: ${comparison["trade"]["lost_wages"]:,}

            **College Total:** ${comparison["college"]["total"]:,}
            * Tuition: ${comparison["college"]["tuition"]:,}
            * Lost Wages: ${comparison["college"]["lost_wages"]:,}

            **Potential Savings with Trade School:** ${comparison["difference"]:,}
            """)

if __name__ == "__main__":
    render_calculators()