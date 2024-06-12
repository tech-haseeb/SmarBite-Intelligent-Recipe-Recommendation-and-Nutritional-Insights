


#import libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import json
import matplotlib.patches as mpatches
from matplotlib import cm
from matplotlib.font_manager import FontProperties
import seaborn as sns

# adding title in streamlit
st.sidebar.markdown(f"<span style='color: black;font-size: 36px;font-weight: bold;'>SmartBite </span>", unsafe_allow_html=True)

st.sidebar.info("Welcome to SmartBite Data Analytics. Here, you can find out the nutritional value of different foods.")

#read csv file
DATA_URL = ("resources/assets_modified/01.csv")

DATA_URL2 = ("resources/recipe_page/recipe.csv")


#for data caching
@st.cache_data(persist=True)



#to load the csv file
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

def load_data2():
    data2 = pd.read_csv(DATA_URL2)
    return data2


#to load the csv file and display it
data = load_data()
data2= load_data2()

#global variable/dataframe
#path to the csv file of the ifct database for demographics page
df_demographics = pd.read_csv("resources/assets_modified/01cat.csv")
df_demographics_nonveg= pd.read_csv("resources/assets_modified/02cat.csv")

#drop row/column if all values there are NA
df_demographics.dropna()


#the main function that is called first and foremost with the navigation options in the sidebar
def main():
    # Register your pages
    pages = {
        "About": about_page,
        "Ingredient Information": page_first,
        "Medical Condition Demographics":disease_demographics,
        "Search for Recipe": page_second,
        "Calorie Calculator": page_three,
        "Calories and Cuisine": page_fourth,
    
        
    }
    st.sidebar.title("Navigation 🧭")
    # Widget to select your page, you can choose between radio buttons or a selectbox
    page = st.sidebar.radio("(Choose an option to get redirected)", tuple(pages.keys()))
    
    # Display the selected page
    pages[page]()

 


#function for the about page
def about_page():
    st.markdown("<h1 style='text-align: center;'>SmartBite 🍕🧈🥙 🍲 🩺</h1>", unsafe_allow_html=True)
    st.image('pic2.jpg')
    st.subheader("About SmartBite 🤔")

    #all the necessary descriptions
    st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Arial, sans-serif;line-height: 1.5;'>Food is an essential parameter that plays an important role in the survival of humans. It also plays a major part in depicting a country’s culture. Healthy, nutritious, and high-quality food results in not only a better lifestyle but also develops a person’s immunity and health. Likewise, the consumption of low-quality food which might be deprived of nutritional value impacts a person’s health negatively and makes them susceptible to all types of diseases. In India, there is a persistent complaint, in any civic body-related food section, about the quality of meals available. Likewise, the quality of the oil is also an important factor while cooking any meal. Therefore, the Quality of oil used in frying the food to affect its taste must be monitored too. Its continuous exposure to relatively high temperatures results in degradation of its quality. The purpose of this study is to build an application for the detection of the quality of food and also to detect repeated frying on cooking oils based on the visual properties of the oils. Classification of food items is done on the basis of time left for consumption, edibility, quality, color, and rancidity. The food items are further classified as stale or usable using artificial intelligence algorithms based on the images acquired through a Cell Phone’s camera.</h6>", unsafe_allow_html=True)
    st.subheader("System Diagram ♺")
    st.image('pic1.png')

    
    

    

#first page function
def page_first():
    st.title("🍉 🍓 🍒  ")
    st.title("SmartBite Ingredient Information")
    st.title(" 🍅 🥕 🥒 ")

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.2;'>To help your body grow properly, stay healthy, and have energy all day, you need to eat enough of all nutrients. These include proteins, carbohydrates, fats, vitamins, minerals, and water. That's why knowing the nutritional value of food is very important. Here, you can find out how much of each nutrient is in different foods, whether you eat them alone or as part of a dish.</h6>",unsafe_allow_html=True)

    
    food_list = st.selectbox("Search your ingredient here:", data["name"].unique())


    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Filter Data Results are :</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>You selected- {food_list}</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>Nutritional Analysis for your selection is as follows-</span>", unsafe_allow_html=True)

    #counts of various nutritional contents of a food item
    count_water = data.loc[(data["name"] == food_list) , 'water'].iloc[0]
    count_protein = data.loc[(data["name"] == food_list) , 'protcnt'].iloc[0]
    count_ash = data.loc[(data["name"] == food_list) , 'ash'].iloc[0]
    count_fat = data.loc[(data["name"] == food_list) , 'fatce'].iloc[0]
    count_fibretotal = data.loc[(data["name"] == food_list) , 'fibtg'].iloc[0]
    count_fibreinsoluble = data.loc[(data["name"] == food_list) , 'fibins'].iloc[0]
    count_fibresoluble = data.loc[(data["name"] == food_list) , 'fibsol'].iloc[0]
    count_carbohydrate = data.loc[(data["name"] == food_list) , 'choavldf'].iloc[0]
    count_energy = data.loc[(data["name"] == food_list) , 'enerc'].iloc[0]

    #displaying the corresponding values to the above parameters
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Water- {count_water}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Protein- {count_protein}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Ash- {count_ash}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Fat- {count_fat}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Total Fibre- {count_fibretotal}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Insoluble Fibre- {count_fibreinsoluble}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Soluble Fibre- {count_fibresoluble}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Carbohydrates- {count_carbohydrate}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Energy- {count_energy}kJ</span>", unsafe_allow_html=True)
    

    
    
    #to print a small iframe of the csv file using the checkbox
    raw_data=st.checkbox('See Raw Data')
    if raw_data: 
        st.write(data)

    
