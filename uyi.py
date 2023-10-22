NUMS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num = int(input())
names = {}
for i in range(num):
    name = input()
    name = name[:-11]
    for j in name:

        if j == '@':
            key = name.find(j)
            names[name[:key]] = names.get(name, 0)

        elif j in NUMS:
            key = name.find(j)
            names[name[:key]] += 1
            break

num = int(input())
answer = []
for i in range(num):
    name = input()
    if name not in names.keys():
        names[name] = names.get(name, 0)
        answer.append(f'{name}@untitled.py')
        names[name] += 1
    else:
        names[name] += 1
        answer.append(f'{name + str(names[name])}@untitled.py')

for i in answer:
    print(i)