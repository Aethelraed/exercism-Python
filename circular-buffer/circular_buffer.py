class BufferFullException(BufferError): pass
class BufferEmptyException(BufferError): pass


class CircularBuffer:
    def __init__(self, capacity): self.capacity,self.data = capacity,[]
    
    def read(self):
        if len(self.data) ==0: raise BufferEmptyException("Circular buffer is empty")
        return self.data.pop(0)
        

    def write(self, data):
        if len(self.data) == self.capacity: raise BufferFullException("Circular buffer is full")
        self.data.append(data)   

    
    def overwrite(self, data):
        if len(self.data) == self.capacity: self.read()
        self.write(data)
            

    def clear(self):  self.data = []
