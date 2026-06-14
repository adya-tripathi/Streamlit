import streamlit as st
import pandas as pd 
import numpy as np
# declarative statistical visualization library of Python
import altair as alt
# Golden Structure
# chart = alt.Chart(data).mark_type().encode(x='column_1',y='column_2',color='column_3')
# alt.Chart(data): Tells data source in use (generally a Pandas DataFrame). 
# mark_*(): Specifies the geometric shape used to represent the data. EX-.mark_point(), .mark_bar(), .mark_line(), and .mark_area(). 
# encode(): Maps columns of df to visual properties of the mark (like position x/y, color, size, shape, or tooltip)
from datetime import time
from datetime import datetime


# every time you interact with any of the things on your app it reruns the whole script from the very begnning
# streamlit is kind of python looper

#to add a title to the page : st.title
st.title("Hello World!")
#To write something : st.write
st.write("This is ADYA TRIPATHI officialy signing in to streamlit")
#To put headings : st.header
# for buttons : st.button
st.header("Exploring Buttons")
button = st.button("CLICK ME")
# this command tels to explicitly display the button clicked status
st.write(f"Button Clicked : {button}")
# whatever will be written in if will show when button is clicked
if button:
    st.write("Hello There😇")
    st.write("Ohhhh..this opens up on clicking")
    st.write("GOOD")
#else:
    #st.write("Byee")

st.header("Exploring st.write/print of streamlit")
# Bold : ** , Italic : * , Emoji printing
# According to the Markdown syntax and emoji shortcode
st.write("**HELLO WORLD**", "*Hello World*", ":sunglasses:", ":smile:", ":angry:")

# can write numbers as well and do algebra
st.write(2+2)

# Dataframes
df = pd.DataFrame({'Col1': [1,2,3,4,5] ,'Col2' : [6,7,8,9,10]})
# Example 4: Multiple arguments
st.write("Below is a DataFrame:", df, "Above is a dataframe.")

#DataFrame using numpy
df2 = pd.DataFrame(np.random.randn(20,3),
                   columns = ['a','b','c'])


# PLotting using altair
# very simple to add interactivity. By writing .interactive() to the end of a chart object
# properties method can add tilte
chart = alt.Chart(df2).mark_circle().encode(x = 'a' , y = 'b' , color = 'c' , size = 'c' , tooltip = ['a','b','c']).properties(title = "A Scatter Plot")
st.write(chart)

st.header("Exploring st.slider")
# for a subheading use subheader
st.subheader("Sliders in Streamlit")
# st.slider will take the text associated with it,the lower and the upper range and an optional default value(originally 0)
age = st.slider("How old are you ?",0,120,25)
# will display the value on the slider
st.write(f"I am **{age}** years old")
st.subheader("Range Slider")
# to build a range slider just pass a tuple of value in the default value place
# using datetime 
# if you dont provide lower and upper boundary 00:00 to 23:59 will be taken..make sure to give the default value as a variable
values = st.slider("Schedule an appointment",value = (time(11,30),time(12,45)))
# to access one of them use array type indexing
st.write(values)
# format can vhange the way values are displayed on the slider
values2 = st.slider("Appointment Date", 
                    value = datetime(2026,1,1,12,30),
                    format = "DD/MM/YY - hh:mm")

st.write(values2)

st.header("📈 Exploring Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a','b','c']
)
st.write(chart_data)
# line charts belongs to streamlit and there are multiple function included here
st.line_chart(chart_data,height = 400)

# for the documentation
#st.help(st.line_chart)


st.header("Exploring st.selectbox")

st.subheader("Demo 1")
colour = st.selectbox("Select you favorite colour",['Select Here','red','blue','black','green','yellow','pink','purple','orange'])
st.write(f"My favourite colour is **{colour}**")

st.subheader("Demo 2")
selected_column = st.selectbox(
    "Select a DataFrame column",
    chart_data.columns
)
st.write(f"The selected column is {selected_column}")
st.line_chart(chart_data[selected_column])


st.header("Exploring st.multiselect")
# multiselect takes a list of values and lets you slect multiple values from the 
# you can also pass a list of default values after the first list
options = st.multiselect(
    "What are your favourite colours?",
    ['red','blue','black','green','yellow','pink','purple','orange'],)
# returns the list of your selected options
st.write(f"My favourite colours are {options}")


st.header("☑️ Exploring st.checkbox")
st.subheader("What are you going to order ?")
pizza= st.checkbox("Pizza 🍕")
burger = st.checkbox("Burger 🍔")
icecream = st.checkbox("Ice Cream 🍦")

