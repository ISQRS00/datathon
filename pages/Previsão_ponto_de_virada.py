import streamlit as st
import pandas as pd
import joblib
import requests
from io import BytesIO
from sklearn.preprocessing import StandardScaler

# 📌 1️⃣ Carregar os arquivos salvos
@st.cache_data
def load_model():
    url = "https://raw.githubusercontent.com/ISQRS00/datathon/main/arquivos_utilizados/modelo_2.pkl"
    try:
        response = requests.get(url)
        response.raise_for_status()
        model = joblib.load(BytesIO(response.content))
        return model
    except Exception as e:
        st.error(f"Erro ao carregar o modelo: {e}")
        return None

@st.cache_data
def load_scaler():
    url = "https://raw.githubusercontent.com/ISQRS00/datathon/main/arquivos_utilizados/scaler_2.pkl"
    try:
        response = requests.get(url)
        response.raise_for_status()
        model = joblib.load(BytesIO(response.content))
        return model
    except Exception as e:
        st.error(f"Erro ao carregar o scaler: {e}")
        return None

@st.cache_data
def load_label_encoder_flg():
    url = "https://raw.githubusercontent.com/ISQRS00/datathon/main/arquivos_utilizados/label_encoder_flg.pkl"
    try:
        response = requests.get(url)
        response.raise_for_status()
        model = joblib.load(BytesIO(response.content))
        return model
    except Exception as e:
        st.error(f"Erro ao carregar o LabelEncoder: {e}")
        return None

@st.cache_data
def load_label_encoder_turma():
    url = "https://raw.githubusercontent.com/ISQRS00/datathon/main/arquivos_utilizados/label_encoder_turma.pkl"
    try:
        response = requests.get(url)
        response.raise_for_status()
        model = joblib.load(BytesIO(response.content))
        return model
    except Exception as e:
        st.error(f"Erro ao carregar o LabelEncoderTurma: {e}")

@st.cache_data
def load_accuracy():
    url = "https://raw.githubusercontent.com/ISQRS00/datathon/main/arquivos_utilizados/acuracia.pkl"
    try:
        response = requests.get(url)
        response.raise_for_status()
        model = joblib.load(BytesIO(response.content))
        return model
    except Exception as e:
        st.error(f"Erro ao carregar a acurácia: {e}")
        return None

modelo = load_model()
scaler = load_scaler()
label_encoder_flg = load_label_encoder_flg()
label_encoder_turma = load_label_encoder_turma()
acuracia = load_accuracy()

# 📌 2️⃣ Criar abas para organização
st.title("Predição do Ponto de Virada")

abas = st.tabs(["Introdução", "Predição"])

# 📌 3️⃣ Aba de Introdução
with abas[0]:
    st.markdown("""
    ### O que é o Ponto de Virada?
    O **Ponto de Virada (IPV)** representa um momento-chave na trajetória do aluno, 
    indicando que ele atingiu um nível de desenvolvimento acadêmico, engajamento 
    e maturidade emocional suficiente para avançar com sucesso para o próximo estágio da aprendizagem.

    ---
    
    ###Como ele é calculado?
    O modelo de previsão analisa diferentes fatores que influenciam o Ponto de Virada, incluindo:

    - **IAN (Indicador de Adequação de Nível):** Mede se o aluno está na fase escolar ideal para sua idade.
    - **IDA (Indicador de Desempenho Acadêmico):** Média das notas em disciplinas essenciais.
    - **IEG (Indicador de Engajamento):** Participação em atividades acadêmicas e voluntariado.
    - **Turma:** A turma do aluno, convertida em um número para análise.
    - **Fase:** O estágio atual do aluno no sistema educacional.

    ---
    
    ### O que o modelo faz?
    Com base nesses fatores, o modelo utiliza **Machine Learning** para prever se o aluno 
    atingiu ou não o Ponto de Virada, fornecendo um diagnóstico que auxilia educadores na tomada de decisões.

    ---
    
    ### Modelos de Machine Learning utilizados:
    Para alcançar alta precisão nas previsões, testamos três modelos diferentes:

    - **🌲 RandomForest:** Algoritmo baseado em árvores de decisão, capaz de lidar bem com dados complexos.  
      - **Acurácia:** 🟢 **95.15%**  
    - **📈 GradientBoosting:** Modelo que melhora continuamente os erros de predição para aumentar a precisão.  
      - **Acurácia:** 🟡 **81.63%**  
    - **📊 LogisticRegression:** Modelo estatístico usado para prever categorias binárias.  
      - **Acurácia:** 🔴 **76.28%**  

    O **RandomForest** foi o modelo que obteve a melhor performance, atingindo **95.15% de acurácia**, 
    sendo utilizado para as previsões apresentadas nesta ferramenta.

    ---
    
    ###  Acesse o Notebook Completo
    Para mais detalhes sobre o treinamento do modelo e a análise dos dados, 
    acesse o notebook completo no GitHub:  
    👉 [Clique aqui para ver o código](https://github.com/ISQRS00/datathon/blob/main/nootbooks/modelo_final_2_ponto_de_virada.ipynb)  
                
    
    ---
    
    ###  Base de entrada e saída utilizadas nesse modelo
    
    O modelo de previsão de ponto de virada foi desenvolvido utilizando uma base de dados mais recente, recentemente liberada. acesse os arquivos no GitHub:
    
    👉 [Clique aqui para baixar o arquivo de entrada](https://github.com/ISQRS00/datathon/blob/main/dados_de_entrada/PEDE%202024%20-%20DATATHON.xlsx)  
    
    👉 [Clique aqui para baixar o arquivo de saída](https://github.com/ISQRS00/datathon/blob/main/datasets/base_modelo_ponto_de_virada.csv)  
                

    """)


