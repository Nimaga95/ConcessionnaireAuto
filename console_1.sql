drop database IF EXISTS glo_2005_Projet_ConcessionnaireNouvelleAuto; #comme cela on peut run le fichier au complet sans dupliquer l'info

CREATE DATABASE IF NOT EXISTS glo_2005_Projet_ConcessionnaireNouvelleAuto;

#select * from Automobile; ## pour tester la méthode import_Automobile_from_csv()
#select * from Client; ## pour tester la méthode import_Client_from_csv()
#select * from Concessionnaire; ## pour tester la méthode import_Concessionnaire_from_csv
#select * from Employe; ## pour tester la méthode import_Employe_from_csv()
#select * from Pieces; ## pour tester la méthode import_Pieces_from_csv()
#select * from fourniAutomobiles; ## pour tester la méthode import_FournisseurAutomobiles_from_csv()
#select * from fourniPieces; ## pour tester la méthode import_FournisseursPieces_from_csv()
select * from FournisseursAutomobiles; ## pour tester la méthode import_FournisseurAutomobiles_from_csv()
select * from FournisseursPieces; ## pour tester la méthode import_FournisseursPieces_from_csv()
#select * from LavageAuto; ## pour tester la méthode import_LavageAuto_from_csv()
#select * from Vente; ## pour tester la méthode import_Vente_from_csv()
#select * from Reparation; ## pour tester la méthode import_Reparation_from_csv()
#select * from Location; ## pour tester la méthode import_Location_from_csv()

USE glo_2005_Projet_ConcessionnaireNouvelleAuto;

CREATE TABLE IF NOT EXISTS Users
(
    id         int AUTO_INCREMENT,
    email  varchar(254)                 UNIQUE NOT NULL,
    passe  varchar(254)                     NOT NULL,
    first_name varchar(50)                      NOT NULL,
    last_name  varchar(50)                      NOT NULL,
    gender     enum ('Male', 'Female', 'Other') NOT NULL,
    birthdate  char(10),
    region     varchar(50),
    phone      varchar(25)                      NOT NULL,
    primary key (id)
);


CREATE TABLE IF NOT EXISTS Concessionnaire
(

    idConcessionnaire              integer NOT NULL AUTO_INCREMENT,
    nomConcessionnaire             varchar(100),
    adresseConcessionnaire         varchar(200) UNIQUE,
    numTelephoneConcessionnaire    varchar(15) UNIQUE,
    adresseCourrielConcessionnaire varchar(100) UNIQUE,
    siteWeb                        varchar(100) UNIQUE,
    PRIMARY KEY (idConcessionnaire)
);
ALTER TABLE Concessionnaire
    AUTO_INCREMENT = 100;

CREATE TABLE IF NOT EXISTS Employe
(
    idEmploye      integer NOT NULL AUTO_INCREMENT,
    prenomEmploye  varchar(100),
    nomEmploye     varchar(100),
    ageEmploye     integer,
    numCellEmploye varchar(15),
    numPoste       integer,
    titreEmploi    varchar(30),#enum ('Laveur', 'Vendeur', 'Loueur', 'Mécanicien','Directeur des ventes', 'Directeur Marketing', 'Secrétaire', 'Concierge'),
    salaireAnnuel  integer,
    anciennete     integer,
    PRIMARY KEY (idEmploye)

);
ALTER TABLE Employe
    AUTO_INCREMENT = 10000;

CREATE TABLE IF NOT EXISTS Client
(
    idClient           integer NOT NULL AUTO_INCREMENT, #add autoindent perhaps
    prenomClient       varchar(100),
    nomClient          varchar(100),
    numTelephoneClient varchar(15),
    adresseClient      varchar(200),
    codePostaleClient  varchar(7),
    ageClient          integer,
    PRIMARY KEY (idClient)
);

ALTER TABLE Client
    AUTO_INCREMENT = 20000;

CREATE TABLE IF NOT EXISTS Automobile
(
    niv           varchar(17),
    marque        varchar(50),
    modele        varchar(50),
    annee         integer,
    couleur       varchar(50),
    odometre      integer,
    nbPlaces      integer,
    prixAuto      double,
    locationVente enum ('Location', 'Vente'),
    sousCategorie varchar(20),
    poidsAuto     integer,
    dateAuto      date,
    PRIMARY KEY (niv)
);


CREATE TABLE IF NOT EXISTS Pieces
(
    idPiece          integer NOT NULL,
    nomPiece         varchar(100),
    categorie        varchar(100),
    poidsPiece       double,
    descriptionPiece varchar(1000),
    prixPiece        double,
    datePiece        date,
    PRIMARY KEY (idPiece)
);

