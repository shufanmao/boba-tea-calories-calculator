import streamlit as st

def run():
    st.set_page_config(
        page_title="Boba Tea Drink Calculator",
        page_icon="🧋",
        layout="centered",
        initial_sidebar_state="expanded",
    )
    st.write("# Welcome to Boba Tea Calculator!🧋 ")

    st.markdown("""
    <h2 style='color:grey; font-size:20px;'>Your ultimate webapp designed to help you make healthier beverage choices on the go!</h2>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h3 style='color:grey; font-size:15px;'>Developed by Shufan Mao for class DSCI510.</h2>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        This innovative app provides an array of features that empower you to understand and compare the caloric impact of various boba tea drinks 波霸奶茶.
      
        Here’s what you can do with Boba Drink Calculator:
        
        🍵 **a. Brand and Drink Selection:** Begin by selecting a bubble tea brand and a specific drink from the database.
        
        🔮 **b. Customization:** Enhance your drink by choosing brands, sizes and toppings. Each addition updates the calorie count, providing a visual representation of the nutritional impact.
        
        🧮 **c. Caloric Comparisons:** Compare the calories of your customized drink with common foods you input, such as fruits or snacks, to better understand their nutritional values. Caluculate the calories of the food you input equivalently to the drink you selected.
        
        📍 **d. Store Locator:** Utilize the geolocation feature to find nearby bubble tea stores, complete with detailed information including opening hours and ratings displayed on an interactive map. Can perform fuzzy search and support different languages. 
        
        📈 **e. Data Visualization:** Explore the nutritional landscape with interactive plots. View key calorie data across various brands and types, empowering you to make well-informed choices.

        📄 **f. milestong Page:** Slide to see the file names and path.
        
        📄 **g. Data Description Page:** Slide to see the data description of the project.
          
        
       👈 Select a demo from the sidebar to see what you can use this calculator to do！
    """
    )
if __name__ == "__main__":
    run()
