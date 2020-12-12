#!/bin/bash

rm -f ../src/signal.vhd
rm -f ../src/tree.vhd
rm -f ../src/matrice.txt
rm -f ../src/intro.vhd
rm -f ../src/final_stage.vhd

python3 write_intro.py
python3 dadda_tree.py

cat ../src/intro.vhd ../src/signal.vhd ../src/tree.vhd ../src/final_stage.vhd > ../src/dadda_tree.vhd

rm ../src/intro.vhd ../src/signal.vhd ../src/tree.vhd ../src/final_stage.vhd


