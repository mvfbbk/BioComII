from ..common.validations import validate_gene_id
from ..data_layer import api
from ..common.gene import Gene


def get_all():
    return api.get_all()


def search(parameter):
    pass


def get_by_gene_id(gene_id):

    validate_gene_id(gene_id)
    gene = api.get_by_gene_id(gene_id)
    g1 = Gene(
        gene_id=gene['gene_id'],
        accession=gene['accession'],
        protein_name=gene['protein_name'],
        location=gene['location'])

