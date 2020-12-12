# matrice

def matrix_generator(mat):
#	global mat
#	mat=[]

	# scorro i partial product tranne l'ultimo (16)
	for i in range(16):
		# scorro i 33 bit del pp per inserirli nella matrice
		for j in range(33):
			#se siamo al primo pp bisogna dichiarare le stringhe
			if i == 0:
				mat.append(["pp" + str(i) + "(" + str(j) + ")"])
			# append del bit attuale (i pp sono shiftati di i*2
			else:
				mat[j+i*2].append("pp" + str(i) + "(" + str(j) + ")")

		# append nella posizione meno significativa del bit di segno relativo a quel pp
		mat[i*2].append("s(" + str(i) + ")")

		# al primo giro si dichiarano le liste al fondo di mat e si mettono i bit di segno di pp0
		if i == 0:
			mat.append(["s(" + str(i) + ")"])
			mat.append(["s(" + str(i) + ")"])

		# append di una lista a mat col bit di segno negato (se siamo al pp1 la lista è già creata)
		if i == 1:
			mat[i*2+33].append("s_n(" + str(i) + ")")
		else:
			mat.append(["s_n(" + str(i) + ")"])

		# aggiunta del 1 al fondo (tranne per il primo e il penultimo)
		if i != 0 and i != 15:
			mat.append(["'1'"])

	# inserimento bit dell'ultimo pp
	for j in range(32):
		mat[j+16*2].append("pp" + str(16) + "(" + str(j) + ")")

