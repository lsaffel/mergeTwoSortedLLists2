# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
def mergeTwoLists(list1, list2):
    # if either list is empty, return the other list
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    a = list1
    b = list2
    list3 = None
    c = None

    while a is not None and b is not None:
        # there are more nodes in both lists
        if a.val <= b.val:
            if list3 is None:
                list3 = a
                c = list3
            else:
                c.next = a
                c = c.next
            a = a.next
        else:
            if list3 is None:
                list3 = b
                c = list3
            else:
                c.next = b
                c = c.next
            b = b.next
    if a is None:
        c.next = b
    else:
        c.next = a
    return list3


if __name__ == '__main__':
    # list3 = mergeTwoLists(list1, list2)
    print("hello")


