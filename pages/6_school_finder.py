import streamlit as st
import csv


st.header("Trade Schools in Kentucky")

# schools_list, virtual_tours = st.columns(2)
csv_data = None
with open("pages\\schools\\links.csv") as csv_fp:
	csv_data = csv.reader(csv_fp)
	_, *rows = csv_data 

for row in rows:
	
	num_cols = 1
	school_name, school_link, is_valid_link, tour_link, contact_link = row
	is_valid_link = is_valid_link == "True"

	# if tour_link: # if value is not empty string
	# 	num_cols += 1
	
	# if contact_link: # if value is not empty string
	# 	num_cols += 1
	
	cols = st.columns([4,1,1])	
	
	if is_valid_link:
		cols[0].link_button(school_name, school_link)
	else:
		cols[0].write(school_name)
		continue # if the webpage doesnt work, no other links will be available
		
	
	if contact_link: # if value is not empty string
		cols[1].link_button("Contact", contact_link)
	else:
		cols[1].write(" ")
	
	if tour_link:
		cols[2].link_button("Virtual Tour", tour_link)
	else:
		cols[2].write(" ")
		

	





