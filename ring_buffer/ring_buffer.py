from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    '''
    When the ring buffer is full and a new element is inserted
    the oldest element in the ring buffer is overwritten with the newest element.
    '''
    def append(self, item):
        pass 
        '''

        current = self.storage.tail
        create a new node 
        check if self.storage.length is equal to capacity
        if true: 
            replace head with new node
        else: 
          add new node as tail  


        '''

        if self.storage.length == self.capacity: 
            if self.current == self.storage.head: 
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head.next
            elif self.current == self.storage.tail: 
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.storage.tail.next = self.storage.head
                self.current = self.storage.tail.next
            else: 
                self.current.value = item
                self.current = self.current.next
        
        else: 
            if self.storage.length == 0: 
                self.storage.add_to_tail(item)
                self.current = self.storage.tail
            else: 
                self.storage.add_to_tail(item)
                self.storage.tail.next = self.storage.head
            

    '''
    returns all of the elements in the buffer in a list in their given order. 
    It should not return any `None` values
     
    '''
    def get(self):
        # Note:  This is the only [] allowed
        current = self.storage.head.next
        list_buffer_contents = [self.storage.head.value]
        
        while current.prev is not None: 
            
            list_buffer_contents.append(current.value)
            current = current.next
            
           
            
        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
