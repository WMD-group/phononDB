# PhononDB
This repository exists to provide easy access to the Kyoto University phonon database [version 2018-04-17](http://phonondb.mtl.kyoto-u.ac.jp/ph20180417/index.html).

The phonon data are licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) unless otherwise specified on the webpage for that particular phonon calculation.

The phonon database has been web scraped and made available for simple querying for in-depth study.
The scripts have only been tested on MacOS, but should work on Linux too.

# Setup

First, you will need to clone this repository
```
git clone https://github.com/WMD-group/phononDB.git
cd phononDB
```
You will need to install the following packages
* [pymatgen](https://pymatgen.org/installation.html)
* [phonopy](https://phonopy.github.io/phonopy/install.html)

Run `extract_files.sh`, which will iteratively extract the raw data.

Run `create_lookup_json.py` which will create a lookup table to allow querying of the data.

(Optional: run `cleanup.sh` to remove the files and directories which are no longer need (`extract_files.sh` and `phonon_db_tarred`).)

Follow `examples/querying_example.ipynb` to find an example notebook to query the data and use phonopy


# Acknowledgements
The phonon calculation database was created by Atsuhi Togo ([github](https://atztogo.github.io), [Google scholar](https://scholar.google.com/citations?user=z8wRUJAAAAAJ&hl=en)) at Kyoto University.

