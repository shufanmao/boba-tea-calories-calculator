# import streamlit as st
# import pandas as pd
# import os
# import requests

# def load_data(file_path):
#     """Load the drinks data from a CSV file."""
#     return pd.read_csv(file_path)

# def get_nutrition_info(food_query, api_key):
#     """Retrieve nutrition info for a given food item from API Ninjas."""
#     url = f"https://api.api-ninjas.com/v1/nutrition?query={food_query}"
#     headers = {"X-Api-Key": api_key}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.json()  # Returns the data as a Python dictionary
#     else:
#         return None

# def calculate_equivalent_drink_to_food(drink_calories, food_calories):
#     """Calculate how many servings of the food match the calories of one drink."""
#     if food_calories > 0:  # Avoid division by zero
#         return drink_calories / food_calories
#     return 0

# def main():
#     st.title('Boba Tea and Nutrition Information Center')

#     # Load brand information
#     brand_data_path = 'data/csv/brand.csv'
#     brand_data = pd.read_csv(brand_data_path)
#     brand_options = brand_data['Brand'].unique()
#     selected_brand = st.selectbox("Choose a brand:", brand_options)

#     # Find CSV path for selected brand
#     csv_file_path = brand_data[brand_data['Brand'] == selected_brand]['CSV Path'].iloc[0]
#     drinks_data = load_data(csv_file_path)
#     drink_options = drinks_data['Drink Name'].unique()
#     selected_drink = st.selectbox("Choose your drink:", drink_options)

#     # Example of handling drink selection and displaying nutrition
#     if selected_drink:
#         st.write(f"You selected {selected_drink} from {selected_brand}")

#         if cup_size in size_calorie_map:
#             calorie_column = size_calorie_map[cup_size]
#             if calorie_column in drink_details:
#                 drink_calories = drink_details[calorie_column]

#         if cup_size == 'Medium Size':
#             if 'Medium Size' in drink_details:
#                 st.markdown(f"Calories for {selected_drink} ({cup_size}): **<span style='color:red'>{drink_calories} kcal</span>**", unsafe_allow_html=True)
#             else:
#                 st.write("There is no such size available for this drink.")

#         elif cup_size == 'Small Size':
#             if 'Small Size' in drink_details:
#                 st.write("There is no such size available for this drink.")
#             else:
#                 st.markdown(f"Calories for {selected_drink} ({cup_size}): **<span style='color:red'>{drink_calories} kcal</span>**", unsafe_allow_html=True)

#         elif cup_size == 'Big Size':
#             if 'Big Size' in drink_details:
#                 st.write("There is no such size available for this drink.")
#             else:
#                 st.markdown(f"Calories for {selected_drink} ({cup_size}): **<span style='color:red'>{drink_calories} kcal</span>**", unsafe_allow_html=True)

#         image_path = drink_details['Path']
#         if os.path.exists(image_path):
#             st.image(image_path, caption=selected_drink, use_column_width=True)
#         else:
#             st.write("No image available for this drink.")

#         image_path = drink_details['Path']
#         if os.path.exists(image_path):
#             st.image(image_path, caption=selected_drink, use_column_width=True)
#         else:
#             st.write("No image available for this drink.")

   
#     st.markdown("---")  # Adds a horizontal line for visual separation

#     # Section for Nutrition Information Finder
#     st.header('Nutrition Information Finder')
#     food_query = st.text_input('Enter a food item to compare \n (e.g., "apple", "In N Out Burger" , "bowl of rice" , "steaks with mashed potatoes" , "plate of spaghetti" , "slice of pizza" , "bowl of salad" , "cup of milk")')
#     quantity = st.number_input('Enter the quantity of the food item:', min_value=1, value=1, step=1)
#     api_key = 'vr/VAkNJkIuMPZgxq/gZIg==cBNGmsFYmZ7PLy98'  

#     if st.button('Get Nutrition Info', key='nutrition'):
#         if food_query:
#             result = get_nutrition_info(food_query, api_key)
#             if result and len(result) > 0:
#                 item = result[0]
#                 food_calories = item.get('calories', 0) * quantity
#                 st.subheader("Nutrition Information (per 100g serving):")
#                 st.markdown(f"**Calories:** {item.get('calories', 'N/A')} kcal for {quantity}x {food_query}")
#                 st.markdown(f"**Fat:** {item.get('fat', 'N/A')} grams")
#                 st.markdown(f"**Carbohydrates:** {item.get('carbs', 'N/A')} grams")
#                 st.markdown(f"**Protein:** {item.get('protein', 'N/A')} grams")
#                 st.markdown(f"**Sugar:** {item.get('sugar', 'N/A')} grams")
#                 if drink_calories > 0 and food_calories > 0:
#                     servings_equivalent = calculate_equivalent_drink_to_food(drink_calories, food_calories / quantity)
#                     servings_equivalent = int(round(servings_equivalent, 0))
#                     st.markdown(f"#### 1 {cup_size} {selected_drink} = {servings_equivalent} {food_query}{'s' if servings_equivalent > 1 else ''}")
#             else:
#                 st.error('Failed to retrieve data or no data available. Try again with a different food item.')
#         else:
#             st.error('Please enter a valid food item.')

