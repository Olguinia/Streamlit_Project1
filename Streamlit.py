#!/usr/bin/env python
# coding: utf-8

# #### Import Libraries

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import seaborn as sns 
import plotly.graph_objects as go 
import plotly.express as px 
from plotly.offline import init_notebook_mode, iplot
import plotly.figure_factory as ff


# #### Application Creation

# In[2]:


# Expand the web app across the whole screen
st.set_page_config(layout="wide")


# In[3]:


#Image
image=Image.open("/Users/user/Desktop/Streamlit project/OSB_LOGO.jpg")
st.image(image,use_column_width=True)


# In[12]:


#create containers horizontally
header = st.container()
data = st.container()
features = st.container()
Interactive_visu = st.container()
Interactive_visu_2 = st.container()
Interactive_visu_3 = st.container()
Interactive_visu_4 = st.container()
Interactive_visu_5 = st.container()
Interactive_visu_6 = st.container()

# In[5]:


with header:
    st.title('OSB Community')
    st.text("""
    If you are in doubt and you are not sure whether you will be accepted or not! or if you will be able to succeed in MHRM and MSBA
    Here is a study to answer all your doubts! 
    """)


# In[6]:


with data:
    st.header("Graduates Dataset")
    st.text("""
    This dataset was collected from AUB-OSB to help OSB identify the most important elements that needs to be probed
    for an efficient and accurate prediction when it comes to estimating a student’s graduate GPA"
    However here we will help you answer all your doubts!
    """)
    students_data = pd.read_csv("/Users/user/Desktop/Streamlit project/OSB_Graduates.csv")
    
    if st.checkbox("Preview Dataset"):
        number = st.slider("Select No of Rows", 1, students_data.shape[0])
        st.write(students_data.head(number))
            
    if st.checkbox("Show Column Names"):
        st.write(students_data.columns)
        
    if st.checkbox("Show Dimensions"):
        st.write(students_data.shape)
        
    if st.checkbox("Show Summary"):
        st.write(students_data.describe())

    if st.checkbox("Show Boxplots for Summary"):
        trace1 = go.Box(y=students_data["Gender"],boxmean = 'sd',name="Gender", fillcolor= "lightcoral",line=dict(color='black'))
        trace2 = go.Box(y=students_data["Program"],boxmean = 'sd',name="Program", fillcolor= "indianred",line=dict(color='black'))
        trace3 = go.Box(y=students_data["Cohort"],boxmean = 'sd',name="Cohort", fillcolor= "brown",line=dict(color='black'))
        trace4 = go.Box(y=students_data["Employed"],boxmean = 'sd',name="Employed", fillcolor= "firebrick",line=dict(color='black'))
        data1 = [trace1, trace2, trace3, trace4]
        fig = go.Figure(data=data1)
        st.write(fig)


# In[24]:

with Interactive_visu:
    st.header("Main Nationalities")
    col,img =st.columns(2)
    nationalities= pd.DataFrame(students_data["Region"].value_counts())
    nationalities =  nationalities.reset_index()
    nationalities.columns= ["Region","Count"]
    
    fig = px.bar(nationalities, y="Region", x="Count", color="Region", orientation="h", hover_name="Region",
             color_discrete_map={
                "Europe": "red",
                "Asia": "firebrick",
                "USA": "darkred",
                "North America": "goldenrod",
                "Africa": "magenta"},
             title="Region of Students at AUB Applying to MSBA AND MHRM")
    fig.update_layout(width=600,height=400)
    col.write(fig)
    
    image1=Image.open("/Users/user/Desktop/Streamlit project/students.jpg")
    new_image = image1.resize((400, 300))
    img.image(new_image,width=None, caption= "OSB students in a MSBA course")
    


# In[20]:


with Interactive_visu_2:
    st.header("Students Ages and their GPA")
    col1,col2 =st.columns(2)
    
    fig1 = ff.create_distplot([students_data.Age_at_Admission],['Age_at_Admission'],colors=['brown'])
    fig1.update_layout(title_text='Students Ages', width=600,height=400)
    col1.write(fig1)
    
    GPA_LOW = students_data[students_data['GPA1'] <=2 ]
    GPA = students_data[students_data['GPA1'] <= 3]
    GPA_HIGH = students_data[students_data['GPA1'] <= 4]
    fig2 = ff.create_distplot([GPA_LOW.Age_at_Admission, GPA.Age_at_Admission, GPA_HIGH.Age_at_Admission], ["LOW", "MED","HIGH"],bin_size=15, colors=["brown","firebrick","maroon"])
    fig2.update_layout(title_text='Age Versus GPA',width=600,height=400)
    col2.write(fig2)


# In[ ]:

