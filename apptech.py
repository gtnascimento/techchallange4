import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from datetime import timedelta

st.set_page_config(page_title="Data Analytics - Fase 4 Tech Challenge | FIAP", layout='wide')

# Barra lateral para navegação
st.sidebar.title("Tech Challenge 4")
escolha = st.sidebar.radio(
    "Escolha uma seção:",
    options=["Introdução", "Objetivo", "Metodologia", "Modelo preditivo", "Análise", "Conclusão", "Referências"],
    index=0,
    help="Navegue pelas diferentes seções do projeto."
)

# Barra horizontal na sidebar
st.sidebar.markdown("---")

st.sidebar.markdown("**Integrantes do Grupo 43:**")
st.sidebar.markdown("Gabriel Tomaz do Nascimento - RM356231")
st.sidebar.markdown("Pedro Costa de Oliveira Neto - RM353263")
st.sidebar.markdown("Thiago Aragão Barros - RM353723")

if escolha == "Introdução":
    st.header(':orange[PÓS TECH – DATA ANALYTICS, 2024 - FIAP]')
    st.subheader(":orange[Fase 4 - Data Viz and Production Models]")
    st.subheader("📘 Introdução")
    st.write("""
    O mercado global de petróleo é dinâmico e impacta diretamente a economia mundial. Cada variação no preço do barril reflete não apenas mudanças nos mercados, mas também eventos geopolíticos, crises econômicas e transformações tecnológicas. Compreender as forças que impulsionam essas flutuações é essencial para empresas, governos e investidores, que precisam estar preparados para adaptar suas estratégias a um ambiente em constante mudança.

    Nesta apresentação, exploramos insights chave sobre os fatores que afetam o preço do petróleo, desde os acontecimentos geopolíticos até a evolução da demanda por energia e inovações tecnológicas. Analisaremos como esses elementos se interconectam para criar um panorama volátil e imprevisível, oferecendo um guia para decisões mais informadas e estratégicas.

    Com isso, buscamos não apenas entender as variações de preço, mas também antecipar tendências, identificar oportunidades e mitigar riscos no setor de energia. Esta análise se torna uma ferramenta indispensável para quem deseja entender o futuro do mercado de petróleo e seus reflexos em outras esferas da economia global.
    """)

    st.image("Cotação-do-Petróleo-2.webp", caption="Extração de petróleo", width=900)
    

elif escolha == "Objetivo":
    st.header(':orange[🎯 OBJETIVO]')
    st.write("""
    A importância desta apresentação está em demonstrar como os conhecimentos adquiridos ao longo do curso de Data Analytics podem ser aplicados a um problema real e complexo. Ao longo deste projeto, tivemos a oportunidade de integrar técnicas de análise de dados, modelagem preditiva e visualização interativa para resolver um desafio do mundo real relacionado à variação do preço do petróleo.

    Essa apresentação não se trata apenas de exibir um modelo ou um dashboard, mas sim de contar uma história por meio dos dados. É essencial mostrar como diferentes fatores, como crises econômicas, mudanças geopolíticas e a dinâmica do mercado de energia, impactam o preço do petróleo. Além disso, a previsão desses preços é uma ferramenta crucial para tomadas de decisão estratégicas, especialmente para empresas do setor energético, onde a previsão precisa de preços pode resultar em ganhos significativos ou evitar perdas.

    Neste contexto, esta apresentação oferece uma oportunidade única de mostrar não só a capacidade técnica adquirida, mas também a habilidade de interpretar e comunicar insights a partir de grandes volumes de dados. A experiência adquirida aqui é um passo fundamental para entender como a análise de dados pode influenciar diretamente o sucesso e a competitividade no mercado global.
    """)

elif escolha == "Metodologia":
    st.header(':orange[🛠️ METODOLOGIA]')
    st.write("""
    Nossa abordagem consiste em:
    1. Coleta de dados: Dados históricos relevantes foram coletados de fontes confiáveis.
    2. Limpeza de dados: Realizamos uma limpeza e tratamento dos dados para garantir qualidade.
    3. Análise exploratória: Investigamos padrões e tendências.
    4. Modelagem: Implementamos técnicas de modelagem preditiva para identificar insights.
    5. Visualização: Usamos ferramentas como Power BI e Streamlit para comunicar os resultados.
    """)

