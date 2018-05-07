CREATE DATABASE bc_test;
USE bc_test;
CREATE TABLE genbank (accession_number VARCHAR(8) NOT NULL DEFAULT 'N/A', map_coord VARCHAR(9) NOT NULL DEFAULT 'N/A', gene_name VARCHAR(15) NOT NULL DEFAULT 'N/A', start_pos VARCHAR(3) NOT NULL DEFAULT 'N/A', prot VARCHAR(10) NOT NULL DEFAULT 'N/A', prod VARCHAR(50) NOT NULL DEFAULT 'N/A', exon_join VARCHAR(10000) NOT NULL DEFAULT 'N/A', exon_num VARCHAR(5) NOT NULL DEFAULT 'N/A', PRIMARY KEY (accession_number));
CREATE TABLE sequences (accession_number VARCHAR(8) NOT NULL DEFAULT 'N/A', DNA_seq   LONGTEXT   NOT NULL, prot_seq  LONGTEXT   NOT NULL, PRIMARY KEY (accession_number));
CREATE TABLE enzymes (id INT NOT NULL AUTO_INCREMENT, enz_name VARCHAR(20), enz_seq VARCHAR(20), PRIMARY KEY (id));
CREATE TABLE genbankTosequenceToexon(gb_accession VARCHAR(8) NOT NULL DEFAULT 'N/A', seq_accession VARCHAR(8)   NOT NULL DEFAULT 'N/A', PRIMARY KEY CLUSTERED (gb_accession, seq_accession), FOREIGN KEY (gb_accession) REFERENCES genbank ( accession_number ) ON UPDATE  NO ACTION  ON DELETE  CASCADE, FOREIGN KEY (seq_accession) REFERENCES sequences ( accession_number ) ON UPDATE  NO ACTION  ON DELETE  CASCADE);CTION  ON DELETE  CASCADE, FOREIGN KEY (seq_accession) REFERENCES sequences ( accession_number ) ON UPDATE  NO ACTION  ON DELETE  CASCADE);
