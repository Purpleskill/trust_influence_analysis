import numpy

file=open('Games_orders.txt',"a") #Si le fichier n'éxiste pas, on le crée
file.close()



a = numpy.array(['1', '2', '3', '4'])

def isPresent(chaine,tableau): #Recherche d'une string dans un tableau de string
    i=0
    present=False
    while not present and i<len(tableau):
        present=tableau[i]==chaine
        i+=1
    return present

def toStr(tableau): #Conversion d'un tableau d'entier en chaine de caractères de ces entiers séparés par des virgules
    res=''
    for i in range(0,len(tableau)):
        res=res+tableau[i]
        if i<len(tableau)-1:
            res=res+','
    return res


        

with open('Games_orders.txt',"r") as fichier: #Lecture du contenu de Games_orders.txt
    global contenu
    contenu=fichier.read()

with open('Games_orders.txt',"a") as fichier: 
    global contenuArray
    global count
    count=0
    contenuArray=contenu.split("\n") #met en forme le contenu en méttant chaque lignes du fichier dans une case d'un tableau
    #print(contenuArray)
    if len(contenuArray)<25: #Si toutes les combinaisons n'ont pas déjà été créées
        while isPresent(toStr(a),contenuArray):
            numpy.random.shuffle(a) #Permutation de la suite de nombre tant qu'elle existe déjà
        fichier.write(toStr(a)+'\n')
        print(toStr(a)) #Affichage de l'ordre des jeux et écriture de celui-ci dans le fichier qui sert d'historique
    else:
        print("Attention ! Le nombre maximum d'arrangements possibles est atteint.")

with open('Game_order.txt','w') as ztreeFile:
    ztreeFile.write("ORDER\t"+"Period\t"+"Game1\t"+"Game2\t"+"Game3\t"+"Game4\t"+"\n")
    ztreeFile.write("ORDER\t"+"1\t"+a[0]+"\t"+a[1]+"\t"+a[2]+"\t"+a[3]) #Ecriture de l'ordre des jeux dans le fichier pour récupération par ztree

    


