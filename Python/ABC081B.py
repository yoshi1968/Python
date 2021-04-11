a = [int(s) for s in input().split()]
c = 0
while(all([i % 2 == 0 for i in a])):
  print(a)
  c += 1
  a = [i // 2 for i in a]
print(c)