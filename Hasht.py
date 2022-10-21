class Hashtable:
    def __init__(self):
        self.MAX = 100
        self.A = [None for i in range(self.MAX)]
    
    def get_hash(self,key):
        key = str(key)
        h = 0
        for i in key:
            h += ord(i)
        
        return h%(self.MAX)
    
    def add_v(self,key,val):
        h = self.get_hash(key)

        self.A[h] = val
    
    def get_v(self,key):
        h = self.get_hash(key)
        return self.A[h]


dict_1 = Hashtable()

dict_1.add_v('First_one', 1)
dict_1.add_v('Sec', 2)

print(dict_1.get_v('First_one'),dict_1.get_v('Sec'))