from .errors import ExonsNotMatchingException
from .utils import location_to_int, calculate_frequencies
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
        self._identify_coding_regions()
        self._align_dna_amino()
        self._caclucate_frequency()

    def _identify_coding_regions(self):
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

        flat_locations = [l for location in locations for l in location]
        self.coding_region_location_min = min(flat_locations)
        self.coding_region_location_max = max(flat_locations)

        self.coding_regions = coding_regions
        # Store coding sequence
        self.coding_sequence = ''.join(coding_regions)

    def _align_dna_amino(self):
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
                    print('error')
                # print('{}: {}: {}: {}: {}'.format(i, dna, aa, amino_min,
                #                                   amino))
            except IndexError as e:
                print('Seq: {} doesnt have AA'.format(dna))

        self.dna_to_aa = dna_to_aa

    def _caclucate_frequency(self):
        self.codon_frequencies = calculate_frequencies(self.dna_to_aa)

    def find_restriction_enzymes(self, restriction_enzymes_list):
        locations = {}
        res = restriction_enzymes_list
        max_length_re = len(max(res))
        res_list = res

        # find the max length of a restriction enzyme to be used a window
        # when itterating over the sequence
        dna_size = len(self.dna_seq_whole)
        res_found = 0
        useful_locations = {}

        for abs_index in range(dna_size):
            # Read only the window
            seq = self.dna_seq_whole[abs_index:abs_index + max_length_re]

            for re in res_list:
                found_index = seq.lower().find(re.lower())
                if found_index > -1:
                    res_found += 1
                    # calculate location in whole
                    loc = abs_index + found_index
                    # use composite key to avoid duplicates
                    key = '{}{}'.format(re, loc)
                    value = {re: loc}

                    locations[key] = value

                    # check if location is within the coding region
                    if (loc < self.coding_region_location_min
                            and loc + len(re) < self.coding_region_location_min
                        ) or (loc > self.coding_region_location_max and
                              loc + len(re) > self.coding_region_location_max):
                        useful_locations[key] = value

        self.all_restriction_enzymes = locations.values()
        self.useful_restriction_enzymes = useful_locations.values()

        return self.all_restriction_enzymes, self.useful_restriction_enzymes