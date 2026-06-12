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
df2 = pd.DataFrame(np.random.randn(200,3),
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
    np.random.randn(50,3),
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


