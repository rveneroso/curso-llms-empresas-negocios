# TODO – Melhorias Futuras (Projeto Marketing com LLM)

Este arquivo lista melhorias e evoluções possíveis para o projeto de
geração de conteúdo com LLM.  
Nenhum dos itens abaixo é obrigatório para o funcionamento atual da
aplicação.  
Eles representam oportunidades de aprendizado, refinamento técnico e
aproximação de um cenário real de uso em empresas.

---

## 1. Prompt Engineering

- [ ] Criar variações de prompt por plataforma (Instagram, LinkedIn, Blog, E-mail)
- [ ] Separar prompts por objetivo (educacional, venda, engajamento, informativo)
- [ ] Incluir exemplos (few-shot prompting) para melhorar consistência da saída
- [ ] Versionar prompts (`marketing_v1.txt`, `marketing_v2.txt`, etc.) com histórico de mudanças
- [ ] Testar prompts mais restritivos para reduzir respostas genéricas

---

## 2. Organização e Arquitetura

- [ ] Criar uma camada `config/` para centralizar:
  - nome do modelo
  - temperatura padrão
  - limites de tokens
- [ ] Criar uma interface comum para geração de conteúdo (ex: `BaseGenerator`)
- [ ] Preparar estrutura para múltiplos projetos além de marketing
- [ ] Adicionar docstrings mais completas nos services

---

## 3. Streamlit (UX / UI)

- [ ] Exibir mensagens de erro mais amigáveis ao usuário
- [ ] Adicionar validação mais completa dos campos de entrada
- [ ] Melhorar layout (colunas, seções, separadores)
- [ ] Adicionar botão para copiar texto gerado
- [ ] Permitir download do conteúdo (TXT / Markdown)

---

## 4. Performance e Custos

- [ ] Implementar cache de respostas (`st.cache_data`) para prompts repetidos
- [ ] Adicionar controle de temperatura via interface
- [ ] Logar tempo de resposta da LLM
- [ ] Monitorar quantidade de tokens gerados (quando disponível)

---

## 5. Observabilidade e Debug

- [ ] Criar logs estruturados para chamadas à LLM
- [ ] Salvar prompts e respostas para análise posterior (modo debug)
- [ ] Criar modo “verbose” para desenvolvimento

---

## 6. Qualidade de Código

- [ ] Padronizar nomes de funções e variáveis
- [ ] Rodar formatter (black / ruff)
- [ ] Adicionar type hints básicos
- [ ] Criar testes simples para:
  - carregamento de prompt
  - montagem do template
  - validação de inputs

---

## 7. Evoluções Funcionais

- [ ] Permitir geração de múltiplas versões do mesmo conteúdo
- [ ] Adicionar campo “objetivo do post” (educar, vender, engajar)
- [ ] Implementar histórico de conteúdos gerados na sessão
- [ ] Comparar respostas entre dois modelos diferentes

---

## Observação Final

Este projeto já cumpre totalmente seu objetivo educacional.
As melhorias listadas aqui devem ser implementadas **apenas se fizerem
sentido dentro do contexto de aprendizado ou reutilização futura**.

Não há necessidade de implementar tudo.
Escolha itens conforme novos projetos ou necessidades reais surgirem.
