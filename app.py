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

