import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from openai import OpenAI
from langchain_openai import ChatOpenAI

#carregar a key da api do módulo .env
load_dotenv()
api_key_openai = os.getenv('OPENAI_API_KEY')

#selecionar modelo de llm
llm = ChatOpenAI(
    openai_api_key=api_key_openai,
    temperature=0.1
)

#criar a entrada que define o que ele vai ser
persona_professor = ChatPromptTemplate.from_messages(
  [
    (
      "system",
        """
        Você é um assistente de aprendizado de programação em Python, focado em precisão. 
        Explique com precisão o conceito abaixo, que está diretamente relacionado à programação ou engenharia de software, em
        pelo menos 100 palavras ou mais. 
        Se o termo não for reconhecido nesse contexto, diga que não tem certeza ou peça mais informações.
        
        # FORMATO DE SAÍDA
        (Coloque a explicação didática e correta sobre o conceito aqui)
        
        
        Pontos Interessantes:
        
        (Coloque aqui 3 pontos interessantes sobre o assunto)
        
        Conceito: {assunto}
        """
    )
  ]
)
#criar o parser (um tipo de "tradutor") que vai transformar a saída da llm em tipo string
parser = StrOutputParser()

#criar o lcel (langchain expression language) (prompt -> llm -> output)
cadeia_lcel = persona_professor | llm | parser

#definir interface
def main():
    while True:
        assunto = input('Digite um assunto que gostaria de aprender ou digite "sair" para encerrar o programa: ')
        if assunto.lower() == 'sair':
            print('\nEncerrando programa. Até logo!')
            break

        resposta = cadeia_lcel.invoke({'assunto': assunto})
        print('\nExplicação: \n')
        print(resposta)
        print('-' * 40)

if __name__ == '__main__':
    main()