def page_second():

    #sidebar title
    st.title("Search for a Recipe 😋")
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>All recipes require a variety of ingredients, such as vegetables, flour, spices and milk products. Here, you can search the possible dishes with any desired combination of ingredients. You can also view the calories in the dish and the cuisine. Please enter a minimum of two ingredients to search for dishes.</h6>",unsafe_allow_html=True)
    st.markdown("")

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Dataset Preview 📋</span>", unsafe_allow_html=True)
    data2

    #default value is NA for the choice
    all_ingredients1 = ["NA"]
    gg = data2.loc[:, data2.columns != 'Name of Dish'].values.tolist()

    #printed a list first in streamlit of the unique values in the particular choice and then copied it to give the options here
    ingredient_1 = st.selectbox('Search for 1st Ingredient',([
    "NA",
    "Potato",
    "Tomato",
    "Cilantro(Coriander leaves)",
    "Brinjal",
    "Carrot",
    "Coriander",
    "Onion",
    "Drumsticks",
    "Capsicum",
    "None",
    "Cabbage",
    "Peas",
    "Fenugreek",
    "Mushrooms",
    "Spinach",
    "Olives",
    "Sweet corn",
    "Kidney beans(Rajma)",
    "Zucchini",
    "Cauliflower",
    "Bitter Gourd",
    "Cucumber",
    "Beetroot",
    "Garlic",
    "Pumpkin",
    "Beans",
    "Green chilli",
    "Broccoli",
    "Bottle Gourd",
    "Sweet potato",
    "Baby corn",
    "Cluster Beans(Gavar)",
    "Colocasia",
    "Radish",
    "Turnip",
    "Ladyfinger(Okra)",
    "Celery",
    "Soyabean",
    "Mint",
    "Ginger",
    "Black Beans",
    "Lemon juice",
    "Lettuce",
    "Spring Onion",
    "Fennel Bulbs",
    "White Beans",
    "Asparagus",
    "Jalapenos",
    "Leek",
    "Brussels Sprouts",
    "Artichoke",
    "Curry leaves",
    "Ivy Gourd (Tendli)",
    "Yam"
    ]))
    st.write('You selected:', ingredient_1)

    #printed a list first in streamlit of the unique values in the particular choice and then copied it to give the options here
    ingredient_2 = st.selectbox('Search for 2nd Ingredient',([
    "NA",
    "Tomato",
    "Beans",
    "Garlic",
    "Onion",
    "Peas",
    "Capsicum",
    "Baby corn",
    "Carrot",
    "Curry leaves",
    "Coriander",
    "Potato",
    "None",
    "Bottle Gourd",
    "Cabbage",
    "Mint",
    "Jalapenos",
    "Brinjal",
    "Cucumber",
    "Cauliflower",
    "Ginger",
    "Olives",
    "Fenugreek",
    "Green chilli",
    "Spinach",
    "Sweet corn",
    "Lemon juice",
    "Cilantro(Coriander leaves)",
    "Beetroot",
    "Spring Onion",
    "Mustard Greens",
    "Mushrooms",
    "Leek",
    "Fennel Bulbs",
    "Broccoli",
    "Celery",
    "White Beans",
    "Turnip"
    ]))
    st.write('You selected:', ingredient_2)


    #printed a list first in streamlit of the unique values in the particular choice and then copied it to give the options here
    ingredient_3 = st.selectbox('Search for 3rd Ingredient',([
    "NA",
    "Onion",
    "Carrot",
    "Mushrooms",
    "Garlic",
    "Pickles",
    "Cabbage",
    "Capsicum",
    "Ginger",
    "Green chilli",
    "Olives",
    "None",
    "Cauliflower",
    "Coriander",
    "Tomato",
    "Pumpkin",
    "Potato",
    "Jalapenos",
    "Curry leaves",
    "Peas",
    "Fenugreek",
    "Beetroot",
    "Sweet corn",
    "Celery",
    "Lemon juice",
    "Cilantro(Coriander leaves)",
    "Lettuce",
    "Kidney beans(Rajma)",
    "Spring Onion",
    "Mint",
    "Spinach",
    "Artichoke"
    ]))
    st.write('You selected:', ingredient_3)

    ingredient_4 = st.selectbox('Search for 4th Ingredient',([
    "NA",
    "Peas",
    "None",
    "Olives",
    "Lemon juice",
    "Tomato",
    "Green chilli",
    "Jalapenos",
    "Garlic",
    "Capsicum",
    "Beetroot",
    "Ladyfinger(Okra)",
    "Sweet corn",
    "Beans",
    "Coriander",
    "Onion",
    "Ginger",
    "Cauliflower",
    "Mushrooms",
    "Baby corn",
    "Curry leaves",
    "Cabbage",
    "Carrot",
    "Pickles",
    "Kidney beans(Rajma)",
    "Celery",
    "Mint",
    "Potato",
    "White Beans",
    "Cilantro(Coriander leaves)",
    "Broccoli",
    "Spring Onion",
    "Spinach",
    "Soyabean",
    "Radish"
    ]))
    st.write('You selected:', ingredient_4)

    ingredient_5 = st.selectbox('Search for 5th Ingredient',([
    "NA",
    "Moong dal",
    "Whole wheat flour(Atta)",
    "White flour(Maida)",
    "Chickpeas(Chhole)",
    "Rice",
    "Masoor dal",
    "None",
    "Gram(Chana)",
    "Toor dal",
    "Gram flour(Besan)",
    "Urad dal",
    "Chana dal",
    "Oats",
    "Corn flour",
    "Bajra(Millet Flour)",
    "Sabudana",
    "Jowar Flour",
    "Rice Flour",
    "Rawa(Semolina)"
    ]))
    st.write('You selected:', ingredient_5)

    ingredient_6 = st.selectbox('Search for 6th Ingredient',([
    "NA",
    "Red Chilli",
    "Garam Masala",
    "Black Pepper",
    "Turmeric",
    "Cumin",
    "Oregano",
    "Cardamom",
    "None",
    "Mustard",
    "Cinnamon",
    "Bay leaves",
    "Parsley",
    "Garlic Cloves",
    "Basil",
    "Coriander seeds",
    "Thyme",
    "Dill",
    "Onion",
    "Fennel seeds",
    "Coriander",
    "Green Chilli",
    "Asafoetida",
    "Ginger",
    "Vanilla",
    "Rosemary",
    "Sesame seeds",
    "Flax Seeds",
    "Saffron",
    "Quinoa",
    "Nigella Seeds",
    "Nutmeg"
    ]))
    st.write('You selected:', ingredient_6)

    ingredient_7 = st.selectbox('Search for 7th Ingredient',([
    "NA",
    "Turmeric",
    "Paprika",
    "Black Pepper",
    "Cumin",
    "Cinnamon",
    "Garam Masala",
    "Red Chilli",
    "Oregano",
    "Asafoetida",
    "None",
    "Mustard",
    "Nutmeg",
    "Cardamom",
    "Bay leaves",
    "Garlic Cloves",
    "Fennel seeds",
    "Cloves",
    "Basil",
    "Parsley",
    "Onion",
    "Dill",
    "Green Chilli",
    "Coriander",
    "Sesame seeds",
    "Fenugreek seeds",
    "Ginger",
    "Poppy seeds",
    "Thyme",
    "Cayenne Peppers",
    "Sunflower Seeds",
    "Rosemary"
    ]))
    st.write('You selected:', ingredient_7)

    ingredient_8 = st.selectbox('Search for 8th Ingredient',([
    "NA",
    "Asafoetida",
    "None",
    "Oregano",
    "Coriander seeds",
    "Nutmeg",
    "Cinnamon",
    "Fennel seeds",
    "Turmeric",
    "Black Pepper",
    "Garam Masala",
    "Red Chilli",
    "Cumin",
    "Mustard",
    "Saffron",
    "Cloves",
    "Onion",
    "Bay leaves",
    "Paprika",
    "Parsley",
    "Garlic Cloves",
    "Basil",
    "Coriander",
    "Green Chilli",
    "Thyme",
    "Sesame seeds",
    "Dill",
    "Cardamom",
    "Ginger",
    "Kasoori Methi",
    "Flax Seeds",
    "Rosemary",
    "Fenugreek seeds",
    "Sunflower Seeds"
    ]))
    st.write('You selected:', ingredient_8)

    ingredient_9 = st.selectbox('Search for 9th Ingredient',([
    "NA",
    "Garam Masala",
    "None",
    "Parsley",
    "Saffron",
    "Turmeric",
    "Bay leaves",
    "Oregano",
    "Mustard",
    "Cardamom",
    "Black Pepper",
    "Coriander seeds",
    "Red Chilli",
    "Fenugreek seeds",
    "Poppy seeds",
    "Cloves",
    "Cumin",
    "Cinnamon",
    "Asafoetida",
    "Basil",
    "Green Chilli",
    "Thyme",
    "Coriander",
    "Cayenne Peppers",
    "Fennel seeds",
    "Onion",
    "Garlic Cloves",
    "Sesame seeds",
    "Kasoori Methi",
    "Dill",
    "Sunflower Seeds",
    "Flax Seeds"
    ]))
    st.write('You selected:', ingredient_9)

    #printed a list first in streamlit of the unique values in the particular choice and then copied it to give the options here
    ingredient_10 = st.selectbox('Search for 10th Ingredient',([
    "NA",
    "White Bread",
    "None",
    "Pita Bread",
    "Whole Wheat Bread",
    "Baguette",
    "Bun",
    "Papad",
    "French Bread"
    ]))
    st.write('You selected:', ingredient_10)

    ingredient_11 = st.selectbox('Search for 11th Ingredient',([
    "NA",
    "Butter",
    "Cheese",
    "None",
    "Ghee",
    "Milk",
    "Paneer(Cottage cheese)",
    "Curd",
    "Sour cream",
    "Buttermilk",
    "Cream"
    ]))
    st.write('You selected:', ingredient_11)


    ingredient_list = [ingredient_1,ingredient_2,ingredient_3,ingredient_4,ingredient_5,ingredient_6,ingredient_7,ingredient_8,ingredient_9,ingredient_10,ingredient_11]

    #Remove NA keyword from list
    ingredient_list = set(filter(lambda x: x != 'NA', ingredient_list))
    ingredient_list = list(ingredient_list)

    #get all recipe names
    all_recipes = list(x for x in data2['Name of Dish'])

    #compare ingredients
    def intersection(list1,list2):
        list3 = [value for value in list2 if value in list1]
        return list3

    score = [0]*len(gg)
    for i in range(len(gg)):
        score[i] = len(intersection(gg[i],ingredient_list))

    max_score = max(score) if max(score) > 1 or len(ingredient_list)==1 else -999

    #find the best match
    most_prob = [all_recipes[x] for x in range(len(score)) if score[x] == max_score]
    recipe = []

    #join results with ,
    recipe = ", ".join(most_prob)
    
    st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>Possible Dishes ⬇️ </span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #000080;font-size: 22px;font-weight: bold;'>{recipe}</span>", unsafe_allow_html=True)
    

    st.title("View calories and cuisine of a dish 🥗 🧑🏾‍🤝‍🧑🏼")

    #take user input to select the dish from the name column (used unique function for non repetition of values)
    dish_name = st.selectbox("Search your dish here:", data2["Name of Dish"].unique())


    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Filter Data Results are :</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>You selected- {dish_name}</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>Analysis for your selection is as follows-</span>", unsafe_allow_html=True)

    #counts of various nutritional contents of a food item
    count_calories = data2.loc[(data2["Name of Dish"] == dish_name) , 'Calories'].iloc[0]
    cuisine = data2.loc[(data2["Name of Dish"] == dish_name) , 'Cuisine'].iloc[0]
    
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Calorie Count - {count_calories} kCal</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Cuisine - {cuisine}</span>", unsafe_allow_html=True)
  
