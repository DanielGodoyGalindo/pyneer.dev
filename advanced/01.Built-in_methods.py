# TODO: Complete the magic methods exercises

class Person:
    def __init__(self, name, age):
        # Initialize name and age attributes
        self.name = name
        self.age = age
    
    def __str__(self):
        # Return user-friendly string: "Person: {name}, Age: {age}"
        return f"Person: {self.name}, Age: {self.age}"
    
    def __repr__(self):
        # Return developer-friendly string: "Person('{name}', {age})"
        return f"Person('{self.name}', {self.age})"
    
    def __eq__(self, other):
        # Return True if both name and age are equal
        return True if self.age == other.age and self.name == other.name else False

class Counter:
    def __init__(self, start, end):
        # Initialize start and end values
        # Add current attribute set to start
        self.start = start
        self.end = end
        self.current = start
    
    def __iter__(self):
        # Return self (this object is the iterator)
        return self
    
    def __next__(self):
        # If current > end, raise StopIteration
        # Otherwise, increment current and return previous value
        if self.current > self.end:
            raise StopIteration
        self.current+=1
        return self.current-1

class MyList:
    def __init__(self, items):
        # Store items as list
        self.items = list(items)
    
    def __len__(self):
        # Return length of items
        return len(self.items)
    
    def __getitem__(self, index):
        # Return item at index
        return self.items[index]
    
    def __contains__(self, item):
        # Return True if item is in items
        return True if item in self.items else False

class Calculator:
    def __init__(self, value=0):
        # Initialize with value
        self.value = value
    
    def __call__(self, operation, num):
        # Make object callable
        # If operation is 'add', add num to value
        # If operation is 'multiply', multiply value by num
        # Return self (for chaining)
        if operation == 'add':
            self.value += num
        if operation == 'multiply':
            self.value *= num
        return self 
    
    def __str__(self):
        # Return current value as string
        return str(self.value)

# Test your classes
p1 = Person("Alice", 25)
p2 = Person("Alice", 25)
print("Person str:", str(p1))
print("Person repr:", repr(p1))
print("Persons equal:", p1 == p2)

counter = Counter(1, 5)
print("Counter values:", list(counter))

my_list = MyList([1, 2, 3, 4, 5])
print("Length:", len(my_list))
print("Item at index 2:", my_list[2])
print("Contains 3:", 3 in my_list)

calc = Calculator(10)
calc("add", 5)("multiply", 2)
print("Calculator result:", str(calc))