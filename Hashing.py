import numpy as np
class Node:
    def __init__(self, key, value, next):
        self.key= key
        self.value= value
        self.next= next

#HashTable class implementing forward chaining
class HashTable:
    def __init__(self, size):
        self.size= size
        self.hashtable= np.array([None]*size)

    #Hash function using modulus operation
    def hash_function(self, key):
        return key% self.size
    
    def insert(self, key, value):
        index= self.hash_function(key)
        new_node= Node(key, value, None)
        if self.hashtable[index] == None:
            self.hashtable[index] = new_node
        else:      
            """ forward chaining
            previous: a-->b-->c and new_node=d-->
            d-->a-b-c
            index==[d-->]
            """ 
            new_node.next= self.hashtable[index]
            self.hashtable[index]= new_node

    #funzzz
    def insert2(self, key, value):
        index= self.hash_function(key)
        new_node= Node(key, value, None)
        if self.hashtable[index] == None:
            self.hashtable[index]= new_node
        else:
            temp= self.hashtable[index]
            while temp.next!=None:
                temp= temp.next
            temp.next= new_node

    def delete(self, key):
        index= self.hash_function(key)
        prev= self.hashtable[index]
        if self.hashtable[index].key == key:
            temp= self.hashtable[index] #collecting deleted value and storing it for garbage cleaning
            self.hashtable[index] = self.hashtable[index].next
        else:
            temp= self.hashtable[index].next
            while temp!=None:
                if temp.key == key:
                    prev.next= temp.next
                    break
                else:
                    prev= temp
                    temp= temp.next
        temp.value= None
        temp.next= None
        temp= None

    def search(self, key):
        index= self.hash_function(key)
        temp= self.hashtable[index] #works like head in LL
        while temp!=None:
            if temp.key == key:
                return temp.value
            temp= temp.next
        return
        
    # Display method
    def display(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            current = self.hashtable[i]
            while current:
                print(f"({current.key}, {current.value}) ->", end=" ")
                current = current.next
            print("None")

"""Main function for testing"""
if __name__=="__main__":
    ht= HashTable(5)
    ht.insert(12, "Apple")
    ht.display()
    print("-------------------")
    ht.insert(17, "Banana")
    ht.insert(10, "Grapes")
    ht.display()
    print("-------------------")
    ht.insert(23, "Watermelon")
    ht.insert(15, "Pineapple")
    ht.delete(10)
    ht.insert(10, "Updated Grapes")
    ht.display()
    print("-------------------")
    print("Search for key 10:",ht.search(10))
    