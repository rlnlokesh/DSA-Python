class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class CicularLinkedList:
    def __init__(self):
        self.head=None
    def printt(self):
        if self.head is None:
            print("Linked List Empty")
            return
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+' --> '
            itr=itr.next
            if itr==self.head:
                break
        print(llstr)

    def get_lenght(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
            if itr==self.head:
                break
        return  count

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        if self.head is None:
            node.next=node
            return
        itr=self.head
        while itr.next!=self.head:
            itr=itr.next
        itr.next=node
        self.head=node


    def insert_at_end(self,data):
        node=Node(data,self.head)
        if self.head is None:
            node.next=node
            self.head=node
        itr = self.head
        while itr.next!=self.head:
            itr=itr.next
        itr.next=node


    def insert_at(self,index,data):
        if index<0 or index>self.get_lenght():
            print("Invalid Index")
        if index==0:
            return self.insert_at_beginning()
        if index==self.get_lenght():
            return self.insert_at_end()
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1

    def find__(self,data):
        count=0
        itr=self.head
        while itr:
            if itr.data==data:
                print("index is ",count)
                break
            itr=itr.next
            count+=1



    def insert_values(self,datalist):
        self.head=None
        for data in datalist:
            self.insert_at_end(data)

    def remove_at(self,index):
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1





    def remove_by_value(self,data):
        count=0
        itr=self.head
        while itr:
            if itr.data==data:
                self.remove_at(count)
                break
            itr=itr.next
            count+=1

    def remove_at_beginning(self):
        return self.remove_at(0)
    def remove_at_end(self):
        return self.remove_at(self.get_lenght()-1)



if __name__ == '__main__':
    ll=CicularLinkedList()
    ll.insert_values([2,3,4,5,6,7])
    ll.insert_at_beginning(33)
    ll.insert_at_end(56)
    ll.insert_at(4,43)
    ll.printt()
    ll.find__(56)
    ll.remove_at(2)
    ll.printt()
    ll.remove_by_value(4)
    ll.printt()