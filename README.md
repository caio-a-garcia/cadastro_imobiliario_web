# Cadastro Imobiliário Web

Sistema de cadastro imobiliário implementado com interface web em Flask e persistência com SQLAlchemy testado no Postgresql.

## Setup do Projeto

### Ambiente

No Windows: com a linha de comando cmd aberta na pasta do projeto
1) `python -m venv <ambiente_virtual>`
2) `<ambiente_virtual>\Scripts\activate`
3) `pip install -r requirements.txt`
4) `set SQLALCHEMY_DATABASE_URI=<banco_de_dados>`
5) `set SECRET_KEY=<alguma_senha_secreta>`

O comando 1 usa o módulo venv do Python para criar um ambiente virtual no diretório <ambiente_virtual>. O diretório de nome <ambiente_virtual> será criado no diretório onde o comando for rodado, se não existir. Para criar o ambiente virtual no diretório local use `python -m venv .`.

O comando 2 executa um arquivo bat que ativa o ambiente virtual. No cmd, quando o comando 2 funciona a linha de comando aparace como:
```(<ambiente_virtual>) C:\caminho\para\projeto>```

O comando 3 usa o gerenciador de pacotes `pip` para instalar as dependências do projeto listadas em `requirements.txt`.

O comando 4 configura a variável de ambiente por meio da qual o
projeto vai acessar o banco de dados. No caso do Postgres essa
variável tem o formato:
`postgresql://{usuario}:{senha}@{caminho}:{porta}/{banco_de_dados}`
Exemplo: `postgresql://postgres:root@localhost:5432/cadastros`

Observações: "postgres" e "5432" são o usuário e porta padrões do Postgres. "localhost" é muito usado em ambiente de desenvolvimento mas no geral não deve ser usado em produção. "banco_de_dados" deve ser o nome do banco que será criado no paço 6 abaixo.

O comando 5 configura uma segunda variável de ambiente que é usada pelo Flask como parte de um sistema de segurança no processo de envio de formulários. Quando usado em produção, o valor dessa variável deve ser secreto e preferencialmente difícil de ser adivinhado.


### Banco de Dados

Para inicializar o banco de dados Postgresql com o PgAdmin aberto:
6) Crie um novo banco de dados:
  - Clique com o botão direito em `Databases (x)`
  - No menu de contexto clique em `Create > Database...`
  - Dê um nome ao banco (ver passo 4) e clique em `Save`
7) Crie as tabelas
  - Com o banco selecionado navegue para o `Query tool`
  - Selecione `Open file`
  - Encontre e selecione o arquivo no caminho `cadastro_imobiliario_web/diagramas_bd/diagrama_fisico.sql'
  - Clique em `Execute/Refresh` (botao de play) para executar o script sql e criar as tabelas

Com o setup pronto, para rodar o projeto basta voltar ao cmd e chamar:
8) `flask run`

Com o projeto rodando, pagina inicial pode ser encontrada no seu browser no endereço 127.0.0.1:5000/ e a API pode ser testada com o Postman (ou outra ferramenta similar)


## Teste da API com Postman:
**Atenção**: as instruções abaixo vão apagar as informações do banco testado! Não faça isso no banco de produção.

Para criar uma tabela para o teste, repita os passos 6 e 7, e o passo 4 com o nome do correto para os testes. Por exemplo:
`postgresql://postgres:root@localhost:5432/teste`

**Esse é o passo que apaga as entradas do banco**
No banco de teste, rode o arquivo `cadastro_imobiliario_web/diagramas_bd/banco_teste.sql` com o Query tool.

Rode o projeto (comando 8) se não estiver já em execução.

No Postman acesse um Workspace, clique em 'import', selecione o arquivo `cadastro_imobiliario_web/tests/CadastroImoveis.postman_collection.json', e clique em `Import`.
Uma vez que esse arquivo for importado, ele estará disponível no Postman para teste futuros. Para atualizar o arquivo, abra o menu de contexto (os três pontos que aparecem ao colocar o mouse sobre CadastroImoveis) e selecione export.

Com o projeto rodando, selecione `Run collection` no menu de contexto de CadastroImoveis, e clique em `Run CadastroImoveis`.
