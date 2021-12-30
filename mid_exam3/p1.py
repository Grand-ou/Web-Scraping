# import requests 
# from bs4 import BeautifulSoup
# url = ''
# re = requests.get(url)
# soup = BeautifulSoup(re.text, 'html.parser')
# print(soup)
# print(soup.title)
# print(soup.find('title'))
# print(soup.title.text)
# print(soup.title.string)
# print(soup.findAll('tag 名稱'))
class Phonebook:
    def __init__(self):
        self.book = {}

    def add(self, a, b):
        self.book[a] = b
        self.book[b] = a
    def search(self, a):
        result = self.book.get(a, 'Cannot find '+a)
        return result
    def delete(self, info):
        data = self.book.get(info, 'Cannot find')
        if data == 'Cannot find':
            return 0
        
        del self.book[info]
        del self.book[data]
        return 1
    def modify(self, info, new_info):
        data = self.book.get(info, 'Cannot find')
        if data == 'Cannot find':
            return 0
        
        del self.book[info]
        del self.book[data]
        self.add(data, new_info)
        


# We will judge your code with the following scripts

pbook = Phonebook()
while True:
    args = input().split()
    if args[0] == "end":
        break
    if args[0] == "s":
        print(pbook.search(args[1]))
    elif args[0] == "a":
        pbook.add(args[1], args[2])
    elif args[0] == 'd':
        pbook.delete(args[1])
    elif args[0] == 'm':
        pbook.modify(args[1], args[2])