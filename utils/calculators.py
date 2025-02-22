def calculate_roi(program_cost, expected_salary, years, current_salary=0):
    """Calculate ROI for trade education."""
    total_cost = program_cost
    total_earnings = sum([(expected_salary - current_salary) for _ in range(years)])
    roi = ((total_earnings - total_cost) / total_cost) * 100
    return roi

def calculate_education_comparison(trade_program, college_program):
    """Compare trade school vs traditional college costs and earnings."""
    trade_costs = {
        "tuition": trade_program["cost"],
        "duration": float(trade_program["duration"].split()[0]),
        "lost_wages": 20000 * float(trade_program["duration"].split()[0]),
        "total": 0
    }
    trade_costs["total"] = trade_costs["tuition"] + trade_costs["lost_wages"]

    college_costs = {
        "tuition": college_program["cost"],
        "duration": 4,
        "lost_wages": 20000 * 4,
        "total": 0
    }
    college_costs["total"] = college_costs["tuition"] + college_costs["lost_wages"]

    return {
        "trade": trade_costs,
        "college": college_costs,
        "difference": college_costs["total"] - trade_costs["total"]
    }
