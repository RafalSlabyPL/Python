line = 'To powinno dzialac bez problemu.'
long_word =0
short_word=0
for a in range(1, len(line.split()), 1):
    if len(line.split()[long_word])<len(line.split()[a]):
        long_word=a
for a in range(1, len(line.split()), 1):
    if len(line.split()[short_word])>len(line.split()[a]):
        long_word=a
print "Najdluzszy wyraz to: ", line.split()[long_word]
print "Najkrotszy wyraz to: ", line.split()[short_word]