#clorie calculator function
def page_three():
    st.title("Calorie Calculator 🍲 🧮")
    
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Nutrients are classified into two categories, macronutrients and micronutrients. Macronutrients are those nutrients which are required in large quantities, and include carbohydrates, proteins, fats and water. Micronutrients are those which are required in relatively small quantities, and include vitamins and minerals. Adequate amounts of these nutrients are required to maintain good health. The adequate amounts vary from person to person, and also depend on the person’s daily calorie consumption. Moreover, the ideal calorie consumption for a person also depends on various factors, including gender. Here, you can find your ideal consumption of various nutrients depending on your daily calorie consumption, and can also find your ideal daily calorie consumption based on your gender.</h6>",unsafe_allow_html=True)
    st.markdown("")

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Add your total daily intake of calories</span>", unsafe_allow_html=True)

    #slider for user input
    x = st.slider('(in terms of Calories)',0,3000)

    #the generalised ideal percentages considered from various data sources
    fat_value= x*(30/100)
    sat_fat_value= x*(7/100)
    trans_fat_value= x*(1/100)
    total_carbs_value= x*(50/100)
    protein_value= x*(20/100)

    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Total Fat count should be- {fat_value} Cal</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Saturated Fat count should be- {sat_fat_value} Cal</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Trans Fat count should be- {trans_fat_value} Cal</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Total Carbohydrates count should be- {total_carbs_value} Cal</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Protein count should be- {protein_value} Cal</span>", unsafe_allow_html=True)


    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Want to know your ideal calorie intake ??</span>", unsafe_allow_html=True)

    st.markdown(f"<span style='color: black;font-size: 20px;font-weight: bold;'>Choose your gender</span>", unsafe_allow_html=True)
    gender = st.selectbox('*Your calorie intake depends on your gender',('Male', 'Female'))

    #display selected choice
    st.markdown(f"<span style='color: black;font-size: 20px;font-weight: bold;'>You selected: {gender}</span>", unsafe_allow_html=True)

    #if else use for all the possible variations - hard coded because choice are very few 
    if (gender == 'Male'):
        st.markdown(f"<span style='color: #367588;font-size: 19px;font-weight: bold;'>Your ideal daily calorie intake should be 2500 Cal</span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color: #367588;font-size: 19px;font-weight: bold;'>Your ideal daily water intake should be 3.7 L</span>", unsafe_allow_html=True)
    elif (gender == 'Female'):
        st.markdown(f"<span style='color: #367588;font-size: 19px;font-weight: bold;'>Your ideal daily calorie intake should be 2000 Cal</span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color: #367588;font-size: 19px;font-weight: bold;'>Your ideal daily water intake should be 2.7 L</span>", unsafe_allow_html=True)
    elif (gender == 'Other'):
        st.markdown(f"<span style='color: #367588;font-size: 19px;font-weight: bold;'>Sorry, info not available :)</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span style='color: #367588;font-size: 19px;font-weight: bold;'>Sorry, info not available :)</span>", unsafe_allow_html=True)
    
   
        
        

