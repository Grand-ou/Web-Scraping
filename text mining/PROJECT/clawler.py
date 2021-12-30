# -*- coding: utf-8 -*-
from GoogleNews import GoogleNews

googlenews = GoogleNews()
googlenews.search('Trump')
googlenews.clear()
googlenews.getpage(2)
result = googlenews.result()
print(len(result))

for n in range(len(result)):
    print(n)
    for index in result[n]:
        print(index, '\n', result[n][index])

    exit()           