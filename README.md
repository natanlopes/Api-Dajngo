# Django REST Framework - Criando APIs poderosas
Este repositório contém um projeto desenvolvido na linguagem Python com o framework web Django e a extensão Django REST Framework para criar APIs REST.

O objetivo deste projeto é ensinar desde os conceitos básicos envolvidos em aplicações de serviços web, passando pela instalação e utilização dos principais recursos do Django REST Framework.



**Conteúdo**:
- O que são APIs?
- O que é REST?
- O que é o Django REST Framework?
- Métodos HTTP suportados
- Recursos de segurança
- Testando as APIs
- Como executar o projeto
- Contribuição
- O que são APIs?



**API**  
---(Application Programming Interface) é um conjunto de protocolos e padrões de programação que permitem a comunicação entre diferentes aplicações ---.

O que é REST?
REST (Representational State Transfer) é um estilo arquitetural de software para sistemas distribuídos, como a World Wide Web. Ele se baseia no protocolo HTTP e utiliza seus métodos (GET, POST, PUT e DELETE) para criar serviços web.




O que é o Django REST Framework?
O Django REST Framework é uma extensão do framework web Django que facilita a criação de APIs RESTful. Ele suporta vários formatos de serialização de dados, autenticação de usuários, paginacão de dados, e muito mais.



Métodos HTTP suportados
Este projeto suporta os seguintes métodos HTTP:

GET - Recuperar informações de um recurso
POST - Criar um novo recurso
PUT - Atualizar um recurso existente
DELETE - Remover um recurso existente
Recursos de segurança
Este projeto utiliza os seguintes recursos de segurança:



Autenticação via Token
Permissionamento
Limitação de requests
Testando as APIs
Este projeto contém testes unitários para todas as APIs criadas. Eles podem ser encontrados no arquivo tests.py. Para executar os testes, execute o seguinte comando:

bash
Copy code
python manage.py test
Como executar o projeto
Clone o repositório:
bash
Copy code
git clone https://github.com/seu-usuario/nome-do-repositorio.git
Crie um ambiente virtual e instale as dependências:
bash
Copy code
cd nome-do-repositorio
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Execute as migrações do banco de dados:
Copy code
python manage.py migrate
Execute o servidor:
Copy code
python manage.py runserver
Agora você pode acessar a API em http://localhost:8000/api/v1/.



Contribuição
Contribuições são sempre bem-vindas! Se você encontrou um bug ou tem alguma sugestão de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request. 
