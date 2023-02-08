from forCSV import *
a=("id", "Type", "Class", "IN")
b=[("1", "a", "Beta", "613"),("2", "b", "Alpha", "2135")]
print("Пожалуйста, введите адрес файла:")
filename=input()
write_to_file(filename, a, b)
DataFrame(filename)
to_add=[("3", "b", "Alpha", "64"), ("4", "a", "Omega", "7845")]
print("---")
add_to_file(filename, to_add)
DataFrame(filename)