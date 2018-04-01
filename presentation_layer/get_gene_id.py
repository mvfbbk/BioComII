from ..logic_layer import api


def get_gene_id(id):
    return api.get_by_gene_id(id)
