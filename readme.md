### Desenvolvido por:
Squad Vale
</br>

<i>Projeto incentivado pela Associação Fundo Social Vale do Jequitinhonha - FSVJ
</br>2022</i>

### Configurações para Windows
#### Instale esses pacotes caso já não os tenha instalados
Download python 3, então:
```shell
pip install virtualenv
```
#### Crie o ambiente virtual
```shell
virtualenv venv
```
#### Ative o ambiente
```shell
venv\Scripts\activate
```
#### Instale as dependências do projeto
```shell
pip install -r requirements.txt
```
#### Rode o projeto
```shell
py app.py
```
</br>

### Configurações para Linux

#### Instale esses pacotes caso já não os tenha 
Verifique se o python3 está instalado
```shell
python3 --version
```
Se não, então instale-o
```shell
sudo apt-get update
sudo apt-get install python3
```
#### Crie o ambiente virtual
```shell
virtualenv venv
```
#### Ative-o
```shell
source venv/bin/activate
```
#### Instale as dependências do projeto
```shell
pip install -r requirements.txt
```
#### Rode o projeto
```shell
python3 app.py
```
</br>

## Visão Geral

O aplicativo FEIRA-KIT é um projeto social incentivado pelo Fundo Social Vale do Jequitinhonha, que tem por finalidade criar uma plataforma semelhante à uma feira livre virtual, onde os pequenos produtores rurais da região poderão cadastrar-se e publicar os ítens que produz e deseja vender, fazendo uma conexão direta com o cliente, para assim realizar as suas vendas.

## Principais tecnologias

- Python
- Flask
- MongoDB

## ESTRUTURA DE DIRETÓRIOS BACK-END

### Dentro da pasta './src' temos a seguinte estrutura:

- constants
  - "httpcodes.py" utilizado para mapear códigos de status HTTP 
  - "products.py" contém as categorias de produtos cadastrados, assim como as unidades de medidas
- controllers
  - "users.py" define rotas para recursos relacionados a usuários
  - "products.py" define rotas para recursos relacionados aos produtos
- core
  - "authenticate.py" autentica os usuários
  - "var_env.py" carrega variáveis de ambiente a partir do arquivo ".env"
- models
  - "id.py" define um modelo de dados para uso no app
  - "product.py" define modelos de dados para representar informações sobre os produtos 
  - "user.py" define modelos de dados para representar informações sobre os usuários 
- program
  - "database.py" cria uma conexão com um banco de dados MongoDB 
  - "server.py" define um servidor Flask para criar a API
- service
  - "id_settings.py" fornece métodos para manipular IDs em documentos BSON, convertendo-os em formato JSON e adicionando-os aos documentos, tanto individualmente quanto em listas
  - "product.py" fornece métodos para realizar operações CRUD em objetos de produto e no banco de dados 
  - "user.py fornece métodos para realizar operações relacionadas a usuários em um sistema. Isso inclui criar, ler, atualizar e excluir informações de usuários, verificar senhas, alterar senhas e buscar usuários por diferentes critérios, como nome e email

### Na raiz do projeto temos os seguintes arquivos:
- .env
  - Contém credenciais de acesso ao banco de dados
- app.py
  - Importa os componentes do projeto e inicializa o servidor
- requirements.txt
  - Lista todas as dependências do projeto
- runtime.txt
  - Especifica a versão do Python que deve ser usada para executar o Projeto

### IMPORTANTE: O arquivo ".env" na raiz do Projeto é o responsável por armazenar credenciais de acesso ao Banco de Dados. **Nunca deve ser compartilhado ou enviado para o Github**

