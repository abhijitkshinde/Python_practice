from tkinter import Y


class node:
    
    def __init__(self,val):
        self.val = val
        self.next = None

class linkedlist:

    def __init__(self):
        self.head = None
    
    def add_at_beggining(self,l_b):
        self.head, l_b.next = l_b, self.head
    


h = linkedlist()
h.head = l1 = node(6)
l1.next = l2 = node(3)
l2.next = l3 = node(4)

h.add_at_beggining(node(7))
h.add_at_beggining(node(11))
l = h.head

while l != None:
    
    print(l.val)
    l = l.next
