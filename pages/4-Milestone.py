import streamlit as st

Research_Questions1_3, Research_Questions_4_8= st.tabs(['Research_Questions1_3' , 'Research_Questions4_8'])

with Research_Questions1_3:
    st.markdown('''
            
    1. Developer Name
                    
        **Shufan Mao**


    2. An explanation of how to use your webapp: what interactivity there is, what the plots/charts mean, what your conclusions were, etc.
                
        **How to Navigate:** 
        
        a. **Hello Page:** All features are accessible from the main menu.
        
        b. **Calorie Calculator & Comparison Tool:** Once a drink is selected, detailed calories information will be displayed, and customization size options are provided.
        
        c. **Store Locator Page:** Enter location to find nearby bubble tea stores and display a map.
        
        d. **Visualization Page:** Interactive charts visualize the results based on your selections and inputs.
        
        e. **Milestone Page:** Detailed information about the project and answer research questions.

        f. **Data Description Page:** Information about the data used in the project.
        
                    
    3. Any major “gotchas” (i.e. things that don’t work, go slowly, could be improved, etc.)      
        
        **Known Limitations and Issues**
      
        **Performance Issues:** The map feature may respond slightly slower due to API constraints and the overhead of downloading images. Minor errors may occur across the app.
        
        **Feature Availability:** Some functionalities, such as topping options, are not yet fully implemented.
      
        **Usability:** Efforts will be made to enhance the design and overall user experience in future updates.    
    
        **FYI:** Some websites are poorly developed because when I tried to scrape certain data, the structure is not consistent so the scrapper may not apply to all cases. Sometimes it might be due to a typo, and then the code may not work. For example, there was a case that "matcha" was misspelled as "match", leading to wrong returned values. 
                
                e.g.[Chatime Matcha Latte Milk Tea](https://chatime.com/drinks/match-latte-milk-tea/)
    ''')
     
with Research_Questions_4_8:
     st.markdown('''
    
    4. What did you set out to study?  (i.e. what was the point of your project?  This should be close to your Milestone 1 assignment, but if you switched gears or changed things, note it here.)
        
        **Purpose:** Initiated to demystify the nutritional content of bubble tea—a popular choice with often underestimated caloric content—the tool aims not just to calculate caloric intake but also to educate users on healthier consumption patterns.
        
    5. What did you Discover/what were your conclusions (i.e. what were your findings?  Were your original assumptions confirmed, etc.?)

        **Discoveries:** The project confirmed my assumptions about caloric variations across different drinks and brands. For example, pure tea categories generally contain fewer calories. However, many milk tea drinks surpass the calorie content of typical Starbucks refreshers, with some reaching up to 700 kcal, about a third of the daily intake recommended for a 2000 calorie diet.
        
    6. What difficulties did you have in completing the project?

        **Data Scraping:** Inconsistencies in website development affected the data scraping efficiency. For instance, a typographical error like "match" instead of "matcha" led to incorrect or null data retrievals.
        
        **Data Integration:** Initial difficulties with integrating VS Code and GitHub Codespace presented technical hurdles that were eventually overcome.
        
        **Data Management:** While initially planned to use SQL for data management, the project's current scope was adequately managed with pandas. As more brands get integrated, transitioning to a more robust database may become necessary.
        
        **Data Visualization:** The project's data visualization capabilities were limited by the Streamlit library. Future iterations may benefit from more advanced visualization tools like Plotly.

    7. What skills did you wish you had while you were doing the project?
            
        **Desired Skills:**
        Advanced Web Scraping: Enhanced web scraping skills would have expedited data collection and improved the project's efficiency.
        Data Management: Proficiency in SQL would have facilitated more efficient data management and integration.
        Advanced Visualization: Advanced data visualization skills would have enabled more sophisticated and interactive data representations.

    8. What would you do “next” to expand or augment the project?
        
        **Future Enhancements:**
        User Profiles: Introduce profiles to track and analyze personal consumption over time.
        Expanded Database: Include more brands and regional varieties, alongside enhanced data visualization tools.
        Health Recommendations: Incorporate generative AI to provide personalized health tips based on user's consumption patterns.
        
            
    See the detiled TXT version in milestone3.txt.
                 
    '''
    )