def page_fourth():
    st.title("View calories and cuisine of a dish 🥗 🧑🏾‍🤝‍🧑🏼")

    #take user input to select the dish from the name column (used unique function for non repetition of values)
    dish_name = st.selectbox("Search your dish here:", data2["Name of Dish"].unique())


    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Filter Data Results are :</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>You selected- {dish_name}</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>Analysis for your selection is as follows-</span>", unsafe_allow_html=True)

    #counts of various nutritional contents of a food item
    count_calories = data2.loc[(data2["Name of Dish"] == dish_name) , 'Calories'].iloc[0]
    cuisine = data2.loc[(data2["Name of Dish"] == dish_name) , 'Cuisine'].iloc[0]
    
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Calorie Count - {count_calories} kCal</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Cuisine - {cuisine}</span>", unsafe_allow_html=True)
    


				
			

def disease_demographics():
    # Register your pages
    pages = {
        "1. Food Suggestions for Diabetic Patients": diabetes_page,
        "2. Food Suggestions for Lactose Intolerance":lactose_page,
        "3. Food Suggestions for Anaemia Patients":anaemia_page,
        "4. Food Suggestions for patients suffering from Kidney Stones":kidneystones_page,
        "5. Food Suggestions for patients suffering from Gallbladder Stones":gallstones_page
    }

    #title 
    st.title("Navigate through demographics 🧭 ")

    #Widget to select your page, you can choose between radio buttons or a selectbox
    page = st.radio("(Choose an option to get redirected)", tuple(pages.keys()))
    
    #Display the selected page
    pages[page]()

