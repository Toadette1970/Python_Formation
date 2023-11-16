import math 

#file = open("FichierNP",'r')

Nb_Premiers = [  ]
Nb_a_tester = 2

def is_prime(n):
    for i in range( 2, int(math.sqrt(n))+1 ):
        if (n % i) == 0:
            return False
    return True

while len(Nb_Premiers)  <= 100:
    if is_prime(Nb_a_tester) == True:
        Nb_Premiers.append(Nb_a_tester)
    else:
        pass
    Nb_a_tester +=1

for MonNombre in Nb_Premiers:
    print(f"{MonNombre}")


#for i,visiteur in enumerate(visiteurs): 
    # visiteurs[i] = "je ne sais quoi"
 #   print(f"N *{i} : {visiteur["nom"]} a {visiteur["age"]} ans")