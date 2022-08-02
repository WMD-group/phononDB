import os
from pymatgen.core import Structure
from monty.serialization import dumpfn

# Get the material ids
db_dir = 'phonon_db'
phonon_dirs = os.listdir(db_dir)

# Validate if the extraction has been
if len(phonon_dirs)<1:
    print("Follow the setup guide in order. You haven't extracted yet")

mp_ids = [dirs.split('-20180417')[0] for dirs in phonon_dirs]

# Load the unit cells used in the phonopy calculations
structures = [Structure.from_file(filename=f'{db_dir}/{dirs}/POSCAR-unitcell') for dirs in phonon_dirs]

# Create lists for the elements and compositions
compositions = [s.compositions for s in structures]
elements = [s.composition.elements for s in structures]

# Begin getting the data we need

# Get the element symbols
els_symbols =[]
for els in elements:
    els_symbols.append(el.symbol for el in els)

#Get the formula
formula_pretty_reduced = [c.reduced_formula for c in compositions]
formula = [c.formula for c in compositions]

# Get the num_elements
num_elements = [len(els) for els in elements]

# Get the natoms
natoms = [int(s.composition.num_atoms) for s in structures]

# Get the chemsys
chemsys = [c.chemical_system for c in compositions]

# Get the spacegroup
spacegroup = [s.get_space_group_info() for s in structures]
spacegroup_symbol = [sg[0] for sg in spacegroup]
spacegroup_number = [sg[1] for sg in spacegroup]

# Get the relative FORCE_SETS filepath
FS_filepath = [f'{db_dir}/{phonon_dir}/FORCE_SETS' for phonon_dir in phonon_dirs]
# Get the relative phonon.yaml filepath
phonon_filepath = [f'{db_dir}/{phonon_dir}/phonon.yaml' for phonon_dir in phonon_dirs]


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

# Dump the dictionary to a json file
dumpfn(info_dict, 'phonon_db_lookup.json')