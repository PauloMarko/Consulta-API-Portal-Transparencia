# Consulta Automatizada à API do Portal da Transparência

 [![Python 3.13+](https://img.shields.io/badge/python-3.13%2B-blue)](https://www.python.org/downloads/) [![Static Badge](https://img.shields.io/badge/0.9%2B-de5fe9?style=flat&label=uv)](https://github.com/astral-sh/uv)

### 1. Descrição do projeto
Este projeto tem como objetivo de desenvolver um sistema modular e reutilizável em Python em que realiza consultas automáticas à [**API do Portal da Transparência**](https://portaldatransparencia.gov.br/api-de-dados) do Governo Federal a partir de uma lista de CPFs e armazene os resultados em um arquivo CSV utilizando os princípios da **Programação Orientada à Objetos (POO)**.

### 2. Funcionalidades
 - Lê CPFs de um arquivo CSV.
 - Consulta a API oficial (com chave própria).
 - Valida e padroniza os dados com Pydantic. 
 - Salva tudo em CSV estruturado (fácil de abrir no Excel/LibreOffice). 
 - Logging completo de erros e sucessos.

### 3. Pré-requisitos
- Python 3.13 ou superior
- Chave de API do Portal da Transparência → [registre aqui](http://portaldatransparencia.gov.br/api-de-dados/cadastrar-email)
- [UV 0.9.10](https://github.com/astral-sh/uv) ou superior (Recomendado para gerenciar o projeto).

### 4. Justificativa
A automatização da coleta de dados públicos permite otimizar o tempo de análise e aumentar a precisão de auditorias, fiscalizações e pesquisas relacionadas ao uso de recursos públicos. Este projeto oferece uma solução prática e extensível para consultas em massa, servindo como base para sistemas mais complexos de análise de dados governamentais.

### 5. Estrutura do projeto
O sistema foi desenvolvido com Python 3.13, estruturado segundo os princípios da **Programação Orientada à Objetos (POO)**. A arquitetura contempla os seguintes componentes:
#### Classes:
- `LeitorCSV`: Responsável por ler arquivo CSV contendo os CPFs a serem consultados.
- `ConsultaAPI`: Responsável por realizar as requisições à API do Portal da Transparência e retornar os dados em formato JSON.
- `ValidarDados`: Responsável pela validação dos dados obtidos pela consulta da API.
- `GravadorCSV`: Responsável por processar os dados obtidos e salvá-los em um novo arquivo CSV estruturado.
- `ControladorAplicacao`: Classe principal que orquestra o fluxo do sistema, coordenando as operações de leitura, consulta e gravação.
#### Bibliotecas:
- `requests` --- para a comunicação com a API REST;
- `pandas` --- para leitura e escrita de arquivos;
- `logging` --- para registro de atividades e erros;
- `dotenv` --- para configuração de chaves de API via variáveis de ambiente (Se não, o programa solicita a chave API).

Além disso, usei o linter e formatador chamado `ruff` que é extremamente rápido, escrito em Rust, projetado para subtituir múltiplas ferramentas de verificação de qualidade de código como Flake8, Black e isort por uma única solução. Ele verifica e corrige automaticamente erros, violações de estilo e outros problemas para melhorar a qualidade e a manutenção do código.

### 6. Fluxo de Execução
1. O usuário fornece um arquivo CSV contendo uma lista de CPFs.
2. O sistema lê os CPFs e inicia o processo de consulta individual à API. 
3. O sistema solicitará ao usuário a chave da API se caso não estiver nas variáveis de ambiente.
4. Para cada CPF,  a API retorna um conjunto de informações (como nome, órgão, tipo de despesa, valores, etc.).
5. Os resultados são armazenados em um arquivo CSV de saída, contendo colunas estruturadas.
6. Logs são gerados para cada operação, registrando eventuais erros de rede, CPFs inválidos ou dados ausentes.

### 7. Como usar
1. Crie um arquivo CSV assim:
	```
	cpfs
	12345678910
	10987654321
	...
	```
	OBS.: o programa vai procurar o arquivo `cpfs.csv` por padrão.

2. Crie (opcional) um arquivo `.env` na pasta raiz:
	```
	CHAVE_API_DADOS={sua_chave_api}
	```

3. Execute:
	```
	python main.py
	```
	Se não tiver o `.env`, o programa irá pedir a chave.

	Resultado -> um arquivo CSV de saída com dezenas de colunas (como nome, se é servidor, etc.).

### 8. Exemplo de linha do CSV de saída

| cpf         | nome          | nis         | favorecidoDespesas | servidor | ... |
| ----------- | ------------- | ----------- | ------------------ | -------- | --- |
| 12345678901 | JOÃO DA SILVA | 12345678910 | False              | True     | ... |

### Autor
Marcos Paulo Alves de Araújo - IFRN Campus Caicó - Informática para Internet 2V - 2025