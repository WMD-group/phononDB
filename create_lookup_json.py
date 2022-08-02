import os
from pymatgen.core import Structure
from monty.serialization import dumpfn
from tqdm import tqdm
import pandas as pd

# Get the material ids
db_dir = 'phonon_db'
phonon_dirs = os.listdir(db_dir)

# Validate if the extraction has been
if len(phonon_dirs)<1:
    print("Follow the setup guide in order. You haven't extracted yet")

print('Creating a list of material-ids')
mp_ids = [dirs.split('-20180417')[0] for dirs in tqdm(phonon_dirs)]
print('Done.')

# Load the unit cells used in the phonopy calculations
print('Loading in the unit cell information for processing')
structures = [Structure.from_file(filename=f'{db_dir}/{dirs}/POSCAR-unitcell') for dirs in tqdm(phonon_dirs)]
print('Done.')


# Create lists for the elements and compositions
print('Starting to process structures to obtain the data')
compositions = [s.composition for s in structures]
elements = [s.composition.elements for s in structures]

# Begin getting the data we need

# Get the element symbols
els_symbols =[]
for els in elements:
    els_symbols.append(el.symbol for el in tqdm(els))

#Get the formula
formula_pretty_reduced = [c.reduced_formula for c in tqdm(compositions)]
formula = [c.formula for c in tqdm(compositions)]

# Get the num_elements
num_elements = [len(els) for els in tqdm(elements)]

# Get the natoms
natoms = [int(s.composition.num_atoms) for s in tqdm(structures)]

# Get the chemsys
chemsys = [c.chemical_system for c in tqdm(compositions)]

# Get the spacegroup
spacegroup = [s.get_space_group_info() for s in tqdm(structures)]
spacegroup_symbol = [sg[0] for sg in tqdm(spacegroup)]
spacegroup_number = [sg[1] for sg in tqdm(spacegroup)]

# Get the relative FORCE_SETS filepath
FS_filepath = [f'{db_dir}/{phonon_dir}/FORCE_SETS' for phonon_dir in tqdm(phonon_dirs)]
# Get the relative phonon.yaml filepath
phonon_filepath = [f'{db_dir}/{phonon_dir}/phonon.yaml' for phonon_dir in tqdm(phonon_dirs)]

print('Data has been processed')


# Create a dictionary
info_dict = {'material_id':mp_ids,
            'elements': els_symbols,
            'formula_pretty_reduced':formula_pretty_reduced,
            'formula': formula,
            'num_elements': num_elements,
            'chemsys': chemsys,
            'spacegroup_symbol': spacegroup_symbol,
            'spacegroup_number': spacegroup_number,
            'FORCE_SETS_filepath': FS_filepath,
            'phonon_filepath': phonon_filepath }

# Dump the dataframe to a json file
df = pd.DataFrame(info_dict)
print('Dumping the dataframe to a json.')
dumpfn(df, 'phonon_db_lookup.json')