# if __name__ == "__main__":
#     main()



import streamlit as st
import pandas as pd
import os
import requests

def load_data(file_path):
    """Load the drinks data from a CSV file."""
    return pd.read_csv(file_path)

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
    st.title('Boba Tea and Nutrition Information Center')

    # Section for Boba Tea Drinks Calorie Calculator
    st.header('Boba Tea Drinks Calorie Calculator')
    drinks_data = load_data('data/csv/coco_output.csv')
    drink_options = drinks_data['Drink Name'].unique()
    selected_drink = st.selectbox("Choose your drink:", drink_options)
    cup_size_options = ['Small Size', 'Medium Size', 'Big Size']
    cup_size = st.radio("Choose your cup size:", cup_size_options)

    drink_calories = 0
    if selected_drink:
        drink_details = drinks_data[drinks_data['Drink Name'] == selected_drink].iloc[0]
        size_calorie_map = {
            'Small Size': 'Small Size Drink Calories',
            'Medium Size': 'Medium Size Drink Calories',
            'Big Size': 'Big Size Drink Calories'
    }
        if cup_size in size_calorie_map:
            calorie_column = size_calorie_map[cup_size]
            if calorie_column in drink_details:
                drink_calories = drink_details[calorie_column]

        if cup_size == 'Medium Size':
            if 'Medium Size' in drink_details:
                st.markdown(f"Calories for {selected_drink} ({cup_size}): **<span style='color:red'>{drink_calories} kcal</span>**", unsafe_allow_html=True)
            else:
                st.write("There is no such size available for this drink.")

        elif cup_size == 'Small Size':
            if 'Small Size' in drink_details:
                st.write("There is no such size available for this drink.")
            else:
                st.markdown(f"Calories for {selected_drink} ({cup_size}): **<span style='color:red'>{drink_calories} kcal</span>**", unsafe_allow_html=True)

        elif cup_size == 'Big Size':
            if 'Big Size' in drink_details:
                st.write("There is no such size available for this drink.")
            else:
                st.markdown(f"Calories for {selected_drink} ({cup_size}): **<span style='color:red'>{drink_calories} kcal</span>**", unsafe_allow_html=True)

        image_path = drink_details['Path']
        print(image_path)
        if os.path.exists(image_path):
            st.image(image_path, caption=selected_drink, use_column_width=True)
        else:
            st.write("No image available for this drink.")

        # image_path = drink_details['Path']
        # if os.path.exists(image_path):
        #     st.image(image_path, caption=selected_drink, use_column_width=True)
        # else:
        #     st.write("No image available for this drink.")

   
    st.markdown("---")  # Adds a horizontal line for visual separation

    # Section for Nutrition Information Finder
    st.header('Nutrition Information Finder')
    food_query = st.text_input('Enter a food item to compare \n (e.g., "apple", "In N Out Burger" , "bowl of rice" , "steaks with mashed potatoes" , "plate of spaghetti" , "slice of pizza" , "bowl of salad" , "cup of milk")')
    quantity = st.number_input('Enter the quantity of the food item:', min_value=1, value=1, step=1)
    api_key = 'vr/VAkNJkIuMPZgxq/gZIg==cBNGmsFYmZ7PLy98'  

    if st.button('Get Nutrition Info', key='nutrition'):
        if food_query:
            result = get_nutrition_info(food_query, api_key)
            if result and len(result) > 0:
                item = result[0]
                food_calories = item.get('calories', 0) * quantity
                st.subheader("Nutrition Information (per 100g serving):")
                st.markdown(f"**Calories:** {item.get('calories', 'N/A')} kcal for {quantity}x {food_query}")
                # st.markdown(f"**Fat:** {item.get('fat', 'N/A')} grams")
                # st.markdown(f"**Carbohydrates:** {item.get('carbs', 'N/A')} grams")
                # st.markdown(f"**Protein:** {item.get('protein', 'N/A')} grams")
                # st.markdown(f"**Sugar:** {item.get('sugar', 'N/A')} grams")
                if drink_calories > 0 and food_calories > 0:
                    servings_equivalent = calculate_equivalent_drink_to_food(drink_calories, food_calories / quantity)
                    servings_equivalent = int(round(servings_equivalent, 0))
                    st.markdown(f"#### 1 {cup_size} {selected_drink} = {servings_equivalent} {food_query}{'s' if servings_equivalent > 1 else ''}")
            else:
                st.error('Failed to retrieve data or no data available. Try again with a different food item.')
        else:
            st.error('Please enter a valid food item.')

if __name__ == "__main__":
    main()