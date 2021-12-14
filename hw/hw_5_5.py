class Phonebook:
    def __init__(self):
        self.book = {}

    def add(self, a, b):
        self.book[a] = b
        self.book[b] = a
    def search(self, a):
        result = self.book.get(a, 'Cannot find '+a)
        return result

# We will judge your code with the following scripts

pbook = Phonebook()
while True:
   args = input().split()
   if args[0] == "end": break
    
   if args[0] == "s":
       print( pbook.search( args[1] ) )
   elif args[0] == "a":
       pbook.add( args[1], args[2] )