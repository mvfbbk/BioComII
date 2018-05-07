import json
from glob import glob

from dummy_data.utils import read_enzymes


def get_all():
    return [{
        'gene_id': 'CBR',
        'accenssion': 'AB1234',
        'protein_name': 'carbon_ill',
        'location': '56080..59221'
    }, {
        'gene_id': 'CBR',
        'accenssion': 'AB1234',
        'protein_name': 'carbon_ill',
        'location': '56080..59221'
    }, {
        'gene_id': 'CBR',
        'accenssion': 'AB1234',
        'protein_name': 'carbon_ill',
        'location': '56080..59221'
    }]


def search(param):
    return [{
        'gene_id': 'CBR',
        'accenssion': 'AB1234',
        'protein_name': 'carbon_ill',
        'location': '56080..59221'
    }, {
        'gene_id': 'CBR',
        'accenssion': 'AB1234',
        'protein_name': 'carbon_ill',
        'location': '56080..59221'
    }, {
        'gene_id': 'CBR',
        'accenssion': 'AB1234',
        'protein_name': 'carbon_ill',
        'location': '56080..59221'
    }]


def get_by_gene_id(id):
    with open('dummy_data/gene_{}.json'.format(id)) as f:
        gene_data = json.load(f)

    return gene_data


def get_all_genes():
    results = []
    files = glob('dummy_data/gene_*.json')

    for file in files:
        with open(file) as f:
            gene_data = json.load(f)
            results.append(gene_data)

    return results


def get_restriction_enzymes():
    return read_enzymes('dummy_data/enzymes.csv')

