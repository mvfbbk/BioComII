import unittest

from data_layer import fake_api

from .. import errors
from ..api import LogicApi


class TestApi(unittest.TestCase):
    def setup_class(self):
        self.api = LogicApi(data_api=fake_api)

    def test_get_all(self):
        data = self.api.get_all()
        self.assertGreater(len(data), 0)

    def test_get_gene_by_id_success(self):
        gene = self.api.get_by_gene_id('cbr')

        self.assertIsNotNone(gene)
        self.assertIsNotNone(gene.gene_id)
        self.assertIsNotNone(gene.accession)
        self.assertIsNotNone(gene.protein_name)
        self.assertIsNotNone(gene.location)
        self.assertIsNotNone(gene.coding_regions)
        self.assertIsNotNone(gene.coding_sequence)
        self.assertIsNotNone(gene.aa_seq)
        self.assertIsNotNone(gene.codon_frequencies)
        self.assertIsNotNone(gene.coding_region_location_min)
        self.assertIsNotNone(gene.coding_region_location_max)

    def test_get_gene_by_id_with_re_success(self):
        gene = self.api.get_by_gene_id('ccr5')
        a, u = gene.find_restriction_enzymes(['GAATTC'])
        
        self.assertIsNotNone(gene.all_restriction_enzymes)
        self.assertIsNotNone(gene.useful_restriction_enzymes)

    def test_get_gene_by_id_with_re_all_success(self):
        gene = self.api.get_gene_with_restriction_enzymes('ccr5')

        self.assertIsNotNone(gene.all_restriction_enzymes)
        self.assertIsNotNone(gene.useful_restriction_enzymes)

    def test_get_gene_by_id_fail(self):
        with self.assertRaises(errors.NoGeneException):
            self.api.get_by_gene_id(None)

    def test_get_overal_codon_frequencies(self):
        freqs = self.api.get_overall_codon_frequencies()
        self.assertIsNotNone(freqs)
