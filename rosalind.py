def count_nucleotides(dna_string):
    # Count occurrences of each nucleotide
    a_count = dna_string.count('A')
    c_count = dna_string.count('C')
    g_count = dna_string.count('G')
    t_count = dna_string.count('T')
    
    # Print the counts in the required format
    print(a_count, c_count, g_count, t_count)

# Sample input
dna_string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
count_nucleotides(dna_string)
