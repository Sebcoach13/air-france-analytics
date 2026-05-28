-- Nettoyage au cas où
DELETE FROM passagers;
DELETE FROM vols;
DELETE FROM avions;
DELETE FROM aeroports;

-- 1. Insertion des Aéroports
INSERT INTO aeroports (aeroport_id, nom_aeroport, ville, pays) VALUES 
('CDG', 'Paris-Charles de Gaulle', 'Paris', 'France'),
('JFK', 'New York-John F. Kennedy', 'New York', 'États-Unis'),
('NCE', 'Nice Côte d''Azur', 'Nice', 'France'),
('HND', 'Tokyo-Haneda', 'Tokyo', 'Japon');

-- 2. Insertion des Avions
INSERT INTO avions (avion_id, immatriculation, modele, capacite_passagers) VALUES 
(1, 'F-HTYA', 'Airbus A350-900', 324),
(2, 'F-GSQN', 'Boeing 777-300ER', 296),
(3, 'F-HZUM', 'Airbus A220-300', 148);

-- 3. Insertion des Vols
INSERT INTO vols (vol_id, numero_vol, aeroport_depart, aeroport_arrivee, date_heure_depart, avion_id, statut, retard_minutes) VALUES 
(101, 'AF015', 'CDG', 'JFK', '2026-05-28 08:30:00', 1, 'À l''heure', 0),
(102, 'AF274', 'CDG', 'HND', '2026-05-28 23:25:00', 2, 'Retardé', 85),
(103, 'AF6200', 'NCE', 'CDG', '2026-05-28 14:15:00', 3, 'Retardé', 20);

-- 4. Insertion des Passagers
INSERT INTO passagers (nom, prenom, classe_voyage, vol_id) VALUES 
('Garnier', 'Mathieu', 'Business', 101),
('Lopez', 'Sofia', 'Economy', 101),
('Chen', 'Wei', 'First', 102),
('Dubois', 'Pierre', 'Economy', 102),
('Muller', 'Emma', 'Premium Eco', 103);