import streamlit as st
import pandas as pd
from csvInfo import display_csv, add_row, remove_row

file_name = 'example.csv'

## Add New Items to Inventory
st.header("Add to Inventory:")
col1, col2 = st.columns(2)
with col1:
    model = st.text_input("Model Number")
    cpu = st.text_input("CPU")
with col2:
    with st.form("serial", clear_on_submit=True):
        sn = st.text_input("Serial Number")
        if st.form_submit_button("Submit"):
            if model != "" and sn !="":
                try:
                    add_row(file_name, [model, sn, cpu])
                    st.success("Added to Inventory")
                except:
                    st.error("Serial Number Already in inventory")
            else:
                st.error("Invalid response")

## Remove Item From Inventory
with st.form("Remove", clear_on_submit=True):
    st.header("Remove from Inventory:")
    sn = st.text_input("Serial Number")
    if st.form_submit_button("Submit"):
        try:
            remove_row(file_name, sn)
            st.success("Removed")
        except:
            st.error("Could not remove item")


## Display Inventory Items
st.header("View Inventory:")
if st.button("View CSV"):
    df = pd.DataFrame(display_csv(file_name))
    st.dataframe(df)

