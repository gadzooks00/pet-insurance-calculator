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

def plot_first_year_bill(bill_cost, plans, base_vet_cost, first_event_cost, calculate_fn):
    fig, ax = plt.subplots(figsize=(6, 4))
    bar_labels = []
    bar_values = []

    bill = base_vet_cost + first_event_cost

    for plan in plans:
        out_of_pocket = calculate_fn(
            bill,
            premium=plan["monthly_premium"] * 12,
            deductible=plan["deductible"],
            reimbursement=plan["reimbursement"],
            max_payout=plan["max_payout"]
        )
        bar_labels.append(plan["name"])
        bar_values.append(out_of_pocket)

    ax.bar(bar_labels, bar_values, label="With Insurance")
    ax.axhline(bill, color="black", linestyle="--", label="No Insurance")
    ax.set_ylabel("Estimated 1-Year Cost ($)")
    ax.set_title("First-Year Cost: Insurance vs No Insurance")
    ax.legend()
    return fig
