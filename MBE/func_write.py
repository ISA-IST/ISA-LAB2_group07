

# creazione funzione
def write_vhdl(operands, targetindex, numadd):

    #apertura file append
    try:
        f_arch = open("dadda_tree.vhd", 'a')
    except:
        print("ERROR: cannot open file")
		
    #controllo numero di argomenti per sapere se HA o FA
    if len(operands) == 3 :
        #scrittura FA
        f_arch.write("FA_" + str(targetindex) + "_" + str(numadd) + " : FA port map (A=>" + operands[0] + ", B=>" + operands[1] + ", C_in=>" + operands[2]  + ", S=>sum_" + str(targetindex) + "(" + str(numadd) + ") , C_out=>C_out_" + str(targetindex) + "(" + str(numadd) + "));\n")
    else if len(operands) == 2:
        f_arch.write("HA_" + str(targetindex) + "_" + str(numadd) + " : HA port map (A=>" + operands[0] + ", B=>" + operands[1] + ", S=>sum_" + str(targetindex) + "(" + str(numadd) + ") , C_out=>C_out_" + str(targetindex) + "(" + str(numadd) + "));\n")
    else :
        f_arch.write("errore nella lista")
        print("errore nella lista")
		
	f_arch.close()



def write_signals(adder_num):
    try:
        f_sgn = open("signal.vhd", 'a')
    except:
        f_sgn = open("signal.vhd", 'w')
        
    for stage in adder_num:
        f_sgn.write("SIGNAL : sum_" + str(stage) + ", C_out_" + str(stage) + ": std_logic_vector (" + str(adder_num[stage]) + " downto 0);\n")
		
	f_sgn.close()