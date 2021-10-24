import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os



st.header('translator')
# header to jeden z podtytułów wykorzystywnaych w Streamlit

st.subheader('O translatorze')
# subheader to jeden z podtytułów wykorzystywnaych w Streamlit

st.text('jest to przykladowy translator z jezyka angielskiego na niemiecki')
st.text('aby przetłumaczyć tekst prosze wpisać w polu fraze/zdanie a nastepnie kliknac ctr+enter')
# text używamy do wyświetlenia dowolnego tekstu. Można korzystać z polskich znaków.


import streamlit as st
from transformers import pipeline,XLMTokenizer, XLMWithLMHeadModel



option = st.selectbox(
    "Opcje",
    [
        "Angielski -> Niemiecki",
        "???",
    ],
)

if option == "Angielski -> Niemiecki":
    text = st.text_area(label="Wpisz tekst")
    if text:
        with st.spinner("Tlumaczenie tekstu, prosze czekac..."):
            translator = pipeline("translation_en_to_de")
            answer = translator(text)
        st.success('Przetlumaczone')
        
        st.code(answer[0]['translation_text'])

