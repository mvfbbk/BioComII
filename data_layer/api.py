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
    with open('dummy_data/dna_seq_whole.txt') as f:
        dna_whole = f.read()
    with open('dummy_data/aa_seq.txt') as f:
        aa_seq = f.read()
    return {
        'gene_id': 'CBR',
        'accession': 'AB003151',
        'protein_name': 'carbonyl reductase',
        'location': '56080..59221',
        'codon_start': 1,
        'cds_locations': ['56173..56461', '57007..57114', '58503..58939'],
        'dna_seq_whole': dna_whole,
        'aa_seq': aa_seq,
        'num_exons': 3,
    }


def get_restriction_enzymes():
    return {
        'EcoRI': '',
        'BAmHI': '',
        'BsuMI': '',
    }


def save_codon_freq_gene():
    pass


def save_codon_freq_whole():
    pass