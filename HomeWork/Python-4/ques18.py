# Sort by Length then Alphabetically

terms = ["cell", "organism", "dna", "gene"]

# output: ['dna', 'cell', 'gene', 'organism']



terms = sorted(terms, key=len)
print(terms)