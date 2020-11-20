#!/bin/bash

rm -f signal.vhd
rm -f tree.vhd
rm -f matrice.txt
rm -f intro.vhd
rm -f final_stage.vhd

python3 write_intro.py
python3 dadda_tree.py

cat intro.vhd signal.vhd tree.vhd final_stage.vhd > dadda_tree.vhd

# rm intro.vhd signal.vhd tree.vhd final_stage.vhd


