def calculate_trade_match(answers):
    """Calculate trade matches based on assessment answers."""
    scores = {
        "Electrical": 0,
        "Plumbing": 0,
        "Welding": 0
    }
    
    # Process mechanical aptitude
    if answers["mechanical_aptitude"] >= 4:
        scores["Electrical"] += 2
        scores["Plumbing"] += 2
        scores["Welding"] += 2

    # Process problem-solving
    if answers["problem_solving"] >= 4:
        scores["Electrical"] += 3
        scores["Plumbing"] += 2

    # Process physical work
    if answers["physical_work"] >= 4:
        scores["Welding"] += 3
        scores["Plumbing"] += 2

    # Process attention to detail
    if answers["detail_oriented"] >= 4:
        scores["Electrical"] += 3
        scores["Welding"] += 2

    # Normalize scores
    max_score = max(scores.values())
    if max_score > 0:
        scores = {k: (v / max_score) * 100 for k, v in scores.items()}

    return scores

ASSESSMENT_QUESTIONS = [
    {
        "id": "mechanical_aptitude",
        "question": "How comfortable are you working with tools and machinery?",
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
