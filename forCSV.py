global columns, data
def write_to_file(filename, columns, data):
    with open(filename, 'w') as file:
        file.write(','.join(columns)+'\n')
        for line in data:
            line=[str(i) for i in line]
            file.write(','.join(line)+'\n')

def read_from_file(filename):
    with open(filename, 'r') as file:
        columns = tuple(file.readline().split(','))
        data = []
        for line in file:
            line = line.split(',')
            data.append(((line[0]), line[1], line[2], (line[3])))
        return columns, data

def DataFrame(filename):
    columns, data=read_from_file("C:\\Users\\AGVKVHome\\Desktop\\Ui\\Well.CSV")
    x=str()
    y=str()
    for i in range(len(columns)):
        x=x+columns[i].ljust(7)
    print(x.rstrip())
    for i in range(len(data)):
        y=""
        for j in range(len(data[i])):
            y=y+data[i][j].ljust(7)
        print(y.rstrip())

def add_to_file(filename, to_add):
    with open(filename, "a") as file:
        for line in to_add:
            line=[str(i) for i in line]
            file.write(','.join(line)+'\n')