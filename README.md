
# Explicador de Conceitos em Python com LangChain + LCEL + OpenAI

Este projeto é uma aplicação simples em Python que utiliza **LangChain** com **LangChain Expression Language (LCEL)** e **OpenAI GPT** para explicar conceitos relacionados à programação e engenharia de software de forma didática e clara.

O usuário informa um termo ou conceito, e o programa retorna uma explicação detalhada, simulando a linguagem de um professor experiente e apaixonado por ensinar.

## Tecnologias utilizadas

- Python 3.x
- LangChain
- LangChain Core
- LangChain OpenAI
- OpenAI API (GPT)
- dotenv

## Objetivos do projeto

1. Praticar a construção de pipelines utilizando LCEL (LangChain Expression Language).
2. Explorar boas práticas na criação de prompts para modelos de linguagem.
3. Criar uma aplicação simples e funcional com foco em aprendizado de conceitos técnicos.
4. Prover uma estrutura básica e clara para uso de LLMs em Python.

## Estrutura do Código

- **dotenv:** para armazenar e carregar a chave da API da OpenAI.
- **ChatOpenAI:** modelo de linguagem utilizado.
- **ChatPromptTemplate:** define o comportamento do assistente e o formato da resposta.
- **StrOutputParser:** transforma a resposta da LLM em uma string simples.
- **cadeia_lcel:** representa o pipeline construído com LCEL (prompt → LLM → output).
- **main():** interface de linha de comando que interage com o usuário.

## Como executar o projeto

1. Clone o repositório.
2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # ou venv\Scripts\activate no Windows
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. Crie um arquivo `.env` na raiz do projeto com sua chave da OpenAI:
    ```
    OPENAI_API_KEY=sua-chave-aqui
    ```
5. Execute o script principal:
    ```bash
    python main.py
    ```

## Exemplo de uso

O usuário será solicitado a inserir um conceito, como por exemplo:

```
Digite um assunto que gostaria de aprender ou digite "sair" para encerrar o programa: POO
```

A resposta retornará uma explicação detalhada e três pontos interessantes relacionados ao tema.

## Possíveis melhorias futuras

- Implementar um glossário interno para respostas mais confiáveis.
- Integrar RAG (retrieval-augmented generation) com bases de dados locais.
- Criar uma interface gráfica utilizando Streamlit.
- Armazenar o histórico das perguntas e respostas.
- Adicionar testes unitários.

## Licença

Este projeto é livre para estudo e uso pessoal.
