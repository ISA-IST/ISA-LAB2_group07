# python

import matrix_generator
import func_write

# number of partial product
pp_num=17

# vettore contenente i target dei vari stadi secondo Dadda
targets = []
# si parte da 2, ultimo stadio
next_target = 2

# vettore contenente il numero di adder istanziati per ogni stage
adder_num = []

# inserisco i vari target in testa al vettore per averli in ordine decrescente fino a raggiungere pp_num
while next_target < pp_num:
	# inserimento e calcolo prossimo target
	targets.insert(0, next_target)
	next_target = int(next_target*(3/2))
	# inizializzo il valore di adder in questo stage a 0
	adder_num.insert(0, 0)

# generazione matrice
matr = []
matrix_generator.matrix_generator(matr)

f = open("matrice.txt", "w")

for i in matr:
	f.write(str(i))
	f.write("\n")

f.close()

# ciclo i target
for stage_num in range(len(targets)):
	# scorro le righe della matrice per vedere se bisogna comprimere
	for i in range(len(matr)):
		# if len(matr[i]) > targets[stage_num]: ---- non serve controllare perché se non è più lunga non entra nelle condizioni successive
			# se la differenza dal target è >= 2 istanzio un fa
			while len(matr[i]) > (targets[stage_num]+1):
				# chiamata a funzione che istanzia fa (con gli ultimi 3 elementi della lista)
				func_write.write_vhdl(matr[i][-3:], stage_num, adder_num[stage_num])

				# elimino gli elementi usati per il fa
				del matr[i][-3:]
				# inserisco in testa a questa riga il sum generato
				matr[i].insert(0, "sum_" + str(stage_num) + "(" + str(adder_num[stage_num]) + ")")
				# inserisco in testa alla riga successiva il carry generato
				if i != len(matr)-1:
					matr[i+1].insert(0, "c_out_" + str(stage_num) + "(" + str(adder_num[stage_num]) + ")")

				adder_num[stage_num] = adder_num[stage_num] + 1

			if len(matr[i]) > targets[stage_num]:
				# chiamata a funzione che istanzia ha (con gli ultimi 2 elementi della lista)
				func_write.write_vhdl(matr[i][-2:], stage_num, adder_num[stage_num])

				# elimino gli elementi usati per il ha
				del matr[i][-2:]
				# inserisco in testa a questa riga il sum generato
				matr[i].insert(0, "sum_" + str(stage_num) + "(" + str(adder_num[stage_num]) + ")")
				# inserisco in testa alla riga successiva il carry generato
				if i != len(matr)-1:
					matr[i+1].insert(0, "c_out_" + str(stage_num) + "(" + str(adder_num[stage_num]) + ")")

				adder_num[stage_num] = adder_num[stage_num] + 1

# final stage

f_final = open("final_stage.vhd", 'w')

# ultimo ha
adder_num.append(0)

f_final.write("\n\tHA_" + str(len(adder_num)-1) +  " : HA port map (A=>" + matr[0][0] + ", B=>" + matr[0][1] + ", S=>sum_" + str(len(adder_num)-1) + ", C_out=>c_out_" + str(len(adder_num)-1) + ");\n")
del matr[0][-2:]
matr[0].insert(0, "sum_" + str(len(adder_num)-1))
matr[1].insert(0, "c_out_" + str(len(adder_num)-1))
adder_num[-1] = 1

# generazione addendi di uscita (RCA)

for i in range(2):

	f_final.write("\n\taddend" + str(i+1) + "_out <= ")

	for j in range(len(matr)-1, 1, -1):
		f_final.write(matr[j][i] + " & ")

	f_final.write(matr[1][i] + ";\n")

f_final.write("\n\tM_lsb <= " + matr[0][0] + ";\n\nEND struct;")

f_final.close()

# dichiarazione segnali usati
func_write.write_signals(adder_num)

