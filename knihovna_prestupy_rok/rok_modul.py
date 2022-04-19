def prestupny_rok(rok):
    if rok % 4 == 0:
        if rok % 100 != 0:
            print (f"{rok} je prestupny rok")
        if rok % 100 == 0:
            if rok % 400 == 0:
               print (f"{rok} je prestupny rok") 
            else:
                print (f"{rok} neni prestupny rok")
    else:
        print (f"{rok} neni prestupny rok")

#je to trochu bramborový, ale hlavně, že to funguje :)