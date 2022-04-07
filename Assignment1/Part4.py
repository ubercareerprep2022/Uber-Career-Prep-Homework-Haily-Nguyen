"""
Haily Nguyen, UCP 2022, Mar 26

Part 4:
Challenge: Implement a Singly Linked List class.
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

    def ll_size(self):
        return self.size

    def push_back(self, item):
        if self.head is None:
            self.tail = self.head = Node(item)
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next
        self.size += 1
        return self.tail.item

    def pop_back(self):
        if self.head is None:
            print("Empty!")
        else:
            popped_node = self.tail.item
            print("The popped node is", popped_node)
            cur = self.head
            while cur:
                if cur.next.next is None:
                    cur.next = None
                    self.tail = cur
                cur = cur.next
            self.size -= 1
        return popped_node

    def insert(self, index, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.size += 1
        elif index > self.size - 1 or index < 0:
            print("Invalid index!")
        else:
            cur = self.head
            # reach the index
            count = 0
            while cur and count < index:
                cur = cur.next
                count += 1
                # insert the item
                new_node.next = cur.next
                cur.next = new_node
            self.size += 1

    def remove(self, index):
        if self.head is None:
            return
        elif index > self.size - 1 or index < 0:
            print("Invalid index!")
        elif index == 0:
            self.head = self.head.next
            self.size -= 1
        else:
            count = 0
            cur = prev = temp = self.head
            while cur:
                if count == index:
                    temp = cur.next
                    break
                prev = cur
                cur = cur.next
                count += 1
            prev.next = temp
            self.size -= 1

    def elementAt(self, index):
        if self.head is None:
            print("Empty!")
        else:
            cur = self.head
            count = 0
            # reach the index
            while cur:
                if count == index:
                    return cur.item
                    break
                count += 1
                cur = cur.next

    # The idea is marking all the item we traverse through (in this case, I marked them as 1)
    # Time complexity O(n)
    def hasCycle(self, head):
        if self.head is None:
            return False
        else:
            while head:
                if head.item == 1:
                    return True
                else:
                    head.item = 1
                    head = head.next
            return False

    # Bonus
    # The idea is using stack ADT and check if the items in the stack is the same as the item
    # we pop from the back of stack
    # Time complexity O(n)
    @staticmethod
    def isPalindrome(head):
        cur = head
        stack = []
        is_palindrome = True

        # push elements to the stack
        while cur:
            stack.append(cur.item)
            cur = cur.next

        # traverse the list again and check by popping from the stack
        while head:
            visited = stack.pop()
            if head.item is visited:
                is_palindrome = True
            else:
                is_palindrome = False
                break
            head = head.next
        return is_palindrome

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


print("TESTING PROGRAM FOR SINGLY LINKED LIST")
if __name__ == '__main__':
    LL = SLL()
    LL.push_back(3)  # testPushBackAddsOneNode
    LL.push_back('a')  # testPushBackAddsOneNode
    LL.push_back(5)
    LL.push_back(6)
    LL.push_back(7)
    print("Initial linked list: ", LL)
    LL.remove(0)  # testEraseRemovesCorrectNode
    print("Removing the first element:", LL)
    LL.remove(5)  # testEraseDoesNothingIfNoNode
    print("Removing the fifth element (no change): ", LL)
    LL.insert(1, 2)  # testPushBackAddsOneNode
    print("Inserting one element: ", LL)
    LL.pop_back()  # testPopBackRemovesCorrectNode
    print("Popping last element: ", LL)
    print("Element at position 3: ", LL.elementAt(3))  # testElementAtReturnNode
    print("Element at position 5: ", LL.elementAt(5))  # testElementAtReturnsNoNodeIfIndexDoesNotExist
    print("Size: ", LL.ll_size())  # testSizeReturnsCorrectSize
    print("Is it palindrome? ", LL.isPalindrome(LL.head))
    LL.pop_back()
    LL.push_back(2)
    LL.push_back(5)
    LL.push_back('a')
    print("Is it palindrome? ", LL.isPalindrome(LL.head))
    print("Palindrome linked list: ", LL)
    LL.head.next.next.next.next = LL.head.next.next
    print("Has cycle? ", LL.hasCycle(LL.head))


