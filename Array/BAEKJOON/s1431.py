'''
시리얼 번호
- a,b 길이가 다르면, 짧은것이 먼저 온다.
- 길이가 같으면 모든 자리수의 합이 작은 것이 먼저 온다(숫자만)
- 사전순으로 비교 -> 숫자가 알파벳보다 사전순으로 작다.
입력)
- 기타 개수 N <= 50
    - 시리얼번호
'''
def tot(v):
    num_tot = 0
    for i in v:
        if i.isdigit() == True:
            num_tot += int(i)
    return num_tot
        

n = int(input())
seri = []
for _ in range(n):
    seri.append(input())

seri = sorted(seri, key=lambda x:(len(x), tot(x), x))
for i in seri:
    print(i)

# for i in range(n-1):
#     for j in range(i+1,n):
#         if len(seri[i]) > len(seri[j]):
#             seri[i], seri[j] = seri[j], seri[i]

#         elif len(seri[i]) == len(seri[j]):
#             suma = 0
#             sumb = 0
#             for x,y in zip(seri[i], seri[j]):
#                 if x.isdigit() == True:
#                     suma += int(x)
#                 if y.isdigit() == True:
#                     sumb += int(y)
#             if suma > sumb :
#                 seri[i], seri[j] = seri[j], seri[i]

#             elif suma == sumb:
#                 for x,y in zip(seri[i], seri[j]):
#                     if x> y :
#                         seri[i], seri[j] = seri[j],seri[i]
#                         break
#                     elif x < y:
#                         break

# for i in seri:
#     print(i)


# def sum_num(v):
#     tot = 0
#     for i in v:
#         if i.isdigit() == True:
#             tot += int(i)
#     return tot


# n = int(input())
# seri = []
# for _ in range(n):
#     seri.append(input())
# seri = sorted(seri, key=lambda x:(len(x), sum_num(x),x))
# for i in seri:
#     print(i)
