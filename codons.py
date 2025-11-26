def create_codon_dict(file_path):
  dict_codon_to_amino = {}

  with open(file_path, 'r') as file:
    rows = file.readlines()
    for row in rows:
      row_cells = row.strip().split('\t')
      codon = row_cells[0]
      amino_acid = row_cells[2]
      dict_codon_to_amino[codon] = amino_acid
  
  return dict_codon_to_amino


