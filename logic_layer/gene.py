from .errors import ExonsNotMatchingException
from .utils import location_to_int
from .codons import codontable, aminoacidtable


class Gene:
    def __init__(self, gene_id, protein_name, accession, location, codon_start,
                 cds_locations, dna_seq_whole, aa_seq, num_exons):
        # Initialiaze data
        self.gene_id = gene_id
        self.protein_name = protein_name
        self.accession = accession
        self.location = location
        self.codon_start = codon_start
        self.cds_locations = cds_locations
        self.dna_seq_whole = dna_seq_whole
        self.aa_seq = aa_seq
        self.num_exons = num_exons

        # Run calculations
        self.identify_coding_regions()
        self.align_dna_amino()

    def identify_coding_regions(self):
        # Check if we have all the exons
        if self.num_exons is not len(self.cds_locations):
            raise ExonsNotMatchingException

        # Convert cds locations to numbers
        locations = []

        for cds_location in self.cds_locations:
            try:
                locations.append((location_to_int(cds_location)))
            except Exception:
                print('{} failed to convert to int'.format(cds_location))

        # Find coding region
        coding_regions = []
        for loc in locations:
            coding_seq = self.dna_seq_whole[loc[0] - 1:loc[1]]
            coding_regions.append(coding_seq)

        self.coding_regions = coding_regions
        # Store coding sequence
        self.coding_sequence = ''.join(coding_regions)
    
    def align_dna_amino(self):
        start = self.codon_start - 1
        s = self.coding_sequence[start:]
        split_seq = [s[i:i + 3] for i in range(0, len(s), 3)]
        dna_to_aa = []

        for i, v in enumerate(split_seq):
            try:
                dna = split_seq[i]
                amino = codontable[dna.upper()]
                amino_min = aminoacidtable[amino.upper()]
    
                if i >= len(self.aa_seq):
                    # print('{}: {}: {} is last codon'.format(i, dna, amino))
                    break

                aa = self.aa_seq[i]
                dna_to_aa.append({dna: aa})
                if aa is not amino_min:
                    print('érror')
                # print('{}: {}: {}: {}: {}'.format(i, dna, aa, amino_min,
                #                                   amino))
            except IndexError as e:      
                print('Seq: {} doesnt have AA'.format(dna))

    def remove_stop_codons(self, seq):
        return [item for item in seq if item not in stop_codon]