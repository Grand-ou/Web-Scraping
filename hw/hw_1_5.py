def ordinal(x):
    if x.isupper():
        return ord(x) - ord('A') + 1
    elif x.islower():
        return ord(x) - ord('a') + 1


list = input()
price = ordinal(list[0]) * (26**2) + ordinal(list[1]) * (26**1) + ordinal(list[2]) * (26**0)
# print(price)
result = []
result.append(int(price/1000))
price = price % 1000
result.append(int(price/500))
price = price % 500
result.append(int(price/100))
price = price % 100
result.append(int(price/50))
price = price % 50
result.append(int(price/10))
price = price % 10
result.append(int(price/1))
price = price % 1
cnt = 0
for i in result:
    print(i, end='')
    if cnt != 5:
        print(',', end='')
    cnt += 1