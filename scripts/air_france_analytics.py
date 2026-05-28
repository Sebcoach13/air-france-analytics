import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# 1. Connexion à MariaDB
USER = "root"
PASSWORD = "root"  # Laisse vide ou ajuste selon ta config
HOST = "127.0.0.1"
PORT = "3306"
DB_NAME = "air_france_db"

connect_args = {'use_pure': True, 'auth_plugin': 'mysql_native_password'}
engine = create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}", connect_args=connect_args)

# 2. Chargement des DataFrames
df_avions = pd.read_sql("SELECT * FROM avions", engine)
df_vols = pd.read_sql("SELECT * FROM vols", engine)
df_passagers = pd.read_sql("SELECT * FROM passagers", engine)

# 3. Calcul du prix du billet par passager
grille_tarifs = {'Economy': 150, 'Premium Eco': 300, 'Business': 900, 'First': 2500}
df_passagers['prix_billet'] = df_passagers['classe_voyage'].map(grille_tarifs)

# 4. Calcul du CA total par Vol
df_ca_vols = df_passagers.groupby('vol_id').agg(
    chiffre_affaires=('prix_billet', 'sum'),
    nb_passagers_real=('passager_id', 'count')
).reset_index()

# 5. Fusion globale
df_global = pd.merge(df_vols, df_avions, on="avion_id", how="inner")
df_global = pd.merge(df_global, df_ca_vols, on="vol_id", how="left")
df_global["chiffre_affaires"] = df_global["chiffre_affaires"].fillna(0)
df_global["nb_passagers_real"] = df_global["nb_passagers_real"].fillna(0).astype(int)

# 6. Affichage textuel dans le terminal
print("\n=============================================")
print("     RAPPORT FINANCIER AIR FRANCE")
print("=============================================")
for index, row in df_global.iterrows():
    print(f"✈️ Vol {row['numero_vol']} : {row['chiffre_affaires']:,} €")

# =====================================================================
# 7. CRÉATION DU GRAPHIQUE (MATPLOTLIB)
# =====================================================================
print("\n📊 Génération du graphique en cours...")

# On configure la taille de la fenêtre du graphique
plt.figure(figsize=(8, 5))

# On crée un graphique à barres (X = numéros de vols, Y = chiffres d'affaires)
plt.bar(df_global['numero_vol'], df_global['chiffre_affaires'], color=['#002157', '#0033a0', '#4a90e2'])

# On ajoute les titres et les labels
plt.title("Chiffre d'Affaires par Vol - Air France", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Numéro de Vol", fontsize=12)
plt.ylabel("Chiffre d'Affaires (€)", fontsize=12)

# On sauvegarde le graphique sous forme d'image sur ton ordinateur
plt.savefig('chiffre_affaires_vols.png', dpi=300, bbox_inches='tight')
print("✅ Graphique sauvegardé sous le nom 'chiffre_affaires_vols.png' à la racine de ton projet !")

# On affiche le graphique à l'écran
plt.show()
