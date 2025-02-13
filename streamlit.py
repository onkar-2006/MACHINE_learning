#import library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


#title of thee page
st.title("hello world")

#print in the streamlit is write
st.write("ur are genious")

#slider
x=st.slider("enter your range" ,min_value=0 , max_value=100 , value=50)
st.write("ur enter value is " ,x)

#buttons
if st.button("say hello"):
    st.write("hello")

#checkbox
check=st.checkbox("is agree")
if check:
    st.write("i agreee")

#radio button
radi=st.radio("enter your choice" ,[1,2,3])
st.write("you enter choice {radi}")

#selectbox
select=st.selectbox("click the selection",[1,2,4])
st.write("your selection{select}")

#file uploader
upload_file=st.file_uploader("choose the file")
if upload_file is not None:
    st.write("ur file is upload sucessfully")

#data frame creation
data={"CGPA":[9.8 ,3.2,4.5] , "placement":[1 , 3 ,5]}
df=pd.DataFrame(data)
st.write(df)

#taking the input from the user
result=st.text_input("enter the number u want")
if result:
    st.write("ur enter number is" ,result)

#graph or plot
fig ,ax=plt.subplots()
ax.plot([1,2,4],[3,4,5])
st.pyplot(fig)

#sidebar
st.sidebar.title("sidebar")
st.sidebar.write("this is the sidebar")

#creating the dataset
col1 ,col2, col3=st.columns(3)
col1.write("this is first column")
col2.write("this is the second column")
col3.write("this is the third column")

#tabs
st1 ,st2 =st.tabs(["tab 1" ,"tab 2"])
with st1:
    st.write("tab one")
with st2:
    st.write("tab two")


#expander
with st.expander("See explanation"):
    st.write("Here is the detailed explanation of the data.")

#session state 
if 'count' not in st.session_state:
    st.session_state.count=0
#seesion state 
st.button('increment' ,on_click=lambda :setattr(st.session_state ,'count' ,st.session_state.count+1))
st.write(f"the current count:{st.session_state.count}")








