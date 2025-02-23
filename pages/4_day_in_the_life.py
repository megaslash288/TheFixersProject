import streamlit as st

TRADE_VIDEOS:dict[str,str] = {
	"Electrician": "https://youtu.be/lifunadBZ3U?si=RFlu2ScZq7Wba8Jd",
	"Plumber": "https://youtu.be/rBNciXF3LHY?si=UDdCpbgOyhawDxF0",
	"Carpenter": "https://youtu.be/xtQXvuUZbAo?si=Dl2YsAWMG_8YjlIn",
	"Welder": "https://youtu.be/CuDwydMjgGg?si=pk52TXij_RdhIz7w",
	"HVAC Technician": "https://youtu.be/GktnK0h3iQM?si=-TFH04TH0WXqM9W5",
	"Fire inspector": "https://youtu.be/1imCjkelufs?si=X8g_Mfw5i2bQYnWJ",
	"Brick Mason": "https://youtu.be/AQlquiosnjU?si=XKiIIcsxSMWN_UfX",
	"Construction Manager": "https://youtu.be/-tuIzDxEK0Y?si=aXthAtuNemKzTo7-",
	"Painter": "https://youtu.be/UkcBxmp8Noc?si=YriDELjygi_4aaMQ",
	"Roofer": "https://youtu.be/0oRvNLDX3iQ?si=iCEdsxdxfeQ_4cF0",
	"Trucker": "https://youtu.be/31Wj5TrIdDE?si=uWnNFi7G-_5Kn-8N",
	"Drywaller": "https://youtu.be/PfYczcpjrN4?si=eJgq3A5utfcK562j",
	"Steel Worker": "https://youtu.be/cmYMCJb3QwI?si=o_O0l41rx7ZKlm79",
}

st.set_page_config(page_title="Day in the Life", page_icon="⭐")

def render_success_stories():
	st.title("A Day in the Life of Trade Professionals")
	st.markdown("""
	Watch inspiring stories from professionals who have built successful careers in the trades.
	Learn about their journeys.
	""")

	

	for name, link in TRADE_VIDEOS.items():
		st.subheader(f"A day in the life of a {name}")
		st.video(link)

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
