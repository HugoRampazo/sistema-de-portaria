# sistema-de-portaria
Esse projeto/sistema web foi criado para ser utilizado em portarias de condomínio, auxiliando no seu controle de acesso.

# como baixar o projeto
Abra o CMD e digite:

cd desktop

git clone https://github.com/HugoRampazo/sistema-de-portaria.git

# como visualizar o projeto
1- Vamos criar o ambiente virtual, abra o CMD:

pip install --upgrade virtualenv

pip install --upgrade virtualenvwrapper-win

pip install --upgrade pip

mkvirtualenv portariavenv

workon portariavenv

2- Agora vamos acessar a pasta do projeto e instalar os pacotes necessários no nosso ambiente virtual (portariavenv), continuando no CMD:

cd desktop

cd sistema-de-portaria

cd portaria

pip install -r requirements.txt


3- Nessa etapa vamos criar um super usuário para conseguir acessar o sistema, continuando no CMD:

cd desktop

cd sistema-de-portaria

cd portaria

python manage.py createsuperuser

    (Informe um usuário, email e senha de sua escolha)

4- Agora vamos colocar nosso site no ar, continuando no CMD:

python manage.py runserver

5- Com o CMD aberto, abra o seu navegador e acesse:

http://localhost:8000/

6- Pronto, agora é só entrar com usuário e senha que você criou para utilizar o sistema.
