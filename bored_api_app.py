import streamlit as st
# we get the output acc to our input from the third server by calling an API and we talk to API's through requests
# requests is a Python library which is sen http request across web
import requests
import time

# bored API is a free public api which returns a activity to do based ob=n the input parameters you give
# now our app wont work on static data but it will take input and send it to another server(Bored API) and receives reply from it
st.set_page_config(layout = 'wide')
st.title("🗯️ Bored API App",text_alignment = 'center')
st.subheader("Bored of your daily routine and want to try something new",text_alignment = 'center')
st.subheader(" !! Bored API App to your rescue !! ",text_alignment = 'center')

# used a form to take the inputs instead of a sidebar selectbox because form is session state and wont rerun the script again and again until submitted
with st.form("user_input"):
    st.subheader("Fill out your preferences")
    selected_type = st.selectbox("What type of activity would you prefer today ?",["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])
    participants = st.number_input("Enter the desired number of participants",min_value = 1,max_value = 10,value = 1,step =1)

    submit_button = st.form_submit_button("✨ Find Me Something To Do")

if submit_button:
    # we create a custom url which modifies itself sccording to the preference of the user usinf f strings
    url = f"https://bored.api.lewagon.com/api/activity?type={selected_type}&participants={participants}"

    try:
        # acc to the selected type the api hits the custom url and brings back raw data returned by the url
        json_data = requests.get(url)
        # we convert that raw data into json format like python dictionary
        # if the api has fetches data successfuly the suggested_activity var will hava a dictionary stored else it will be empty dict
        suggested_activity = json_data.json()
        with st.sidebar:
            with st.expander("Fetched JSON data"):
                st.write(suggested_activity)

        if "error" in suggested_activity:
            st.error("No activity found matching those filters.Please try shuffling them")
        else:
            # info and metric for style rather than plain text
            st.info("Suggested Activity")
            # we crete a loading placeholder and then display the loading comments
            loading_placeholder = st.empty()
            with loading_placeholder.container():
                st.write("Analysing Preferences...")
                time.sleep(1)
                st.write("Searching our database...")
                time.sleep(1)
                st.write("Generating Response...")
                time.sleep(1)
            # just before displaying our activity we make the palceholder empty and the comments vanish making it look like that is actually searched and then displayed the result
            loading_placeholder.empty()

            st.success(suggested_activity['activity'])

            spacer, col1 ,spacer ,col2,spacer = st.columns([0.5,2,1,2,0.5])
            with col1:
                st.metric(label='Participants needed', value=suggested_activity['participants'])
            with col2:
                st.metric(label='Category', value=suggested_activity['type'].capitalize())
    except Exception as e:
        st.error("ERROR OCCURED.Check your NETWORK CONNECTION or Please try later!")


    
else: 
    st.write("👆**Please fill out the above form**")

# Placeholders
    # since the script lops every time you interact with anything on the app
    # st.empty() is a layout feature that breaks this rule. It creates a placeholder—a reserved, blank slot on your web page that can be changed, overwritten, or completely erased at any point while your script is executing.
    # 2 ways to interact with an st.empty() placeholder
    # Method 1: Direct Overwriting (Single Object)
    # You can assign your placeholder to a variable and use it to replace a single item (like text, an image, or a chart) over and over again.
    # Method 2: The Container Group (Multiple Objects)
    # If you want to place multiple elements inside a placeholder (like an info box, a spinner, and some text lines) and erase them all simultaneously, combine it with a .container() block. This is the exact method you just used to fix your loading animations!
