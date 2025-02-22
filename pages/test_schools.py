import streamlit as st
import requests
from bs4 import BeautifulSoup

url = "https://www.findmytradeschool.com/trade-schools/kentucky/"

def get_links_for_schools(url):
	# Send a request to the webpage
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
	}
	response = requests.get(url, headers=headers)
	if response.status_code != 200:
		raise Exception(f"Failed to fetch page, status code: {response.status_code}")
	
	# Parse the HTML content
	soup = BeautifulSoup(response.text, 'html.parser')
	
	# Find the table with class "tableizer-table"
	table = soup.find('table', class_='tableizer-table')
	if not table:
		raise Exception("Table with class 'tableizer-table' not found")
	
	# Find tbody and its rows
	tbody = table.find('tbody')
	if not tbody:
		raise Exception("No <tbody> found inside the table")
	
	rows = tbody.find_all('tr')
	
	# Collect a elements inside td elements of each row
	 # Collect a elements inside td elements of each row and store in a dictionary
	links_dict = {}
	for row in rows:
		for td in row.find_all('td'):
			for a in td.find_all('a'):
				link_text = a.get_text(strip=True)
				link_href = a.get('href')
				if link_text and link_href:
					links_dict[link_text] = link_href
	
	return links_dict

st.header("Trade Schools in Kentucky")
schools_list, *_ = st.columns(1)

for school_name, school_website in get_links_for_schools(url).items():
	schools_list.link_button(school_name, school_website)