def diabetes_page():
    st.title("Diabetes")

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Diabetes is a condition in which the glucose level in blood (also called as blood sugar level) is too high. The pancreas produces a hormone called insulin which helps in the generation of energy from glucose. When the insulin produced is not sufficient to generate energy from glucose, the glucose stays in blood, which ultimately leads to diabetes. Diabetes is of two types, type 1 and type 2 diabetes. While the cause of type 1 diabetes is unknown, obesity and excessive consumption of sugar is one of the causes of type 2 diabetes. Diabetic patients need to control their sugar consumption, so as not to increase the glucose level in the blood. Also, since carbohydrates are broken down into glucose, they increase the glucose level in blood. Therefore, carbohydrate consumption also needs to be controlled. Carbohydrates also include fiber, but fiber does not raise blood sugar levels as it is expelled from the body undigested.</h6>",unsafe_allow_html=True)
    st.markdown("")

    glus_largest=df_demographics.groupby('category')['glus'].nlargest(5)
    st.write(glus_largest)

    categories=['Grains', 'Legumes', 'Vegetables', 'Fruits', 'Spices', 'Nuts', 'Seeds', 'Juice', 'Sugar', 'Dairy', 'Eggs', 'White Meat', 'Red Meat', 'Seafood']
    
    #diabetes

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Analysis of Glucose Content</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Glucose (grams)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Here, the food items in the dataset which are highest in glucose are displayed. Raisins and tamarind are at the top of the list. People having diabetes should consume these food items in very controlled quantities, in order to avoid raising their blood sugar level.</h6>",unsafe_allow_html=True)
    
    st.markdown("")
    
    carbs= df_demographics[df_demographics['category'].isin(categories)]

    carbs_rich= carbs.sort_values(by='glus', ascending= False)
    
    top_20_carbs=carbs_rich.head(20)
    
    fig1 = px.bar(top_20_carbs, x='name', y='glus', color='glus')
    fig1.update_layout(title='Top 20 Foods High in Glucose', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig1)
    
      

