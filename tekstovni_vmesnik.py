import model

def izpis_igre(igra):
    tekst = f'===============================\n\nŠtevilo prestalih poskusov: {model.stevilo_dovoljenih_napak - igra.stevilo_napak()}\n\n{igra.pravilni_del_gesla()}\n\nNeuspeli poskusi: {igra.nepravilni_ugibi()}\n\n==============================='
    return tekst

def izpis_zmage(igra):
    return f'Zmaga, geslo je bilo {igra.geslo}'

def izpis_poraza(igra):
    return f'Poraz, geslo je bilo {igra.geslo}'

def neveljaven_vnos(igra):
    return f'\nNeveljaven vnos.\n'

def zahtevaj_vnos():
    return input('Črka: ')

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        poskus = zahtevaj_vnos()
        if igra.ugibaj(poskus) == 'Neveljaven vnos':
            print(neveljaven_vnos(igra))
        elif igra.zmaga():
            print(izpis_zmage(igra))
            break
        elif igra.poraz():
            print(izpis_poraza(igra))
            break
    return

pozeni_vmesnik()