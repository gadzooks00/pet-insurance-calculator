import streamlit as st
from insurance_math import (
    calculate_out_of_pocket,
    simulate_yearly_costs,
    simulate_no_insurance_costs
)
from plot_helpers import plot_cumulative_costs, plot_first_year_bill

st.set_page_config(layout="wide")
st.title("🩺 Pet Insurance Cost Simulator")

col1, col2 = st.columns(2)

with col1:
    st.header("📋 Insurance Plans")
    num_plans = st.number_input("Number of Insurance Plans to Compare", min_value=1, max_value=10, value=2)
    plans = []

    for i in range(num_plans):
        with st.expander(f"Plan {i+1} Settings", expanded=False):
            name = st.text_input(f"Plan {i+1} - Name", value=f"Plan {chr(65+i)}", key=f"name_{i}")
            default_premium = 40.78 if i == 0 else 12.11
            default_deductible = 250.0 if i == 0 else 500.0
            default_reimbursement = 90.0 if i == 0 else 70.0
            default_max = "unlimited" if i == 0 else "10000"

            monthly_premium = st.number_input(
                f"{name} - Monthly Premium ($)",
                min_value=0.0,
                value=default_premium,
                step=5.0,
                key=f"premium_{i}"
            )
            deductible = st.number_input(
                f"{name} - Annual Deductible ($)",
                min_value=0.0,
                value=default_deductible,
                step=5.0,
                key=f"deductible_{i}"
            )
            reimbursement = st.slider(
                f"{name} - Reimbursement %", 50.0, 100.0,
                value=default_reimbursement,
                step=0.1,
                key=f"reimbursement_{i}"
            )
            annual_max = st.text_input(f"{name} - Annual Max Payout ($ or 'unlimited')", value=default_max, key=f"max_{i}")
            if annual_max.strip().lower() == "unlimited":
                annual_max = float("inf")
            else:
                try:
                    annual_max = float(annual_max)
                except:
                    annual_max = 10000.0
            plans.append({
                "name": name,
                "monthly_premium": monthly_premium,
                "deductible": deductible,
                "reimbursement": reimbursement / 100.0,
                "max_payout": annual_max
            })

with col2:
    st.header("📈 Simulation Setup")
    years = st.slider("Years to Simulate", 5, 20, 15)
    vet_inflation = st.number_input("Vet Cost Inflation Rate (%)", value=5.9, step=0.1) / 100
    premium_inflation = st.number_input("Premium Cost Increase Rate (%)", value=13.0, step=0.1) / 100
    base_year_vet_cost = st.number_input("Base Year Vet Cost ($)", value=600.0, step=10.0)

    st.subheader("⚠️ Add Health Events")
    health_events = []
    num_events = st.number_input("Number of Health Events", min_value=0, max_value=10, value=2)
    default_event_data = [(3, 3000.0), (6, 600.0)]
    for i in range(num_events):
        default_year = default_event_data[i][0] if i < len(default_event_data) else i + 3
        default_cost = default_event_data[i][1] if i < len(default_event_data) else 1200.0
        with st.expander(f"Health Event {i+1}", expanded=False):
            year = st.number_input(f"Year of Event {i+1}", min_value=1, max_value=years, value=default_year, key=f"event_year_{i}")
            cost = st.number_input(f"Cost of Event {i+1} ($)", min_value=0.0, value=default_cost, step=10.0, key=f"event_cost_{i}")
            health_events.append((year, cost))
    event_dict = {int(year): float(cost) for year, cost in health_events}

# Cumulative Cost Chart
c1, c2 = st.columns(2)

with c1:
    st.markdown("### 📆 Cumulative Cost Comparison Over Time")
    no_insurance_costs = simulate_no_insurance_costs(base_year_vet_cost, event_dict, years, vet_inflation)

    insurance_costs_by_plan = {
        plan["name"]: simulate_yearly_costs(base_year_vet_cost, event_dict, years, vet_inflation, premium_inflation, plan)
        for plan in plans
    }

    fig1 = plot_cumulative_costs(years, no_insurance_costs, insurance_costs_by_plan)
    st.pyplot(fig1)

with c2:
    st.markdown("### 💥 Estimated First-Year Cost Comparison (Single Event)")
    first_event_cost = sorted(health_events, key=lambda x: x[0])[0][1] if health_events else 0.0
    fig2 = plot_first_year_bill(plans, base_year_vet_cost, first_event_cost)
    st.pyplot(fig2)