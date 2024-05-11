#Instalando Biblioteca
pip install -q -U google-generativeai

#Importando bibliotecas
import google.generativeai as genai
import re
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm, IntPrompt
from rich.console import Console

#Confirgurando API
genai.configure(api_key='SUA API AQUI')

#Funções
def gerar_casos_de_teste(requisito):
  """
  Gera casos de teste a partir de um requisito de software.
  """
  print(Panel(f"[bold blue]Gerando casos de teste para o requisito:[/]\n{requisito}", title=":test_tube: GeminiQA", expand=False))
  prompt = f"""
  Você é um especialista em testes de software.
  Gere casos de teste completos para o seguinte requisito:
  "{requisito}"

  Inclua:
  * [bold]ID do Caso de Teste[/]
  * [bold]Descrição do Teste[/]
  * [bold]Precondições[/]
  * [bold]Etapas do Teste[/]
  * [bold]Resultado Esperado[/]

  Formate cada caso de teste como uma lista com os titulos em negrito
  [bold]ID do Caso de Teste:[/] [blue]ID-001[/]
  [bold]Descrição do Teste:[/] Verificar se o sistema permite login com credenciais válidas.
  [bold]Precondições:[/] O usuário possui uma conta válida.
  [bold]Etapas do Teste:[/]
    1. Acessar a página de login.
    2. Inserir as credenciais válidas do usuário.
    3. Clicar no botão "Entrar".
  [bold]Resultado Esperado:[/] O sistema deve redirecionar o usuário para a página principal.
  

  """
  safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
  }
  completion = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    safety_settings=safety_settings
  )
  response = completion.generate_content(prompt) 

  # Formata a resposta com Panel
  print(Panel(response.text, title=":clipboard: Casos de Teste Gerados", expand=False)) 

def buscar_informacao(pergunta):
  """
  Busca informações diretamente do Gemini.
  """
  print(Panel(f"[bold blue]Buscando informações sobre:[/]\n{pergunta}", title=":mag: QApp", expand=False))

  # Prompt para o Gemini 
  prompt = f"""
  Contexto: Estou buscando informações sobre testes de software.
  Pergunta: {pergunta}

  
  Formate as respostas com titulo em negrito e cada informação com um marcador
  Em caso de muitas informações diferentes, manter formatação para cada uma

  [bold]Informaçõeslo:[/] Para garantinr a qualidade do software
  
   """

  safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
  }
  completion = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    safety_settings=safety_settings
  )
  response = completion.generate_content(prompt)

  print(Panel(response.text, title=":bulb: Informação Encontrada", expand=False))

#Menu Principal
while True:
  print(Panel("[bold blue]Menu QApp[/]", title=":robot: ", expand=False))
  print("[1] Gerar Casos de Teste")
  print("[2] Buscar Informação")
  print("[0] Sair")

  opcao = IntPrompt.ask("[bold blue]Escolha uma opção[/]", choices=["0", "1", "2"])

  if opcao == 1:
    requisito = Prompt.ask("[bold blue]Sobre qual funcionalidade?[/]")
    gerar_casos_de_teste(requisito)
  elif opcao == 2:
    pergunta = Prompt.ask("[bold blue]Qual é a sua pergunta?[/]")
    buscar_informacao(pergunta)
  elif opcao == 0:
    break
  else:
    print("[bold red]Opção inválida![/]")

  print("\n") # Adiciona uma linha em branco para melhor organização

print(Panel("[bold blue]Obrigado por usar o QApp![/]", title=":wave: Até logo", expand=False))
