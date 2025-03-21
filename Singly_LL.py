class SinglyLinkedList:
    class Node:
        def __init__(self, elem):
            self.elem= elem
            self.next= None
    def __init__(self):
        self.head= None

    # 1. Linked List creation from an array
    def create_from_array(self, arr):
        if not arr:
            return
        self.head= self.Node(arr[0])
        current= self.head
        for i in range(1,len(arr)):
            current.next= self.Node(arr[i])
            current= current.next

    # 2. Printing
    def iterate(self):
        current= self.head
        while current:
            print(f"{current.elem}--> ",end="")
            current= current.next
        print()

    # 3. Counting items
    def count(self):
        count= 0
        temp= self.head
        while temp:
            count+=1
            temp= temp.next
        return count
    
    # 4. Retrieve index of an element
    def index(self, elem):
        idx= 0
        temp= self.head
        while temp:
            if temp.elem == elem:
                return idx
            temp= temp.next
            idx+=1
        return f'Not exist'
    
    # 5. Retrieving node from an index
    def NodeAt(self, idx):
        current_idx= 0
        temp= self.head
        while temp:
            if current_idx == idx:
                return temp
            current_idx+=1
            temp= temp.next    
        return False
    
    # 6. Update value in a specific index
    def update(self, index, new_value):
        node= self.NodeAt(index) #searching node at given index
        if node:
            node.elem= new_value
            return True 
        return False
    
    # 7. Insert a node in the LL
    def insert(self, index, elem):
        new_node= self.Node(elem)
        if index == 0:
            new_node.next=self.head
            self.head= new_node
            return
        prev_node= self.NodeAt(index-1)
        if prev_node:
            new_node.next=  prev_node.next
            prev_node.next= new_node

    # 8. Deletion
    def delete(self, index):
        if index == 0 and self.head:
            self.head= self.head.next
            return
        prev_node= self.NodeAt(index-1)
        if prev_node and prev_node.next:
            prev_node.next= prev_node.next.next

    # 9. Copying a LL
    def copy(self): #original list's address
        new_LL= SinglyLinkedList()
        if not self.head:
            return new_LL
        new_LL.head= self.Node(self.head.elem)
        temp= self.head.next
        new_temp= new_LL.head
        while temp:
            new_temp.next= self.Node(temp.elem)
            temp= temp.next
            new_temp= new_temp.next
        return new_LL

    # 10. Out-of-place reverse
    def out_of_place_reverse(self):
        reversed_LL= SinglyLinkedList()
        temp= self.head
        while temp:
            new_node= self.Node(temp.elem)
            new_node.next= reversed_LL.head
            reversed_LL.head= new_node
            temp= temp.next
        return reversed_LL

    # 11. In place reverse
    def in_place_reverse(self):
        prev= None
        temp= self.head
        while temp:
            next_node= temp.next
            temp.next= prev
            prev=temp
            temp= next_node
        self.head= prev

    
"""Driver Code for Testing"""
if __name__== "__main__":
    list_=SinglyLinkedList()
# 1. Linked List creation from an array
    arr= [1,2,3,4,5]
    list_.create_from_array(arr)
    print("Original List:")
    list_.iterate()
# 2. Iterate through the linked list
    # print("Iterating through the list:")
    # list_.iterate()
# 3. Counting items
    print(f"Total elements of this LL: {list_.count()}")
# 4. Retrieving index of an element
    element_to_find= 6
    print(f"Index of element {element_to_find}: {list_.index(element_to_find)}")
    element_to_find= 2
    print(f"Index of element {element_to_find}: {list_.index(element_to_find)}")
# 5. Retrieving node from given index  
    index_to_find= 4
    print(f"Element at index {index_to_find}: {list_.NodeAt(index_to_find).elem}")
    index_to_find= -1
    print(f"Element at index {index_to_find}: {list_.NodeAt(index_to_find)}")
# 6. Update value in a specific index
    index_to_update= 1
    new_value= 10
    if list_.update(index_to_update, new_value):
        print(f"Updated value at index {index_to_update} to {new_value}")
        list_.iterate()
# 7. Insert a node in the LL
    print("Inserting 99 at index 0:")
    list_.insert(0,99)
    list_.iterate()
    print("Inserting 143 at index 5:")
    list_.insert(5,143)
    list_.iterate()
# 8. Deletion
    print("Removing the node at index 2:")
    list_.delete(2)
    list_.iterate()
    list_.delete(60)
    list_.iterate()
# 9. Copying a LL
    copied_LL=list_.copy()
    print("Copied LinkedList:")
    copied_LL.iterate()
# 10. Out-of-place reverse
    reversed_list = list_.out_of_place_reverse()
    print("Reversed list (out of place):")
    reversed_list.iterate()
# 12. In-place reverse of a linked list
    list_.in_place_reverse()
    print("Reversed list (in place):")
    list_.iterate()
