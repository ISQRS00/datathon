import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import date, timedelta
from plotly.subplots import make_subplots
# Configurações do Streamlit
st.set_page_config(page_title="Deploy | Datathon | FIAP", layout='wide')

# Função para carregar imagens
def load_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))
# Configuração para a página em modo wide
#st.set_page_config(page_title="Dashboard de Previsões de Preço de Petróleo", layout='wide')
# Dicionário com informações dos insights


# Criando a interface do Streamlit
with st.container():
    # Título da aplicação
    st.header("Análises")
    
    # Criando as abas principais
    main_tabs = st.tabs(["Pedra - Visão", "Pedra - Fase", "Desepenho acadêmico","Desempnho psicosocial","Desempnho psicopedagógico","Ponto de virada","Conclusão","Link"])

    # Aba de Insights
   
    # Aba de Dados Históricos
    with main_tabs[0]:
        st.markdown(f"""
            A classificação das pedras é realizada com base na nota INDE (Índice de Desenvolvimento Educacional), que, por sua vez, considera outros indicadores apresentados nas demais páginas.
            No primeiro gráfico desta análise, é possível verificar, pela média do INDE, que todos os valores estão dentro da faixa correspondente a cada classificação de pedra. Já no segundo gráfico, observamos a distribuição dos alunos por categoria, sendo a classificação Ametista a mais predominante, seguida por Ágata, Quartzo e Topázio
            De maneira geral, percebe-se que o percentual de alunos classificados como Ametista e Quartzo tem diminuído ao longo dos anos, enquanto as classificações Topázio e Ágata têm apresentado crescimento.
        """)
    
        # Exibindo a imagem relacionada ao gráfico de preços
        img = load_image("https://raw.githubusercontent.com/ISQRS00/datathon/refs/heads/main/prints/pedravis%C3%A3o.PNG")
        st.image(img, use_container_width=True)
    
    with main_tabs[1]:
        (f"""
         
          Neste gráfico, podemos observar a distribuição das pedras por ano e fase.  
        De modo geral, a distribuição por fase tende a permanecer relativamente estável, porém alguns pontos se destacam:

        - **A classificação Quartzo** apresenta um percentual maior nas fases intermediárias e finais.  
          - Em 2020, na fase 6, atingiu seu pico, representando **53%** dos alunos dessa fase.  
          - Já em 2022, na fase 7, alcançou **39%**.  
          - Nessas ocasiões, Quartzo superou as classificações **Ametista** e **Ágata**, que costumam ser predominantes.

        - **As classificações Ametista e Ágata** são as mais frequentes na maioria das fases e anos, mantendo uma participação significativa.

        - **A classificação Topázio** possui a menor representatividade em comparação com as demais.  
          - Destaca-se na fase 1, onde já teve uma participação relevante, mas que vem diminuindo.  
          - Na fase 6, nos anos de 2020 e 2021, não houve registros dessa classificação.
           
           """)


        img = load_image("https://raw.githubusercontent.com/ISQRS00/datathon/refs/heads/main/prints/pedras_fases.PNG")
        st.image(img, use_container_width=True)

    with main_tabs[2]:
        (f"""
         
          As métricas IDA (Indicador de Desempenho Acadêmico) e IEG (Indicador de Engajamento) apresentaram comportamentos semelhantes ao longo dos três anos analisados. Ambas atingiram seu pico em 2020, sofreram uma queda em 2021 e registraram uma recuperação em 2022. Esses indicadores são de grande importância, pois fazem parte das três variáveis que possuem peso 0,2 no cálculo do INDE para fases inferiores a 8.
          
          Ao analisar esses indicadores por ano e tipo de pedra, observa-se que, apesar da tendência geral, algumas classificações não seguiram exatamente esse padrão. Por exemplo, a métrica IEG para Topázio apresentou pequenas quedas contínuas até 2022, enquanto a métrica IDA para Quartzo teve seu pico em 2021, justamente quando a média geral desse indicador caiu.
          
          Já a métrica IAN (Indicador de Adequação de Nível) apresenta uma tendência de queda contínua. Mesmo ao segmentar essa métrica por ano e tipo de pedra, não há variações significativas, pois todas as classificações seguem essa mesma trajetória de declínio.
           
           """) 
        
        

    # Aba de "Motivo da escolha do modelo"

        img = load_image("https://raw.githubusercontent.com/ISQRS00/datathon/refs/heads/main/prints/desempenho_academico.png")
        st.image(img, use_container_width=True)
    
    with main_tabs[3]:
        st.markdown(f"""
         As métricas IAA (Indicador de Autoavaliação) e IPS (Indicador Psicossocial) apresentaram, de modo geral, um desempenho estável, com a métrica IPS mostrando um aumento gradual ao longo do tempo. Ambas possuem o mesmo peso (0,1) no cálculo do INDE para fases inferiores a 8.
                    
        """)
        img = load_image("https://raw.githubusercontent.com/ISQRS00/datathon/refs/heads/main/prints/psicosocial.PNG")
        st.image(img, use_container_width=True)

    with main_tabs[4]:
        st.markdown(f"""
        A métrica IPV (Indicador do Ponto de Virada) é uma das mais importantes para o cálculo do INDE em fases inferiores a 7, pois possui peso 0,2. Ela se manteve estável ao longo dos anos, apresentando apenas uma pequena queda.

A métrica IPP (Indicador Psicopedagógico), que considera as avaliações feitas por psicólogos, registrou um leve aumento em 2021, seguido por uma queda de mais de 1 ponto em 2022. Ao analisar essas métrica por ano e tipo de pedra, observa-se que essa queda ocorreu em todas as classificações ao longo do período.
                    
        """)
        img = load_image("https://raw.githubusercontent.com/ISQRS00/datathon/refs/heads/main/prints/psicopedag%C3%B3gico.PNG")
        st.image(img, use_container_width=True)

    with main_tabs[5]:
        st.markdown(f"""
         O percentual de alunos que atingiram o Ponto de Virada varia significativamente entre as fases. De modo geral, a média para os anos analisados é de 16%. No entanto, um ponto que chama atenção é a fase 6, onde, em 2020 e 2021, apenas 3% e 4% dos alunos, respectivamente, atingiram essa métrica. Em 2022, porém, esse percentual saltou para 56%, destoando completamente do padrão histórico.
         Ao analisar essa métrica por tipo de pedra, observa-se que a maioria dos alunos que alcançam o Ponto de Virada pertence às classificações Topázio ou Ametista, embora esta última apresente um percentual menor. As demais classificações, por outro lado, têm pouca ou nenhuma representatividade nesse indicador.
                    
        """)

        img = load_image("https://raw.githubusercontent.com/ISQRS00/datathon/refs/heads/main/prints/ponto_de_virada.PNG")
        st.image(img, use_container_width=True)

        
    with main_tabs[6]:
        st.markdown("""
                    



A análise das métricas educacionais ao longo dos anos revela padrões importantes e algumas oscilações significativas no desempenho e engajamento dos alunos. Observamos que as métricas IDA (Indicador de Desempenho Acadêmico) e IEG (Indicador de Engajamento) seguiram um comportamento semelhante, com um pico em 2020, queda em 2021 e recuperação em 2022, embora algumas classificações de pedra tenham apresentado variações específicas. Já a métrica IAN (Indicador de Adequação de Nível) mostrou uma tendência contínua de queda, sem distinção relevante entre classificações.



As métricas IAA (Indicador de Autoavaliação) e IPS (Indicador Psicossocial) mantiveram-se relativamente estáveis, com um leve crescimento do IPS. No entanto, a métrica IPP (Indicador Psicopedagógico) demonstrou um aumento em 2021, seguido por uma queda expressiva em 2022, afetando todas as classificações de tipo de pedra. A métrica IPV (Indicador do Ponto de Virada), essencial no calculo INDE das fases inferiores a 7, manteve-se estável, exceto por uma queda gradual ao longo dos anos.



A classificação das pedras evidencia que Ametista e Ágata são predominantes na maioria das fases e anos, enquanto Quartzo se destaca mais nas fases intermediárias e finais. Topázio, por sua vez, tem menor representatividade, embora tenha aumentado sua presença em algumas fases. Além disso, o percentual de alunos que atingiram o Ponto de Virada manteve-se estável na maioria das fases, mas apresentou um crescimento atípico na fase 6 em 2022, passando de 4% em 2020 para 56% em 2022.



Esses dados demonstram que, apesar da estabilidade de algumas métricas, há variações relevantes que podem indicar mudanças estruturais ou intervenções pontuais que impactam o desempenho dos alunos ao longo do tempo. A análise contínua dessas métricas é essencial para compreender essas dinâmicas e promover estratégias mais eficazes para o desenvolvimento acadêmico e engajamento dos estudantes. """)

    with main_tabs[7]:
        st.markdown("""
        ### Link do Nootbook e do PowerBI
Você pode baixar o dashboard interativo para análise no Power BI diretamente pelo link abaixo:
        [Arquivo do Power BI](https://github.com/ISQRS00/datathon/blob/main/dashboard/datathon_fase_5.pbix)
                    
        """)
