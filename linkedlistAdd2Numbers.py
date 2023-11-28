# 2 Linked List add two numbers
# 1 -> 2 -> 3
# 4 -> 5 -> 6
# output = 321+654 = 975 = 5 -> 7 -> 9

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummyNode = ListNode(0)
    tail = dummyNode
    carry = 0

    while l1 is not None or l2 is not None or carry != 0:
        digit1 = l1.val if l1 is not None else 0
        digit2 = l2.val if l2 is not None else 0

        _sum = digit1 + digit2 + carry
        digit = _sum % 10
        carry = _sum // 10

        newNode = ListNode(digit)
        tail.next = newNode
        tail = tail.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummyNode.next

# Example usage:
if __name__ == "__main__":
    # Creating two linked lists representing numbers
    l1 = ListNode(1, ListNode(2, ListNode(3)))
    l2 = ListNode(4, ListNode(5, ListNode(6)))

    # Adding two numbers represented by linked lists
    result = addTwoNumbers(l1, l2)

    # Displaying the result
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")
