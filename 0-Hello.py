import streamlit as st

def run():
    st.set_page_config(
        page_title="Boba Drink Calculator",
        page_icon="🧋",
        layout="centered",
        initial_sidebar_state="expanded",
    )
    st.write("# Welcome to Boba Drink Calculator! 👋")

    st.markdown("""
    <h2 style='color:grey; font-size:20px;'>Your ultimate webapp designed to help you make healthier beverage choices on the go!</h2>
    """, unsafe_allow_html=True)

    st.markdown(
        """
       This innovative app provides an array of features that empower you to understand and compare the caloric impact of various boba tea drinks 波霸奶茶.
       
       Here’s what you can do with Boba Drink Calculator:

       1. **Calorie Calculator:** Quickly determine the calories in your favorite beverages. Select from popular brands and customize by drink size and variations for instant, accurate results.

            1.1 **Calories Comparison Tool**: Compare the calorie content of your drinks with alternative food equivalents. Utilize our comprehensive food API for visual insights and detailed nutritional trade-offs.

       2. **Store Locator:** Find where to buy your favorite drinks with ease. Our integration with Google Maps API allows you to search by postal code or city to discover nearby store locations.

       3. **Data Visualization:** Explore the nutritional landscape with interactive plots. View key calorie data across various brands and types, empowering you to make well-informed choices.

       👈 Select a demo from the sidebar to see what you can use the calculator to do！
    """
    )

if __name__ == "__main__":
    run()
