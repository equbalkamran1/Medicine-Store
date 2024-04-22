import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(layout="wide")
st.title('Naseem Medical Hall Receipt Generator')






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

self_receipt2=(self_receipt.set_index('Name')
        .replace('\$\s+','', regex=True)
        .astype(float)
        .map('{:,.2f}'.format))
st.table(self_receipt2)

del col1
del col2

col1, _,col2 = st.columns([18, 20, 6])

result_predisc='₹{:.2f}'.format(self_receipt.SP_Amount.sum())
result_postdisc='₹{:.2f}'.format(self_receipt.SP_Amount.sum()-self_receipt.SP_Amount.sum()*disc_per/100)

old_price_text = '<p style="font-family:sans-serif; color:Blue; font-size: 36px;">Amount before discount</p>'
old_price_val='<p style="font-family:sans-serif; color:Blue; font-size: 36px;">'+result_predisc+'</p>'
col1.markdown(old_price_text, unsafe_allow_html=True)
col2.markdown(old_price_val, unsafe_allow_html=True)

disc_text='<p style="font-family:sans-serif; color:Blue; font-size: 36px;">Discount</p>'
disc_val='-{:.2f}%'.format(disc_per)
col1.markdown(disc_text, unsafe_allow_html=True)
col2.markdown('<p style="font-family:sans-serif; color:Blue; font-size: 36px;">'+disc_val+'</p>', unsafe_allow_html=True)



new_price_text = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">Final Amount after discount</p>'
new_price_val='<p style="font-family:sans-serif; color:Green; font-size: 42px;">'+result_postdisc+'</p>'
col1.markdown(new_price_text, unsafe_allow_html=True)
col2.markdown(new_price_val, unsafe_allow_html=True)
