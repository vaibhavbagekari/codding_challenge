class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class NodeOperation:
    def pushNode(self,head_ref, data_val):
        new_node = Node(data_val)
        new_node.next = head_ref
        head_ref = new_node
        return head_ref
    
    def printNode(self,head):
        while (head != None):
            print("%d->" % head.data,end="")
            head = head.next
        print("Null")

    def getLen(self, head):
        temp = head
        len = 0

        while (temp != None):
            len += 1
            temp = temp.next

        return len
    def printMiddle(self, head):
        if head != None:
            len = self.getLen(head)
            temp = head

            midIdx = len / 2
            while midIdx!=0:
                temp = temp.next
                midIdx -= 1

            print("the middle element is : ", temp.data)

head = None
temp = NodeOperation()
head = temp.pushNode(head, 5)
head = temp.pushNode(head, 4)
head = temp.pushNode(head, 3)
head = temp.pushNode(head, 2)
head = temp.pushNode(head, 1)
temp.printNode(head)
temp.printMiddle(head)
