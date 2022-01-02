import streamlit as st
from io import StringIO
import pandas as pd

### FUNCTIONS

def format_csv(df):
    features = df.columns.to_list()
    new_df = pd.DataFrame()
    two_sided = ['engine', 'conflict']
    new_col = []
    for feature in features:
        col_list = df[feature].dropna().to_list()
        if feature in two_sided:
            start = 0
            finish = 2
            for i in range(0,len(col_list)//2):
                chunk = col_list[start:finish]
                line = str.join(';', chunk)
                line = feature + ';' +  line + ';;'
                new_col.append(line)
                start = finish
                finish += 2
        else:
            start = 0
            finish = 4
            for i in range(0,len(col_list)//4):
                chunk = col_list[start:finish]
                line = str.join(';', chunk)
                line = feature + ';' +  line + ';;'
                new_col.append(line)
                start = finish
                finish += 4
        new_df = pd.DataFrame(new_col)
        
    return new_df

st.set_page_config(page_title="CSV Converter", page_icon="", layout='wide')
st.title('Story Engine CSV Converter')

st.markdown('Use this to convert a simple csv file to the format needed for the Story Engine Web app')

col1, col2, col3 = st.columns([3,1,3])
with col1:
    st.image('politics_cards.png')
with col2: 
    st.image('arrow.png')
with col3:
    st.image('politics.png')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    new_df = format_csv(df)

    csv = new_df.to_csv(index=False, header=False).encode('utf-8')

    st.download_button(
        label="Download Re-formatted CSV",
        data=csv,
        file_name='formatted_cardset.csv',
        mime='text/csv',
    )




