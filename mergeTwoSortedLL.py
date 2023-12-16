class LinkedListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def mergeLL(self,l1:LinkedListNode, l2:LinkedListNode):
        dummy = LinkedListNode()
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l2
        elif l2:
            tail.next = l1
        return dummy.next
    
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    # Create linked list 1: 1 -> 3 -> 5
    l1 = LinkedListNode(1)
    l1.next = LinkedListNode(3)
    l1.next.next = LinkedListNode(5)

    # Create linked list 2: 2 -> 4 -> 6
    l2 = LinkedListNode(2)
    l2.next = LinkedListNode(4)
    l2.next.next = LinkedListNode(6)

    # Merge the linked lists
    solution = Solution()
    merged_list = solution.mergeLL(l1, l2)

    # Print the merged list
    print("Merged Linked List:")
    printLinkedList(merged_list)
