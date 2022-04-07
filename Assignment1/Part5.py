"""
Haily Nguyen, UCP 2022, Mar 26

Part 5:
Challenge: Reverse a Linked List.
"""


class Node:
    def __init__(self, item=None, next_item=None):
        self.item = item
        self.next = next_item

    def __str__(self):
        return str(self.item)


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, item):
        if self.head is None:
            self.tail = self.head = Node(item)
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next
        self.size += 1

    # Iterative method
    # Time complexity O(n)
    # Space complexity O(1)
    def reverse_linked_list1(self, head):
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        self.head = prev

    # Recursive method
    # Time complexity O(n)
    # Space complexity O(n)
    def reverse_linked_list2(self, head):
        # base case
        if head is None or head.next is None:  # if None
            return head

        # recursive approach
        last_item = self.reverse_linked_list2(head.next)
        head.next.next = head
        head.next = None

        # change the header pointer
        return last_item

    # Stack method
    # Time complexity O(n)
    # Space complexity O(n)
    @staticmethod
    def reverse_linked_list3(head):
        stack, cur = [], head
        while cur:
            stack.append(cur)
            cur = cur.next

        head = cur = stack.pop()

        # pop until stack is not empty
        while len(stack) > 0:
            cur.next = stack.pop()
            cur = cur.next

        cur.next = None
        return head

    def __str__(self):
        ll_string = ""
        cur = self.head
        while cur:
            if cur.next is None:
                ll_string += str(cur.item)
                break
            ll_string += str(cur.item) + " -> "
            cur = cur.next
        return ll_string


print("TESTING PROGRAM FOR REVERSING A SINGLY LINKED LIST")
if __name__ == '__main__':
    LL = SLL()
    LL.push(3)  # testPushBackAddsOneNode
    LL.push(4)
    LL.push('a')  # testPushBackAddsOneNode
    LL.push(5)
    LL.push(6)
    LL.push(7)
    print(LL)
    LL.reverse_linked_list1(LL.head)
    print("Iterative:", LL)
    LL.head = LL.reverse_linked_list2(LL.head)
    print("Recursive: ", LL)
    LL.head = LL.reverse_linked_list3(LL.head)
    print("Stack: ", LL)

