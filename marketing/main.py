# Para executar esse código via terminal do PyCharm ou mesmo no bash: python -m streamlit run main.py

#
# Observação: para consultar modelos das LLM's, acessar o site: https://arena.ai/leaderboard
#

from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from utils import load_prompt

load_dotenv()

st.title("Gerador de Conteúdo com LLM")

# --- Campos de entrada ---

topic = st.text_input(
    "Tema",
    placeholder="Ex: saúde mental, alimentação saudável, prevenção, etc."
)

platform = st.selectbox(
    "Plataforma",
    ['Instagram', 'Facebook', 'LinkedIn', 'Blog', 'E-mail']
)

tone = st.selectbox(
    "Tom",
    ['Normal', 'Informativo', 'Inspirador', 'Urgente', 'Informal']
)

length = st.selectbox(
    "Tamanho",
    ['Curto', 'Médio', 'Longo']
)

audience = st.selectbox(
    "Público-alvo",
    ['Geral', 'Jovens adultos', 'Famílias', 'Idosos', 'Adolescentes']
)

cta = st.checkbox("Incluir CTA")

hashtags = st.checkbox("Retornar Hashtags")

keywords = st.text_area(
    "Palavras-chave (SEO)",
    placeholder="Ex: bem-estar, medicina preventiva...",
    height=80
)

generate_button = st.button("Gerar conteúdo")

id_model = "llama-3.3-70b-versatile"

if generate_button:

    if not topic:
        st.warning("Por favor, informe o tema do conteúdo.")
        st.stop()

    prompt_text = load_prompt("prompts/marketing_v3.txt")

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "Você é um redator profissional de marketing digital."),
        ("human", prompt_text)
    ])

    llm = ChatGroq(
        model=id_model,
        temperature=0.7, # Determina o nível de 'criatividade' da resposta gerada. Quanto mais próximo de 1, mais aleatória é a resposta.
        max_tokens=None,  # Limite de tokens a serem gerados. None indica que não há limite nos tokens gerados.
        timeout=None,  # Tempo máximo de espera pela resposta. None indica que não há tempo máximo.
        max_retries=2, # Máximo de retentativas em caso de falhas.
    )

    chain = prompt_template | llm

    with st.spinner("Gerando conteúdo..."):
        response = chain.invoke({
            "topic": topic,
            "platform": platform,
            "tone": tone,
            "length": length,
            "audience": audience,
            "keywords": keywords or "Não informado",
            "cta": "Sim" if cta else "Não",
            "hashtags": "Sim" if hashtags else "Não"
        })

    st.subheader("Conteúdo gerado")
    st.text_area("Resultado", response.content, height=300)



