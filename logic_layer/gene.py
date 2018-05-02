from .errors import ExonsNotMatchingException
from .utils import location_to_int


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

    def identify_coding_regions(self):
        # Check if we have all the exons
        if self.num_exons is not len(self.cds_locations):
            raise ExonsNotMatchingException

        # Convert cds locations to numbers
        locations = []

        for cds_location in self.cds_locations:
            try:
                a, b = location_to_int(cds_location)
                locations.append((a, b))
            except Exception:
                print('{} failed to convert to int'.format(cds_location))
        
        # Find coding region
        coding_regions = []
        for loc in locations:
            coding_seq = self.dna_seq_whole[loc[0]:loc[1]]
            coding_regions.append(coding_seq)
        
        self.coding_regions = coding_regions
