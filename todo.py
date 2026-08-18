import numpy as np
import pandas as pd
import streamlit as st

# Page Config
st.set_page_config(
    page_title="Smart Expense Tracker", page_icon="💳", layout="wide"
)

st.title("💳 Smart Expense & Budget Tracker")
st.caption(
    "Track daily expenses with category filters and interactive analytics"
)

# Initial Sample Data
if "expenses" not in st.session_state:
    st.session_state.expenses = pd.DataFrame(
        [
            {
                "Date": "2026-08-01",
                "Category": "Food",
                "Note": "Lunch",
                "Amount": 450,
                "Payment": "UPI",
            },
            {
                "Date": "2026-08-02",
                "Category": "Transport",
                "Note": "Auto Fare",
                "Amount": 120,
                "Payment": "Cash",
            },
            {
                "Date": "2026-08-03",
                "Category": "Books",
                "Note": "Python Book",
                "Amount": 600,
                "Payment": "UPI",
            },
            {
                "Date": "2026-08-03",
                "Category": "Shopping",
                "Note": "T-Shirt",
                "Amount": 800,
                "Payment": "Card",
            },
            {
                "Date": "2026-08-04",
                "Category": "Entertainment",
                "Note": "Movie Ticket",
                "Amount": 300,
                "Payment": "UPI",
            },
        ]
    )

# Sidebar - Add Expense
st.sidebar.header("➕ Add New Expense")
date_input = st.sidebar.date_input("Date")
category_input = st.sidebar.selectbox(
    "Category",
    ["Food", "Transport", "Shopping", "Books", "Entertainment", "Bills"],
)
note_input = st.sidebar.text_input("Note / Description")
amount_input = st.sidebar.number_input("Amount (₹)", min_value=1, step=10)
payment_input = st.sidebar.selectbox(
    "Payment Mode", ["UPI", "Cash", "Card", "Net Banking"]
)

if st.sidebar.button("Add Expense", type="primary"):
    new_entry = pd.DataFrame(
        [
            {
                "Date": str(date_input),
                "Category": category_input,
                "Note": note_input,
                "Amount": amount_input,
                "Payment": payment_input,
            }
        ]
    )
    st.session_state.expenses = pd.concat(
        [st.session_state.expenses, new_entry], ignore_index=True
    )
    st.sidebar.success("Expense Added!")

df = st.session_state.expenses

# Sidebar - Filter
st.sidebar.divider()
st.sidebar.header("🔍 Filter Analytics")
selected_categories = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique(),
)

filtered_df = df[df["Category"].isin(selected_categories)]

# Dashboard Metrics
col1, col2, col3 = st.columns(3)
total_spent = filtered_df["Amount"].sum()
avg_spent = filtered_df["Amount"].mean() if not filtered_df.empty else 0
total_trans = len(filtered_df)

col1.metric("💰 Total Spent", f"₹ {total_spent:,.0f}")
col2.metric("📊 Average Expense", f"₹ {avg_spent:,.0f}")
col3.metric("🧾 Total Transactions", f"{total_trans}")

st.divider()

# Charts Breakdown
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("📊 Category Wise Spending")
    if not filtered_df.empty:
        chart_data = filtered_df.groupby("Category")["Amount"].sum()
        st.bar_chart(chart_data)
    else:
        st.warning("No data found for selected filter.")

with col_chart2:
    st.subheader("💳 Payment Mode Split")
    if not filtered_df.empty:
        pay_data = filtered_df.groupby("Payment")["Amount"].sum()
        st.bar_chart(pay_data)
    else:
        st.warning("No data found for selected filter.")

st.divider()

# Recent Transactions Table
st.subheader("📋 Recent Expenses History")
st.dataframe(filtered_df, use_container_width=True)

st.caption("Created by Goutam Gulati")
