import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(layout="wide")
st.title('Naseem Medical Hall Receipt Generator')



hide_streamlit_style = """
            <style>
            tbody th {display:none}
            .blank{
            display: none;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)




med_count=st.number_input('Select Number of Medicines',1,15,4)
disc_per=st.slider('Select Discount Percentage',0,100,10)
med_master=pd.read_excel('Medicine Master.xlsx')
col1, col2 = st.columns(2)
self_receipt=pd.DataFrame(columns=['Name','Selling Price','Quantiy','SP_Amount','Discounted Amount'])

for i in range(med_count):
    med_name=col1.selectbox('Select Medicine',med_master.Name,key = str(i))
    med_qty=col2.number_input('Select Quantity',1,15,key=str(i)+str(i))
    med_sp=med_master['Cost Price'][med_master[med_master['Name']==med_name].index.values[0]]
    self_receipt.loc[len(self_receipt)] = [med_name,med_sp,med_qty,med_qty*med_sp,med_qty*med_sp-med_qty*med_sp*disc_per/100]

st.table(self_receipt)

result='Final Amount with discount of {}%=  ₹{}'.format(disc_per,self_receipt.SP_Amount.sum()*disc_per/100)

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">'+result+'</p>'
st.markdown(new_title, unsafe_allow_html=True)