elif escolha == "Modelo preditivo":
    st.header(':orange[🧠 MODELO DE MACHINE LEARNING]')
    st.write("""
    Nesta seção, apresentamos um modelo preditivo para análise do preço do petróleo. O modelo utiliza técnicas de aprendizado de máquina para prever variações nos preços com base em dados históricos entre 1987 e 2024 do site Ipeadata. Treinamos o modelo com métricas ARIMA.
             
    Abaixo você poderá escolher a quantidade de dias para a previsão do preço. Limitamos em 10 dias para garantir uma melhor eficácia.
            
  
    """)

    # Carregar o modelo ARIMA salvo
    model = joblib.load("arima.joblib")

    st.subheader("Previsão com ARIMA")

    # Carregar os dados
    data_file_path = "precopetroleo.csv"
    data = pd.read_csv(data_file_path, header=None, delimiter=";")

    # Renomear as colunas para 'data' e 'valor'
    data.columns = ['data', 'valor']

    # Converter a coluna 'data' para datetime
    data['data'] = pd.to_datetime(data['data'])

    # Definir a coluna 'data' como o índice
    data.set_index('data', inplace=True)

    # Previsões
    forecast_steps = st.slider("Clique e arraste o mouse para prever o valor nos próximos dias", 1, 10, 10)
    forecast = model.forecast(steps=forecast_steps)

    # Definir a última data real como 21/11/2024
    ultima_data_real = pd.Timestamp("2024-11-21")
    datas_futuras = pd.date_range(start=ultima_data_real + timedelta(days=1), periods=forecast_steps, freq='B')

    # Criar o DataFrame de previsão
    arima_forecast_df = pd.DataFrame({'Data': datas_futuras, 'Previsao': forecast})

    # Ajustar a coluna de data para exibir apenas a data
    arima_forecast_df['Data'] = arima_forecast_df['Data'].dt.date

    # Renomear as colunas da tabela de previsões
    arima_forecast_df.rename(columns={'Data': 'Data (Futura)', 'Previsao': 'Previsão (Valor)'}, inplace=True)

    # Exibir a tabela com as colunas renomeadas
    st.write(f"Previsão para os próximos {forecast_steps} dias:", arima_forecast_df)

    st.write("Link do colab com o modelo completo https://drive.google.com/file/d/14QrBM1iNg5gBGcYCUcuw3rCLE0_cCQnu/view?usp=sharing ")

    st.header(':orange[[Atenção!]]')
    st.write("""
    O modelo pode apresentar algum erro para executar na web devido ao tamanho do arquivo arima.joblib.

    Sabendo disso, deixamos abaixo o método para executar localmente.

    1º Acesse link: https://github.com/gtnascimento/techchallange

    2º Clique em <> Code e faça o download do arquivo .ZIP do projeto.

    3º Extraia o arquivo e abra a pasta.

    4º Execute o arquivo apptech.py (o mesmo será executado em seu editor de código).

    5º No terminal do editor, digite "streamlit run apptech.py" (sem aspas).

    6º O programa irá abrir localmente em seu navegador e desta forma todos os arquivos irão carregar normalmente.
    """)


