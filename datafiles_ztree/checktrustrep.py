# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 09:43:24 2019

@author: Juliette Maussion
"""
import math

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

def checkTrust (roles, sending_amount, receiving_amount, trustscore, nb_subjects):
    n = len(nb_subjects)
    m = len(sending_amount[0])
    #initialisation des parametres
    
    alpha = [[0]]*n
    beta = [[0]]*n
    atf = [[0]]*n
    expect_trust = [[0]]*n
    trend_factor = [[0]]*n
    current_trust = [[0]]*n
    aggregate_trust = [[0]]*n
    change_rate = [[0]]*n
    trust_value = [[0.5]]*n

        
    eps = 0.3
    phi = 0.1
    max_atf = 2
    threshold = 0.25
    c = 0.9
    
    atf = [[]]*n
    adj_atf  = [[]]*n
    maximum_sending_amount = [[]]*n
    send_proportion = [[]]*n
    delta = [[]]*n
    
    for t in range(m):
        for i in range(n):
            if sending_amount != -1:
                p = i #partner p
        
#    send_proportion[t] = sending_amount[t]/maximum_sending_amount[t]
#    current_trust[t] = math.log(send_proportion[t]*(math.e-1)+1)
#    delta[t] = abs(current_trust[t] - current_trust[t-1])
#    beta[t] = c*delta[t] + (1-c)*beta[t-1]
#    alpha[t] = threshold + (c*delta[t])/(1+beta[t])
#    aggregate_trust = alpha * current_trust + (1-alpha)*aggregate_trust
#    if current_trust - aggregate_trust > eps :
#        trend_factor[t] = trend_factor[t-1] + phi
#    elif aggregate_trust[t] - current_trust[t] >eps :
#        trend_factor[t] = trend_factor[t-1] -phi
#    else:
#        trend_factor[t] = trend_factor[t-1]
#    
#    if atf[t]>max_atf:
#        adj_atf[t]=atf[t]/2
#    else:
#        adj_atf[t]=atf[t]
#    
#    if current_trust - aggregate_trust > phi :
#        atf[t]=adj_atf[t-1] + (current_trust[t]-aggregate_trust[t])/2
#    elif aggregate_trust[t] - current_trust[t] >phi :
#        atf[t]=adj_atf[t-1] + (aggregate_trust[t]-current_trust[t])
#    else:
#        atf[t]=adj_atf[t-1] 
#    
#    if atf[t]>max_atf:
#        change_rate[t] = 0
#    else :
#        change_rate[t] = math.cos(math.pi /2 * atf[t] / max_atf)
#        
#    expect_trust[t] = trend_factor[t]*current_trust[t]+(1-trend_factor[t])*aggregate_trust[t]
#    trust_value[t] = expect_trust[t] * change_rate[t]
#    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    