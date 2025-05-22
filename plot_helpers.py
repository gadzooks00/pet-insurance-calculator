import matplotlib.pyplot as plt

def plot_cumulative_costs(years, no_insurance_costs, insurance_costs_by_plan):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(range(1, years + 1), no_insurance_costs, "--", label="No Insurance", color='black')

    for plan_name, costs in insurance_costs_by_plan.items():
        ax.plot(range(1, years + 1), costs, label=f"{plan_name} (w/ Insurance)")

    ax.set_xlabel("Year")
    ax.set_ylabel("Cumulative Cost ($)")
    ax.set_title("Lifetime Cost of Pet Care")
    ax.grid(True)
    ax.legend()
    return fig

def plot_first_year_bill(plans, base_vet_cost, first_event_cost):
    fig, ax = plt.subplots(figsize=(8, 5))
    bar_labels = []
    premiums = []
    routine_costs = []
    event_costs = []
    totals = []

    total_uninsured = base_vet_cost + first_event_cost

    for plan in plans:
        premium = plan["monthly_premium"] * 12
        deductible = plan["deductible"]
        reimbursement = plan["reimbursement"]
        max_payout = plan["max_payout"]

        if first_event_cost <= deductible:
            reimbursed = 0
        else:
            reimbursed = min((first_event_cost - deductible) * reimbursement, max_payout)

        net_event_cost = first_event_cost - reimbursed
        total = base_vet_cost + net_event_cost + premium

        bar_labels.append(plan["name"])
        premiums.append(premium)
        routine_costs.append(base_vet_cost)
        event_costs.append(net_event_cost)
        totals.append(total)

    x = range(len(bar_labels))
    bar1 = ax.bar(x, routine_costs, label="Routine Care")
    bar2 = ax.bar(x, event_costs, bottom=routine_costs, label="Event Cost")
    bar3 = ax.bar(x, premiums, bottom=[r + e for r, e in zip(routine_costs, event_costs)], label="Premium")

    for i in x:
        # Label each component separately on the total bar
        y_offset = 0
        ax.text(i, y_offset + routine_costs[i]/2, f"Routine: ${routine_costs[i]:,.0f}",
                ha='center', va='center', fontsize=7, color='white')
        y_offset += routine_costs[i]
        ax.text(i, y_offset + event_costs[i]/2, f"Event: ${event_costs[i]:,.0f}",
                ha='center', va='center', fontsize=7, color='white')
        y_offset += event_costs[i]
        ax.text(i, y_offset + premiums[i]/2, f"Premium: ${premiums[i]:,.0f}",
                ha='center', va='center', fontsize=7, color='white')
        ax.text(i, totals[i] + 25, f"Total: ${totals[i]:,.0f}", ha='center', va='bottom', fontsize=8)

    ax.axhline(total_uninsured, color="black", linestyle="--", label="No Insurance")
    ax.set_xticks(x)
    ax.set_xticklabels(bar_labels)
    ax.set_ylabel("Estimated 1-Year Cost ($)")
    ax.set_title("First-Year Cost Breakdown: Insurance vs No Insurance")
    ax.legend()
    return fig