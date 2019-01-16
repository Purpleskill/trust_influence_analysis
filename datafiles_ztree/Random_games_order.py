import numpy

file=open('Games_orders.txt',"a")
file.close()



a = numpy.array(['1', '2', '3', '4'])

def isPresent(chaine,tableau):
    i=0
    present=False
    while not present and i<len(tableau):
        present=tableau[i]==chaine
        i+=1
    return present

def toStr(tableau):
    res=''
    for i in range(0,len(tableau)):
        res=res+tableau[i]
        if i<len(tableau)-1:
            res=res+','
    return res

        

with open('Games_orders.txt',"r") as fichier:
    global contenu
    contenu=fichier.read()

with open('Games_orders.txt',"a") as fichier:
    global contenuArray
    global count
    count=0
    contenuArray=contenu.split("\n")
    #print(contenuArray)
    if len(contenuArray)<25:
        while isPresent(toStr(a),contenuArray):
            numpy.random.shuffle(a) #Permutation de a
        fichier.write(toStr(a)+'\n')
        print(toStr(a))
    else:
        print("Attention ! Le nombre maximum d'arrangements possible est atteint.")

with open('Game_order.txt','w') as ztreeFile:
    ztreeFile.write(toStr(a))

    


