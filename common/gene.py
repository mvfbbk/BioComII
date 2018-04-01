class Gene:
    def __init__(self,
                 gene_id,
                 protein_name,
                 accession,
                 location,
                 num_exons=None):
        self.gene_id = gene_id
        self.protein_name = protein_name
        self.accession = accession
        self.location = location
