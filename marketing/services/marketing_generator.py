from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from utils.prompt_loader import load_prompt


def generate_marketing_content(
    *,
    topic: str,
    platform: str,
    tone: str,
    length: str,
    audience: str,
    keywords: str,
    cta: bool,
    hashtags: bool,
    model_id: str = "llama-3.3-70b-versatile",
    temperature: float = 0.7,
) -> str:
    """
    Gera conteúdo de marketing utilizando LLM via LangChain.
    Retorna apenas o texto final gerado pela LLM.
    """

    prompt_text = load_prompt("prompts/marketing_v3.txt")

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "Você é um redator profissional de marketing digital."),
        ("human", prompt_text),
    ])

    llm = ChatGroq(
        model=model_id,
        temperature=temperature,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    chain = prompt_template | llm

    response = chain.invoke({
        "topic": topic,
        "platform": platform,
        "tone": tone,
        "length": length,
        "audience": audience,
        "keywords": keywords or "Não informado",
        "cta": "Sim" if cta else "Não",
        "hashtags": "Sim" if hashtags else "Não",
    })

    return response.content
