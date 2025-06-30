# Titulo do projeto

Consiste em desenvolver uma plataforma para ...

## Equipe do projeto

NomeCompleto1

NomeCompleto2

NomeCompleto3

## Sumário

1. Requisitos
2. Configuração de acesso aos dados
3. Estrutura do projeto
4. Instale os requisitos do projeto
5. Executando o projeto
6. Telas do projeto

A ordem dos itens do sumário podem e devem ser ajustadas para melhor entendimento sobre o projeto

Lembre-se que as instruções presentes neste arquivo devem permitir que outra pessoa possa clonar o repositório público e utilizar o projeto


## 🔧 Requisitos:

- NodeJS LTS v.X.Y.Z

- React Native v.X.Y.Z

- ExpoGo (link googlePlayStore) / (link applePlayStore)

- Banco de dados: qual? EX: SQLite. Especificar as tabelas criadas e utilizadas

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
nomeDoProjeto/
├── apresentacao
│   ├── apresentacao.pdf
│   └── apresentacao.pptx
├── documentacao
│   ├── 01_cartaDeApresentacao.pdf
│   ├── 02_cartaDeAutorizacao.pdf
│   ├── 03_declaracaoDeUsoDeDadosPublicos.pdf
│   └── 04_roteiroDeExtensao.pdf
├── frontend
│   ├── assets
│   ├── src
│   ├── .gitignore
│   ├── package.json
│   ├── readme.md
│   └── ...demais arquivos
├── backend
│   ├── src
│   ├── .gitignore
│   ├── readme.md
│   └── ...demais arquivos
├── video
│   ├── apresentacao.gif
│   ├── apresentacao.mkv
│   ├── apresentacao.mp4
│   └── video.txt  O conteúdo deste arquivo deve ser o local público onde está o vídeo caso tenha mais de 10MB
└── readme.md  Este arquivo é uma visão geral do projeto e não precisa ser igual a este arquivo
```

## 📦 Instale os requisitos do projeto:
```
python -m venv venv

cd venv

source /venv/bin/activate

pip install -r requirements.txt
```

## 🚀 Execute o projeto:
```
python main.py
```

## Telas do projeto

Capture todas as telas do projeto e identifique-as

Tela 1: login

Tela 2: criacao de usuario

Tela 3: recuperacao de senha

Tela 4: tela inicial

...e assim por diante
