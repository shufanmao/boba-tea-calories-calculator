import streamlit as st
import pandas as pd
import os
import requests

def load_data(file_path):
    """Load the drinks data from a CSV file."""
    return pd.read_csv(file_path)

def display_calories_coco_chatime(drinks_data, selected_drink, selected_brand):
    """Display calories and images for Coco, Chatime, and Kungfu brands."""
    if selected_brand in ['coco', 'chatime']:
        # Determine available sizes based on non-empty calorie information
        size_options = ['Small', 'Medium', 'Big']
        available_sizes = []
        for size in size_options:
            calorie_column = f"{size} Size Calories"
            # Check if the column exists and if it has non-empty values for the selected drink
            if calorie_column in drinks_data.columns:
                if not pd.isna(drinks_data.loc[drinks_data['Drink Name'] == selected_drink, calorie_column].iloc[0]):
                    available_sizes.append(size)

        if available_sizes:
            selected_size = st.selectbox("Choose the size:", available_sizes)
            calorie_column = f"{selected_size} Size Calories"
            # Display calories
            calories = drinks_data.loc[drinks_data['Drink Name'] == selected_drink, calorie_column].iloc[0]
            st.write(f"{selected_size} size: {calories} kcal")
        else:
            st.write("No available calorie information for this drink.")

        # Attempt to display an image if the path is available
        if 'Path' in drinks_data.columns:
            image_path = drinks_data.loc[drinks_data['Drink Name'] == selected_drink, 'Path'].iloc[0]
            if os.path.exists(image_path):
                st.image(image_path, caption=selected_drink)
        else:
            pass
        return calories
    
def display_calories_kungfu(drinks_data, selected_drink, selected_toppings, toppings_data):
    """Display calories and images for Kungfu brand with optional toppings."""
    # Determine available drink sizes based on non-empty calorie information
    size_options = ['Small', 'Medium', 'Big']
    available_sizes = []
    for size in size_options:
        calorie_column = f"{size} Size Calories"
        if calorie_column in drinks_data.columns and not pd.isna(drinks_data.loc[drinks_data['Drink Name'] == selected_drink, calorie_column].iloc[0]):
            available_sizes.append(size)

    if available_sizes:
        selected_size = st.selectbox("Choose the drink size:", available_sizes)
        calorie_column = f"{selected_size} Size Calories"
        base_calories = drinks_data.loc[drinks_data['Drink Name'] == selected_drink, calorie_column].iloc[0]
        st.write(f"{selected_size} size: {base_calories} kcal")
    else:
        st.write("No available calorie information for this drink.")
        return 0  # Return early if no calorie data is available

    total_calories = base_calories

    # Ensure topping selections come after drink size selection
    if selected_toppings:
        for topping in selected_toppings:
            if topping in toppings_data['Topping'].values:
                # Assume sizes are in the data and allow user to select size
                topping_sizes = toppings_data[toppings_data['Topping'] == topping]['Size'].unique()
                if topping_sizes.size > 0:
                    selected_topping_size = st.selectbox(f"Choose size for {topping}:", topping_sizes)
                    topping_calories = toppings_data[(toppings_data['Topping'] == topping) & (toppings_data['Size'] == selected_topping_size)]['Calories'].iloc[0]
                    total_calories += topping_calories
                    st.markdown(f"Added <em>{topping}</em> will add <span style='color:red; font-weight:bold;'>{topping_calories}</span> kcal</span>", unsafe_allow_html=True)
                else:
                    st.write("No size data for selected topping.")
            else:
                st.write(f"Topping {topping} not found in the data.")

    # Display total calories
    st.write(f"Total Calories for your selection: {total_calories} kcal")

    # Attempt to display an image if the path is available
    if 'Path' in drinks_data.columns and os.path.exists(drinks_data.loc[drinks_data['Drink Name'] == selected_drink, 'Path'].iloc[0]):
        st.image(drinks_data.loc[drinks_data['Drink Name'] == selected_drink, 'Path'].iloc[0], caption=selected_drink)

    return total_calories
           
def display_calories_sharetea(drinks_data, selected_drink, selected_toppings, toppings_data):
    """Function to display total calories for a Sharetea drink with optional toppings."""
    total_calories = 0
    # Check if the drink data has a 'Calories' column and the drink exists in the data
    if 'Calories' in drinks_data.columns and selected_drink in drinks_data['Drink Name'].values:
        drink_calories = drinks_data[drinks_data['Drink Name'] == selected_drink]['Calories'].iloc[0]
        total_calories += drink_calories
        st.write(f"Calories for your selected drink: {drink_calories} kcal")
    else:
        st.write("Selected drink not found in the data.")

    # Add calories for each selected topping
    for topping in selected_toppings:
        if topping in toppings_data['Topping'].values:
            topping_calories = toppings_data[toppings_data['Topping'] == topping]['Calories'].iloc[0]
            total_calories += topping_calories
            st.markdown(f"Added <em>{topping}</em> will add <span style='color:red; font-weight:bold;'>{topping_calories}</span> kcal</span>", unsafe_allow_html=True)

    # Display total calories
    st.write(f"Total Calories for your selection: {total_calories} kcal")
    return total_calories