CREATE TABLE IF NOT EXISTS LavageAuto
(
    idLavage   integer NOT NULL AUTO_INCREMENT,
    typeLavage varchar(50),
    prixLavage double,
    niv        varchar(17),
    idClient   integer,
    idEmploye  integer,
    dateLavage date,
    PRIMARY KEY (idLavage),
    FOREIGN KEY (idClient)
        REFERENCES Client (idClient)
        ON UPDATE CASCADE #on veut que le nom change partout
        ON DELETE NO ACTION,
    FOREIGN KEY (idEmploye)
        REFERENCES Employe (idEmploye)
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    FOREIGN KEY (niv)
        REFERENCES automobile (niv)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
);
ALTER TABLE LavageAuto
    AUTO_INCREMENT = 30000;

CREATE TABLE IF NOT EXISTS Vente
(
    idVente          integer NOT NULL AUTO_INCREMENT,
    niv              varchar(17),
    idClient         integer,
    idEmploye        integer,
    dureeFinancement integer, # remplacer durée financement par prix total de l'auto
    tauxInteret      double,
    dateVente        date,
    PRIMARY KEY (idVente),
    FOREIGN KEY (niv)
        REFERENCES automobile (niv)
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    FOREIGN KEY (idClient)
        REFERENCES Client (idClient)
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    FOREIGN KEY (idEmploye)
        REFERENCES employe (idEmploye)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
);
ALTER TABLE Vente
    AUTO_INCREMENT = 40000;

CREATE TABLE IF NOT EXISTS Reparation
(
    idReparation   integer NOT NULL AUTO_INCREMENT,
    niv            varchar(17),
    idClient       integer,
    idEmploye      integer,
    idPiece        integer,
    tempsDeTravail integer, #heures
    coutReparation double,
    dateReparation date,
    PRIMARY KEY (idReparation),
    FOREIGN KEY (niv)
        REFERENCES automobile (niv)
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    FOREIGN KEY (idClient)
        REFERENCES Client (idClient)
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    FOREIGN KEY (idEmploye)
        REFERENCES employe (idEmploye)
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    FOREIGN KEY (idPiece)
        REFERENCES Pieces (idPiece)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
);
ALTER TABLE Reparation
    AUTO_INCREMENT = 50000;

CREATE TABLE IF NOT EXISTS Location
(
    idLocation    integer NOT NULL AUTO_INCREMENT,
    niv           varchar(17),
    idClient      integer,
    idEmploye     integer,
    dureeLocation integer, #mois ## rajouter colonne prix par mois
    tauxInteret   double,
    dateLocation  date,
    PRIMARY KEY (idLocation),
    FOREIGN KEY (niv)
        REFERENCES automobile (niv)
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    FOREIGN KEY (idClient)
        REFERENCES Client (idClient)
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    FOREIGN KEY (idEmploye)
        REFERENCES employe (idEmploye)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
);
ALTER TABLE Location
    AUTO_INCREMENT = 60000;


CREATE TABLE IF NOT EXISTS FournisseursPieces
(
    idFournisseursPieces              integer NOT NULL AUTO_INCREMENT,
    nomFournisseursPieces             varchar(50),
    adresseFournisseursPieces         varchar(200),
    numTelephoneFournisseursPieces    varchar(15),
    adresseCourrielFournisseursPieces varchar(100),
    villeFournisseursPieces           varchar(100),
    provinceEtatFournisseursPieces    varchar(50),
    paysFournisseursPieces            varchar(50),
    PRIMARY KEY (idFournisseursPieces)
);
ALTER TABLE Fournisseurspieces
    AUTO_INCREMENT = 70000;

CREATE TABLE IF NOT EXISTS FournisseursAutomobiles
(
    idFournisseursVehicules              integer NOT NULL AUTO_INCREMENT,
    nomFournisseursVehicules             varchar(50),
    adresseFournisseursVehicules         varchar(200),
    numTelephoneFournisseursVehicules    varchar(15),
    adresseCourrielFournisseursVehicules varchar(100),
    villeFournisseursVehicules           varchar(100),
    provinceEtatFournisseursVehicules    varchar(50),
    paysFournisseursVehicules            varchar(50),
    PRIMARY KEY (idFournisseursVehicules)
);
ALTER TABLE FournisseursAutomobiles
    AUTO_INCREMENT = 80000;


