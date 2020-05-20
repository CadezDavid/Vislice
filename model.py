import random
import string

stevilo_dovoljenih_napak = 10
pravilna_crka = '+'
ponovljena_crka = '/'
napacna_crka = '-'
zmaga = 'z'
poraz = 'p'
ZACETEK = 6745

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke == None:
            self.crke = list()
        else:
            self.crke = crke    

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]
    
    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]
    
    def stevilo_napak(self):
        return len(self.napacne_crke())
    
    def zmaga(self):
        return all([(crka in self.crke) for crka in self.geslo])
    
    def poraz(self):
        return self.stevilo_napak() > stevilo_dovoljenih_napak
    
    def pravilni_del_gesla(self):
        uganjen_del_gesla = str()
        for crka in self.geslo:
            if crka in self.crke:
                uganjen_del_gesla += crka
            else:
                uganjen_del_gesla += '_'
        return uganjen_del_gesla
    
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())
    
    def ugibaj(self, crka):
        if crka not in string.ascii_letters or len(crka) != 1:
            return 'Neveljaven vnos'
        crka = crka.upper()
        if crka in self.geslo and crka not in self.crke:
            stanje = pravilna_crka
        elif crka in self.crke:
            stanje = ponovljena_crka
        elif crka not in self.geslo:
            stanje = napacna_crka
        if crka not in self.crke:
            self.crke.append(crka)
        if self.zmaga():
            return zmaga
        elif self.poraz():
            return poraz
        return stanje
    
with open('besede.txt', 'r') as datoteka_z_besedami:
    bazen_besed = [vrstica.strip().upper() for vrstica in datoteka_z_besedami]

def nova_igra():
    return Igra(random.choice(bazen_besed))

igra = nova_igra()
igra.zmaga()
igra.ugibaj('a')

class Vislice:

    def __init__(self):
        self.igre = dict{}
    
    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys())

    def nova_igra(self):
        igra = nova_igra()
        id_igre = self.prost_id_igre()
        self.igre[id_igre] = (igra, ZACETEK)
        return id_igre
    
    def ugibaj(self, id_igre, crka):
        igra, _ = self.igre[id_igre]
        poskus = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, poskus)