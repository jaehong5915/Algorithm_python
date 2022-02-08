import string

s = input()
alpha = list(string.ascii_lowercase)
for i in s:
    if i in alpha:
        alpha[alpha.index(i)] = s.index(i)

for i in range(len(alpha)):
    if type(alpha[i]) is str:
        alpha[i] = -1
result = ' '.join(str(s) for s in alpha)
print(result)