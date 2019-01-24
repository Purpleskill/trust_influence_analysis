# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 09:43:24 2019

@author: Juliette Maussion
"""

def checkReputation(notesRecues, reputationAffichee):
    
    correct = True
    reputationCalculee = []
    print(len(notesRecues))
    
    for i in range(1,len(notesRecues)):
        print('Round :',i+1)
        reputationCalculee.append(0)
        
        #calcul classique de moyenne
        for j in range(0,i):
            reputationCalculee[i-1] += notesRecues[j]/5;
        reputationCalculee[i-1] = reputationCalculee[i-1]/i
        print("Reputation calculee :", reputationCalculee[i-1],"\n Reputation affichee : ",reputationAffichee[i-1])
        
        if round(reputationCalculee[i-1],2)==reputationAffichee[i-1]:
            print("Reputation Calculee Ok")
        else : 
            print("Erreur de calcul !")
            correct = False
    return correct

#test joueur 1 
notes=[3,5,4,3,3,2]
reputation=[0.6,0.8,0.8,0.75,0.72]
checkReputation(notes,reputation)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    