def display_calories_boba_time(drinks_data, filter_conditions, selected_drink):
    """Function to display calories for Boba Time brand."""
    if 'Size' in drinks_data.columns:
        size_options = drinks_data.loc[drinks_data['Drink Name'] == selected_drink, 'Size'].dropna().unique()
        if size_options.size > 0:
            selected_size = st.selectbox("Choose the size:", size_options)
            filter_conditions &= (drinks_data['Size'] == selected_size)
            filtered_data = drinks_data[filter_conditions]
            if not filtered_data.empty and 'Calories' in filtered_data.columns:
                calories = filtered_data['Calories'].iloc[0]
                st.write(f"Calories for your selection: {calories} kcal")
            else:
                st.write("No data available for the selected size. Please try different selections.")
        else:
            st.write("No sizes available for the selected drink.")
    else:
        st.write("Size information is not available for this brand.")
    return calories

def get_nutrition_info(food_query, api_key):
    """Retrieve nutrition info for a given food item from API Ninjas."""
    url = f"https://api.api-ninjas.com/v1/nutrition?query={food_query}"
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  # Returns the data as a Python dictionary
    else:
        return None
    
def calculate_equivalent_drink_to_food(drink_calories, food_calories):
    """Calculate how many servings of the food match the calories of one drink."""
    if food_calories > 0:  # Avoid division by zero
        return drink_calories / food_calories
    return 0

def main():
    st.title('Boba Tea Calorie Calculator')

    # Define configurations for each brand
    brand_files = {
        "coco": "data/csv/coco.csv",
        "chatime": "data/csv/chatime.csv",
        "kungfu": "data/csv/kungfu_simple.csv",
        "sharetea": "data/csv/sharetea.csv",
        "boba_time": "data/csv/bobatime.csv"
    }
    toppings_files = {
        "topping_sharetea": "data/csv/topping_sharetea.csv",
        "topping_kungfu": "data/csv/topping_kungfu.csv"
        #"topping_gongcha": "data/csv/topping_gongcha.csv"
    }

    # Let user choose a brand
    selected_brand = st.selectbox("Select a brand:", list(brand_files.keys()))

    # Load data for the selected brand
    drinks_data = load_data(brand_files[selected_brand])
    
    # User selects a drink
    selected_drink = st.selectbox("Choose your drink:", drinks_data['Drink Name'].unique())
    
    if selected_brand in ['sharetea', 'kungfu']:
        toppings_file = toppings_files[f"topping_{selected_brand}"]
        toppings_data = load_data(toppings_file)
        selected_toppings = st.multiselect('Add Toppings', toppings_data['Topping'].unique())

    drink_calories = 0
    if selected_brand in ['coco', 'chatime']:
        drink_calories = display_calories_coco_chatime(drinks_data, selected_drink, selected_brand)
    elif selected_brand == 'kungfu':
        drink_calories = display_calories_kungfu(drinks_data, selected_drink, selected_toppings, toppings_data)
    elif selected_brand == 'sharetea':
        drink_calories = display_calories_sharetea(drinks_data, selected_drink, selected_toppings, toppings_data)
    elif selected_brand == 'boba_time':
        filter_conditions = pd.Series([True] * len(drinks_data))
        drink_calories = display_calories_boba_time(drinks_data, filter_conditions, selected_drink)
    
    st.markdown("---")  # Adds a horizontal line for visual separation

    # Section for Nutrition Information Finder
    st.header('Nutrition Information Finder')
    food_query = st.text_input('Enter a food item to compare \n (e.g., "apple", "In N Out Burger" , "bowl of rice" , "steaks with mashed potatoes" , "plate of spaghetti" , "slice of pizza" , "bowl of salad" , "cup of milk")')
    api_key = 'vr/VAkNJkIuMPZgxq/gZIg==cBNGmsFYmZ7PLy98'  

    if st.button('Get Nutrition Info', key='nutrition'):
        if food_query:
            result = get_nutrition_info(food_query, api_key)
            if result and len(result) > 0:
                item = result[0]
                food_calories = float(item.get('calories', 0))
                st.subheader("Nutrition Information:")
                st.write(f"**Serving Size** {item.get('serving_size_g', 'N/A')} grams")
                st.write(f"**Calories:** {item.get('calories', 'N/A')} kcal")
                st.write(f"**Sugar:** {item.get('sugar_g', 'N/A')} grams")
                st.write(f"**Fat Total:** {item.get('fat_total_g', 'N/A')} grams")
                st.write(f"**Saturated Fat:** {item.get('fat_saturated_g', 'N/A')} grams")
                st.write(f"**Protein:** {item.get('protein_g', 'N/A')} grams")
                st.write(f"**Sodium:** {item.get('sodium_mg', 'N/A')} mg")
                st.write(f"**Potassium:** {item.get('potassium_mg', 'N/A')} mg")
                st.write(f"**Cholesterol:** {item.get('cholesterol_mg', 'N/A')} mg")
                st.write(f"**Carbohydrates Total:** {item.get('carbohydrates_total_g', 'N/A')} grams")
                st.write(f"**Fiber:** {item.get('fiber_g', 'N/A')} grams")
                
                if drink_calories > 0 and food_calories > 0:
                    servings_equivalent = calculate_equivalent_drink_to_food(drink_calories, food_calories)
                    servings_equivalent = int(round(servings_equivalent, 0))
                    st.write("")
                    
                    st.markdown(f"<span style='font-size:20px; color:red;'><b>1 {selected_drink} = {servings_equivalent} * {item.get('serving_size_g', 'N/A')}g {food_query}{'(s)' if servings_equivalent > 1 else ''}</b></span>", unsafe_allow_html=True)

                    st.write("")
                    st.write("**Nutrition facts: The Percent Daily Values are based on a 2,000 calorie diet, so your values may change depending on your calorie needs.*")
            else:
                st.error('Failed to retrieve data or no data available. Try again with a different food item.')
        else:
            st.error('Please enter a valid food item.')

if __name__ == "__main__":
    main()
