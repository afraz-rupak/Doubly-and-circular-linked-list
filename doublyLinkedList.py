class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node

        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def insertFront(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insertAfter(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                nxt.prev = new_node
            cur = cur.next

    def insertBefore(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
            cur = cur.next


    def deleteFront(self):
        cur = self.head
        self.head = self.head.next
        self.head.prev = cur.prev
        cur = self.head

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:

                if not cur.next:
                    cur = None
                    self.head = None
                    return


                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur.data == key:

                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return

                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def deleteLast(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        temp = cur.prev
        temp.next = None

    def updateValue(self, old, new):
        cur = self.head
        while cur.next.data != old:
            cur = cur.next
        cur.next.data = new
        return

    def updateFront(self, data):
        self.head.data = data

    def updateLast(self, data):

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.data = data

    def asc_ordered_list(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        if temp.data > data:
            new_node.next = temp
            self.head = new_node
            return

        while temp.next:
            if temp.next.data > data:
                break
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def search_list(self, key):
        cur = self.head
        p = 1
        while cur:
            if cur.data == key:
                break
            p += 1
            cur = cur.next
        print(key, "data index : ", p)

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


lis = DoublyLinkedList()

def start():
    print('''
    1.Append (insert last)
    2.Insert Front
    3.Insert After
    4.Insert Before
    5.Insert Sorted Order
    6.updateFront
    7.updateLast
    8.updateAfter
    9.Delete any node
    10.Delete Front
    11.Delete last
    12.Search Index Of Value
    13.PrintList
    14. Exit
    ''')
    op = int(input("Enter the option: "))
    if op == 1:
        lis.append(int(input("Append the element: ")))
        start()
    elif op == 2:
        lis.insertFront(int(input("InsertFront the element: ")))
        start()
    elif op == 3:
        # insertAt
        i = int(input("index the element: "))
        d = int(input("data the element: "))
        lis.insertAfter(i, d)
        start()
    elif op == 4:
        # insertBeforeValue
        lis.insertBefore(int(input("index the element: ")), int(input("data the element: ")))
        start()
    elif op == 5:
        # insertSortedOrder
        lis.asc_ordered_list(int(input("Append (insert Sorted Order) the element: ")))
        start()
    elif op == 6:
        lis.updateFront(int(input("Update 1st index the element: ")))
        start()
    elif op == 7:
        # updateLast
        lis.updateLast(int(input("Update last index the element: ")))
        start()
    elif op == 8:
        # updateAt
        lis.updateValue(int(input("data the element: ")), int(input("update data the element: ")))
        start()
    elif op == 9:
        # deleteFront
        lis.delete(int(input("you can delete any node. please enter data for delete : ")))
        start()
    elif op == 10:
        # deleteFront
        lis.deleteFront()
        start()

    elif op == 11:
        # deleteLast
        lis.deleteLast()
        start()

    elif op == 12:
        # search
        lis.search_list(int(input("data the element: ")))
        start()
    elif op == 13:
        # print deleteLast
        lis.print_list()
        start()
    elif op == 14:
        print("Exit the program")


print("Welcome to Doubly linked list")
start()
