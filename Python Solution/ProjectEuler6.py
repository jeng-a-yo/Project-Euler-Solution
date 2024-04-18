# sum1 = 0
# sum2 = 0
# for a in range(1, 101):
#     sum1 += a**2
#     sum2 += a
# print(sum2**2-sum1)
print(sum([a for a in range(1, 101)]) ** 2 -sum([b ** 2 for b in [c for c in range(1, 101)]]))
