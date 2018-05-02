/*selecting the database*/

USE bc_test;

/*SQL script to generate the genbank table in the database*/

CREATE TABLE genbank
(
    accession_number VARCHAR(8) NOT NULL DEFAULT 'N/A',
    gene_name VARCHAR(8) NOT NULL DEFAULT 'N/A',
    map_coord VARCHAR(9) NOT NULL DEFAULT 'N/A',
    EC_num VARCHAR(8) NOT NULL DEFAULT 'N/A',
    prot VARCHAR(10) NOT NULL DEFAULT 'N/A',
    prod VARCHAR(50) NOT NULL DEFAULT 'N/A',
    PRIMARY KEY (accession_number)
 );

/*SQL script to generate the sequences table in the database*/

CREATE TABLE sequences 
(
    id        INT        NOT NULL AUTO_INCREMENT,
    accession_number VARCHAR(8) NOT NULL DEFAULT 'N/A',
    DNA_seq   LONGTEXT   NOT NULL,
    prot_seq  LONGTEXT   NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (accession_number) REFERENCES genbank(accession_number)
);

/*SQL script to generate the exon data table in the database*/

CREATE TABLE exon_data (
    id                 INT          NOT NULL AUTO_INCREMENT,
    accession_number   VARCHAR(8)   NOT NULL DEFAULT 'N/A',
    exon_num           INT          NOT NULL DEFAULT 0,
    exon_coords        VARCHAR(255) NOT NULL DEFAULT 'N/A',
    exon_len           INT          NOT NULL DEFAULT 0,
    PRIMARY KEY (id),
    FOREIGN KEY (accession_number) REFERENCES genbank(accession_number)
);

/*SQL script to generate the universal code table in the database*/

CREATE TABLE u_code 
(
    id          INT         NOT NULL AUTO_INCREMENT,
    codon ENUM('ATT', 'ATC', 'ATA', 'CTT', 'CTC', 'CTA', 'CTG', 'TTA', 
    'TTG', 'GTT', 'GTC', 'GTA', 'GTG', 'TTT', 'TTC', 'TGT', 'TGC', 'GCT', 
    'GCC', 'GCA', 'GCG', 'GGT', 'GGC', 'GGA', 'GGG', 'CCT', 'CCC', 'CCA', 
    'CCG', 'ACT', 'ACC', 'ACA', 'ACG', 'TCT', 'TCC', 'TCA', 'TCG', 'AGT', 
    'AGC', 'TAT', 'TAC', 'TGG', 'CAA', 'CAG', 'AAT', 'AAC', 'CAT', 'CAC', 
    'GAA', 'GAG', 'GAT', 'GAC', 'AAA', 'AAG', 'CGT', 'CGC', 'CGA', 'CGG', 
    'AGA', 'AGG', 'TAA', 'TAG', 'TGA', 'NNN') DEFAULT 'NNN',
    3_letter_AA ENUM('Ala', 'Cys', 'Asp', 'Glu', 'Phe', 'Gly', 'His', 
    'Ile', 'Lys', 'Met', 'Asn', 'Pro', 'Gln', 'Arg', 'Ser', 'Thr', 'Val', 
    'Trp', 'Tyr', 'Stop') NOT NULL DEFAULT 'Stop',
    1_letter_AA ENUM('A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 
    'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'X') DEFAULT 'X',
    codon_stat FLOAT NOT NULL DEFAULT 0.00,
    PRIMARY KEY (id)
)