def lactose_page():
    st.title("Food Suggestions for Lactose Intolerant Patients")

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Lactose is a sugar present in milk and dairy products. Lactose intolerance is a digestive problem which is caused due to low amounts of an enzyme called lactase. Lactase helps in digestion of lactose, and therefore when this enzyme is deficient, then lactose passes undigested through the intestines, possibly causing symptoms such as nausea, diarrhoea, and gas. People having lactose intolerance do not need to completely avoid dairy products, however, they can consume only upto 12 grams of lactose at a time safely.  </h6>",unsafe_allow_html=True)
    st.markdown("")
    
    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Analysis of Lactose Content</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Lactose (grams)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>The amounts of lactose in some common dairy products are displayed here with the help of a bar graph.</h6>",unsafe_allow_html=True)
    st.markdown("")
    #Based on categories
    categories=['Grains', 'Legumes', 'Vegetables', 'Fruits', 'Spices', 'Nuts', 'Seeds', 'Juice', 'Sugar', 'Dairy', 'Eggs', 'White Meat', 'Red Meat', 'Seafood']
    
    #lactose

    lact= df_demographics[df_demographics['category'].isin(categories)]

    lactose_rich= lact.sort_values(by='lactose', ascending= False)
    
    top_20=lactose_rich.head(4)
    
    fig = px.bar(top_20, x='lactose', y='name', color='lactose')
    fig.update_layout(title='Foods with Lactose Content', autosize=False,width=750, height=700,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig)


    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>People with lactose intolerance should consume small amounts of milk or products at a time. Also, there are some dairy products that have low amounts of lactose. These include:</h6>",unsafe_allow_html=True)
    st.markdown("")
    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Dairy products with less amount of lactose</span>", unsafe_allow_html=True)

    
    cols = st.columns(2)
    
    
    cols[0].write(f"<h6 style='text-align: left;font-size:22px;font-weight: bold;line-height: 1.3;'>Food items</h6>",unsafe_allow_html=True)

    cols[0].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>Butter</h6>",unsafe_allow_html=True)
    cols[0].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>Ghee</h6>",unsafe_allow_html=True)
    cols[0].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>Parmesan Cheese</h6>",unsafe_allow_html=True)
    cols[0].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>Cheddar Cheese</h6>",unsafe_allow_html=True)
    cols[0].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>Swiss Cheese</h6>",unsafe_allow_html=True)    
    cols[0].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>Heavy Cream</h6>",unsafe_allow_html=True)
    cols[0].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>Probiotic Yoghurt</h6>",unsafe_allow_html=True)

    cols[1].write(f"<h6 style='text-align: left;font-size:22px;font-weight: bold;line-height: 1.3;'>Lactose Content (per 100grams)</h6>",unsafe_allow_html=True)

    cols[1].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>0.688 g</h6>",unsafe_allow_html=True)
    cols[1].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>0.0029 g</h6>",unsafe_allow_html=True)
    cols[1].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>0 g</h6>",unsafe_allow_html=True)
    cols[1].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>0.1 g</h6>",unsafe_allow_html=True)    
    cols[1].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>0.1 g</h6>",unsafe_allow_html=True)
    cols[1].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>3 g</h6>",unsafe_allow_html=True)
    cols[1].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>5 g</h6>",unsafe_allow_html=True)

    st.write("")


    st.write("")
    st.title("Alternatives to compensate for other nutrients present in dairy products")

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Milk products should not be completely avoided, as it can cause deficiencies of calcium and vitamin D. Calcium deficiency can cause easy occurrence of bone fractures, weak and brittle nails, and muscle cramps while deficiency of vitamin D can cause osteoporosis, increased risk of heart disease, muscle pain and hair loss. People having lactose intolerance should make sure that they consume enough calcium and Vitamin D from other foods that do not contain lactose.</h6>",unsafe_allow_html=True)
    st.markdown("")

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Top Calcium Rich Food Items</span>", unsafe_allow_html=True)

    #high calcium items 
    calcium= df_demographics[df_demographics['category'].isin(['Grains', 'Legumes', 'Vegetables', 'Fruits', 'Spices', 'Nuts', 'Seeds', 'Juice', 'Sugar', 'Eggs', 'White Meat', 'Red Meat', 'Seafood'])]

    calcium_top=calcium.sort_values(by='ca', ascending= False)
    
    calcium_top=calcium_top.head(15)

    fig_calcium_food = go.Figure(go.Funnelarea(values=calcium_top['ca'].values, text=calcium_top['name'],title = { "text": "Food items with high Calcium percentages"},marker = {"colors": ["deepskyblue", "lightsalmon", "tan", "teal", "silver","deepskyblue", "lightsalmon", "tan", "teal", "silver"],"line": {"color": ["wheat", "wheat", "blue", "wheat", "wheat","wheat", "wheat", "blue", "wheat", "wheat"]}}))

    fig_calcium_food.update_layout(height=800, width=700)

    st.plotly_chart(fig_calcium_food)

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Top Foods rich in Vitamin D</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>There are five forms of vitamin D, of which vitamin D2 and D3 are the most common. Vitamin D2 is found in plant-based foods while vitamin D3 is found in animal-sourced foods.</h6>",unsafe_allow_html=True)
    st.markdown("")
    

    #d2
    st.markdown(f"<span style='color:#367588;font-size: 24px;font-weight: bold;'>Top Foods rich in Vitamin D2</span>", unsafe_allow_html=True)

    vitd2= df_demographics[df_demographics['category'].isin(['Grains', 'Legumes', 'Vegetables', 'Fruits', 'Spices', 'Nuts', 'Seeds', 'Juice', 'Sugar'])]

    vitd2_top=vitd2.sort_values(by='ergcal', ascending= False)
    
    vitd2_top=vitd2_top.head(15)

    fig_vitd2_food = go.Figure(go.Funnelarea(values=vitd2_top['ergcal'].values, text=vitd2_top['name'],title = { "text": "Food items with high Vitamin D2 percentages"},marker = {"colors": ["deepskyblue", "lightsalmon", "tan", "teal", "silver","deepskyblue", "lightsalmon", "tan", "teal", "silver"],"line": {"color": ["wheat", "wheat", "blue", "wheat", "wheat","wheat", "wheat", "blue", "wheat", "wheat"]}}))

    fig_vitd2_food.update_layout(height=800, width=700)

    st.plotly_chart(fig_vitd2_food)

    #d3
    st.markdown(f"<span style='color: #367588;font-size: 24px;font-weight: bold;'>Top Foods rich in Vitamin D3</span>", unsafe_allow_html=True)

    vitd3= df_demographics[df_demographics['category'].isin(['Eggs', 'White Meat', 'Red Meat', 'Seafood'])]

    vitd3_top=vitd3.sort_values(by='chocal', ascending= False)
    
    vitd3_top=vitd3_top.head(15)

    fig_vitd3_food = go.Figure(go.Funnelarea(values=vitd3_top['chocal'].values, text=vitd3_top['name'],title = { "text": "Food items with high Vitamin D3 percentages"},marker = {"colors": ["deepskyblue", "lightsalmon", "tan", "teal", "silver","deepskyblue", "lightsalmon", "tan", "teal", "silver"],"line": {"color": ["wheat", "wheat", "blue", "wheat", "wheat","wheat", "wheat", "blue", "wheat", "wheat"]}}))

    fig_vitd3_food.update_layout(height=800, width=700)

    st.plotly_chart(fig_vitd3_food)