if pizza:
    st.write("Great,Here's some more for you")
if burger:
    st.write("You seem quite hungry..Have some from our side")
if icecream:
    st.write("Yayyy..Great minds ,always think of Ice Cream")
    st.subheader("Which flavour would you like")
    st.checkbox("Chocolate")
    st.checkbox("Vanilla")
    st.checkbox("Strawberry")
    st.checkbox("Mint")
st.subheader("Would you like a coffee as well ?")
coffee = st.toggle("Coffee")
if coffee:
    st.write("Okayy..your order will be ready soon")


# this function lets you write mathematical formulas its like an encription library which has encrypted mathematical functions like sigma pie etc
st.header("Exploring st.latex")
# r prefix: when r written the exp uses raw strings This prevents Python from interpreting backslashes (\) as escape characters.
st.latex(r''' 
   a + ar^2 + ar^3 + \dots + ar^{n-1} = 
         \sum_{k=0}^{n-1}ar^k =
         a\left(\frac{1-r^{n}}{1-r}\right)
 ''') 
st.latex(r'''
\left(\frac{1}{n-1}\right) + \left(\frac{1}{n+1}\right) = \frac{2n}{n^2-1}
''')

st.header("Exploring Streamlit Secrets")
# you do not hardcode your passwords or api keys in the code you store them in a secrets.toml file which is mentioned in gitignore so
# that the file is never pushed to github and your passwords and api keys are always safe and not publically accessible
#st.secrets behaves directly like a Python dictionary : the secret name is key and the the secret is value,can also be grouped inth etoml file

st.write(st.secrets["message"])
st.write(st.secrets["passwords"]["user_2"])


st.header("Exploring file uploader")
# this will upload a file 
uploaded_file = st.file_uploader("Choose file")
# till the uploaded file remains none st.stop wont let the code run further and keep displaying the warning
if uploaded_file is None:
    st.warning("Please upload a file to move further")
    st.stop()
# the uploaded csv file stored in df
df = pd.read_csv(uploaded_file)
# only preview the cols you select only if kyou toggle data preview on
data_preview = st.toggle("Data Preview")
if data_preview:
    cols_to_preview = st.multiselect("Which columns to display ?",df.columns)
    st.write(df[cols_to_preview])
    

st.header("Layout of the app")
st.subheader("Sidebar")
# Method 1 
choco_eaten = st.sidebar.slider("How many chocolates have you eaten ?",0,50,0)
st.write(f"I ate {choco_eaten} chocolates")
# Method 2 : everthing within with will be displayed in the sidebar
with st.sidebar:
    age = st.slider("Age ?",0,100,25)
    st.write(f"My age is {age} years")
    
st.subheader("Expander")
with st.expander("Data Preview"):
    st.write("This is the file's data that the user uploaded")
    st.write(df)

# using columns 
# so that the app uses the full window 
st.set_page_config(page_title = "FirstStreamlitApp",page_icon = "📈",layout = 'wide')

with st.expander("About this app"):
    st.write("This app shows the various ways on how you can layout your Streamlit app")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=100)

st.sidebar.header("User Data")
user_name = st.sidebar.text_input("Please enter your name")
user_age = st.sidebar.number_input("Please enter your age")
user_colour = st.sidebar.selectbox("Select you favorite colour",['Select Here','red','blue','black','green','yellow','pink','purple','orange'])
st.sidebar.write(f"My favourite colour is **{user_colour}**")

st.subheader("User Output from the sidebar")
# if a single number is passed then equal columns are generated for different sized columns you can pass a tuple of numbers
col1,col2,col3 = st.columns(3,gap = 'large')
with col1:
    if user_name != "":
        st.write(f"Hello {user_name}")
    else:
        st.write("Please enter your name")

with col2:
    if user_name != "":
        st.write(f"Your age was recorded")
    else:
        st.write("Please enter your age")

with col3:
    if user_name != "":
        st.write(f"Your selected colour was noted")
    else:
        st.write("Please enter the colour of your choice")

st.success("Hello")
st.warning("Hello")
st.error("Hello")

st.header("Exploring the progress bar")
import time
# interactive, animated,used to give users a visual cue that your app is busy processing something(like loading a dataset, training a machine learning model, or scraping a website)
# initializing the bar
my_bar = st.progress(0)

# standard Python loop that runs 100 times. 
# The variable percent_complete starts at 0(given earlier)
for percent_complete in range(100):
    # this is to create the effect of incresing progress visible
    time.sleep(0.005)
    # On every iteration of the loop,we call the method my_bar object to update its value.
    my_bar.progress(percent_complete + 1)
