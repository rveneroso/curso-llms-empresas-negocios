# Uso do LangChain vs chamada direta à LLM

## Visão geral

Existem duas formas principais de interagir com uma Large Language Model (LLM) neste projeto:

1. Realizar chamadas diretas à LLM, construindo manualmente as mensagens.
2. Utilizar a biblioteca LangChain para estruturar prompts e criar cadeias de execução (*chains*).

Ambas as abordagens produzem resultados equivalentes do ponto de vista da LLM. A principal diferença está **na organização do código, reutilização de prompts e escalabilidade do projeto**.

---

## Chamada direta à LLM (sem LangChain)

Na abordagem direta, o desenvolvedor constrói explicitamente a estrutura das mensagens e as envia à LLM em uma única chamada.

Exemplo conceitual:

```python
template = [
    ("system", "Você é um redator profissional."),
    ("human", "Olá! Quem é você?")
]

res = llm.invoke(template)
```
## Características da chamada direta à LLM

A chamada direta à LLM se caracteriza por uma comunicação sem camadas adicionais de abstração. O desenvolvedor constrói manualmente a estrutura das mensagens e as envia diretamente ao modelo, mantendo controle explícito sobre o que é transmitido.

Essa abordagem resulta em código simples, fácil de compreender e adequado para projetos iniciais, testes rápidos ou provas de conceito. Ela favorece o aprendizado, pois torna visível a relação direta entre o prompt enviado e a resposta gerada pela LLM.

---

## Vantagens da chamada direta

- Menor complexidade estrutural do código.
- Curva de aprendizado reduzida.
- Maior transparência sobre o conteúdo enviado à LLM.
- Facilidade para experimentação e prototipagem rápida.
- Boa opção para scripts pequenos ou fluxos simples.

---

## Limitações da chamada direta

- Prompts tendem a ficar espalhados pelo código.
- Dificuldade de reutilizar prompts em diferentes contextos.
- Pouca padronização conforme o projeto cresce.
- Manutenção mais difícil em aplicações com múltiplos fluxos.
- Escala mal em cenários corporativos ou projetos maiores.

---

## Características do uso do LangChain

O LangChain introduz uma separação clara entre a estrutura do prompt, os dados dinâmicos e a execução da chamada à LLM. Essa abordagem incentiva a organização do código e o tratamento dos prompts como componentes reutilizáveis.

Ao utilizar templates, o código se torna mais declarativo, facilitando a leitura, manutenção e evolução da aplicação. O LangChain também prepara o projeto para fluxos mais complexos, como cadeias de múltiplas etapas.

---

## Vantagens do uso do LangChain

- Melhor organização do código conforme o projeto cresce.
- Reutilização e versionamento natural de prompts.
- Facilidade para ajustes, testes e refatorações.
- Base sólida para recursos avançados, como:
  - Retrieval-Augmented Generation (RAG)
  - múltiplas etapas de geração
  - uso de ferramentas externas
  - memória de contexto
- Alinhamento com padrões comuns em ambientes corporativos.

---

## Limitações do uso do LangChain

- Introduz mais abstração em comparação à chamada direta.
- Código ligeiramente mais verboso.
- Curva de aprendizado maior para iniciantes.
- Pode ser excessivo em projetos muito simples ou experimentais.

---

## Comparação resumida

| Aspecto | Chamada direta | LangChain |
|--------|----------------|-----------|
| Simplicidade inicial | Alta | Média |
| Transparência | Alta | Média |
| Organização do código | Manual | Estruturada |
| Reutilização de prompts | Baixa | Alta |
| Escalabilidade | Limitada | Elevada |
| Adequação a projetos grandes | Baixa | Alta |

---

## Decisão arquitetural

Neste projeto, o LangChain foi adotado como uma decisão arquitetural consciente. Embora não seja estritamente necessário no estágio inicial, ele oferece melhor organização, facilita a evolução do código e permite que os prompts sejam tratados como artefatos versionáveis.

O LangChain não altera a inteligência ou o comportamento intrínseco da LLM. Ele atua como uma camada de organização e orquestração, cujos benefícios se tornam mais evidentes à medida que o projeto cresce em complexidade.
