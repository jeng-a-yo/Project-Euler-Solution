import time
st = time.time()

with open("p067_triangle.txt") as f:
    data = f.read()

data = data.strip().split('\n')
# print(data)

for a in range(len(data)):
    data[a] = data[a].strip().split(' ')
    data[a] = [int(x) for x in data[a]]
    # data[a] = list(map(lambda x: int(x), data[a]))
    # print(data[a])


for i in range(len(data) - 2, -1, -1):
    # if i == 90:
    #     break
    for j in range(len(data[i])):

        # print(i, j)
        data[i][j] = data[i][j] + max(data[i+1][j], data[i+1][j+1])

    data.pop()

print(data[0][0])

et = time.time()
print(et - st)
