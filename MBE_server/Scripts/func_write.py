# creazione funzione
def write_vhdl(operands, targetindex, numadd):

    #apertura file append
	try:
		f_arch = open("../src/tree.vhd", 'a')
	except:
		print("ERROR: cannot open file")

    #controllo numero di argomenti per sapere se HA o FA
	if len(operands) == 3 :
	#scrittura FA
		f_arch.write("\tFA_" + str(targetindex) + "_" + str(numadd) + " : FA port map (A=>" + operands[0] + ", B=>" + operands[1] + ", C_in=>" + operands[2]  + ", S=>sum_" + str(targetindex) + "(" + str(numadd) + ") , C_out=>c_out_" + str(targetindex) + "(" + str(numadd) + "));\n")
	elif len(operands) == 2:
		f_arch.write("\tHA_" + str(targetindex) + "_" + str(numadd) + " : HA port map (A=>" + operands[0] + ", B=>" + operands[1] + ", S=>sum_" + str(targetindex) + "(" + str(numadd) + ") , C_out=>c_out_" + str(targetindex) + "(" + str(numadd) + "));\n")
	else :
		f_arch.write("errore nella lista")
		print("errore nella lista")

	f_arch.close()



def write_signals(adder_num):
	try:
		f_sgn = open("../src/signal.vhd", 'a')
	except:
		f_sgn = open("../src/signal.vhd", 'w')

	for i in range(len(adder_num)):
		if adder_num[i] != 1:
			f_sgn.write("\tSIGNAL sum_" + str(i) + ", c_out_" + str(i) + ": STD_LOGIC_VECTOR (" + str(adder_num[i]-1) + " downto 0);\n")
		else:
			f_sgn.write("\tSIGNAL sum_" + str(i) + ", c_out_" + str(i) + ": STD_LOGIC;\n\n")

	f_sgn.write("BEGIN\n\n")

	f_sgn.close()
