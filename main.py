import streamlit as st
import pandas as pd
import numpy as np
import txtformat
#import create_plots
import data_manipulate

st.title('Finite Element Analysis text file format and data manipulation!')

st.write('Format, manipulate and display data from tensor output files that have been\nsaved as .txt files')

st.header('Run .txt formatting')

delimFileOpener = st.file_uploader(label="Select .txt file to add delimeters", type=['txt'], accept_multiple_files=False, key='format_file1', help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
if st.button('Add Delimeters'):
    if delimFileOpener is None:
        st.warning('Please submit a file')
    else:
        delimFile = delimFileOpener.getvalue()
        txtformat.delim(delimFile)

elemFileOpener = st.file_uploader(label="Select .txt file to add element labels", type=['txt'], accept_multiple_files=False, key='format_file2', help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

if st.button('Add Labels'):
    if elemFileOpener is None:
        st.warning('Please submit a file')
    else:   
        elemFile = elemFileOpener.getvalue()
        txtformat.addElem(elemFile)

st.header('Add extra columns to .txt file')
colname = st.text_input(label='Name of column', value='coolrate')
origcolFileOpener = st.file_uploader(label="Select .txt file to add a column to.", type=['txt'], accept_multiple_files=False, key='format_file3', help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
newcolFileOpener = st.file_uploader(label="Select .txt file that contains column.", type=['txt'], accept_multiple_files=False, key='format_file4', help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")


if st.button('Add column'):
    if origcolFileOpener is None or newcolFileOpener is None:
        st.warning('Please submit a file')
    elif colname is None:
        st.warning('Please enter a column name')
    else:  
        origcolFile = origcolFileOpener.getvalue()
        newcolFile = newcolFileOpener.getvalue()
        data_manipulate.addCol(colname, origcolFile, newcolFile)


    