SysChamadosAPI

Uma API simples em Python para gerenciamento de chamados. Este projeto oferece uma interface leve e fácil de usar para criar, consultar, atualizar e excluir registros de chamados, ideal para sistemas de suporte de pequena escala.

Funcionalidades





Criação e gerenciamento de chamados com informações essenciais (ex.: título, descrição, status).



Endpoints RESTful para integração simplificada.



Desenvolvido com Python e [insira o framework, ex.: Flask/FastAPI, se aplicável].



Fácil de implantar e extender.

Instalação





Clonar o repositório:

git clone https://github.com/younglherme/SysChamadosAPI.git
cd SysChamadosAPI



Configurar um ambiente virtual (recomendado):

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate



Instalar dependências:

pip install -r requirements.txt



Executar a API:

python app.py  # Ajuste para o nome do script principal, se diferente

Uso





Inicie o servidor da API (veja a seção de Instalação).



Acesse a API em http://localhost:5000 (ou a porta configurada).



Use ferramentas como curl, Postman ou um navegador para interagir com os endpoints.

Exemplos de endpoints:





GET /tickets: Lista todos os chamados.



POST /tickets: Cria um novo chamado (ex.: envie JSON com title, description, status).



GET /tickets/<id>: Consulta um chamado específico por ID.



PUT /tickets/<id>: Atualiza um chamado.



DELETE /tickets/<id>: Exclui um chamado.

Exemplo de requisição curl para criar um chamado:

curl -X POST http://localhost:5000/tickets -H "Content-Type: application/json" -d '{"title":"Chamado #1","description":"Problema de exemplo","status":"aberto"}'

Requisitos





Python 3.8+



Dependências listadas em requirements.txt (ex.: Flask, FastAPI ou outras usadas no projeto).
