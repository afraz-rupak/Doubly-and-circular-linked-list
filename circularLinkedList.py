class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class circularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            cur = self.head
            while True:
                cur = cur.next
                if cur.next == self.head:
                    break
            cur.next = new_node
            new_node.prev = cur
            new_node.next = self.head
            self.head.prev = new_node.next

    def insertFront(self, data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = newNode
            newNode.prev = newNode

        else:
            newNode = node(data)
            self.head.prev = newNode
            newNode.next = self.head
            cur = self.head
            while True:
                cur = cur.next
                if cur.next == self.head:
                    break
            self.head = newNode
            cur.next = self.head
            self.head.prev = cur.next

    def listlength(self):
        cur = self.head
        length = 0
        while True:
            length += 1
            cur = cur.next
            if cur == self.head:
                break
        return length

    def insertAt(self, data, pos):
        new_node = node(data)
        if pos < 1 or pos > self.listlength():
            print(pos, "is Invalid!")
        elif pos == 1:
            self.insertFront(data)
        else:
            cur = self.head
            c = 0
            while cur.next:
                if c == pos - 1:
                    prev = cur.prev
                    prev.next = new_node
                    new_node.next = cur
                    new_node.prev = prev
                    cur.prev = new_node
                    return
                c += 1
                cur = cur.next

    def insertBefore(self, key, data):
        cur = self.head
        c = 0
        while cur:
            if c == 0 and cur.data == key:
                self.insertFront(data)
                return
            elif cur.data == key:
                new_node = node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
                return
            cur = cur.next
            c = 1

    def asc_ordered_list(self, data):
        if self.head == None:
            return
        else:
            curr = self.head
            while curr.next:
                nxt = curr.next
                while nxt:
                    if curr.data > nxt.data:
                        curr.data, nxt.data = nxt.data, curr.data
                    nxt = nxt.next
                curr = curr.next

        curr = None
        new_node = node(data)

        if self.head == None:
            self.head = new_node

        elif self.head.data >= new_node.data:
            new_node.next = self.head
            new_node.next.prev = new_node
            self.head = new_node

        else:
            curr = self.head
            while curr.next and curr.next.data < new_node.data:
                curr = curr.next

            new_node.next = curr.next

            if curr.next:
                new_node.next.prev = new_node

            curr.next = new_node
            new_node.prev = curr

    def deleteFront(self):
        cur = self.head
        if cur.next == self.head:
            cur = None
            self.head = None
            return
        else:
            nxt = cur.next
            while True:
                cur = cur.next
                if cur.next == self.head:
                    break
            cur.next = nxt
            nxt.prev = cur.next
            self.head.next = nxt
            self.head.prev = cur.next
            cur = None
            self.head = nxt
            return

    def deleteLast(self):
        cur = self.head
        while True:
            cur = cur.next
            if cur.next == self.head:
                break
        prev = cur.prev
        prev.next = self.head
        self.head.prev = prev
        cur.prev = None
        cur.next = None
        cur = None

    def deleteValue(self, key):
        cur = self.head
        c = 0
        while True:
            if cur.data == key and cur == self.head:
                c = 1
                if cur.next == self.head:
                    cur = None
                    self.head = None
                    return
                else:
                    self.deleteFront()
                    return
            elif cur.data == key:
                c = 1
                nxt = cur.next
                prev = cur.prev
                prev.next = nxt
                nxt.prev = prev
                cur.prev = None
                cur.next = None
                cur = None
                return

            elif cur.data == key and cur.next == self.head:
                c = 1
                self.deleteLast()
                break
                return
            cur = cur.next
        if c == 0:
            print("The value is not present in the list.")
            return

    def deleteAt(self, position):
        cur = self.head
        if position < 0 or position > self.listlength():
            print(position, "is Invalid position")
        elif position == 1:
            self.deleteFront()
            return
        elif position == self.listlength():
            self.deleteLast()
            return
        else:
            c = 0
            while True:
                if c == position - 1:
                    prev = cur.prev
                    prev.next = cur.next
                    cur.next.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                c += 1
                cur = cur.next
                if cur == self.head:
                    break

    def print_list(self):
        l = self.listlength()
        if l:
            cur = self.head
            while True:
                print(cur.data)
                cur = cur.next
                if cur == self.head:
                    break
        else:
            print("List is empty")

    def searchIndexOfValue(self, posi):
        if posi < 0 or posi >= self.listlength():
            print(posi, "is Invalid!")
            return
        cur = self.head
        length = 0
        while True:
            if length == posi:
                print("The value of the position ", posi, "is", cur.data)
                return
            length += 1
            cur = cur.next
            if cur == self.head:
                break

    def valueOfIndex(self, data):
        cur = self.head
        length = 0
        while True:
            if cur.data == data:
                print(data, "data index : ", length)
                return
            length += 1
            cur = cur.next
            if cur == self.head:
                break

    def updateFront(self, data):
        cur = self.head
        cur.data = data

    def updateLast(self, data):
        cur = self.head
        while True:
            cur = cur.next
            if cur.next == self.head:
                break
        cur.data = data

    def updateAt(self, pos, data):
        if pos < 0 or pos >= self.listlength():
            print(pos, "is Invalid !")
            return
        cur = self.head
        length = 0
        while True:
            if length == pos:
                cur.data = data
                return
            length += 1
            cur = cur.next
            if cur == self.head:
                break

    def updateValue(self, value, upValue):
        cur = self.head
        c = 0
        while True:
            if cur.data == value:
                c = 1
                cur.data = upValue
                print("Value is updated.")
                return
            cur = cur.next
            if cur == self.head:
                break
        if c == 0:
            print("The value is not present in the list.")


lis = circularDoublyLinkedList()


def start():
    print('''
    option list:
    1.Append(InsertLast)
    2.Insert Font
    3.Insert At
    4.Insert Before Value
    5.Insert Sorted Order
    6.Update Front
    7.Update Last
    8.Update At
    9.Update Value
    10.Delete Front
    11.Delete Last
    12.Delete At
    13.Delete Value
    14.Value Of Index
    15.Search Index Of Value
    16.Print List
    17.Exit
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
        i = int(input("Data the element: "))
        d = int(input("Index the element: "))
        lis.insertAt(i, d)
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
        # Update Front
        lis.updateFront(int(input("Update 1st index the element: ")))
        start()
    elif op == 7:
        # updateLast
        lis.updateLast(int(input("Update last index the element: ")))
        start()
    elif op == 8:
        # Update At
        lis.updateAt(int(input("Update index the element: ")), int(input("Update data enter the element: ")))
        start()
    elif op == 9:
        # Update Value
        lis.updateValue(int(input("Update data the element: ")), int(input("replace data enter the element: ")))
        start()
    elif op == 10:
        # deleteFront
        lis.deleteFront()
        start()
    elif op == 11:
        # Delete Last
        lis.deleteLast()
        start()
    elif op == 12:
        # Delete At
        lis.deleteAt(int(input("Delete index of the element: ")), )
        start()
    elif op == 13:
        # Delete Value
        lis.deleteValue(int(input("Enter data which need to delete : ")))
        start()
    elif op == 14:
        # Value Of Index
        lis.valueOfIndex(int(input("enter a data for it's index : ")))
        start()
    elif op == 15:
        # Search Index Of Value
        lis.searchIndexOfValue(int(input("Enter the value of position : ")))
        start()
    elif op == 16:
        # print
        lis.print_list()
        start()
    elif op == 17:
        print("Exit the program")


print("Welcome to Circular linked list")
start()