st.balloons()
st.toast("Your task has finished")

# how it is used in projects
with st.status("Processing your data...", expanded=True) as status:
    st.write("Searching database...")
    time.sleep(1)
    st.write("Downloading images...")
    time.sleep(1)
    st.write("Cleaning data...")
    time.sleep(1)
    
    # Converts the loading spinner into a green success checkmark
    status.update(label="Process complete!", state="complete", expanded=False)


st.header("Exploring st.form")
# the values of the variables in the form do not change until you submit the form
# Using with notation
st.subheader("Coffee Machine")
with st.form("My Form"):
    st.write("**Order your coffee**")

    # Input variables
    coffee_bean = st.selectbox("Coffee Bean",["Arabica","Robusta"])
    coffee_roast = st.selectbox("Coffee roast", ["Light", "Medium", "Dark"])
    brewing_val = st.selectbox("Brewing method", ["Aeropress", "Drip", "French press", "Moka pot", "Siphon"])
    serving_type_val = st.selectbox("Serving format", ["Hot", "Iced", "Frappe"])
    # st.slider will take only int/float values..for string values use st.select_slider
    milk_val = st.select_slider("Milk intensity", ["None", "Low", "Medium", "High"])
    owncup_val = st.checkbox("Bring own cup")

    # every form must have a submit button
    submitted = st.form_submit_button("Submit")

if submitted:
    st.markdown(f"""
    You coffee was ordered😁
    - Coffee bean: `{coffee_bean}`
    - Coffee roast: `{coffee_roast}`
    - Brewing: `{brewing_val}`
    - Serving type: `{serving_type_val}`
    - Milk: `{milk_val}`
    - Bring own cup: `{owncup_val}`    
    """)
else:
    st.write("Please place your order!")

# Using object notation

form = st.form("my_form")
selected_val = form.slider("Select a value",0,10)
form.form_submit_button("Submit")

st.write("Selected value :",selected_val)

st.header("Query parameter")
# Query parameters are the key-value pairs you see at the end of a website link after a question mark
# This line tells Streamlit to look up at the browser's URL bar and grab everything after the ?
# will retrieve a dictionary with different keys and list of its values stored in query_params
query_params = st.query_params
st.write(query_params)
# we can fetch the values of the list using keys
# the first notation is preferred bcuz if there are no query params then the second one throws error
# if the list empty the value assigned is none
firstname = query_params.get("name")
surname = query_params.get('surname')

if firstname != None and surname != None:
    st.write(f"Hello {firstname} {surname}.How are you?")


st.header("Caching in Streamlit")
# since the whole code reruns everytime you interact with something on the app...if you are doing some heavy operation like loading a big dataset it would make the app very slow 
# Caching allows you to save the output of a heavy function so you can completely skip running its code on a rerun.
# 2 types of caching:
# 1.@st.cache_data : used when a function returns serializable data that could be saved on a file like list,datframe,etc.Everytime data is pulled from the app a fresh copy of data is given to the user
# without caching it was taking 0.9176 seconds to load the data for thr first time and 0.8313 for the second
# with caching first it took 1.06 sec but the second time it was only 0.46
# because with caching the data is being stored in the cache and when the code is rerun it not running the loading part because the loading function is same..the cache will be updated only if the function is changed
# if a time.sleep(n) is included in the data loading function then without caching it would take n seconds to run the function everytime but with caching only first time data laoding is slow after that the data copy from the cache is provided so it would be fast
from time import time
st.subheader("Data cahching")
a0 = time()
@st.cache_data
def load_data():
    df = pd.DataFrame(
        np.random.randn(2000000,5),columns = ['a','b','c','d','e']
    )
    return df
st.write(load_data())
a1 = time()
st.info(a1-a0)
# 2.@st.cache_resource : used when funtions returns a global object/resource that you do not want to clone in your memory like a ml model


# st.session_state is a global Python dictionary that survives reruns, remembers data, choices, or counters for a single user session.
# the session variable are the ones which wont be updated even if rerun happens only updated if explicitly changed
# forms are also session state
st.header("st.session_state")

def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs/2.2046

def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg*2.2046

st.subheader("Input")
col1 , spacer , col2 = st.columns([2,1,2])
with col1:
    # key will store the result in the session state dictionary with lbs as its key
    # on_change makes sure that as soon as the value of one of them is changed the others is change first before rerunning the script
    pounds = st.number_input("Pounds:",key = "lbs",on_change =lbs_to_kg)
with col2:
    kilogram = st.number_input("Kilograms:",key = "kg",on_change =kg_to_lbs)
st.subheader("Output")
st.write(st.session_state)
