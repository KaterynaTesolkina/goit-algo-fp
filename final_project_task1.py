class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
            
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def merge_sort_linked_list(head):
    if not head or not head.next:
        return head
    
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None
    
    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(next_to_middle)
    
    sorted_list = sorted_merge(left, right)
    return sorted_list

def get_middle(head):
    if not head:
        return head
    
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def sorted_merge(left, right):
    if not left:
        return right
    if not right:
        return left
    
    if left.data <= right.data:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, right.next)
    
    return result

def merge_two_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    
    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    
    return dummy.next

# Створення списків
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

# Об'єднання двох відсортованих списків
merged_list_head = merge_two_sorted_lists(list1.head, list2.head)
merged_list = LinkedList()
merged_list.head = merged_list_head

print("Об'єднаний список:")
merged_list.print_list()

# Сортування злиттям
unsorted_list = LinkedList()
unsorted_list.append(4)
unsorted_list.append(3)
unsorted_list.append(1)
unsorted_list.append(5)
unsorted_list.append(2)

print("Несортований список:")
unsorted_list.print_list()

sorted_list_head = merge_sort_linked_list(unsorted_list.head)
sorted_list = LinkedList()
sorted_list.head = sorted_list_head

print("Відсортований список:")
sorted_list.print_list()

# Реверсування списку
reversed_list_head = reverse_linked_list(merged_list.head)
reversed_list = LinkedList()
reversed_list.head = reversed_list_head

print("Реверсований список:")
reversed_list.print_list()