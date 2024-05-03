class Cons:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def to_array(self):
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])
    def __str__(self):
        return self.to_array()

    @classmethod
    def from_array(cls, arr):
        if not arr:
            return None
        else:
            return cls(arr[0], cls.from_array(arr[1:]))

    def filter(self, fn):
        if self.tail is None:  # Base case: end of the list
            if fn(self.head):
                return Cons(self.head, None)
            else:
                return None
        else:
            filtered_tail = self.tail.filter(fn)
            if fn(self.head):
                return Cons(self.head, filtered_tail)
            else:
                return filtered_tail  # Return the filtered tail directly
    def map(self, fn):
        if self.tail is None:  # Base case: end of the list
            return Cons(fn(self.head), None)
        else:
            return Cons(fn(self.head), self.tail.map(fn)) # Return the filtered tail directly
        



digits = Cons.from_array(["1","2","3","4","5"])
integers = digits.map(int) \
                 .filter(lambda n: n > 3) \
                 .to_array()  # yields [4,5]
print(integers)