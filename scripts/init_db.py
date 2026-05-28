import mysql.connector

# =====================================================================
# CONFIGURATION DE TA BDD MARIADB
# =====================================================================
config = {
    'user': 'root',
    'password': 'root',  # ⚠️ METS TON VRAI MOT DE PASSE MARIADB ICI
    'host': '127.0.0.1',     # Ton PC local
    'use_pure': True
}

db_name = 'air_france_db'

try:
    # 1. Connexion au serveur MariaDB
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("🔌 Connexion réussie à MariaDB !")

    # 2. Création de la base de données
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4;")
    cursor.execute(f"USE {db_name};")
    print(f"📁 Base de données '{db_name}' prête.")

    # 3. Lecture et exécution du Schéma (Tables)
    print("⏳ Création des tables...")
    with open('sql/air_france_schema.sql', 'r', encoding='utf-8') as f:
        schema_queries = f.read().split(';')
        for query in schema_queries:
            if query.strip():
                cursor.execute(query)

    # 4. Lecture et exécution des Données (Seed)
    print("⏳ Injection des données de test...")
    with open('sql/air_france_data.sql', 'r', encoding='utf-8') as f:
        data_queries = f.read().split(';')
        for query in data_queries:
            if query.strip():
                cursor.execute(query)

    # 5. Validation
    conn.commit()
    print("✅ Tout est parfait ! Ta base MariaDB est créée et alimentée.")

except mysql.connector.Error as err:
    print(f"❌ Erreur MariaDB : {err}")
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()