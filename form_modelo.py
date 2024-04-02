import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO
from io import BytesIO
import datetime
from modelo import modeloBolsista


def prob_bolsista():
    data_simulacao = st.date_input("Data da simulação:", datetime.date(2024, 1, 1))
    nome_aluno = st.text_input('Nome do Aluno:')
    IAA = st.slider('Média das Notas de Auto avaliaçao do Aluno?',  0.0, 10.0,  0.0)
    IEG = st.slider('Média das Notas de Engajamento do Aluno?',  0.0, 10.0,  0.0)
    IPS = st.slider('Média das Notas Psicossociais do Aluno?',  0.0, 10.0,  0.0)
    IDA = st.slider('Média das Notas do Indicador de Aprendizagem?',  0.0, 10.0,  0.0)
    port = st.slider('Média das Notas de Português do Aluno?',  0.0, 10.0,  0.0)
    mat = st.slider('Média das Notas de Matemática do Aluno?',  0.0, 10.0,  0.0)
    ing = st.slider('Média das Notas de Inglês do Aluno?',  0.0, 10.0,  0.0)


    if st.button('Enviar'):
        dadosBolsista = [IAA, IEG, IPS, IDA, port, mat, ing]
        modeloBolsista(data_simulacao, nome_aluno, dadosBolsista)