def anaemia_page():
    st.title("Iron deficiency Anaemia")

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Haemoglobin is the protein in the red blood cells that is responsible for carrying oxygen to the tissues. Anaemia occurs when the level of haemoglobin in the blood is low.  The symptoms of anaemia include headaches, fatigue, weakness, dizziness, shortness of breath, and various other symptoms. Iron is needed to make haemoglobin. Thus, when there is a deficiency of iron, it leads to low levels of haemoglobin in the blood, causing anaemia. It may be caused by low consumption of iron, internal bleeding, and inability to absorb iron. Also, it is especially common in women, due to pregnancy and blood loss during menstruation. It is therefore necessary, especially for women, to consume foods that are rich in iron. The below pyramid shows the foods which have highest amounts of iron.</h6>",unsafe_allow_html=True)
    st.markdown("")

    #iron deficiency
    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Top Foods rich in Iron</span>", unsafe_allow_html=True)

    iron= df_demographics

    iron_top=iron.sort_values(by='fe', ascending= False)
    
    iron_top=iron_top.head(15)

    fig_iron_food = go.Figure(go.Funnelarea(values=iron_top['fe'].values, text=iron_top['name'],title = { "text": "Food items with high Vitamin D3 percentages"},marker = {"colors": ["deepskyblue", "lightsalmon", "tan", "teal", "silver","deepskyblue", "lightsalmon", "tan", "teal", "silver"],"line": {"color": ["wheat", "wheat", "blue", "wheat", "wheat","wheat", "wheat", "blue", "wheat", "wheat"]}}))

    fig_iron_food.update_layout(height=800, width=700)

    st.plotly_chart(fig_iron_food)

     

def kidneystones_page():
    st.title("Kidney Stones")

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Kidney stones are caused due to accumulation of certain minerals in the urine. The most prominent cause of kidney stones is dehydration. Dehydration causes an increase in the concentrations of minerals in the urine. There are 4 types of kidney stones: calcium oxalate and calcium phosphate stones, uric acid stones, struvite stones, and cystine stones. Calcium oxalate stones are the most common.</h6>",unsafe_allow_html=True)

    st.header("Excessive consumption of the following nutrients can cause kidney stones:")

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>1. Oxalate: Foods such as nuts, chocolate, tea, spinach are high in oxalate. Consuming these foods excessively can increase the amounts of oxalate in the urine and thereby increase the risk of calcium oxalate stones.</h6>",unsafe_allow_html=True)
    st.markdown("")
    

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>2. Sodium: High consumption of sodium can increase the formation of calcium in the urine. Therefore, to avoid kidney stones, the consumption of salt should be limited. Processed foods, canned foods, and fast food should be avoided as they are high in sodium. Baking soda should also be avoided.</h6>",unsafe_allow_html=True)
    st.markdown("")
    
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>3. Animal Protein: Excessive consumption of animal protein can increase the amounts of uric acid in the urine, thus increasing the risk of uric acid stones.</h6>",unsafe_allow_html=True)
    st.markdown("")

    #1st graph

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Foods highest in oxalate (should not be consumed)</span>", unsafe_allow_html=True)

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Consumption of foods high in oxalate raises the urinary oxalate levels. This increases the risk of calcium oxalate stones. Therefore, consumption of oxalate-containing foods should be minimized. The below graph shows the foods in the dataset which have highest oxalate levels.</h6>",unsafe_allow_html=True)
    st.markdown("")
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Oxalates (milligrams)</span>", unsafe_allow_html=True)
    
    #Based on categories
    categories=['Grains', 'Legumes', 'Vegetables', 'Fruits', 'Spices', 'Nuts', 'Seeds', 'Juice', 'Sugar', 'Dairy', 'Eggs', 'White Meat', 'Red Meat', 'Seafood']
    
    #oxalates

    oxalates= df_demographics[df_demographics['category'].isin(categories)]

    oxalates_rich= oxalates.sort_values(by='oxalt', ascending= False)
    
    top_20=oxalates_rich.head(10)
    
    fig1 = px.bar(top_20, x='name', y='oxalt', color='oxalt')
    fig1.update_layout(title='Foods having highest amounts of Oxalate', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig1)

    #2nd graph

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Foods highest in citric acid (should be consumed)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>For prevention of kidney stones, one must stay adequately hydrated. Also, the consumption of citrus fruits should be increased. Citrus fruits have high amounts of citric acid, which is beneficial for people having kidney stones as it increases the amounts of citrate in the urine. Citrate binds with calcium oxalate and prevents the formation of crystals. The below graph shows the foods from the dataset having the highest amounts of citric acid.</h6>",unsafe_allow_html=True)
    st.markdown("")
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Citric Acid (milligrams)</span>", unsafe_allow_html=True)
    #citric acid

    citric= df_demographics[df_demographics['category'].isin(categories)]

    citric_rich= citric.sort_values(by='citac', ascending= False)
    
    top_20=citric_rich.head(10)
    
    fig2 = px.bar(top_20, x='name', y='citac', color='citac')
    fig2.update_layout(title='Top Foods rich in Citric Acid', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig2)

    #3rd graph

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Foods highest in calcium (should be consumed) </span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>It is a common misconception that calcium intake should be reduced in order to prevent kidney stones. However, calcium binds with oxalate in the intestine, and leads to the formation of calcium oxalate in the intestine, which in turn reduces the oxalate absorption and urinary oxalate excretion. Therefore, calcium intake should be kept sufficiently high. Following are some calcium-rich foods from the dataset.</h6>",unsafe_allow_html=True)
    st.markdown("")
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Calcium (milligrams)</span>", unsafe_allow_html=True)
    #calcium

    calc= df_demographics[df_demographics['category'].isin(categories)]

    calc_rich= calc.sort_values(by='ca', ascending= False)
    
    top_20=calc_rich.head(10)
    
    fig3 = px.bar(top_20, x='name', y='ca', color='ca')
    fig3.update_layout(title='Top Foods rich in Calcium', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig3)

 

