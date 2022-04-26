# Cadastro Imobili�rio Web

Sistema de cadastro imobili�rio implementado com interface web em Flask e persist�ncia com SQLAlchemy testado no Postgresql.

## Setup do Projeto

No Windows: com a linha de comando cmd aberta na pasta do projeto
1) `python -m venv <ambiente_virtual>`
2) `<ambiente_virtual>\Scripts\activate`
3) `pip install -r requirements.txt`

O comando 1 usa o m�dulo venv do Python para criar um ambiente virtual no diret�rio <ambiente_virtual>. O diret�rio de nome <ambiente_virtual> sera criado no diret�rio onde o comando for rodado, se n�o existir. Para criar o ambiente virtual no diret�rio local use `python -m venv .`.

O comando 2 executa um arquivo bat que ativa o ambiente virtual. No cmd, quando o comando 2 funciona a linha de comando aparace como:
```(<ambiente_virtual>) C:\caminho\para\projeto>```

O comando 3 usa o gerenciador de pacotes `pip` para instalar as depend�ncias do projeto listadas em `requirements.txt`.


Para inicializar o banco de dados Postgresql com o PgAdmin aberto:
4) Crie um novo banco de dados:
  - Clique com o bot�o direito em `Databases (x)`
  - No menu de contexto clique em `Create > Database...`
  - D� um nome ao banco e clique em `Save`
5) Crie as tabelas
  - Com o banco selecionado navegue para o `Query tool`
  - Selecione `Open file`
  - Encontre e selecione o arquivo no caminho `cadastro_imobiliario_web/diagramas_bd/diagrama_fisico.sql'
  - Clique em `Execute/Refresh` (botao de play) para executar o script sql e criar as tabelas