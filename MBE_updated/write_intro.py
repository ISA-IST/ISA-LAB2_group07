f = open("intro.vhd", 'w')

f.write("\nLIBRARY ieee;\nUSE ieee.std_logic_1164.all;\n")
f.write("USE ieee.std_logic_arith.all;\n\nENTITY dadda_tree IS\n")
f.write("PORT (\n\tpp0, pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9,\n")
f.write("\tpp10, pp11, pp12, pp13, pp14, pp15: IN STD_LOGIC_VECTOR(32 downto 0);\n")
f.write("\tpp16: IN STD_LOGIC_VECTOR(31 downto 0);\n")
f.write("\taddend1_out, addend2_out: OUT STD_LOGIC_VECTOR(62 downto 0);\n")
f.write("\tM_lsb: OUT STD_LOGIC\n);\nEND dadda_tree;\n\n")
f.write("ARCHITECTURE struct OF dadda_tree IS\n")
f.write("\nCOMPONENT FA IS\nPORT(\n\ta, b, c_in : IN std_logic;\n")
f.write("\t	s, c_out : OUT std_logic);\nEND COMPONENT;\n\nCOMPONENT HA IS\n")
f.write("PORT(\n\ta, b : IN std_logic;\n\t	s, c_out : OUT std_logic);\nEND COMPONENT;\n")

f.close()
