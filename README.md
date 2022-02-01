# P12_Developpez_une_architecture_back-end_securisee_en_utilisant_Django_ORM
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)


## Description :


Epic_events est un CRM permettant de gérer les données clients de manière sécurisée.


## Fonctionnalités :

Customers :
  - Lister les clients (pour les groupes sales & support)
  - Créer un nouveau client (pour le groupe sales)
  - Afficher un client (pour les groupes sales & support)
  - Modifier un client (pour le groupe sales)
  - Supprimer un client (pour le groupe sales)

Contracts :
  - Lister les contrats (pour les groupes sales & support)
  - Créer un nouveau contrat (pour le groupe sales)
  - Afficher un contrat (pour les groupes sales & support)
  - Modifier un contrat (pour le groupe sales)
  - Supprimer un contrat : (pour le groupe sales)
 
Events :
  - Lister les événements (pour les groupes sales & support)
  - Afficher un événement (pour les groupes sales & support)
  - Modifier un événement (pour le groupe sales)


## Installation :


Cloner ce dépôt de code à l'aide de la commande :
```$ git clone https://github.com/Christophe-Ringot/P12_Developpez_une_architecture_back-end_securisee_en_utilisant_Django_ORM.git```

Créer un environnement virtuel pour le projet :
```$ python -m venv env``` sous windows ou ```$ python3 -m venv env``` sous macos ou linux.

Activez l'environnement virtuel :
```$ env\Scripts\activate``` sous windows ou ```$ source env/bin/activate sous macos ou linux.```

Installez les dépendances de à l'aide de la commande :
```pip install -r requirements.txt```

Mettre en place la base de données à l'aide de pgAdmin 4 (vous pouvez modifier les informations depuis le settings.py de l'application)


## Exécution :

Se rendre sur le dossier avec la commande :
```$ cd epic_events```

Effectuer les migrations :
```$ python manage.py makemigrations``` & ```$ python manage.py migrate```

Créer un nouveau compte administrateur :
```$ python manage.py createsuperuser```

Lancez le serveur avec la commande :
```$ python manage.py runserver```