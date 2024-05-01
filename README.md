**Projeto Gasto Comum**

O projeto "Gasto Comum" é uma aplicação web desenvolvida para facilitar o controle e a divisão de gastos entre várias pessoas. A ideia principal é permitir que os usuários registrem seus gastos e os dividam entre os participantes, tornando a administração financeira mais fácil e transparente.

### Funcionalidades Principais

1. **Cadastro de Gastos**: Os usuários podem cadastrar novos gastos, especificando o tipo de despesa, o valor, uma descrição opcional e outros detalhes relevantes.

2. **Cadastro de Usuários**: É possível cadastrar novos usuários, fornecendo informações como nome, endereço de e-mail e senha.

3. **Divisão de Gastos**: Os gastos registrados podem ser divididos entre os usuários cadastrados, permitindo que cada pessoa contribua com uma parte do valor total.

4. **Autenticação de Usuários**: O acesso à aplicação é protegido por um sistema de autenticação, onde os usuários precisam fazer login com seu e-mail e senha para acessar suas contas.

### Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do backend da aplicação.
- **Django**: Framework web em Python que fornece uma estrutura robusta para construir aplicativos web.
- **PostgreSQL**: Banco de dados relacional utilizado para armazenar os dados da aplicação.
- **HTML, CSS e JavaScript**: Tecnologias de front-end utilizadas para criar a interface do usuário e fornecer interatividade na aplicação.

### Como Executar o Projeto

1. **Instalação das Dependências**: Antes de executar o projeto, certifique-se de instalar todas as dependências listadas no arquivo `requirements.txt`.
   ```
   pip install -r requirements.txt
   ```

2. **Configuração do Banco de Dados**: Configure as informações de conexão com o banco de dados PostgreSQL no arquivo `settings.py`.

3. **Criação do Banco de Dados**: Execute as migrações do Django para criar o esquema do banco de dados.
   ```
   python manage.py migrate
   ```

4. **Execução do Servidor**: Inicie o servidor de desenvolvimento Django.
   ```
   python manage.py runserver
   ```

5. **Acesso à Aplicação**: Abra um navegador da web e acesse a URL `http://localhost:8000` para usar o aplicativo. Você será redirecionado para a página de login, onde poderá fazer login ou criar uma nova conta.


### Instruções para o Django Admin:
- Para cadastrar usuários e gastos, utilize o Django Admin.
- Para acessar o Django Admin, é necessário criar um superusuário utilizando o comando:
  ```
  python manage.py createsuperuser
  ```
- Após criar o superusuário, acesse o Django Admin em `http://localhost:8000/admin`.

Este é um projeto em desenvolvimento contínuo, com o objetivo de fornecer uma solução eficiente para o controle de gastos compartilhados entre usuários.

### Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar solicitações de pull request para melhorar o projeto.

Para mais informações, consulte a documentação completa do Django em [https://docs.djangoproject.com/en/stable/](https://docs.djangoproject.com/en/stable/).