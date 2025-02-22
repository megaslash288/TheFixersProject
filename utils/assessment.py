def calculate_trade_match(answers):
    """Calculate trade matches based on assessment answers."""
    scores = {
        "Electrical": 0,
        "Plumbing": 0,
        "Welding": 0,
        "Carpenter": 0,
        "Construction": 0,
        "HVAC Technician": 0,
        "Fire Inspector": 0,
        "Brickmason": 0,
        "Painter": 0,
        "Roofer": 0,
        "Trucker": 0,
        "Drywaller/Plasterer": 0,
        "Steelworker": 0
    }
    
    # Process comfort around heavy machinery
    if answers["mechanical_aptitude"] >= 4:
        scores["Construction"] += 1
        scores["Steelworker"] += 1

    if answers["mechanical_aptitude"] >= 3:
        scores["Construction"] += 1
        scores["Steelworker"] += 1
        scores["Welding"] += 1
        scores["Trucker"] += 1
        scores["Electrical"]
         
    if answers["mechanical_aptitude"] >= 2:
        scores["Construction"] += 1
        scores["Welding"] += 1
        scores["Trucker"] += 1
        scores["Steelworker"] += 1

    # Process mechanical aptitude aka mechanical_aptitude2
    if answers["mechanical_aptitude2"] >= 4:
        scores["Electrical"] += 1
        scores["Plumbing"] += 1
        scores["HVAC Technician"] += 1
    
    if answers["mechanical_aptitude2"] >= 3:
        scores["Electrical"] += 1
        scores["Plumbing"] += 1
        scores["HVAC Technician"] += 1

    if answers["mechanical_aptitude2"] >= 2:
        scores["Electrical"] += 1
        scores["Plumbing"] += 1
        scores["HVAC Technician"] += 1
        scores["Trucker"] += 1

    # Process risk
    if answers["risk"] >= 4:
        scores["Steelworker"] += 1
        scores["Welding"] += 1
    if answers["risk"] >= 3:
        scores["Roofer"] += 1
        scores["Steelworker"] += 1
        scores["Welding"] += 1

    # Process problem-solving
    if answers["problem_solving"] >= 4:
        scores["Electrical"] += 1
        scores["HVAC Technician"] += 1
    
    if answers["problem_solving"] >= 3:
        scores["Electrical"] += 1
        scores["Plumbing"] += 1
        scores["HVAC Technician"] += 1
    
    if answers["problem_solving"] >= 2:
        scores["Electrical"] += 1
        scores["Plumbing"] += 1
        scores["HVAC Technician"] += 1

    # Process physical work
    if answers["physical_work"] >= 4:
        scores["Carpenter"] += 1
        scores["Roofer"] += 1
        scores["Construction"] += 1
        
    if answers["physical_work"] >= 3:
        scores["Welding"] += 1
        scores["Roofer"] += 1
        scores["Drywaller/Plasterer"] += 1
        scores["Brickmason"] += 1
        scores["Construction"] += 1
        scores["Steelworker"] += 1

    if answers["physical_work"] >= 2:
        scores["Plumbing"] += 1
        scores["Welding"] += 1
        scores["Roofer"] += 1
        scores["Drywaller/Plasterer"] += 1
        scores["Brickmason"] += 1
        scores["Construction"] += 1
        scores["Steelworker"] += 1

    # Process attention to detail
    if answers["detail_oriented"] >= 4:
        scores["Electrical"] += 1
        scores["Fire Inspector"] += 2
        


    if answers["detail_oriented"] >= 3:
        scores["Electrical"] += 1
        scores["Welding"] += 1
        scores["Fire Inspector"] += 1
        scores["Painter"] += 1
        scores["Roofer"] += 1
        scores["Drywaller/Plasterer"] += 1
        scores["HVAC Technician"] += 1

    if answers["detail_oriented"] >= 2:
        scores["Electrical"] += 1
        scores["Welding"] += 1
        scores["Fire Inspector"] += 1
        scores["Painter"] += 1
        scores["Roofer"] += 1
        scores["Drywaller/Plasterer"] += 1
        scores["HVAC Technician"] += 1

    
    # Normalize scores
    max_score = max(scores.values())
    if max_score > 0:
        scores = {k: (v / max_score) * 100 for k, v in scores.items()}

    return scores

ASSESSMENT_QUESTIONS = [
    {
        "id": "mechanical_aptitude",
        "question": "How comfortable are you working with and around heavy machinery?",
        "type": "slider",
        "min": 1,
        "max": 5
    },
    {
        "id": "mechanical_aptitude2",
        "question": "How comfortable are you wwith taking apart machinery and wiring?",
        "type": "slider",
        "min": 1,
        "max": 5
    },
    {
        "id": "risk",
        "question": "How comfortable with risks inherent to your job?",
        "type": "slider",
        "min": 1,
        "max": 5
    },
    {
        "id": "problem_solving",
        "question": "How much do you enjoy solving complex problems?",
        "type": "slider",
        "min": 1,
        "max": 5
    },
    {
        "id": "physical_work",
        "question": "How comfortable are you with physical work?",
        "type": "slider",
        "min": 1,
        "max": 5
    },
    {
        "id": "detail_oriented",
        "question": "How detail-oriented are you?",
        "type": "slider",
        "min": 1,
        "max": 5
    }
]
