lore = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce et felis sit amet orci interdum \n' \
       'commodo quis at felis. Morbi purus eros, venenatis at tortor ac, vehicula tempus justo. \n' \
       'Curabitur ut neque vitae nunc laoreet lobortis. Vivamus ac interdum neque. In vehicula \n' \
       'dolor sed libero tincidunt aliquam. Phasellus iaculis ac felis eu efficitur. Suspendisse ultricies \n' \
       'erat augue, ac consectetur risus scelerisque ac. Nam lectus arcu, ultricies in purus sed, viverra \n' \
       'condimentum nisi. Cras sodales arcu turpis, id euismod lacus pretium sit amet. Proin in sapien sed lacus \n' \
       'consectetur      gravida.'
sentence = raw_input("Wpisz swoje zdanie. Pozostawienie tego zdania pustego policzy ciagi znakow w tekscie:")
if sentence == "":
    print lore
    number = len(lore.split())
else:
    number = len(sentence.split())
print number
