import streamlit as st
import pandas as pd
import plotly.express as px

# Load datasets
def load_data():
    files = {
        "Coco": "data/csv/coco_drinks_calories.csv",
        "Kungfu": "data/csv/kungfu.csv",
        "Chatime": "data/csv/chatime_drinks_calories.csv",
        "Sharetea": "data/csv/share tea.csv",
        "Boba Time": "data/csv/boba time.csv",
        "Gongcha": "data/csv/gongcha.csv"
    }
    data = {name: pd.read_csv(path) for name, path in files.items()}
    return data

data = load_data()
# Streamlit sidebar options
brand = st.sidebar.selectbox('Select the brand:', list(data.keys()))
chart_type = st.sidebar.selectbox('Select chart type:', ['Bar Chart', 'Pie Chart', 'Histogram'])

# Display data
st.write(f"Data for {brand}:")
st.dataframe(data[brand].head())

# Function to create bar chart
def create_bar_chart(df, x, y):
    fig = px.bar(df, x=x, y=y)
    st.plotly_chart(fig)

# Function to create pie chart
def create_pie_chart(df, values, names):
    fig = px.pie(df, values=values, names=names)
    st.plotly_chart(fig)

# Function to create histogram
def create_histogram(df, x):
    fig = px.histogram(df, x=x)
    st.plotly_chart(fig)

# Plotting based on selection
if chart_type == 'Bar Chart':
    create_bar_chart(data[brand], 'Drink Name', 'Calories')  # Update 'Calories' if necessary to match your column names
elif chart_type == 'Pie Chart':
    create_pie_chart(data[brand], 'Calories', 'Drink Name')  # Update 'Calories' if necessary
elif chart_type == 'Histogram':
    create_histogram(data[brand], 'Calories')  # Update 'Calories' if necessary

