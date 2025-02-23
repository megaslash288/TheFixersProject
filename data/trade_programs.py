# import csv
# from utils.UnpackCSVFunction import retrieve_wage


TRADE_PROGRAMS = {
    "Electrical": {
        "description": "Learn to install, maintain, and repair electrical systems",
        "duration": "4 years",
        "avg_salary": 4,
        #"demand_growth": "14%",
        "certification": "Licensed Electrician",
        "programs": [
            {"name": "Residential Electrician", "duration": "2 years", "cost": 15000},
            {"name": "Industrial Electrician", "duration": "4 years", "cost": 25000}
        ]
    },
    "Plumbing": {
        "description": "Master the installation and repair of piping systems",
        "duration": "4 years",
        "avg_salary": 53000,
        #"demand_growth": "12%",
        "certification": "Licensed Plumber",
        "programs": [
            {"name": "Residential Plumbing", "duration": "2 years", "cost": 14000},
            {"name": "Commercial Plumbing", "duration": "4 years", "cost": 24000}
        ]
    },
    "Welding": {
        "description": "Learn various welding techniques and metal fabrication",
        "duration": "2 years",
        "avg_salary": 44000,
        #"demand_growth": "8%",
        "certification": "Certified Welder",
        "programs": [
            {"name": "Basic Welding", "duration": "1 year", "cost": 12000},
            {"name": "Advanced Welding", "duration": "2 years", "cost": 20000}
        ]
    },
    "Carpenter": {
        "description": "Insert Carpenter description here. there is probably wood involved",
        "duration": "2 years",
        "avg_salary": 55555,
        #"demand_growth": 300000%,
        "certification": "Certified Carpenter",
        "programs": [
            {"name": "carpentry", "duration": "1 year", "cost": 14000}
        ]
    },
    "HVAC Technician": {
        "description": "Installing, maintaining, and repairing HVAC systems in both residential and commercial settings",
        "duration": "2 years",
        "avg_salary": 55555,
        #"demand_growth": 300000%,
        "certification": "Certified HVAC Technician",
        "programs": [
            {"name": "HVAC tech", "duration": "1 year", "cost": 14000}
        ]
    },
    "Fire Inspector": {
        "description": "Ensuring that a location is up to fire safety codes",
        "duration": "2 years",
        "avg_salary": 55555,
        #"demand_growth": 300000%,
        "certification": "Certified Fire Inspector",
        "programs": [
            {"name": "Fire inspector", "duration": "1 year", "cost": 14000}
        ]
    },
    "Brickmason": {
        "description": "Laying and maintaining concrete and brick masonry in both residential and commercial settings",
        "duration": "2 years",
        "avg_salary": 55555,
        #"demand_growth": 300000%,
        "certification": "Certified Mason",
        "programs": [
            {"name": "Masonry", "duration": "1 year", "cost": 14000}
        ]
    },
    "Painter": {
        "description": "Painting interior and exterior walls and structures in both residential and commercial settings",
        "duration": "2 years",
        "avg_salary": 55555,
        #"demand_growth": 300000%,
        "certification": "None",
        "programs": [
            {"name": "Painter", "duration": "1 year", "cost": 14000}
        ]
    },
    "Roofer": {
        "description": "Laying tile and shingles on roofs and maintaining roofs in both commercial and residential settings",
        "duration": "2 years",
        "avg_salary": 55555,
        #"demand_growth": 300000%,
        "certification": "Certified Roofer",
        "programs": [
            {"name": "Roofing", "duration": "1 year", "cost": 14000}
        ]
    },
    "Trucker": {
        "description": "Operating a semi-truck to move cargo both locally and around the country",
        "duration": "1 year",
        "avg_salary": 55555,
        #"demand_growth": 300000%,
        "certification": "CDL License, Residential Driver's License",
        "programs": [
            {"name": "CDL Truck driver", "duration": "1 year", "cost": 14000}
        ]
    },    
    "Drywaller/Plasterer": {
        "description": "Installing drywall or plaster in construction environments",
        "duration": "1 year",
        "avg_salary": 55555,
        #"demand_growth": 300000%,
        "certification": "Plasterer Apprenticeship",
        "programs": [
            {"name": "Plasterer", "duration": "1 year", "cost": 14000}
        ]
    },    
    "Steelworker": {
        "description": "Insert Steelworker description here. there is probably a steel mill involved",
        "duration": "2 years",
        "avg_salary": 55555,
        #"demand_growth": 300000%,
        "certification": "Certified Steelworker",
        "programs": [
            {"name": "Steelworker", "duration": "1 year", "cost": 14000}
        ]
    }
}
