**`Chapter 16 (Python OOP)`**

### **`Task 1: Basic Class and Object Creation`**

**`Problem:`**

1. `Create a class Car with the following attributes (Use the __init__ method):`  
   * `make (string)`  
     * `model (string)`  
     * `year (integer)`  
   2. `Create an instance of the class with values for make, model, and year.`  
   3. `Print the instance's attributes.`

**`Example Output:`**

`Make: Toyota`  
`Model: Camry`  
`Year: 2020`

---

### **`Task 2: Constructor Method (__init__)`**

**`Problem:`**

1. `Create a class Rectangle with the following attributes:`  
   * `width (integer)`  
     * `height (integer)`  
   2. `Use the __init__ method to initialize the attributes when an object is created.`  
   3. `Create an instance of Rectangle and print its width and height.`

**`Example Output:`**

`Width: 5`  
`Height: 10`

---

### **`Task 3: Instance Method`**

**`Problem:`**

1. `Modify the Rectangle class from Task 2 to include a method area() that calculates and returns the area of the rectangle (width * height).`  
   2. `Create an instance and call the area() method to get the rectangle's area.`

**`Example Output:`**

`Area: 50`  
---

### **`Task 4: Inheritance`**

**`Problem:`**

1. `Create a class Vehicle with the attributes make, model, and year.`  
   2. `Create a subclass ElectricCar that inherits from Vehicle and adds the attribute battery_size (integer).`  
   3. `Create an instance of ElectricCar, and print the attributes from both Vehicle and ElectricCar.`

**`Example Output:`**

`Make: Tesla`  
`Model: Model S`  
`Year: 2022`  
`Battery Size: 100`

---

### **`Task 5: Method Overriding`**

**`Problem:`**

1. `In Task 4, override the __init__ method of ElectricCar to initialize both the attributes of Vehicle and ElectricCar (using super()).`  
   2. `Call the __init__ method from ElectricCar and print the values of all attributes.`

**`Example Output:`**

`Make: Tesla`  
`Model: Model X`  
`Year: 2023`  
`Battery Size: 120`

---

### **`Task 6: Dunder Method (__str__)`**

**`Problem:`**

1. `Create a class Book with attributes title, author, and year_published.`

`Override the __str__() method to return a string in the format:`  
`"[Title] by [Author] (Published: [Year])"`

`Create an instance of Book and print it to see the custom string representation.`

**`Example Output:`**

`The Great Gatsby by F. Scott Fitzgerald (Published: 1925)`

---

### **`Task 7: Dunder Method (__eq__)`**

**`Problem:`**

1. `Create a class Person with attributes name and age.`  
   2. `Override the __eq__() method to compare two Person objects based on their name and age.`  
   3. `Create two instances of Person and check if they are equal using the == operator.`

**`Example Output:`**

`Are they equal? True`

---

### **`Task 8: Class Method and Static Method`**

**`Problem:`**

1. `Create a class Employee with the following:`  
   * `name (string)`  
     * `salary (float)`  
   2. `Add a class method from_string() that creates an Employee instance from a string in the format "name, salary".`  
   3. `Add a static method is_high_salary() that checks if an employee's salary is above 100,000.`  
   4. `Demonstrate creating an employee from a string and checking their salary.`

**`Example Output:`**

`Employee name: Alice, Salary: 120000`  
`Is the salary high? True`

---

### **`Bonus Task 9: Create a Custom Iterator for a Fibonacci Sequence`**

#### **`Problem:`**

`Create a custom iterator class called FibonacciIterator that generates numbers in the Fibonacci sequence. The iterator should take an input n, which specifies the maximum number of Fibonacci numbers to generate.`

1. `Implement the __iter__ and __next__ methods to make the class an iterator.`  
2. `Use the iterator to generate and print the Fibonacci sequence up to n terms.`

**`Example Input:`**

`fib = FibonacciIterator(5)`  
`for num in fib:`  
    `print(num)`

**`Expected Output:`**

`0`  
`1`  
`1`  
`2`  
`3`

**`Challenge:`**

1. `Extend the iterator to raise a StopIteration exception when the maximum n is reached.`  
2. `Use the iterator with the list() function, e.g., list(FibonacciIterator(7)) should output [0, 1, 1, 2, 3, 5, 8].`

---

`These tasks cover a range of OOP principles from basic classes and objects to advanced techniques like method overriding, dunder methods, inheritance, and class/static methods.`

### 

