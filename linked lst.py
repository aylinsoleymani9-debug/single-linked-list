class dnode:
    def __init__(self, d):
        self.Data = d
        self.next = None
        self.prev = None
class dlinked_list:
    def __init__(self):
        self.head=None
    def insert_first(self,x):
        if self.head is None:
            self.head=dnode(x)
        else:
            a=dnode(x)
            a.next=self.head
            a.next.prev=a
            self.head=a
    
def insert_after(self, x, y):
    if self.head is None:
        print("error")
        return
    c = self.head
    while c:
        if c.Data == x:
            a = dnode(y)
            a.next = c.next
            a.prev = c
            if c.next:
                c.next.prev = a
            c.next = a
            return
        c = c.next
    print("not found")

def insert_before(self, x, y):
    if self.head is None:
        print("error")
        return
    if self.head.Data == x:
        self.insert_first(y)
        return
    c = self.head
    while c:
        if c.Data == x:
            a = dnode(y)
            a.next = c
            a.prev = c.prev
            c.prev.next = a
            c.prev = a
            return
        c = c.next
    print("not found")

def del_first(self):
    if self.head is None:
        print("error")
        return
    self.head = self.head.next
    if self.head:
        self.head.prev = None

    def del_last(self):
        if self.head is None:
            print("errot")
            return
        c=self.head
        while c.next:
            c=c.next
        if c.prev:
            c.prev.next=None
        else:
            self.head=None
        del c
    def del_after(self,x):
        if self.head is None:
            print("errot")
            return
        c=self.head
        while c:
            if c.Data==x:
                if c.next:
                    a=c.next
                    c.next=c.next.next
                    if c.next:
                        c.next.prev=c
                    del a
                    return
            c=c.next
        print("not found")
        
def del_before(self, x):
    if self.head is None or self.head.next is None:
        print("error")
        return
    c = self.head.next
    while c:
        if c.Data == x:
            a = c.prev
            if a.prev:
                a.prev.next = c
                c.prev = a.prev
            else:
                self.head = c
                c.prev = None
            del a
            return
        c = c.next
    print("not found")

    def del_x(self,x):
        if self.head is None:
            print("errot")
            return
        if self.head.Data==x:
            self.del_first()
            return
        c=self.head
        while c:
            if c.Data==x:
                c.prev.next=c.next
                if c.next:
                    c.next.prev=c.prev
                del c
                return
            c=c.next
        print("not found")
    def del_all(self):
        while self.head:
            self.del_first()
        


        
