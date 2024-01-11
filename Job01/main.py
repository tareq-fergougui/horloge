import time
import threading

heure_actuelle = (0, 0, 0)
heure_alarme = None

def afficher_heure():
    while True:
        print(f"{heure_actuelle[0]:02d}:{heure_actuelle[1]:02d}:{heure_actuelle[2]:02d}")
        time.sleep(1)
        heure_suivante()

def heure_suivante():
    global heure_actuelle
    heure_actuelle = (heure_actuelle[0], heure_actuelle[1], heure_actuelle[2] + 1)

    if heure_actuelle[2] == 60:
        heure_actuelle = (heure_actuelle[0], heure_actuelle[1] + 1, 0)
        if heure_actuelle[1] == 60:
            heure_actuelle = (heure_actuelle[0] + 1, 0, 0)
            if heure_actuelle[0] == 24:
                heure_actuelle = (0, 0, 0)

def regler_heure(heures, minutes, secondes):
    global heure_actuelle
    heure_actuelle = (heures, minutes, secondes)

def regler_alarme(heures, minutes, secondes):
    global heure_alarme
    heure_alarme = (heures, minutes, secondes)

def verifier_alarme():
    while True:
        if heure_alarme is not None and heure_alarme == heure_actuelle:
            print("ALARME ! L'heure de l'alarme est atteinte.")
        time.sleep(1)

thread_affichage_heure = threading.Thread(target=afficher_heure)
thread_verifier_alarme = threading.Thread(target=verifier_alarme)

thread_affichage_heure.start()
thread_verifier_alarme.start()

regler_heure(16, 30, 0)
regler_alarme(16, 31, 0)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Programme arrêté.")