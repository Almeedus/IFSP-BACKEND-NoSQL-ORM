# IFSP BACKEND Flask NoSQL ORM

Projeto realizado em Flask com o intuito de realizar um CRUD num banco de dados não relacional (NoSQL), no caso o MongoDB. O projeto realiza o processo de vida util de um produto numa papelaria(C- criação do produto no banco, R- leitura individual e geral dos registros, U- atualização do produto, D- deleção do produto no banco de dados).

Rotas:
- ### GET: /
    - Hello World

- ### GET: /buscar/id
    - Retorna um JSON do produto

- ### GET: /buscar
    - Retorna um JSON de todos os produtos na base de dados

- ### POST: /cadastrar
    - Retorna uma mensagem de sucesso ao cadastrar 
        - Formato de JSON para envio:
    ```
    {
        "name":"Lapiseira",
        "quantity": "210",
        "price":"0.90"
    }
    ```

- ### PUT: /atualizar/id
    - Retorna uma mensagem de sucesso ao atualizar 
        - Formato de JSON para envio:
    ```
    {
        "name":"Lapiseira",
        "quantity": "210",
        "price":"0.90"
    }
    ```


- ### DELETE: /deletar/id
    - Retorna uma mensagem de sucesso ao deletar