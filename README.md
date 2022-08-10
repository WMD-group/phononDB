# PhononDB
<h2 align="center">:exclamation: NOTICE :exclamation:</h2>
A MongoDB implementation of this dataset is currently being worked on and will be hosted remotely. The current implementation described below will make a local installation of the 10,034 phonon calculations on your device. I recommend that you have at least 2.5GB of free storage for full installation of the extracted data.

# Introduction
This repository exists to provide easy access to the Kyoto University phonon database [version 2018-04-17](http://phonondb.mtl.kyoto-u.ac.jp/ph20180417/index.html).

The phonon data are licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) unless otherwise specified on the webpage for that particular phonon calculation.

The phonon database has been web scraped and made available for simple querying for in-depth study.
The scripts have only been tested on MacOS and RHEL, but should work on other Linux distributions too.


# Setup

First, you will need to clone this repository
```
git clone https://github.com/WMD-group/phononDB.git
cd phononDB
```
You will need to install the following packages
* [pymatgen](https://pymatgen.org/installation.html)
* [phonopy](https://phonopy.github.io/phonopy/install.html)

Run `extract_files_*.sh`, which will iteratively extract the raw data.
* `extract_files_mac.sh` has been tested to work on MacOS
* `extract_files_linux.sh` has been tested to work on RHEL (Linux)

Run `create_lookup_json.py` which will create a lookup table to allow querying of the data.

(Optional: run `cleanup.sh` to remove the files and directories which are no longer need (`extract_files.sh` and `phonon_db_tarred`).)

Follow `examples/querying_example.ipynb` to find an example notebook to query the data and use phonopy


# Acknowledgements
The phonon calculation database was created by Atsuhi Togo ([github](https://atztogo.github.io), [Google scholar](https://scholar.google.com/citations?user=z8wRUJAAAAAJ&hl=en)) at Kyoto University.

