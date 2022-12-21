#with open('file.txt', 'w') as data:
# data.write('line 1\n')
# data.write('line 2\n')
colors = ['red', 'green', 'blue']
data = open('python/lessons/2/file.txt', 'a')
data.writelines(colors) # разделителей не будет
data.close()
exit()
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()