elif escolha == "Análise":
    st.header(':orange[📊 ANÁLISE]')
    st.subheader("Dashboard")
    st.write("""
    Nesta seção, demonstramos visualizações criadas no Power BI para comunicar os resultados de maneira eficaz.
    """)

    # Link público do Power BI
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiNmIxYmM4NDUtMjQ3Zi00Y2JmLWI3MTMtNjA0MDM2NzQ3Yzg4IiwidCI6ImUxZmU2YjcwLWNjY2EtNDQzMi05NDRkLThkM2I5YWE4M2RhNCJ9"

    # Incorporar o Power BI no Streamlit
    st.components.v1.iframe(power_bi_url, width=800, height=600)
    st.subheader(":orange[Abaixo iremos detalhar a criação do dashboard e os insights obtidos durante este processo.]")
    st.write(
        """
        **:orange[Filtros:]**

        **Data:** possibilidade de filtrar desde o menor até o maior período da base de dados do IPEA.

        **Evento:** Os eventos selecionados para o dashboard representam momentos históricos que geraram impactos significativos no mercado de petróleo tipo Brent devido à sua relação direta com oferta, demanda e instabilidade geopolítica. Cada evento foi escolhido com base em sua capacidade de influenciar as dinâmicas do mercado global e provocar oscilações relevantes nos preços.



        **:orange[Cards:]**

        **Card Preço Médio:** A média do preço bruto dos barris de petróleo tipo Brent.

        **Card Maior Preço:** O maior preço do barril de petróleo tipo Brent.

        **Card Menor Preço:** O menor preço do barril de petróleo tipo Brent.

        **Card Eventos Selecionados:** Card que demonstra a quantidade de eventos selecionados de acordo com o contexto de filtros.

        **:orange[Gráficos:]**

        **Gráfico de linha:** O gráfico de linha foi incluído porque é ideal para representar a evolução dos preços do petróleo ao longo do tempo. Ele oferece uma visão contínua e fluida.

        **Gráfico de Barra:** O gráfico de barras horizontal com o preço médio foi incluído para facilitar a comparação entre períodos por evento de forma clara e objetiva. Ele permite identificar rapidamente os eventos em que o preço médio do barril foi mais alto ou mais baixo, destacando tendências gerais no comportamento dos preços
        """
    )
    st.subheader(":orange[Insights]")
    st.write(
        """
        A base de dados contém apenas duas informações brutas: datas e os preços do barril de petróleo. Isoladamente, esses números oferecem pouco contexto para tomada de decisão ou análise crítica. No entanto, ao visualizar e investigar os picos, vales e tendências, podemos identificar momentos cruciais que desafiam a estabilidade do mercado global.

        A base de dados contém apenas duas informações brutas: datas e os preços do barril de petróleo. Isoladamente, esses números oferecem pouco contexto para tomada de decisão ou análise crítica. No entanto, ao visualizar e investigar os picos, vales e tendências, podemos identificar momentos cruciais que desafiam a estabilidade do mercado global.

        Abaixo trazemos alguns insights que tivemos no desenvolvimento do Tech Challenge #4
        """
    )    
    st.write(
       """
        **1. Impacto do colapso da demanda durante a pandemia da COVID-19**
        Em março de 2020, o preço do barril de petróleo sofreu uma queda drástica devido à redução significativa da demanda causada pelos lockdowns globais. Em abril de 2020, o petróleo WTI atingiu valores negativos pela primeira vez na história, evidenciando a gravidade do choque de demanda. Este evento ressalta que choques de demanda podem ser mais disruptivos do que choques de oferta. A queda é claramente visível no gráfico de barras abaixo, que apresenta o preço médio do período.
       """
    )

    st.image("grafico1.png", caption="Grafico de Barras", width=300)

    st.write(
       """
        **2. Acordos da OPEP+ estabilizam o mercado pós pandemia**
        Após o colapso inicial de 2020, os cortes de produção da OPEP+ em abril ajudaram a estabilizar os preços. Esses cortes foram os maiores da história e mantiveram os preços em níveis mais sustentáveis, marcando o papel do cartel na regulação do mercado. Este contexto mostra a capacidade da OPEP+ de influenciar as decisões geopolíticas para o equilíbrio do mercado.

        Podemos visualizar como após este período o preço do petróleo voltou a subir pela retomada gradual da economia global e pelo aumento da demanda por energia.
       """
    )

    st.image("grafico2.png", caption="Grafico de linhas", width=800)

    st.write(
       """
        **3. O efeito das tensões militares e ataques a petroleiros**
        Eventos como os ataques a petroleiros no Golfo de Omã em 2019 geraram picos momentâneos nos preços do petróleo. Esse tipo de instabilidade no Oriente Médio continua sendo um fator de volatilidade. Este evento enfatiza como tensões geopolíticas podem causar flutuações de curto prazo, mesmo sem mudanças significativas na demanda ou oferta global.

        Podemos visualizar como após este período o preço do petróleo voltou a subir pela retomada gradual da economia global e pelo aumento da demanda por energia.

        Podemos perceber a alta dos preços em Maio de 2019.
       """
    )

    st.image("grafico3.png", caption="Grafico de linhas", width=800)

    st.write(
       """
        Se comparamos este evento a Reimposição de Sanções Econômicas ao Irã, que aconteceu no ano seguinte (2020, var -17%) e Acordo de Corte de Produção da OPEP+ que aconteceu no ano anterior (2018, var 51,6%), percebemos o quão impactante foram os conflitos no Oriente Médio
       """
    )

    st.image("grafico4.png", caption="Grafico de fúnil", width=800)

    st.write(
       """
        **4. Avanços no fracking e a estabilização dos preços a partir de 2010**
        O desenvolvimento do petróleo de xisto nos EUA a partir de 2010 criou um novo equilíbrio no mercado. A oferta global aumentou significativamente, reduzindo o poder da OPEP+. Este contexto pode ser usado para explicar quedas prolongadas nos preços, mostrando como inovações tecnológicas podem remodelar o mercado.
        Podemos perceber este aumento significativo visualizando o gráfico abaixo. A queda veio em 2015 em consequência da produção de petróleo de xisto nos Estados Unidos.

       """
    )

    st.image("grafico5.png", caption="Grafico de linhas", width=800)

    st.write(
        """
        **:orange[Eventos considerados para o desenvolvimento do dashboard]**

        **1. Invasão do Kuwait pelo Iraque (1990)**

        • **Período:** Agosto de 1990 - fevereiro de 1991.  
        • **Impacto:** A crise levou a um pico abrupto nos preços devido ao temor de interrupções na produção e transporte na região do Golfo.

        **2. Invasão do Iraque pelos EUA (2003)**

        • **Período:** Março de 2003.  
        • **Impacto:** Gerou incerteza inicial, mas com o tempo estabilizou o fornecimento global de petróleo, reduzindo os preços.

        **3. Colapso do Lehman Brothers (2008)**

        • **Período:** Setembro de 2008.  
        • **Impacto:** Parte da crise financeira global, levou a uma queda significativa na demanda por petróleo e uma redução drástica nos preços. Este colapso explica como crises econômicas impactam diretamente no setor energético.

        **4. Crise da Dívida Europeia e Avanços no Petróleo de Xisto (2010–2013)**

        • **Período:** 2010–2013.  
        • **Impacto:** Enquanto a crise econômica na Europa pressionava os preços para baixo, a revolução do petróleo de xisto nos EUA (fracking) aumentou a oferta global, reduzindo ainda mais os preços no longo prazo.

        **5. Primavera Árabe (2010–2012)**

        • **Período:** 2010–2012.  
        • **Impacto:** Instabilidade política no Oriente Médio afetou os preços, com alta volatilidade devido às incertezas regionais.

        **6. Acordo de Paris (2015)**

        • **Período:** Assinado em dezembro de 2015, com implementação contínua.  
        • **Impacto:** Indiretamente influenciou o mercado de petróleo, promovendo transição energética e maior pressão para desinvestimentos em combustíveis fósseis.

        **7. Acordo de Corte de Produção da OPEP (2017 em diante)**

        • **Período:** Frequentemente revisado desde 2017, com cortes notáveis em abril de 2020 (em resposta à pandemia) e em outubro de 2022, quando a produção foi reduzida em 2 milhões de barris por dia, o maior corte desde 2020. A decisão de 2022 foi estendida até o final de 2023 para estabilizar o mercado frente às incertezas globais.  
        • **Impacto:** Geralmente causa alta nos preços devido à redução da oferta global. O corte em 2020 ajudou a conter a queda nos preços durante a crise da COVID-19.

        **8. Reimposição de Sanções Econômicas ao Irã (2018–2019)**

        • **Período:** 2018–2019.  
        • **Impacto:** Reduziu a oferta global de petróleo, elevando os preços. As sanções foram intensificadas pelos EUA sob a administração Trump.

        **9. Ataques a Petroleiros e Tensões Militares (2019)**

        • **Período:** Episódios frequentes; destaque para ataques no Golfo de Omã (2019) e tensões no Estreito de Ormuz.  
        • **Impacto:** Geralmente elevam os preços por aumentarem os riscos de fornecimento. O ataque de 2019 gerou picos momentâneos de preços devido ao medo de interrupções no transporte.

        **10. Lockdowns Globais devido à COVID-19 (2020–2021)**

        • **Período:** Março de 2020 - meados de 2021.  
        • **Impacto:** Queda histórica na demanda, resultando em preços negativos momentâneos em abril de 2020. Destaca a vulnerabilidade do mercado a choques de demanda.
        """
    )



