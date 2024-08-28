class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def add_(l1, l2):
    result = ListNode()
    r = result
    carry = 0


    while l1 or l2 or carry:
        if l1:
            val1 = l1.value
        else:
            val1=0
        if l2:
            val2 = l2.value
        else:
            val2=0



        total = val1 + val2 + carry

        carry = (total)// 10

        r.next = ListNode((total)% 10)

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

        r = r.next

    return result.next

def display(result):
    while result:
        print(result.value, end=" -> ")
        result = result.next
    print("None")


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))


result = add_(l1, l2)


print("Result:")
display(result)
# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def print(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data)+' --> '
#             itr = itr.next
#         print(llstr)
#
#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count+=1
#             itr = itr.next
#
#         return count
#
#     def insert_at_begining(self, data):
#         node = Node(data, self.head)
#         self.head = node
#
#
#     def remove_at(self, index):
#
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 break
#
#             itr = itr.next
#             count+=1
#
#     def remove_atbackindex(self,backindex):
#         i=0
#         itr=self.head
#
#         while itr:
#             if self.get_length()-i==backindex:
#                 break
#             itr=itr.next
#             i+=1
#         self.remove_at(i)
#
#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_begining(data)
#
#
#
#
#
# if __name__ == '__main__':
#     ll = LinkedList()
#
#
#     ll.insert_values([45,7,12,567,99])
#
#     ll.print()
#     ll.remove_atbackindex(3)
#     ll.print()


