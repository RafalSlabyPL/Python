l = ["6", "9", "69", "997", "69"]
new_number = ""
for number in l:
    new_number += str(number).zfill(3)
print new_number