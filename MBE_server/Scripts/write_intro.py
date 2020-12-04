# number of pp
pp=17

# parallelism
n_bits=32

f = open("../src/intro.vhd", 'w')

f.write("\nLIBRARY ieee;\nUSE ieee.std_logic_1164.all;\n")
f.write("USE ieee.std_logic_arith.all;\n\nENTITY dadda_tree IS\n")
f.write("PORT (")

for i in range(pp-1):
	if i != 0:
		f.write(", ")
	if (i%10)==0:
		f.write("\n\t")
	f.write("pp" + str(i))

f.write(": IN STD_LOGIC_VECTOR(" + str(n_bits) + " downto 0);\n")
f.write("\tpp" + str(pp-1) + ": IN STD_LOGIC_VECTOR(" + str(n_bits-1) + " downto 0);\n")
f.write("\ts: IN STD_LOGIC_VECTOR(" + str(pp-2) + " downto 0);\n")
f.write("\ts_n: IN STD_LOGIC_VECTOR(" + str(pp-2) + " downto 0);\n")
f.write("\taddend1_out, addend2_out: OUT STD_LOGIC_VECTOR(" + str(n_bits*2-2) + " downto 0);\n")

f.write("\tM_lsb: OUT STD_LOGIC\n);\nEND dadda_tree;\n\n")
f.write("ARCHITECTURE struct OF dadda_tree IS\n")
f.write("\n\tCOMPONENT FA IS\n\tPORT(\n\t\ta, b, c_in : IN std_logic;\n")
f.write("\t\ts, c_out : OUT std_logic);\n\tEND COMPONENT;\n\n\tCOMPONENT HA IS\n")
f.write("\tPORT(\n\t\ta, b : IN std_logic;\n\t\ts, c_out : OUT std_logic);\n\tEND COMPONENT;\n\n")

f.close()