with Interactive_visu_3:
    st.header("Being Employed or a Part Timer can affect your GPA?")
    col1,col2 = st.columns(2)
    EMPLOYED = students_data[["Employed","GPA2"]].copy()
    emp = pd.DataFrame(EMPLOYED["Employed"].value_counts())
    emp =  emp.reset_index()
    emp.columns = ["Employed","Count"]
    GPA2 = students_data["GPA2"]
    emp["GPA2"] = GPA2
    fig3 = px.bar(emp, x='Employed', y='GPA2',color="Employed",
             color_discrete_map={
                "Yes": "firebrick",
                "No": "darkred"},)
    fig3.update_layout(title_text='Employed Versus GPA')
    col1.write(fig3)
    
    COHORT = students_data[["Cohort","GPA2"]].copy()
    FP = pd.DataFrame(COHORT["Cohort"].value_counts())
    FP =  FP.reset_index()
    FP.columns = ["Cohort","Count"]
    GPA2 = students_data["GPA2"]
    FP["GPA2"] = GPA2
    fig4 = px.bar(FP, x='Cohort', y='GPA2',color="Cohort",
             color_discrete_map={
                "PT": "darkred",
                "FT": "firebrick"},)
    fig4.update_layout(title_text='Part Time Versus GPA')
    col2.write(fig4)


with Interactive_visu_4:
    st.header("Only AUB business students are accepted in MSBA and MHRM?")
    col1,col2 = st.columns(2)
    Last_deg= pd.DataFrame(students_data["Last_Degree"].value_counts())
    Last_deg = Last_deg.reset_index()
    Last_deg.columns = ["Last_Degree","Count"]
    fig5 = px.pie(Last_deg, values='Count', names='Last_Degree', color_discrete_sequence=px.colors.sequential.RdBu)
    fig5.update_layout(width=600,height=400)
    col1.write(fig5)
        
   
    uni= pd.DataFrame(students_data["Undergrad_University"].value_counts())
    uni = uni.reset_index()
    uni.columns = ["Undergrad_University","Count"]
    
    top_uni = col2.text_input ("How many of the top universities that applies to MSBA and MHRM would you like to see?" , 5)
    top_uni = int(top_uni)
    uni = uni.head(top_uni)
    
    fig6 = px.pie(uni, values='Count', names='Undergrad_University', color_discrete_sequence=px.colors.sequential.RdBu)
    fig6.update_layout(width=600,height=400)
    col2.write(fig6) 



with Interactive_visu_5:
    st.header("Is it true that only males succeed in MSBA and MHRM?")
    col1,col2 = st.columns(2)
    succ = students_data[["Gender","GPA2"]].copy()
    FM = pd.DataFrame(succ["Gender"].value_counts())
    FM =  FM.reset_index()
    FM.columns = ["Gender","Count"]
    GPA2 = students_data["GPA2"]
    FM["GPA2"] = GPA2
    fig7 = px.bar(FM, x='Gender', y='GPA2',color="Gender",
             color_discrete_map={
                "F": "brown",
                "M": "firebrick"},)
    fig7.update_layout(title_text='Gender Versus GPA')
    fig7.update_layout(width=600,height=400)
    col1.write(fig7)


    col2.text("""


    The OSB Discourse Community welcomes students from all over the world!
    No matter your age or your nationality, you can be part of their community.
    The only skill you should have is to be a dreamer!
    If you are employed and worried about pursuing a Master's degree,
    OSB gives you the opportunity to apply for a part-time degree!
    Don't QUIT your job ! You can Do it ! 

    You can be an engineer, a business person, a doctor, a lawyer, a financial expert, etc.,
    and still hold an MSBA or MHRM degree.
    Even though most of our students are from AUB, LAU, NDU, and USJ,there are no boundaries.
    The OSB community is open to anyone at anytime.
    And no, we do not discriminate! Whether you are a male or female,
    you will both succeed equally and have the same career opportunities!

    We hope that this small interactive study helped you overcome your doubts and join our community !

    Remember, you only need to be a dreamer!
 
    """)


with Interactive_visu_6:
    st.header("Get to know our students undergrad universities and bachelor degrees!")
    uni = students_data[["Undergrad_University","Last_Degree"]].copy()
    uni1 = pd.DataFrame(uni["Undergrad_University"].value_counts())
    uni1 =  uni1.reset_index()
    uni1.columns = ["Undergrad_University","Count"]
    Last_Degree = students_data["Last_Degree"]
    uni1["Last_Degree"] = Last_Degree
    lastdegree_options = uni1["Last_Degree"].unique().tolist()
    lastdegree_options = st.selectbox("Which bachelor degree would you like to see?", lastdegree_options, 0)
    uni1 = uni1[uni1["Last_Degree"] == lastdegree_options]
    fig8= px.bar(uni1, x='Undergrad_University', y='Count',color="Last_Degree",color_discrete_sequence=px.colors.sequential.RdBu)
    st.write(fig8)
