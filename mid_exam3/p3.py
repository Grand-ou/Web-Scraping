class nft:
    def __init__(self, head, glass, body, num):
        self.head = head
        self.glass = glass
        self.body = body
        self.num = num
class Meerkat:
    def __init__(self):
        self.total = []
        self.d = []
        self.num = 1
        self.holder = []
    def create(self, head, glass, body):
        newnft = nft(head, glass, body, self.num)
        self.d.append(newnft)
        self.total.append(newnft)
        self.num += 1
    def mint(self, name):
        if len(self.d) < 1:
            print('sold out')
        else :
            soldednft = self.d[0]
            self.d.pop(0)
            print(name + ' mint #' + str(soldednft.num))
            # print(name, end=':')
            if name not in self.holder:
                self.holder.append(name)
                # print(name, len(self.holder))
    def show_total_num(self):
        print(self.num-1)
    def show_total_holder(self):
        print(len(self.holder))
    def show_property(self, id):
        for i in self.d:
            if i.num == id:
                print('#'+str(id)+' not exist')
                return 0
        for i in self.total:
            if i.num == id:
                print('#'+str(id)+' has '+i.head+' head, '+i.glass+' glass, and '+i.body+' body.')
                return 0
        print('#'+str(id)+' not exist')

# We will judge your code with the following scripts

my_kats = Meerkat()
while True:
    print(' ')
    args = input().split()
    if args[0] == "end":
        break
    if args[0] == "create":
        my_kats.create(args[1], args[2], args[3])
    elif args[0] == "mint":
        my_kats.mint(args[1])
    elif args[0] == 'show_total_num':
        my_kats.show_total_num()
    elif args[0] == 'show_total_holder':
        my_kats.show_total_holder()
    elif args[0] == "show_property":
        my_kats.show_property(int(args[1]))