CREATE TABLE IF NOT EXISTS FourniPieces
(
    idFournisseursPieces int,
    idPiece              int,
    FOREIGN KEY (idFournisseursPieces)
        REFERENCES FournisseursPieces (idFournisseursPieces)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN KEY (idPiece)
        REFERENCES Pieces (idPiece)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS FourniAutomobiles
(
    idFournisseursVehicules int,
    niv                     varchar(17),
    FOREIGN KEY (idFournisseursVehicules)
        REFERENCES FournisseursAutomobiles (idFournisseursVehicules)
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    FOREIGN KEY (niv)
        REFERENCES automobile (niv)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
);



#intercept un insert d'un numero de telephone identique dans le tableau FournisseursAutomobiles
DELIMITER //
CREATE TRIGGER FournisseursAutomobilesDup
    BEFORE INSERT ON FournisseursAutomobiles
    FOR EACH ROW
    BEGIN
        IF (SELECT numTelephoneFournisseursVehicules
            FROM FournisseursAutomobiles
            WHERE numTelephoneFournisseursVehicules = NEW.numTelephoneFournisseursVehicules)
        THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Vous avez deja un fournisseur avec ce numero de telephone';
        end if ;
    end //
#test
# insert into fournisseursautomobiles (nomFournisseursVehicules, adresseFournisseursVehicules, numTelephoneFournisseursVehicules, adresseCourrielFournisseursVehicules, villeFournisseursVehicules, provinceEtatFournisseursVehicules, paysFournisseursVehicules) VALUES ('Noé Dubois','21 Rue des Cerisiers','819-555-0492','noe.dubois@business.com','Rouyn-Noranda','Québec','Canada');


#intercept un insert d'un numero de telephone identique dans le tableau FournisseursPieces
DELIMITER //
CREATE TRIGGER FournisseursPiecesDup
    BEFORE INSERT ON FournisseursPieces
    FOR EACH ROW
    BEGIN
        IF (SELECT numTelephoneFournisseursPieces
            FROM FournisseursPieces
            WHERE numTelephoneFournisseursPieces = NEW.numTelephoneFournisseursPieces)
        THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Vous avez deja un fournisseur avec ce numero de telephone';
        end if ;
    end //
#test
# INSERT INTO FournisseursPieces      (nomFournisseursPieces, adresseFournisseursPieces, numTelephoneFournisseursPieces, adresseCourrielFournisseursPieces, villeFournisseursPieces, provinceEtatFournisseursPieces, paysFournisseursPieces) VALUES ('Sophie ','4848 Rue Sherbrooke','819-555-5678','sophie.thibault@business.com','Sherbrooke','Québec','Canada');




#procedure que le boss utilise pour voir les piece qu'il a acheté
drop procedure IF EXISTS statistics;

DELIMITER //

CREATE PROCEDURE statistics(IN timeframe varchar(10), in VoirIDPiece integer (1), in VoirNomPiece integer(1), in VoirDescription integer(1), in VoirPrix integer(1), in Voircategorie integer(1), in VoirpoidsPiece integer(1), in VoirdatePiece integer(1))
BEGIN
    DECLARE now_date DATE;
    DECLARE last_week DATE;
    DECLARE last_month DATE;
    DECLARE last_trimester DATE;
    DECLARE last_semester DATE;
    DECLARE last_year DATE;
    DECLARE all_date DATE;

    SET now_date := UTC_DATE();
    SET last_week := DATE_SUB(now_date, INTERVAL 7 DAY);
    SET last_month := DATE_SUB(now_date, INTERVAL 1 MONTH);
    SET last_trimester := DATE_SUB(now_date, INTERVAL 3 MONTH);
    SET last_semester := DATE_SUB(now_date, INTERVAL 6 MONTH);
    SET last_year := DATE_SUB(now_date, INTERVAL 1 YEAR);
    SET all_date := DATE_SUB(now_date, INTERVAL 6 YEAR);

    DROP TEMPORARY TABLE IF EXISTS date;
    CREATE TEMPORARY TABLE IF NOT EXISTS date LIKE Pieces;

    IF timeframe = 'semaine' THEN
        INSERT INTO date SELECT * FROM Pieces P WHERE P.datePiece BETWEEN last_week AND now_date;
    ELSEIF timeframe = 'mois' THEN
        INSERT INTO date SELECT * FROM Pieces P WHERE P.datePiece BETWEEN last_month AND now_date;
    ELSEIF timeframe = 'year' THEN
        INSERT INTO date SELECT * FROM Pieces P WHERE P.datePiece BETWEEN last_year AND now_date;
    END IF;

    IF VoirIDPiece = 0 THEN
        ALTER TABLE date
            DROP COLUMN idPiece;
    end if;

    IF VoirNomPiece = 0 THEN
        ALTER TABLE date
            DROP COLUMN nomPiece;
    end if;

    IF Voircategorie = 0 THEN
        ALTER TABLE date
            DROP COLUMN categorie;
    end if;

    IF VoirpoidsPiece = 0 THEN
        ALTER TABLE date
            DROP COLUMN poidsPiece;
    end if;

    IF VoirDescription = 0 THEN
        ALTER TABLE date
            DROP COLUMN descriptionPiece;
    end if;

     IF VoirPrix = 0 THEN
        ALTER TABLE date
            DROP COLUMN prixPiece;
    end if;

     IF VoirdatePiece = 0 THEN
        ALTER TABLE date
            DROP COLUMN datePiece;
    end if;

    SELECT * from date;
END //

DELIMITER ;

#TEST
# call statistics('semaine', 0, 0, 0, 0, 0, 0, 0);
# call statistics('mois', 0, 0, 0, 0, 0, 0, 0);
# call statistics('year', 0, 0, 0, 0, 0, 0, 0);



#deuxieme version de la procedure precendente avec des commentaires.


DROP PROCEDURE IF EXISTS statisticsPieces;
DELIMITER //
    -- this procedures takes in 7 inputs. The first will be the desired timeframe and the 6 others are the colums we want to see in the Pieces table. Creates a Temporary table called Date.
CREATE PROCEDURE statisticsPieces(IN timeframe VARCHAR(10), IN VoirIDPiece integer(1), IN VoirNomPiece integer(1),
                             IN VoirDescription integer(1), IN VoirPrix integer(1), IN Voircategorie integer(1),
                             IN VoirpoidsPiece integer(1), IN VoirdatePiece integer(1))
BEGIN
    -- Declare the variables that will be used to choose the desired timeframe.
    DECLARE now_date, last_week, last_month, last_trimester, last_semester, last_year, all_date DATE;
    SET now_date := UTC_DATE(), last_week := DATE_SUB(now_date, INTERVAL 7 DAY), last_month := DATE_SUB(now_date, INTERVAL 1 MONTH),
        last_trimester := DATE_SUB(now_date, INTERVAL 3 MONTH), last_semester := DATE_SUB(now_date, INTERVAL 6 MONTH),
        last_year := DATE_SUB(now_date, INTERVAL 1 YEAR), all_date := DATE_SUB(now_date, INTERVAL 10 YEAR);

    -- Drops the temporary "date" table if it exists, then creates it as a copy of the "Pieces" table.
    DROP TEMPORARY TABLE IF EXISTS date;
    CREATE TEMPORARY TABLE IF NOT EXISTS date LIKE Pieces;

    -- Inserts rows from the "Pieces" table into the "date" table based on the selected timeframe.
    INSERT INTO date
    SELECT *
    FROM Pieces P
    WHERE (timeframe = 'semaine' AND P.datePiece BETWEEN last_week AND now_date)
       OR (timeframe = 'mois' AND P.datePiece BETWEEN last_month AND now_date)
       OR (timeframe = 'year' AND P.datePiece BETWEEN last_year AND now_date)
       OR (timeframe = 'all' AND P.datePiece BETWEEN all_date AND now_date);

    -- Drops columns from the "date" table based on the input parameters.
    IF VoirIDPiece = 0 THEN ALTER TABLE date
        DROP COLUMN idPiece;
    END IF;
    IF VoirNomPiece = 0 THEN ALTER TABLE date
        DROP COLUMN nomPiece;
    END IF;
    IF Voircategorie = 0 THEN ALTER TABLE date
        DROP COLUMN categorie;
    END IF;
    IF VoirpoidsPiece = 0 THEN ALTER TABLE date
        DROP COLUMN poidsPiece;
    END IF;
    IF VoirDescription = 0 THEN ALTER TABLE date
        DROP COLUMN descriptionPiece;
    END IF;
    IF VoirPrix = 0 THEN ALTER TABLE date
        DROP COLUMN prixPiece;
    END IF;
    IF VoirdatePiece = 0 THEN ALTER TABLE date
        DROP COLUMN datePiece;
    END IF;

    -- Selects all columns from the "date" table and returns the result.
    SELECT * FROM date;

END //
DELIMITER ;

#test with statisticsPieces
#
call statisticsPieces('all', 1, 1, 0, 1, 1, 1, 1);
# call statisticsPieces('mois', 0, 0, 0, 0, 0, 0, 0);
# call statisticsPieces('year', 0, 0, 0, 0, 0, 0, 0);

