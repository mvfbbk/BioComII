import json
import os

from .errors import NoGeneException
from .gene import Gene
from .utils import calculate_frequencies
from .validations import validate_gene_id


class LogicApi:
    def __init__(self, data_api):
        self.data_api = data_api

    def get_all(self):
        return self.data_api.get_all()

    def search(self, parameter):
        return self.data_api.search(parameter)

    def get_by_gene_id(self, gene_id):
        if gene_id is None:
            raise NoGeneException

        validate_gene_id(gene_id)
        # Get gene from the database layer
        gene = self.data_api.get_by_gene_id(gene_id)

        return self._gene_dict_to_gene(gene)

    def get_overall_codon_frequencies(self):
        genes = self.data_api.get_all_genes()
        dna_to_aa_all = []
        data = {}

        try:
            with open('./data/overall_frequencies.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError as e:
            print(e)

        if len(data) is not 0:
            return data

        for gene_dict in genes:
            g = self._gene_dict_to_gene(gene_dict)
            dna_to_aa_all = dna_to_aa_all + g.dna_to_aa

        overall_freq = calculate_frequencies(dna_to_aa_all)
        
        try:
            os.mkdir('./data')
        except FileExistsError:
            pass

        try:
            with open('./data/overall_frequencies.json', 'w') as f:
                json.dump(overall_freq, f)
        except Exception as e:
            print(e)

        return overall_freq

    def get_gene_with_restriction_enzymes(self, gene_id,
                                          restriction_enzymes_list=None):
        if gene_id is None:
            raise NoGeneException

        if restriction_enzymes_list is None:
            res = self.data_api.get_restriction_enzymes()
        else:
            res = restriction_enzymes_list

        gene = self.get_by_gene_id(gene_id)
        gene.find_restriction_enzymes(res)

        return gene

    def get_restriction_enzymes(self):
        return self.data_api.get_restriction_enzymes()

    def _gene_dict_to_gene(self, gene_dict):
        return Gene(
            gene_id=gene_dict['gene_id'],
            accession=gene_dict['accession'],
            protein_name=gene_dict['protein_name'],
            location=gene_dict['location'],
            codon_start=gene_dict['codon_start'],
            cds_locations=gene_dict['cds_locations'],
            dna_seq_whole=gene_dict['dna_seq_whole'],
            aa_seq=gene_dict['aa_seq'],
            num_exons=gene_dict['num_exons'],
        )
