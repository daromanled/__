class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [' +str(current.value) +', '
            while current.next != None:
                current = current.next
                out += str(current.value) + ', '
            return out[:-2] + ']'
        return 'LinkedList []'


    def clear(self):
        self.__init__()
    def add(self, x):
        self.length+=1
        if self.first == None:
            self.last = self.first = Node(x, None)
        else:
            self.last.next = self.last = Node(x, None)  
    
    def rev(self):
        head = self.first
        new_head = None
        while head:
            head.next, head, new_head = new_head, head.next, head # look Ma, no temp vars!
        return new_head
    
    def print_reversed(self):

        node = self.head
        values = []
        while node:
            values.append(node.data)
            node = node.nextNode

        for value in reversed(values):
            print(value)
        
    def ret(self):
        out = LinkedList()
        out.first = self.last
        print(out)
        if self.first != None:
            current = self.first
            #finist = self.last
            self.first, self.last = self.last, self.first
            prev = None
            nxt = current.next
            while current != self.first:
                current.next = prev
                
                
                prev = current
                print(current, current.value, current.next)
                current = nxt
                #print(nxt.value)
                nxt = nxt.next
                #out.add(next)
                #print(nxt.value)
                #print('')
    
    def rev(self):
        tmp =[]
        if self.first != None:
            current = self.first
            tmp.append(current.value)
            while current.next != None:
                current = current.next
                tmp.append(current.value)
        tmp = tmp[::-1]
        out = LinkedList()
        for i in tmp:
            out.add(i)
        return out

L = LinkedList()
L.add(1)
L.add(2)
L.add(3)
L.add(4)
L.add(5)
L.add(6)
L.add(7)
print(L)
#L.print_reversed()
L = L.rev()
print(L)
#O(n) - сложность
#память - n
#Мне кажется, что для массива (array) сложность и потребление памяти будут такими же.
