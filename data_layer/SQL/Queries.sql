/*SQL queries*/

/*Query Name All: retrieve all information in Genbank Table*/

SELECT *
FROM genbank gb 
WHERE gb.gene_name              != 'N/A' 
        AND gb.accession_number != 'N/A' 
        AND gb.prot             != 'N/A' 
        AND gb.prod             != 'N/A' 
        AND gb.map_coord        != 'N/A';

/*Query Name DB_Wide: retrieve all sequences and information in Genbank Table*/

SELECT gb.*, s.DNA_seq, s.prot_seq 
FROM genbank gb, sequences s
WHERE gb.gene_name              != 'N/A' 
        AND gb.accession_number != 'N/A' 
        AND gb.prot             != 'N/A' 
        AND gb.prod             != 'N/A' 
        AND gb.map_coord        != 'N/A';

/*Query Name Summary: retrieve all information in Genbank Table for a given gene name*/

SELECT * 
FROM genbank gb 
WHERE gb.accession_number = '%s' 
        OR gb.gene_name   = '%s' 
        OR gb.prot        = '%s' 
        OR gb.map_coord   = '%s' 
        OR gb.prod        = '%s';
        

/*Query Name Details: retrieve all information in Genbank Table for a given gene name*/
SELECT gd.*, sd.seqence_dna, sd.seqence_prot, et.coods, et.len, et.start
FROM TABLE genbank_data gd, seqence_data sd, exon_transf et
WHERE      gd.gene      LIKE '%s'
        OR gd.accession LIKE '%s'
        OR gd.prot_id   LIKE '%s'
        OR gd.prot_name LIKE '%s'
        OR gd.map_coord LIKE '%s';
