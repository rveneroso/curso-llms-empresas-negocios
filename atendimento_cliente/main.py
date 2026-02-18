from langchain_groq import ChatGroq
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from langchain_community.document_loaders import PyMuPDFLoader
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnablePassthrough

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Diretório onde estão os arquivos que serão lidos e cujo conteúdo formará o contexto a ser utilizado pela LLM.
docs_path = os.getenv("CONTENT_PATH")
id_model = os.getenv("GROQ_MODEL")
temperature = 0.7

template_rag = """
Pergunta: {input}
Contexto: {context}
"""


def load_llm(id_model, temperature):
    llm = ChatGroq(
        model=id_model,
        temperature=temperature,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=os.getenv("GROQ_API_KEY")
    )
    return llm


# Carrega o conteúdo do arquivo cujo nome é passado à função.
def extract_text_pdf(file_path):
    loader = PyMuPDFLoader(file_path)
    doc = loader.load()
    content = "\n".join([page.page_content for page in doc])
    return content


def show_res(res):
    if "</think>" in res:
        res = res.split("</think>")[-1].strip()
    else:
        res = res.strip()
    print(res)


# Carrega a LLM de acordo com o modelo e temperatura definidos
llm = load_llm(id_model, temperature)

# Lẽ os arquivos PDF existentes no diretório configurado como variável de ambiente
docs_path = Path(docs_path)
pdf_files = [f for f in docs_path.glob("*.pdf")]

# Cria a variável com os conteúdos de todos os arquivos presentes no diretório configurado.
loaded_documents = [extract_text_pdf(pdf) for pdf in pdf_files]

# Quebra o conteúdo carregado dos arquivos em partes de 500 tokens. Define também que 50 tokens de uma determinada
# parte serão utilizados na parte seguinte
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = []
for doc in loaded_documents:
    chunks.extend(text_splitter.split_text(doc))

# Define o nome do modelo de embedding a ser utilizado. O segundo modelo é mais preciso, mas mais complexo
embedding_model = "sentence-transformers/all-mpnet-base-v2"
# embedding_model = "BAAI/bge-m3"

# Cria a variável embeddings com base no modelo previamente definido
embeddings = HuggingFaceEmbeddings(model_name = embedding_model)

# Armazena o resultado da aplicação dos embeddings sobre o conteúdo de chunks. Ou seja: faz o embedding do texto
# proveniente do arquivo PDF que foi criado anteriormente.
vectorstore = FAISS.from_texts(chunks, embedding=embeddings)

# Salva o resultado da operação anterior em arquivos locais do projeto
vectorstore.save_local("index_faiss")

# Cria o recuperador de resposta. A busca será feita por semelhança (similarity) e serão recuperados 5 documentos.
retriever = vectorstore.as_retriever(search_type = "similarity", search_kwargs={"k": 6})

prompt_rag = PromptTemplate(
    input_variables=["context", "input"],
    template=template_rag,
)

system_prompt = """Você é um assistente virtual prestativo e está respondendo perguntas gerais sobre os serviços de uma empresa.
Use os seguintes pedaços de contexto recuperado para responder à pergunta.
Se você não sabe a resposta, apenas comente que não sabe dizer com certeza.
Mas caso seja uma dúvida muito comum, pode sugerir como alternativa uma solução possível.
Mantenha a resposta concisa.
Responda em português. \n\n"""
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "Pergunta: {input}\n\n Contexto: {context}"),
    ]
)

chain_rag = (
    {"context": retriever, "input": RunnablePassthrough()}
    | qa_prompt
    | llm
    | StrOutputParser()
)

# Observação: se a LLM for chamada passando um pergunta completamente fora do contexto gerado pelos documentos
# previamente carregados, ainda assim haverá uma resposta baseada no conhecimento adquirido pela LLM. No
# resultado é informado que não foi encontrada uma resposta razoável nos textos fornecidos.
# Esse comportamento foi mantido usando os 2 prompts: prompt_rag e qa_prompt
res = chain_rag.invoke("Como devo proceder para encerrar minha conta?")
show_res(res)

retriever = vectorstore.as_retriever(
    search_type='mmr',
    search_kwargs={'k':3, 'fetch_k':4}
)

# input_test = "Gostaria de saber qual é o critério que esse algoritmo usa para definir o tamanho de embeddings"
#
# result = embeddings.embed_query(input_test)
# print(len(chunks))




# loader = PyMuPDFLoader(file_path)
# doc = loader.load()
# pprint.pp(doc[0].metadata)



#
# llm = load_llm(id_model, temperature)
#
# prompt_rag = PromptTemplate.from_template(template_rag)
# print(prompt_rag)
#
#
# prompt = "Como alterar minha senha?"
#
# template = ChatPromptTemplate.from_messages([
#     ("system", "Você é um assistente virtual prestativo e está respondendo perguntas gerais"),
#     ("human", "{prompt}")
# ])
#
# # chain = template | llm | StrOutputParser()
#
# chain_rag = prompt_rag | llm | StrOutputParser()
#
# input = "como alterar minhar senha?"
#
# res = chain_rag.invoke({"context": context, "input": input})
#
# show_res(res)

# res = chain.invoke({"prompt": prompt})
# show_res(res)
