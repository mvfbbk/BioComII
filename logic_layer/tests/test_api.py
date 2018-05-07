import unittest

from .. import api, errors


class TestApi(unittest.TestCase):
    def test_get_all(self):
        data = api.get_all()
        self.assertGreater(len(data), 0)

    def test_get_gene_by_id_success(self):
        gene = api.get_by_gene_id(1)
        self.assertIsNotNone(gene)
        self.assertIsNotNone(gene.gene_id)
        self.assertIsNotNone(gene.accession)
        self.assertIsNotNone(gene.protein_name)
        self.assertIsNotNone(gene.location)
        self.assertIsNotNone(gene.coding_regions)
        self.assertIsNotNone(gene.coding_sequence)
        self.assertIsNotNone(gene.aa_seq)
        # self.assertEqual(len(gene.coding_sequence)/3, len(gene.aa_seq))
        # print(gene.coding_sequence)


    def test_get_gene_by_id_fail(self):
        with self.assertRaises(errors.NoGeneException):
            api.get_by_gene_id(None)