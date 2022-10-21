class Hashtable:
    def __init__(self):
        self.MAX = 10
        self.A = [[] for i in range(self.MAX)]
    
    def get_hash(self,key):
        key = str(key)
        h = 0
        for i in key:
            h += ord(i)
        return h%(self.MAX)
    
    #__setitem__ lets you give value like object[key] = val and __getitem__ lets you call item like object[key] 

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for i,items in enumerate(self.A[h]):
            if len(items) == 2 and items[0] == key:
                self.A[h][i] = (key,val)
                found = True
                break
        if found == False:
            self.A[h].append((key,val))
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        for items in (self.A[h]):
            if items[0] == key:
                return items[1]
    
    def __delitem__(self,key):
        h  = self.get_hash(key)
        for i,items in enumerate(self.A[h]):
            if len(items) == 2 and items[0] == key:
                del self.A[h][i]
                break



dict_1 = Hashtable()

dict_1['March 6'] =  1
dict_1['March 17'] =  2

print(dict_1['March 6'],dict_1['March 17'])

del dict_1['March 17']

print(dict_1['March 6'],dict_1['March 17'])