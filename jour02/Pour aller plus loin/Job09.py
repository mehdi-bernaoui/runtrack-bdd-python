def triangle(a, b, c):

    if a+b > c and a+c > c and b+c > a:
        if a*a+b*b == c*c or a ** 2 + c ** 2 == b ** 2 or a **2 == b ** 2 + c ** 2:
            print("triangle rectangle")
            if a == b or b == c or a == c:
                print("triangle rectangle isocèle")
        elif a == b == c:
            print("triangle équilatéral")
        elif a == b or b == c or a == c:
                print("triangle isocèle")
        else:
            print("triangle quelconque")
    else:
        print("triangle non-réalisable")

triangle(3,4,5)
triangle(2,2,2)
triangle(8,2,15)