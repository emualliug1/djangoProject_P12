# Projet 12
## Epic Events

### Objectif :
Développez une architecture back-end sécurisée en utilisant Django ORM

### Commencer :
Assurez-vous que python est installé sur votre machine :

    python -V

Vérifiez que vous disposez du module venv :
    
    python -m venv --help
  
Si Python n'est pas installé sur votre machine :
    
    https://www.python.org/downloads/
    
Si vous ne disposez pas du module virtual env:
    
    py -m pip install --user virtualenv


### postgreSQL configuration
Assurez-vous que vous avez postgreSQL sur votre machine, ou cliquez [ici](https://www.postgresql.org/download/).

Après avoir lancé le PgAdmin4 :
 - Créez une base de données avec `epic events` comme nom de base de données.


### Une fois Python installé :
   
 Ouvrir une invite de commande et utiliser la commande :`cd` pour aller dans le repertoire ou vous voulez copier le projet. 
    Vous pouvez aussi créer un nouveau repertoire avec la commande: `mkdir`
    Une fois dans le bon repertoire il vous suffit de taper: 
 
    git clone https://github.com/emualliug1/P12
    
Créer un environnement virtuel avec venv :`python -m venv ***nom de l'environnement***` : pour créer l'environnement virtuel --- exemple : 

    py -m venv env
    
Activez l'environnement virtuel : `***nom de l'environnement***/Scripts/activate.bat` --- exemple : 

    env/Scripts/activate.bat
    
Installez les packages avec pip : 

    pip install -r requirements.txt

Migrer les tables vers la base de données :

    py manage.py migrate

Creer un Super utilisateur :

	py manage.py createsuperuser

Lancez l'API avec : 

    py manage.py runserver
