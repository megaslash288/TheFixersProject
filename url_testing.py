import requests
from bs4 import BeautifulSoup
import time
from itertools import zip_longest
from pprint import pprint

headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def is_url_ok(url: str) -> bool:
    try:
        response = requests.get(url)
        return response.ok
    except requests.RequestException:
        return False

school_names = []
school_links = []
link_validity = []
school_vtours = []

def get_table_rows(url):
	# Send a request to the webpage
	
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
	
	return rows, links_dict

# Example usage:
if __name__ == "__main__":
	url = "https://www.findmytradeschool.com/trade-schools/kentucky/"  # Replace with the actual URL
	rows, links_dict = get_table_rows(url)
	for row in rows:
		print(row.prettify())  # Print each row nicely formatted
	for name, href in links_dict.items():
		print(f"{name}: {href}")  # Print each collected <a> element as a dictionary entry
		school_names.append(name)
		school_links.append(href)
	print(len(links_dict))
	# school_names = [None]*len(links_dict)
	# school_links = [None]*len(links_dict)
	link_validity = [None]*len(school_names)
	school_vtours = [None]*len(school_names)
	pprint(list(zip(school_names, school_links)))
	
	
	
	start_time = time.perf_counter()
	keywords = ["virtual tour", "campus tour", "3d tour"]#, "visit us"]

	for i, link in enumerate(school_links):
		print("#"*20)
		try:
			print(f"Trying {link}")
			r = requests.get(link, headers=headers, timeout=3)
			if r.ok: # validity check
				print(f"{link} is good")
				link_validity[i] = True

				# checking for tour info
				soup = BeautifulSoup(r.text, "html.parser")
				for link in soup.find_all("a", href=True):
					if any(keyword in link.text.lower() or keyword in link["href"].lower() for keyword in keywords):
						# if found, append link to vtours
						school_vtours[i] = link["href"]
						continue
					else: # if not found, append None
						school_vtours[i] = None
						continue


			else: # if link not valid
				print(f"{link} is bad")
				link_validity[i] = False # bad link append false
				school_vtours[i] = None # bad link, no tour
				continue
		except Exception:
			print(f"{link} threw exception")
			link_validity[i] = False # bad link, not valid
			school_vtours[i] = None # bad link, no tour
			continue
		print(len(school_names), len(school_links), len(link_validity), len(school_vtours))

	
	end_time = time.perf_counter()
	print(f"took {end_time - start_time} seconds")
	with open("pages\\schools\\links.csv", "w", encoding="utf-8") as fp:
		fp.write("school_name, school_link, valid_link, virtual_tour_link\n")
		for name, link, valid, tour in zip_longest(school_names, school_links, link_validity, school_vtours):
			fp.write(f"{name}, {link}, {valid}, {tour}\n")