elif escolha == "Conclusão":
    st.header(':orange[💡 CONCLUSÃO]')
    st.write(
        """
        Ao longo deste trabalho foi possível explorar as dinâmicas complexas do mercado global de petróleo e como eventos históricos, geopolíticos e econômicos moldam o comportamento dos preços. A análise demonstrou que, embora o mercado seja influenciado por fatores de longo prazo, como a transição energética impulsionada pelo Acordo de Paris, eventos pontuais, como tensões militares, crises financeiras e decisões estratégicas de corte de produção pela OPEP+, podem gerar oscilações significativas em períodos curtos.

        O uso de ferramentas analíticas e visuais foi essencial para transformar uma base de dados inicial simples, com preços diários do barril de petróleo, em um painel interativo capaz de gerar insights. Por meio do cruzamento de dados com eventos históricos, identificamos picos, quedas e tendências nos preços, ilustrando o impacto de decisões e acontecimentos globais.

        Este trabalho reforça a importância de integrar técnicas de análise de dados com o storytelling, conectando informações técnicas à realidade prática do mercado. Destaca-se como a análise de dados pode servir como base para decisões estratégicas e como a interpretação adequada de grandes volumes de informações pode mitigar riscos e identificar oportunidades em um setor tão volátil quanto o energético.

        Por fim, o projeto não apenas cumpriu seu objetivo de entender e apresentar as variações no preço do petróleo, mas também demonstrou como dados, contexto histórico e insights analíticos podem se unir para fornecer respostas a questões globais, servindo de modelo para futuras abordagens em problemas complexos do mercado.
        """
    )


