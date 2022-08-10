#!/bin/bash
# untar all the phonon data
mkdir phonon_db
FILES="phonon_db_tarred/*.lzma"

for f in $FILES
do
    echo "Processing $f file"
    tar --lzma -xvpf $f --directory phonon_db
done