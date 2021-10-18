
def reverse(x):
    return x[::-1]
def ordinal(x):
    if x.isupper():
        return ord(x) - ord('A') + 1
    elif x.islower():
        return ord(x) - ord('a') + 1



ciper = input()
encry = input()
ciper = reverse(ciper)
result = ''
for i in range(3):
    if (ordinal(ciper[i]) + ordinal(encry[i]) ) % 2 == 0:
        result = result + chr((ordinal(ciper[i]) * ordinal(encry[i]) - 1) % 26 + ord('A'))
    if (ordinal(ciper[i]) + ordinal(encry[i]) ) % 2 == 1:
        # print(ordinal(ciper[i]), ordinal(encry[i]))
        if ordinal(encry[i]) == 1:
            result = 'z'
            continue
        result = result + chr(((ordinal(ciper[i]) - 1) % ordinal(encry[i])) + ord('a') )
print(result)