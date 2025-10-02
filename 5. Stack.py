class Node:
    def __init__(self, elem, next=None):
        self.elem= elem
        self.next= next

class Stack:
    def __init__(self):
        self.top= None

    def push(self, elem):
        newNode= Node(elem)
        newNode.next= self.top
        self.top= newNode

    def pop(self):
        if self.top == None: #or, if self.is_empty:
            raise IndexError("Stack is already empty")
        removed= self.top
        self.top= self.top.next
        return removed.elem
    
    def peek(self):
        if self.top == None:
            raise IndexError("Stack is empty")
        return self.top.elem
    
    def is_Empty(self):
        if self.top == None:
            return True
        return False
    
    def display_stack(self):
        current = self.top
        print("Stack (top to bottom): ", end="")
        while current:
            print(f"{current.elem} -> ", end="")
            current = current.next
        print("None")

    def __str__(self):
        return str(self.elem)
    
def filter_and_sort_stack(st,k):
    st2= Stack()
    while not st.is_Empty():
        current=st.pop()
        if current<=k:
            st2.push(current)
    while not st2.is_Empty():
        temp=st2.pop()
        while not st.is_Empty() and st.top.elem>temp:
            st2.push(st.pop())
        st.push(temp)
    return st
    
'''Tester Code'''
st= Stack()
st.push(4)
st.push(10)
st.push(20)
st.display_stack()
print(f"Popped Element:{st.pop()}")
st.display_stack()
print(f"Peeked Element:{st.peek()}")
print("----------------------")
st=Stack()
st.push(50)
st.push(40)
st.push(70)
st.push(20)
st.push(10)
st.push(80)
st.push(30)
k=40
print("------------------------------")
print()
st.display_stack()
filter_and_sort_stack(st,k).display_stack()




