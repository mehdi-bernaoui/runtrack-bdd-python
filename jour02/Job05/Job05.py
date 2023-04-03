def calcule(num1 , operator , num2):
    if operator == "+":
        resultat = num1 + num2
        print(resultat)
    elif operator == "-":
        resultat = num1 - num2
        print(resultat)
    elif operator == "*":
        resultat = num1 * num2
        print(resultat)
    elif operator == "/":
        resultat = num1 / num2
        print(resultat)
    elif operator == "%":
        resultat = num1 % num2
        print(resultat)
    else:
        print("erreur")


calcule(5,"+",6)
calcule(40,"-",2)
calcule(26,"/",16)
calcule(36,"*",6)
calcule(54,"%",15)
calcule(42, ",", 25)