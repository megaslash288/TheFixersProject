import streamlit as st
#import streamlit_carousel as stc
# from data.trade_programs import TRADE_PROGRAMS
from data.career_paths import CAREER_PATHS
import plotly.express as px
import BLS_Import

# attribution for icon
# <a href="https://www.freepik.com/icons/technical-school/2">Icon by srip</a>

def calc_avg_wage(level:int):
	# `level` = 0: Apprentice
	total = 0
	for trade_levels in CAREER_PATHS.values():
		for level in trade_levels:
			if level["level"] == "Apprentice":
				salary_range = level["salary"]
				salary_min, salary_max = map(int, salary_range.split("-"))
				total += (salary_max + salary_min) / 2
	total /= len(CAREER_PATHS.keys())
	return total




st.set_page_config(
	page_title="Trade Career Explorer",
	page_icon="icon.png",
	layout="wide"
)


def main():
	st.title("Trade Career Explorer")
	
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
	# col1, col2, col3 = st.columns(3)
	col1, col2 = st.columns(2)

	with col1:
		# perform avg starting salary
		avg_starting_salary = calc_avg_wage(0)
		st.metric("Average Starting Salary", f"${avg_starting_salary:,.2f}")
		
	# with col2:
	# 	st.metric("Average ", "12%")
	with col2:
		st.metric("Programs Available", len(CAREER_PATHS))

	# Featured Trades
	st.subheader("Featured Trade Programs")
	features_programs = ["Electrical", "Welding", "Carpenter"]
	links = ["https://www.loujatc.com/", "https://www.knightschoolofwelding.com/", "https://toptradeschools.com/near-you/carpenter/kentucky/louisville/"]

	
	# Create three columns for featured trades
	cols = st.columns(3)
	
	# TODO: use career paths
	# for idx, (trade, details) in enumerate(list(TRADE_PROGRAMS.items())[:3]):
	# use trade path level 2 (`trade_level = 1`)
	trade_level = 1
	for idx, trade_name in enumerate(features_programs):
		with cols[idx]:
			st.markdown(f"### {trade_name}")
			# avg salary of level 3
			salary_range = CAREER_PATHS[trade_name][trade_level]["salary"]
			salary_min, salary_max = map(int, salary_range.split("-"))
			avg_salary = (salary_max + salary_min) / 2
			print(f"{salary_min=}; {salary_max=}; {avg_salary=}")
			st.markdown(f"**Average Salary:** ${avg_salary:,.2f}")

			# get duration of level 3
			duration = CAREER_PATHS[trade_name][trade_level]["years"]
			st.markdown(f"**Duration:** {duration}")
			# st.button(f"Learn More About {trade_name}", key=f"learn_more_{trade_name}")
			st.link_button(f"Learn More About {trade_name}", links[idx])

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
	
	st.markdown('<a href="https://www.freepik.com/icons/technical-school/2">Icon by srip</a>', unsafe_allow_html=True)
	#generatecsv
	BLS_Import.CreateCSV()

if __name__ == "__main__":
	main()
