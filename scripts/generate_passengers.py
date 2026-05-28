import random
import mysql.connector
from faker import Faker

fake = Faker('fr_FR')

config = {
    'user': 'root',
    'password': 'root', 
    'host': '127.0.0.1',
    'database': 'air_france_db',
    'use_pure': True,
    'auth_plugin': 'mysql_native_password'
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    print("Nettoyage de la table passagers...")
    cursor.execute("DELETE FROM passagers;")
    
    # On définit les capacités max de chaque vol pour éviter le surbooking
    capabilites = {101: 324, 102: 296, 103: 148}
    remplissage = {101: 0, 102: 0, 103: 0}

    print("Génération des passagers (avec limite de capacité)...")
    classes = ['Economy', 'Premium Eco', 'Business', 'First']

    # On essaie de générer 550 passagers au total
    for _ in range(550):
        # On ne garde que les vols qui ne sont pas encore pleins
        vols_disponibles = [v for v, cap in capabilites.items() if remplissage[v] < cap]
        
        # Si tous les avions sont pleins, on arrête la boucle
        if not vols_disponibles:
            break
            
        vol_id = random.choice(vols_disponibles)
        nom = fake.last_name()
        prenom = fake.first_name()
        classe = random.choice(classes)

        query = "INSERT INTO passagers (nom, prenom, classe_voyage, vol_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nom, prenom, classe, vol_id))
        
        # On comptabilise le passager pour ce vol
        remplissage[vol_id] += 1

    conn.commit()
    print("✅ Les passagers ont été ajoutés sans dépasser la capacité des avions.")

except mysql.connector.Error as err:
    print(f"Erreur MariaDB : {err}")
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
