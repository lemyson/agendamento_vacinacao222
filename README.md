# agendamento_vacinacao222
link heroku: https://secret-reaches-54434.herokuapp.com/agen/

Itens essenciais.
# python
# Django
# postgresql

Executando o projeto localmente:
    Instale a virtualenv, execute:
    $ pip install virtualenv
    Crie uma localenv
    $ mkdir my_project_env
    $ cd my_project_env
    $ virtualenv -p /usr/bin/python3.9 my_project
    $ source my_project/bin/activate
    $ cd my_project

    se não conseguir criar a virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/
    Criada a virtualenv, execute para instalar dependências:

    $ pip install -r requirements.txt

    Faça o download do projeto executando:

    $ git clone https://github.com/lemyson/agendamento_vacinacao222.git

    Execute:

    $ cd agendador

    Execute:

    $ python manage.py makemigrations
    $ python manage.py migrate

    Por fim, execute:

    $ python manage.py loaddata auth.json
    $ python manage.py loaddata agenda.json