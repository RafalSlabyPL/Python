line = 'To powinno dzialac bez problemu.'
all_chars = len(line.split()[0])
for a in range(1, len(line.split()), 1):
   all_chars += len(line.split()[a])
print "W danej lini lacznie jest: ", len(line)," znakow, ale tylko ", all_chars, " liter"
