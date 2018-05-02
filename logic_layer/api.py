from .gene import Gene
from .validations import validate_gene_id
from data_layer import api

from .errors import NoGeneException


def get_all():
    return api.get_all()


def search(parameter):
    return api.search(parameter)


def get_by_gene_id(gene_id):
    if gene_id is None:
        raise NoGeneException

    validate_gene_id(gene_id)
    # Get gene from the database layer
    gene = api.get_by_gene_id(gene_id)

    g1 = Gene(
        gene_id=gene['gene_id'],
        accession=gene['accession'],
        protein_name=gene['protein_name'],
        location=gene['location'],
        codon_start=gene['codon_start'],
        cds_locations=gene['cds_locations'],
        dna_seq_whole=gene['dna_seq_whole'],
        aa_seq=gene['aa_seq'],
        num_exons=gene['num_exons'],
        )
    return g1 
