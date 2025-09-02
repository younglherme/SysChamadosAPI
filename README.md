# SysChamadosAPI

Uma API simples em Python para gerenciamento de chamados. Este projeto oferece uma interface leve e fácil de usar para criar, consultar, atualizar e excluir registros de chamados, ideal para sistemas de suporte de pequena escala.

## Funcionalidades

- Criação e gerenciamento de chamados com informações essenciais (ex.: título, descrição, status).
- Endpoints RESTful para integração simplificada.
- Desenvolvido com Python e Flask.
- Fácil de implantar e extender.

## Instalação

1. Clonar o repositório:
   ```bash
   git clone https://github.com/younglherme/SysChamadosAPI.git
   cd SysChamadosAPI


## Configurar um ambiente virtual (recomendado):

- python -m venv venv

- source venv/bin/activate # No Windows: venv\Scripts\activate

## Instalar dependências:
```
 pip install -r requirements.txt

```

## Uso.

- Inicie o servidor da API (veja a seção de Instalação).

- Acesse a API em http://localhost:5000 (ou a porta configurada).

- Use ferramentas como curl, Postman ou um navegador para interagir com os endpoints.

## Exemplos de endpoints:

- GET /tickets: Lista todos os chamados.

- POST /tickets: Cria um novo chamado.

- GET /tickets/: Consulta um chamado específico por ID.

- PUT /tickets/: Atualiza um chamado.

- DELETE /tickets/: Exclui um chamado.

### Requisitos.

- Python 3.8+

- requirements.txt

