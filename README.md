# 📦 Catálogo Django (Atividade Extra) Aluno : Alan Santos

Uma aplicação web desenvolvida em Python utilizando o framework Django para o gerenciamento e exibição de um catálogo de itens/produtos.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar o ambiente local e rodar a aplicação na sua máquina.

### 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:
* **Python 3.10 ou superior**
* **Git**
* **WSL (Windows Subsystem for Linux)** _(Caso esteja no Windows, como o projeto foi estruturado no Ubuntu)_

---

### 🔧 Passo a Passo para Instalação e Configuração

**1. Clonar o repositório:**
Abra o terminal (de preferência o terminal do WSL/Ubuntu) e clone o projeto

**2. Criar o ambiente virtual (venv):
Crie um ambiente isolado para instalar as dependências do projeto: python3 -m venv venv

**3. Ativar o ambiente virtual: source venv/bin/activate

**4. Instalar as dependências:
Com o ambiente virtual devidamente ativo, instale os pacotes necessários: pip install -r requirements.txt

**5. Executar as Migrações do Banco de Dados:
Crie a estrutura das tabelas no banco de dados padrão (SQLite):  python manage.py migrate

**6. Criar um usuário administrador (Opcional):
Caso precise acessar o painel de administração do Django (/admin), crie um superusuário executando:  python manage.py createsuperuser

Executar com o comando --->  python manage.py runserver

Agora, abra o seu navegador e acesse o endereço local:
👉 http://127.0.0.1:8000/

Para acessar a interface administrativa, utilize:
👉 http://127.0.0.1:8000/admin/
