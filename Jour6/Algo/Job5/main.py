#Job5

def WC(nombreDeMarches,hauteurDuneMarche):

    pourUneSemaine = nombreDeMarches * hauteurDuneMarche * 2 * 5 *7

    M = pourUneSemaine // 60

    CM = M % 60

    zzz = CM / 100 + M
    print("\n")
    print("Pour",nombreDeMarches, "marches de",hauteurDuneMarche,"cm, le gardien parcourt",zzz,"m par semaine.\n")
WC(50,10)