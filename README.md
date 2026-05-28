# ✈️ Air France Analytics — Pipeline de Données & CI/CD

Ce projet met en place un pipeline de données complet, robuste et automatisé pour l'analyse des vols, de la capacité des avions et du taux de remplissage des passagers d'Air France. Il intègre une base de données **MariaDB**, un traitement analytique avec **Pandas**, une génération de données réalistes avec **Faker** et une validation automatisée via un pipeline **CI/CD (GitHub Actions)**.

---

## 🏗️ Architecture du Projet

Le projet respecte une architecture claire et compartimentée :

```text
air-france-analytics/
├── .github/
│   └── workflows/
│       └── ci.yml             # Configuration du pipeline CI/CD GitHub Actions
├── scripts/
│   ├── init_db.py             # Initialisation de la BDD et injection du schéma
│   ├── generate_passengers.py # Génération de 150 faux passagers réalistes (Faker)
│   └── air_france_analytics.py# Aspiration des données et calculs des KPI (Pandas)
├── sql/
│   ├── air_france_schema.sql  # Structure des tables (DDL)
│   └── air_france_data.sql    # Données d'ensemencement initiales (Seed)
├── .gitignore                 # Exclusion des fichiers temporaires et virtuels
└── README.md                  # Documentation du projet
📊 Structure de la Base de Données (Schéma Relationnel)
La base de données air_france_db est hautement relationnelle et s'articule autour de 4 tables clés :

aeroports : Centralise les hubs et destinations (Code ID, Nom, Ville, Pays).

avions : Contient la flotte, l'immatriculation et la capacité maximale de passagers.

vols : Planifie les trajets en liant un avion, un aéroport de départ et d'arrivée, avec gestion des statuts et retards.

passagers : Répertorie les voyageurs, leur classe de voyage (Business, Economy...) et leur affectation à un vol_id (Clé Étrangère).

Diagramme de Modélisation Entité-Relation (ERD)
Extrait de code
erDiagram
    aeroports {
        string aeroport_id PK
        string nom_aeroport
        string ville
        string pays
    }
    avions {
        int avion_id PK
        string immatriculation
        string modele
        int capacite_passagers
    }
    vols {
        int vol_id PK
        string numero_vol
        string aeroport_depart FK
        string aeroport_arrivee FK
        datetime date_heure_depart
        int avion_id FK
        string statut
        int retard_minutes
    }
    passagers {
        int passager_id PK
        string nom
        string prenom
        string classe_voyage
        int vol_id FK
    }

    vols }|--|| avions : "utilisera"
    vols }|--|| aeroports : "part_de"
    vols }|--|| aeroports : "arrive_a"
    passagers }|--|| vols : "reserve"
🚀 Installation et Utilisation Locale
1. Prérequis
Python 3.10 ou supérieur

Un serveur MariaDB (ou MySQL) actif sur le port 3306.

2. Installation des dépendances
Installez les bibliothèques requises à l'aide de pip :

PowerShell
pip install mysql-connector-python sqlalchemy pandas faker matplotlib
3. Exécution du Pipeline
Étape A : Initialiser la structure et injecter le seed SQL

PowerShell
python scripts/init_db.py
Étape B : Générer dynamiquement le volume de passagers
Pour simuler une activité réelle et obtenir des statistiques de remplissage cohérentes, lancez le script de génération (génère 150 passagers uniques distribués aléatoirement) :

PowerShell
python scripts/generate_passengers.py
Étape C : Lancer le rapport analytique
Aspire les tables SQL sous forme de DataFrames Pandas, calcule les taux de remplissage et génère le rapport :

PowerShell
python scripts/air_france_analytics.py
🤖 Pipeline CI/CD (GitHub Actions)
Ce projet intègre une démarche DevOps de pointe grâce à un workflow d'Intégration Continue (ci.yml).

Flux de Circulation des Données & Workflow CI/CD
Extrait de code
graph TD
    A[sql/air_france_schema.sql] -->|1. Crée les tables| B[(MariaDB Locale)]
    C[sql/air_france_data.sql] -->|2. Injecte le Seed| B
    D[scripts/generate_passengers.py] -->|3. Injecte 150 passagers Faker| B
    B -->|4. Aspire via SQLAlchemy| E[scripts/air_france_analytics.py]
    E -->|5. Calcule les KPI| F[Rapport final Pandas]
    
    subgraph CI/CD GitHub Actions
        G[git push] --> H[Serveur Virtuel Linux]
        H --> I[Docker MariaDB temporaire]
        I --> J[Exécution automatique des tests]
    end
À chaque git push ou Pull Request sur la branche principale :

Conteneurisation éphémère : GitHub Actions instancie un conteneur Linux (Ubuntu) et un service de base de données MariaDB 10.6 virtuel en arrière-plan.

Setup Environnement : Python est installé et l'intégralité des dépendances (pandas, sqlalchemy, faker, matplotlib...) est injectée.

Tests d'Intégration automatiques :

Validation de la création des tables et des contraintes relationnelles (init_db.py).

Validation de l'algorithme de génération de données (generate_passengers.py).

Validation du script d'analyse métier (air_france_analytics.py).

Le pipeline est configuré pour bloquer toute mise en production si un script lève une exception ou si une régression est détectée.

🛠️ Technologies Utilisées
Base de données : MariaDB / MySQL

Langage & Driver : Python 3.10, mysql-connector-python

ORMe & Mapping : SQLAlchemy

Data Science / Analytics : Pandas

Data Generation : Faker

Visualisation : Matplotlib

CI/CD & DevOps : GitHub Actions, YAML, Conteneurs Docker (Services GitHub)

Gestion de version : Git & GitHub