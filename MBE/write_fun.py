



# creazione funzione
def write_vhdl(operands,targetindex,numadd):

    #apertura file append
    try:
        f_arch = open("dadda_tree.vhdl", 'a')
    except:
        f_arch = open("dadda_tree.vhdl", 'w')
    #controllo numero di argomenti per sapere se HA o FA
    if len(operands) == 3 :
        #scrittura FA
        f_arch.write("FA_" + str(targetindex) + "_" + str(numadd) + " : FA port map (A=>" + str(operands[0]) + ", B=>" + str(operands[1]) + ", C=>" + str(operands[2])  + ", S=>sum_" + str(targetindex) + "(" + str(numadd) + ") , C_out=>C_out_" + str(targetindex) + "(" + str(numadd) + "));")
    else if len(operands) == 2:
        f_arch.write("FA_" + str(targetindex) + "_" + str(numadd) + " : FA port map (A=>" + str(operands[0]) + ", B=>" + str(operands[1]) + ", S=>sum_" + str(targetindex) + "(" + str(numadd) + ") , C_out=>C_out_" + str(targetindex) + "(" + str(numadd) + "));")
    else :
        f_arch.write("errore nella lista")
        print("errore nella lista")



def write_vhdl_sgn(adder_num):
    try:
        f_sgn = open("signal.vhdl", 'a')
    except:
        f_sgn = open("signal.vhdl", 'w')
        
    for stage in adder_num:
        f_sgn.write("SIGNAL : sum_" + str(stage) + ", C_out_" + str(stage) + ": std_logic_vector (" + str(adder_num[stage]) + " downto 0);")
