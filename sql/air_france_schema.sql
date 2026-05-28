CREATE TABLE IF NOT EXISTS aeroports (
    aeroport_id VARCHAR(3) PRIMARY KEY,
    nom_aeroport VARCHAR(100) NOT NULL,
    ville VARCHAR(100) NOT NULL,
    pays VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS avions (
    avion_id INT AUTO_INCREMENT PRIMARY KEY,
    immatriculation VARCHAR(10) UNIQUE NOT NULL,
    modele VARCHAR(50) NOT NULL,
    capacite_passagers INT NOT NULL
);

CREATE TABLE IF NOT EXISTS vols (
    vol_id INT AUTO_INCREMENT PRIMARY KEY,
    numero_vol VARCHAR(10) NOT NULL,
    aeroport_depart VARCHAR(3) NOT NULL,
    aeroport_arrivee VARCHAR(3) NOT NULL,
    date_heure_depart DATETIME NOT NULL,
    avion_id INT NOT NULL,
    statut VARCHAR(20) DEFAULT 'À l''heure',
    retard_minutes INT DEFAULT 0,
    FOREIGN KEY (aeroport_depart) REFERENCES aeroports(aeroport_id),
    FOREIGN KEY (aeroport_arrivee) REFERENCES aeroports(aeroport_id),
    FOREIGN KEY (avion_id) REFERENCES avions(avion_id)
);

CREATE TABLE IF NOT EXISTS passagers (
    passager_id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    classe_voyage VARCHAR(20) NOT NULL,
    vol_id INT NOT NULL,
    FOREIGN KEY (vol_id) REFERENCES vols(vol_id)
);

