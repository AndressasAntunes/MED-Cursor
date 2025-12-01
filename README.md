# Controle Financeiro Pessoal

Sistema de gerenciamento financeiro pessoal desenvolvido em Django para controle de receitas e despesas.

## Características

- ✅ Cadastro de transações (Receitas e Despesas)
- ✅ Visualização de saldo total
- ✅ Listagem de todas as transações
- ✅ Exclusão de transações
- ✅ Interface responsiva e moderna

## Instalação

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute as migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Crie um superusuário (opcional, para acessar o admin):
```bash
python manage.py createsuperuser
```

4. Execute o servidor de desenvolvimento:
```bash
python manage.py runserver
```

5. Acesse o sistema em: http://127.0.0.1:8000/

## Estrutura do Projeto

- `controle_financeiro/` - Configurações do projeto Django
- `core/` - Aplicativo principal com modelos, views e templates
  - `models.py` - Modelo Transacao
  - `views.py` - Views (home, adicionar_transacao, excluir_transacao)
  - `forms.py` - Formulário baseado no modelo
  - `urls.py` - Rotas do aplicativo
  - `templates/core/` - Templates HTML

## Funcionalidades

### Home (/)
- Exibe o saldo total (Receitas - Despesas)
- Lista todas as transações ordenadas por data
- Botão para adicionar nova transação
- Botão de exclusão para cada transação

### Adicionar Transação (/adicionar/)
- Formulário para cadastrar nova transação
- Campos: Descrição, Valor, Data, Tipo (Receita/Despesa)

### Excluir Transação (/excluir/<id>/)
- Confirmação antes de excluir
- Exclusão permanente da transação

## Tecnologias Utilizadas

- Django 4.2
- SQLite (banco de dados padrão)
- HTML5/CSS3
- Django Humanize (formatação de valores)

