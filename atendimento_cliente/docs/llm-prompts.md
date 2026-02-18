# Uso da role `system` em chamadas a LLMs

## Visão geral

Em aplicações que utilizam Large Language Models (LLMs), como aquelas integradas via LangChain, as mensagens enviadas ao modelo podem assumir diferentes *roles*. A mais importante delas é a role `system`, responsável por definir o comportamento global da LLM durante a geração das respostas.

A mensagem com role `system` estabelece o contexto inicial da interação, indicando ao modelo **quem ele deve ser**, **como deve se comportar** e **quais princípios deve seguir** ao responder às solicitações do usuário. Ela funciona como uma instrução de alto nível que influencia todas as mensagens subsequentes dentro de uma mesma chamada.

---

## Função da role `system`

A role `system` não deve ser tratada como um prompt comum. Diferentemente de uma mensagem enviada pelo usuário, ela atua como um **contexto persistente**, moldando a forma como a LLM interpreta e responde às mensagens da role `human`.

Ao definir, por exemplo, que a LLM é “um redator profissional de marketing digital”, o modelo passa a gerar respostas alinhadas a esse papel, adotando vocabulário, estilo e estrutura compatíveis, sem que essa instrução precise ser repetida a cada interação.

---

## Uso da role `system` no projeto de Marketing

Neste projeto, o objetivo da aplicação é gerar textos prontos para publicação em diferentes plataformas (Instagram, Facebook, LinkedIn, Blog, E-mail, etc.). Portanto, a role `system` é utilizada para orientar a LLM a se comportar como um profissional experiente em redação de conteúdo para marketing digital.

Isso inclui habilidades como:
- criação de textos persuasivos e claros;
- adaptação do estilo de escrita à plataforma escolhida;
- adequação do tom (informativo, inspirador, informal, urgente);
- consideração do público-alvo definido pelo usuário;
- foco em engajamento e comunicação eficaz.

Dessa forma, a LLM deixa de atuar como um gerador genérico de texto e passa a operar dentro de um contexto profissional específico.

---

## Separação de responsabilidades entre roles

Uma boa prática adotada neste projeto é separar claramente as responsabilidades entre as roles:

- **Role `system`**  
  Deve conter regras estáveis e de alto nível, como identidade profissional da LLM, princípios gerais de escrita e objetivos do conteúdo.

- **Role `human`**  
  Deve conter informações variáveis fornecidas pelo usuário, como tema, plataforma, tamanho do texto, tom desejado, presença de CTA e palavras-chave.

Essa separação torna o código mais organizado, melhora a legibilidade dos prompts e facilita ajustes e manutenções futuras.

---

## Prioridade e conflitos de instruções

Em situações onde há conflito entre instruções, a mensagem com role `system` tende a ter prioridade sobre as demais. Por esse motivo, diretrizes amplas e estruturais — como evitar textos genéricos ou manter linguagem clara e profissional — devem ser definidas no `system`.

Já ajustes pontuais e contextuais devem ser tratados nas mensagens da role `human`.

---

## Boas práticas de manutenção

Em aplicações reais, o `system prompt` costuma ser:
- fixo;
- versionado junto ao código;
- documentado para facilitar entendimento por outros desenvolvedores.

Essa abordagem garante consistência no comportamento da LLM ao longo do tempo e facilita a evolução do projeto, testes de qualidade e revisões técnicas.