elif escolha == "Referências":
    st.header(':orange[🔗 Referências bibliográficas]')
    st.markdown("""
    As Sanções americanas sufocam o Irã  
    Fonte: [https://www.dw.com/pt-br/assim-as-sanções-americanas-sufocam-o-irã/a-49353775](https://www.dw.com/pt-br/assim-as-sanções-americanas-sufocam-o-irã/a-49353775)
    """)

    st.markdown("""
    Oil Economic Landscape of Saudi Arabia  
    Fonte: [https://www.cmegroup.com/pt/education/featured-reports/oil-economic-landscape-of-saudi-arabia.html](https://www.cmegroup.com/pt/education/featured-reports/oil-economic-landscape-of-saudi-arabia.html)
    """)

    st.markdown("""
    Petroleo tem menor preço em 18 anos por queda na demanda devido covid 19  
    Fonte: [https://veja.abril.com.br/economia/petroleo-tem-menor-preco-em-18-anos-por-queda-na-demanda-devido-covid-19/](https://veja.abril.com.br/economia/petroleo-tem-menor-preco-em-18-anos-por-queda-na-demanda-devido-covid-19/)
    """)

    st.markdown("""
    Iraque ataca e anexa o kuwait  
    Fonte: [https://www.dw.com/pt-br/1990-iraque-ataca-e-anexa-o-kuwait/a-602073](https://www.dw.com/pt-br/1990-iraque-ataca-e-anexa-o-kuwait/a-602073)
    """)

    st.markdown("""
    O petróleo impulsionou a invasão do Iraque pelos EUA?  
    Fonte: [https://www.greelane.com/pt/humanidades/problemas/oil-drive-us-invasion-of-iraq-3968261/](https://www.greelane.com/pt/humanidades/problemas/oil-drive-us-invasion-of-iraq-3968261/)
    """)

    st.markdown("""
    Crise da Dívida na Zona do Euro e Políticas de Austeridade prejudicam Crescimento  
    Fonte: [https://brasil.un.org/pt-br/61516-crise-da-d%C3%ADvida-na-zona-do-euro-e-pol%C3%ADticas-de-austeridade-prejudicam-crescimento-avalia-onu](https://brasil.un.org/pt-br/61516-crise-da-d%C3%ADvida-na-zona-do-euro-e-pol%C3%ADticas-de-austeridade-prejudicam-crescimento-avalia-onu)
    """)

    st.markdown("""
    A Crise Financeira de 2008: Por que o Lehman Brothers quebrou?  
    Fonte: [https://www.independent.co.uk/news/business/analysis-and-features/financial-crisis-2008-why-lehman-brothers-what-happened-10-years-anniversary-a8531581.html](https://www.independent.co.uk/news/business/analysis-and-features/financial-crisis-2008-why-lehman-brothers-what-happened-10-years-anniversary-a8531581.html)
    """)

    st.markdown("""
    Explosão em Petroleiros Dispara Alerta no Estreito de Ormuz  
    Fonte: [https://poder360.com.br/internacional/explosao-em-petroleiros-dispara-alerta-no-estreito-de-ormuz/](https://poder360.com.br/internacional/explosao-em-petroleiros-dispara-alerta-no-estreito-de-ormuz/)
    """)

    st.markdown("""
    Acordo de Paris: Os 5 anos do pacto climático que mudou o mundo  
    Fonte: [https://exame.com/esg/acordo-de-paris-os-5-anos-do-pacto-climatico-que-mudou-o-mundo/](https://exame.com/esg/acordo-de-paris-os-5-anos-do-pacto-climatico-que-mudou-o-mundo/)
    """)

    st.markdown("""
    Impacto mundial do corte na produção de petróleo pela OPEP  
    Fonte: [https://borainvestir.b3.com.br/tipos-de-investimentos/renda-variavel/commodities/entenda-o-impacto-mundial-do-corte-na-producao-de-petroleo-pela-opep/](https://borainvestir.b3.com.br/tipos-de-investimentos/renda-variavel/commodities/entenda-o-impacto-mundial-do-corte-na-producao-de-petroleo-pela-opep/)
                
    Cotação do petróleo: entenda como funciona o preço dessa commodity            
    https://www.suno.com.br/artigos/cotacao-do-petroleo/            
    """)


# Rodapé
st.markdown("---")
st.markdown("Desenvolvido como parte do **FIAP Pós Tech – Data Analytics, 2024**.")
