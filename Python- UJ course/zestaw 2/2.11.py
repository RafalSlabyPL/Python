napis = 'word'
napis_z_podkreslaniami = napis[0]
for a in range(1, len(napis), 1):
    napis_z_podkreslaniami +='_' + napis[a]
print(napis_z_podkreslaniami)

