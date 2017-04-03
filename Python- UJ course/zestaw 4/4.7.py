seq = [1,(2,3),[],[4,(5,6,7)],8,[(9, 10)]]

def spawdzenie (wejscie):
    flaga = False
    wyjscie=[]
    while flaga == False:
        if len(wejscie)<2:
            flaga = True
        for element in wejscie:
            if isinstance (element,(tuple,list)):
                for x in element:
                    wejscie += [x]
                wejscie.remove(element)
            else:
                wyjscie += [element]
                wejscie.remove(element)

    wyjscie.sort()
    print ("Koncowa lisa elementow: ", wyjscie)

spawdzenie (seq)