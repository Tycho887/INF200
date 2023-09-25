import math
B = 50000 # Bæreevne
e = math.e # Eulers tall
k = 0.2 # Vekstrate pr. time
#%% Oppgave a)
# Løser likningen med hensyn på C, og får uttrykket under:
C = B/(5000*e**(-k*0))-1
print("Oppgave a) C =", C)
#%% Oppgave b)
def population(t):
    N = B/(1+(C*e**(-k*t)))
    return N
print("Oppgave b) Populasjonen etter 24t:", round(population(24)))
#%% Oppgave c)
# Prøvde meg frem på forskjellige t-verdier og endte opp med ca. 22 timer
print("Oppgave c) 90% av bæreevnen, altså", round(population(22)),"er oppnådd etter ca. 22 timer")