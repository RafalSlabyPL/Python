line = 'To powinno dzialac bez problemu.'
firs_char = line.split()[0][0]
last_char = line.split()[0][len(line.split()[0])-1]
for a in range(1, len(line.split()), 1):
    firs_char += line.split()[a][0]
for a in range(1, len(line.split()), 1):
    last_char += line.split()[a][len(line.split()[a]) - 1]
print "Wyraz zlozony tylko z pierwszych liter to: ", firs_char
print "Wyraz zlozony tylko z ostatnich znakow to: ", last_char