def gallstones_page():
   #gall stones

    st.title("Gallbladder Stones")

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>The gallbladder is an organ that stores bile, which is a fluid that is produced by the liver and used for digestion.  According to Harvard Health Publications, 80% of gallbladder stones, or gallstones, are formed when the amount of cholesterol in the bile is high. There are several risk factors that may lead to the formation of gallstones. Among these, the diet related risk factors include excessive consumption of high-fat or high-cholesterol foods, or low consumption of fibrous foods.  To avoid formation of gallstones, it is recommended to consume high-fiber foods, whole grains, healthy (unsaturated) fats, and foods high in vitamin C. Consumption of refined carbohydrates, sugar, and saturated fats should be reduced.</h6>",unsafe_allow_html=True)
    st.markdown("")
    
    #Based on categories
    categories=['Grains', 'Legumes', 'Vegetables', 'Fruits', 'Spices', 'Nuts', 'Seeds', 'Juice', 'Sugar', 'Dairy', 'Eggs', 'White Meat', 'Red Meat', 'Seafood']
    
    #4th graph
    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Foods highest in saturated fat (should not be consumed)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Higher consumption of saturated fats increases levels of bad cholesterol, which in turn increases the risk of gallstones. Following are the foods from the dataset having highest amounts of saturated fat. The consumption of these foods should be minimized.</h6>",unsafe_allow_html=True)
    st.markdown("")
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Saturated Fat (milligrams)</span>", unsafe_allow_html=True)
    
    #saturated fat

    fasat= df_demographics[df_demographics['category'].isin(categories)]

    fasat_rich= fasat.sort_values(by='fasat', ascending= False)
    
    top_20=fasat_rich.head(20)
    
    fig4 = px.bar(top_20, x='name', y='fasat', color='fasat')
    fig4.update_layout(title='Foods having highest amounts of Saturated Fat', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig4)

    #5th graph

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Foods highest in fiber (should be consumed)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Dietary fiber, especially insoluble fiber, reduces bile acids and the levels of cholesterol in bile. Therefore, consumption of a high-fiber diet can prevent formation of gallstones. The foods in the dataset that are highest in fiber are shown in the graph below.</h6>",unsafe_allow_html=True)
    st.markdown("")
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Fiber (grams)</span>", unsafe_allow_html=True)


    #fiber

    fibtg= df_demographics[df_demographics['category'].isin(categories)]

    fibtg_rich= fibtg.sort_values(by='fibtg', ascending= False)
    
    top_20=fibtg_rich.head(20)
    
    fig5 = px.bar(top_20, x='name', y='fibtg', color='fibtg')
    fig5.update_layout(title='Top Foods rich in Fiber', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig5)


    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Foods highest in Vitamin C (should be consumed)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Vitamin C helps to break down cholesterol in the gallbladder and regulates its conversion into bile acids. Therefore, lack of vitamin C increases the risk of gallstones. The graph shows the foods in the dataset that have the highest levels of vitamin C. Adequate amounts of vitamin C should be consumed to reduce the risk of gallstones.</h6>",unsafe_allow_html=True)
    st.markdown("")
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Vitamin C (milligrams)</span>", unsafe_allow_html=True)
    
    #vitamin c

    vitc= df_demographics[df_demographics['category'].isin(categories)]

    vitc_rich= vitc.sort_values(by='vitc', ascending= False)
    
    top_20=vitc_rich.head(20)
    
    fig6 = px.bar(top_20, x='name', y='vitc', color='vitc')
    fig6.update_layout(title='Top Foods rich in Vitamin C', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig6)

  

if __name__ == "__main__":
    main()