# 📌 4️⃣ Aba de Predição
with abas[1]:
    st.write("Insira os dados abaixo para verificar se o aluno atingiu o Ponto de Virada.")

    # Criar inputs do usuário (valores entre 0 e 10)
    num_ian = st.number_input("Número IAN", min_value=0.0, max_value=10.0, value=5.0)
    num_ida = st.number_input("Número IDA", min_value=0.0, max_value=10.0, value=5.0)
    num_ieg = st.number_input("Número IEG", min_value=0.0, max_value=10.0, value=5.0)
    num_fase = st.number_input("Número da Fase", min_value=0.0, max_value=10.0, value=5.0)

    # Criar um dicionário fixo para as turmas
    dict_turma = dict_turma = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'X', 23: 'Y', 24: 'Z'}

    # Criar um input de texto para a letra da Turma, com padrão "A"
    letra_turma = st.text_input("Digite a letra da Turma (A a Z, exceto W):", value="A", max_chars=1)

    # Verificar se a letra da turma é válida e converter para número correspondente
    if letra_turma.upper() in dict_turma.values():
        turma_transformada = [key for key, value in dict_turma.items() if value == letra_turma.upper()][0]
        valid_turma = True
    else:
        turma_transformada = None
        valid_turma = False
        st.error("Por favor, insira uma letra entre A e Z. Não existe turma com a letra W.")

    # Criar DataFrame com os inputs do usuário
    entrada_usuario = pd.DataFrame([[num_ian, num_ida, num_ieg, turma_transformada, num_fase]], 
                                   columns=["num_ian", "num_ida", "num_ieg", "_des_turma", "num_fase"])

    # Aplicar o scaler apenas se a turma for válida
    if scaler and valid_turma:
        entrada_tratada = scaler.transform(entrada_usuario)
        entrada_tratada = pd.DataFrame(entrada_tratada, columns=["num_ian", "num_ida", "num_ieg", "_des_turma", "num_fase"])
    else:
        st.error("Scaler não carregado corretamente ou turma inválida.")

    # Fazer a predição apenas se todos os requisitos forem atendidos
    if modelo and scaler and label_encoder_flg and label_encoder_turma and valid_turma and st.button("Verificar Ponto de Virada"):
        resultado_predito = modelo.predict(entrada_tratada)[0]  # Fazer predição
        
        # Converter a predição para a categoria original
        resultado_final = label_encoder_flg.inverse_transform([resultado_predito])[0]

        # 📌 Exibir resultado
        if resultado_final == "Sim":  
            st.success("✅ O aluno atingiu o ponto de virada!")
        else:
            st.warning("❌ O aluno ainda não atingiu o ponto de virada.")
