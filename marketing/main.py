# Para executar esse código via terminal do PyCharm ou mesmo no bash: python -m streamlit run main.py

#
# Observação: para consultar modelos das LLM's, acessar o site: https://arena.ai/leaderboard
#

from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
from services.marketing_generator import generate_marketing_content

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

    try:
        with st.spinner("Gerando conteúdo..."):
            content = generate_marketing_content(
                topic=topic,
                platform=platform,
                tone=tone,
                length=length,
                audience=audience,
                keywords=keywords,
                cta=cta,
                hashtags=hashtags,
            )

        st.subheader("Conteúdo gerado")
        st.text_area("Resultado", content, height=300)

    except Exception as e:
        st.error(f"Ocorreu um erro ao gerar o conteúdo: {e}")




