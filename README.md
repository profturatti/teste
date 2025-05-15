# Titulo do projeto

Consiste em desenvolver uma plataforma para ...
## 🔧 Requisitos:

- Python 3.8+

- Flask

- Banco de dados: qual?

### 🗃️ Tabela 'usuarios' com os seguintes campos:
```
id: UUID or int (primary key)
timestamp: timestamp
nomeCompleto: text (nullable)
telefone: text (nullable)
email: text (nullable)
```

## 🔐 Configuração de acesso ao banco de dados
```
DATABASE_URL=https://backend_do_seu_projeto.com
DATABASE_KEY=chave_de_acesso
```

## 📁 Estrutura do projeto:
```
projeto/
├── main.py
├── database_client.py
├── templates/
│   └── index.html
├── static/
│   └── figura.jpg
└── requirements.txt
```

## 📦 Instale os requisitos do projeto:
```
python -m venv venv

pip install -r requirements.txt
```

## 🚀 Execute o projeto:
```
python main.py
```
