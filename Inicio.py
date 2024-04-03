from analises import realizar_analise
from form_modelo import prob_bolsista

import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import pandas as pd

with st.sidebar:
    selected = option_menu("Datathon", ["Home", 'Sobre a Passos Mágicos','Análises','Modelo','Conclusão'],
        icons=['house', 'book', 'bar-chart', 'cloud-upload', 'book'], menu_icon="cast", default_index=0)
    # selected

if selected == "Home":
    st.title("Datathon")
    st.write("O Datathon é um projeto que contempla a última fase da Pós-Tech em Data Analytics da instituição de ensino FIAP. É o desafio final que englobará os conhecimentos obtidos em todas as disciplinas do curso. Este não é apenas um hackathon para dados; é uma missão para iluminar e amplificar o trabalho vital da ONG Passos Mágicos, uma luz de esperança na vida de crianças e jovens em um município carente de São Paulo.")
if selected == "Sobre a Passos Mágicos":
    st.title("Sobre a Passos Mágicos")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("A Passos Mágicos atua desde 1992 num programa que visa a transformação de crianças e jovens de baixa renda, por meio da educação. Para isso, conta com uma equipe de profissionais qualificados e afetuosos e com uma metodologia baseada em quatro pilares fundamentais para que essa mudança seja possível: uma educação de qualidade, um suporte psicológico eficiente, a ampliação da visão de mundo do aluno e o encorajamento para que repliquem os ensinamentos recebidos e a transformação ocorrida em suas vidas.")
    with col2:
        st.image("data:image/png;base64,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", caption="")
if selected == "Análises":
    st.title("Análise dos Dados")
    realizar_analise()
if selected == "Modelo":
    st.title("Simulador de Bolsa de Estudo")
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image("data:image/png;base64,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", caption="")
    st.write("Com base nos dados fornecidos, foram identificados padrões para simular a probabilidade de um aluno adquirir uma bolsa de estudos em alguma instituição pela Passos Mágicos.")
    st.write("Nesta avaliação será considerado os indicadores de aprendizado, auto avaliação, engajamento do aluno, indicador psicossocial, notas em português, matemática, inglês e o ponto de virada.")
    st.write("O intuito é demonstrar para a Associação uma possibilidade de motivação aos alunos com base no esforço realizado através da educação.")
    st.write("Acreditamos que com um estudo aprofundado juntamente à ONG, outros dados relevantes poderão ser utilizados a fim de construir um modelo mais robusto.")

    prob_bolsista()


