def aliments(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print("Orange, Mandarine et Kiwi")
        elif saison == "ete":
            print("Poire, Fraise et Cassis")
        else :
            print("erreur de composition")
    elif type == "legumes":
        if saison == "hiver":
            print("Carotte, Topinambour et Endive")
        elif saison == "ete":
            print("Artichaut, Aubergine et Navet")
        else :
            print("erreur de composition")
    else :
        print("erreur de composition")

aliments("fruits", "hiver")
aliments("fruits", "ete")
aliments("legumes", "hiver")
aliments("legumes", "ete")
aliments("fruits", "saison")
aliments("fruit", "ete")