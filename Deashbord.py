import streamlit as st
import pandas as pd
import plotly.express as px

# Load Dataset
def load_data():
    df = pd.read_csv("Walmart.csv")  # Update with actual filename
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# Streamlit App Title
st.title("E-Commerce Sales Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")
selected_category = st.sidebar.multiselect("Select Category", df["Category"].unique())
selected_date = st.sidebar.date_input("Select Date", df["Date"].min())

# Apply Filters
if selected_category:
    df = df[df["Category"].isin(selected_category)]
df = df[df["Date"] >= pd.to_datetime(selected_date)]

# Sales Over Time
st.subheader("Monthly Sales Trend")
df["Month"] = df["Date"].dt.month
fig = px.line(df.groupby("Month")["Sales"].sum().reset_index(), x="Month", y="Sales", title="Monthly Sales Trend")
st.plotly_chart(fig)

# Category-wise Sales
st.subheader("Top-Selling Categories")
fig = px.bar(df.groupby("Category")["Sales"].sum().reset_index(), x="Category", y="Sales", color="Sales", title="Top-Selling Categories")
st.plotly_chart(fig)

# Preferred Payment Methods
st.subheader("Preferred Payment Methods")
fig = px.pie(df, names="Payment_Method", title="Preferred Payment Methods")
st.plotly_chart(fig)

# Peak Sales Hours
st.subheader("Peak Sales Hours")
fig = px.histogram(df, x="Time", nbins=24, title="Peak Sales Hours", color_discrete_sequence=['blue'])
st.plotly_chart(fig)

# Branch-wise Sales
st.subheader("Branch-Wise Sales")
fig = px.bar(df.groupby("Branch")["Sales"].sum().reset_index(), x="Branch", y="Sales", color="Sales", title="Branch-Wise Sales")
st.plotly_chart(fig)

st.write("### Thank you for visiting the dashboard!")
