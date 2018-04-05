/* file to create and test SQL queries*/

/*Query Name All: retrieve all information in Genbank Table*/
SELECT *
FROM TABLE genbank_data;

/*Query Name Summary: retrieve all information in Genbank Table for a given gene name*/
SELECT * 
FROM TABLE genbank_data gd
WHERE      gd.gene      LIKE %(input)%
        OR gd.accession LIKE %(input)%
        OR gd.prot_id   LIKE %(input)%
        OR gd.prot_name LIKE %(input)%
        OR gd.map_coord LIKE %(input)%;
        

/*Query Name Details: retrieve all information in Genbank Table for a given gene name*/
SELECT gd.*, sd.seqence_dna, sd.seqence_prot, et.coods, et.len, et.start
FROM TABLE genbank_data gd, seqence_data sd, exon_transf et
WHERE      gd.gene      LIKE %(input)%
        OR gd.accession LIKE %(input)%
        OR gd.prot_id   LIKE %(input)%
        OR gd.prot_name LIKE %(input)%
        OR gd.map_coord LIKE %(input)%;

/*Query Name Populate: collect codon usage data from BL and populate gen_code table*/
ALTER TABLE gen_code ADD codon_stats FLOAT DEFAULT 0;
INSERT INTO gen_code
VALUES %(input);


/*placeholder for querry needed to fetch the written usage data*/