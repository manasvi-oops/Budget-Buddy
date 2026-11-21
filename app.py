import streamlit as st 

st.set_page_config(page_title="Budget Buddy", page_icon="💰")

st.title("Student Budget Buddy")

income = st.number_input("Monthly income($)",min_value=0,value=10000,step=500)

st.subheader("Monthly expenses")
rent = st.number_input("Rent/hostel",min_value=0,value=0,step=100)
food = st.number_input("Food",min_value=0,value=0,step=100)
travel = st.number_input("Travel",min_value=0,value=0,step=100)
other = st.number_input("Other",min_value=0,value=0,step=100)

total = rent + food + travel + other
savings = income - total

col1,col2=st.columns(2)
col1.metric("Total expenses",f"${total}")
col2.metric("Leftover",f"4{savings}")

if income > 0:
    st.progress(min(total/income,1.0))
    st.write(f"You spend {total/income:.0%}of your income.")

if savings < 0:
    st.error(("You're overspending.Cut expenses first."))
elif savings<income*0.2:
    st.warning("Savings are under 20%. Try trimming food or travel.")
else:
    st.success("Good job.You're saving well.")

import pandas as pd

st.subheader("Where your money goes")
chart_data = pd.DataFrame(
    {"Amount": [rent, food, travel, other]},
    index=["Rent", "Food", "Travel", "Other"],
)
st.bar_chart(chart_data)