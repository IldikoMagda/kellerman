################CreateDatabaseSchema

CREATE TABLE Kinase (
    kinase_name VARCHAR(255) NOT NULL,
    gene_name VARCHAR(50) NOT NULL,
    cell_location VARCHAR(255) NOT NULL,
    family VARCHAR(255) NOT NULL,
    protein_group VARCHAR(255) NOT NULL,
    phosphosite_location INT,
    protein_image VARCHAR(255) NOT NULL,
    PRIMARY KEY (kinase_name)
);
    
CREATE TABLE Inhibitor (
    inhibitor_name VARCHAR(255) NOT NULL,
    chemical_structure VARCHAR(255) NOT NULL, 
    kinase_name VARCHAR(255) NOT NULL,
    class VARCHAR(255) NOT NULL,
    PRIMARY KEY (inhibitor_name)
);

CREATE TABLE Phosphosite (
    chromosome VARCHAR(150) NOT NULL,
    phosphosite_location INT,
    kinase_name VARCHAR(255) NOT NULL,
    neighbouring_seq VARCHAR(500) NOT NULL,
    PRIMARY KEY (phosphosite_location),
    FOREIGN KEY (kinase_name) REFERENCES Kinase(kinase_name)
);

CREATE TABLE Kinase_Inhibitor_Relation (
    inhibitor VARCHAR(255) NOT NULL,
    kinase VARCHAR(255) NOT NULL,
    FOERIGN KEY (inhibitor) REFERENCES Inhibitor(inhibitor_name)
    FOERIGN KEY (kinase) REFERENCES Kinase(kinase_name)
);
    
    

