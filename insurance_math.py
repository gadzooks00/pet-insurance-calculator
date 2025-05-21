def calculate_out_of_pocket(bill, premium, deductible, reimbursement, max_payout):
    """
    Calculates the total cost to the user for a given vet bill with insurance.
    """
    if bill <= deductible:
        return bill + premium
    payout = min((bill - deductible) * reimbursement, max_payout)
    return bill - payout + premium

def simulate_yearly_costs(
    base_vet_cost,
    event_dict,
    years,
    vet_inflation,
    premium_inflation,
    plan
):
    """
    Simulate cumulative cost over time for a given insurance plan.
    """
    vet_cost = base_vet_cost
    premium = plan["monthly_premium"] * 12
    cumulative_cost = 0
    cumulative_costs = []

    for year in range(1, years + 1):
        vet_cost *= (1 + vet_inflation) if year > 1 else 1
        premium *= (1 + premium_inflation) if year > 1 else 1
        year_cost = vet_cost + event_dict.get(year, 0)

        if year_cost <= plan["deductible"]:
            payout = 0
        else:
            payout = min((year_cost - plan["deductible"]) * plan["reimbursement"], plan["max_payout"])

        out_of_pocket = year_cost - payout + premium
        cumulative_cost += out_of_pocket
        cumulative_costs.append(cumulative_cost)

    return cumulative_costs

def simulate_no_insurance_costs(base_vet_cost, event_dict, years, vet_inflation):
    """
    Simulate cumulative vet costs over time without insurance.
    """
    vet_cost = base_vet_cost
    cumulative_cost = 0
    cumulative_costs = []

    for year in range(1, years + 1):
        vet_cost *= (1 + vet_inflation) if year > 1 else 1
        year_cost = vet_cost + event_dict.get(year, 0)
        cumulative_cost += year_cost
        cumulative_costs.append(cumulative_cost)

    return cumulative_costs
