import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt

# Define a function to load the brand configuration data with improved caching
@st.cache_data

def load_brand_data():
    st.cache_data.clear() 
    try:
        # Correct path should be provided here
        return pd.read_csv("/Users/shufanmao/Documents/GitHub/boba-tea-calories-calculator/data/csv/brand.csv")
    except FileNotFoundError:
        st.error("Brand data file not found. Please check the file path.")
        st.stop()  # Halt execution
    except Exception as e:
        st.error(f"An error occurred while loading brand data: {str(e)}")
        st.stop()  # Halt execution

# Attempt to load the brand data
brand_data = load_brand_data()

# Verify that brand_data is loaded successfully
if brand_data is None or brand_data.empty:
    st.error("Failed to load brand data or data is empty.")
    st.stop()

# Function to load data for a specific brand with caching
@st.cache_data
def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        st.error(f"Failed to load data from {file_path}: {str(e)}")
        st.stop()

# Sidebar for Brand selection
brand_choice = st.sidebar.selectbox('Select the brand:', brand_data['Brand'])
selected_brand = brand_data[brand_data['Brand'] == brand_choice].iloc[0]

# Load specific brand data based on CSV Path
data = load_data(selected_brand['CSV Path'])

# Sidebar for Data Column and Chart Type selection
column_options = [selected_brand[col] for col in brand_data.columns if col.startswith('Column') and pd.notna(selected_brand[col])]
selected_x_column = st.sidebar.selectbox('Select X-axis data:', column_options)
selected_y_column = st.sidebar.selectbox('Select Y-axis data:', column_options, index=1 if len(column_options) > 1 else 0)
chart_type = st.sidebar.radio("Select chart type:", ('Box Plot', 'Histogram', 'Pie Chart', 'Scatter Plot'))

# Function to create and display charts based on selected type
def create_chart(df, x_col, y_col, chart_type):
    plt.figure(figsize=(10, 5))
    if chart_type == 'Box Plot':
        plt.boxplot(pd.to_numeric(df[x_col], errors='coerce').dropna())
        plt.title(f"Box Plot of {x_col}")
    elif chart_type == 'Histogram':
        plt.hist(pd.to_numeric(df[y_col], errors='coerce').dropna(), bins=15, color='skyblue')
        plt.title(f"Histogram of {y_col}")
    elif chart_type == 'Pie Chart':
        pie_data = df[y_col].dropna().value_counts()
        plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
        plt.title(f"Pie Chart of {y_col}")
    elif chart_type == 'Scatter Plot':
        plt.scatter(pd.to_numeric(df[x_col], errors='coerce').dropna(), pd.to_numeric(df[y_col], errors='coerce').dropna())
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f"Scatter Plot of {x_col} vs {y_col}")
    plt.tight_layout()
    st.pyplot(plt)

# Display DataFrame and create chart based on user selections
st.write(f"Displaying data for {brand_choice}:")
st.dataframe(data.head())
create_chart(data, selected_x_column, selected_y_column, chart_type)
