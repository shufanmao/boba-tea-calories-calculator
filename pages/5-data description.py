import streamlit as st

st.markdown('''
# Data Description
''')

Boba_Tea_Brands, CSV_Folder, Picture_Folder, Downloaded_data= st.tabs(['Boba_Tea_Brands', 'CSV_Folder', 'Picture_Folder' , 'Downloaded_data'])

with Boba_Tea_Brands:
    st.markdown('''
    Boba Tea Brands Available:
    1. Gong Cha
        - [Nutritional Information](https://gongchausa.com/nutritional-information/)
    2. Kung Fu Tea
        - [Nutritional Information](https://www.kungfutea.com/)
    3. Sharetea
        - [Nutritional Information](https://www.1992sharetea.com/nutrition-facts)
    4. Coco 
        - [Menu](https://cocobubbletea.com/menu)
    5. Boba Time
        - [Website](https://itsbobatime.com/)
    6. Chatime
        - [Website](https://chatime.com/)
    ''')

with CSV_Folder:
    st.markdown('''
    CSV Folder Path 
                
        data/csv
    
    CSV files which contain calories information for each brand:      
                
        - boba time.csv
        - chatime_drinks_calories.csv
        - coco_drinks_calories.csv
        - coco_output
        - gongcha.csv
        - kungfu.csv
        - share tea.csv
                
    CSV files which contain topping files: ##which are distracted from calories files.
        
        - toppings_gongcha.csv
        - toppings_sharetea.csv
                
    CSV files which contain brand matching paths: 
        
        - brand.csv
    ''')

with Picture_Folder:
    st.markdown('''
    Picture folder which contains drink pictures from different brands.
                
        - data/pic/coco
        - data/pic/gongcha  
    ''')

with Downloaded_data:
    st.markdown('''
    Downloaded data folder which contains pdf or csv files donwloaded from different each brands' websites.
                       
        path = data/downloaded_data
                
    The Collection of all downloaded data:
        
        All Boba Tea Calorie Information.xlsx

              
    ''')