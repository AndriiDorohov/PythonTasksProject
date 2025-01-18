**`Chapter 5 (Python loops)`**

### **`Task 1: Loop through a List and Modify Elements`**

**`Problem:`**

1. `Create a list of integers: [3, 7, 1, 9, 4].`  
   2. `Use a for loop to iterate through the list and:`  
      * `Multiply each number by 3.`  
      * `Replace numbers greater than 15 with 'Too large'.`  
      * `Print the modified list after the loop.`

**`Example Output:`**

`[9, 21, 3, 'Too large', 12]`

`Consider checking on enumerate built-in function`

---

### **`Task 2: Sum of Even Numbers in a List`**

**`Problem:`**

1. `Create a list of integers: [10, 20, 30, 40, 50, 11, 17, 22].`  
   2. `Use a for loop to iterate through the list and calculate the sum of only the even numbers.`  
   3. `Print the sum of even numbers and how many even numbers were found.`

**`Example Output:`**

`Sum of even numbers: 172`  
`Number of even numbers: 6`

---

### **`Task 3: Loop through a Range with Step`**

**`Problem:`**

1. `Use a for loop with range() to print every third number between 10 and 30 (inclusive).`  
   2. `After printing the numbers, print the sum of these numbers.`

**`Example Output:`**

`10`  
`13`  
`16`  
`19`  
`22`  
`25`  
`28`  
`Sum: 133`

---

### **`Task 4: Nested Loops for Matrix Printing`**

**`Problem:`**

`Create a 2D list (matrix) representing a grid of numbers:`

`matrix = [`  
    `[1, 2, 3],`  
    `[4, 5, 6],`  
    `[7, 8, 9]`  
`]`

1. `Use a nested for loop to print each row in the matrix on a new line.`  
2. `Modify the program to sum the values in each row and print the sum after each row.`

**`Example Output:`**

`Row: [1, 2, 3] Sum: 6`  
`Row: [4, 5, 6] Sum: 15`  
`Row: [7, 8, 9] Sum: 24`  
---

### **`Task 5: Reverse List and Print Indices`**

**`Problem:`**

1. `Create a list of strings: ['apple', 'banana', 'cherry', 'date', 'elderberry'].`  
   2. `Use a loop to:`  
      * `Reverse the list without using the reverse() function.`  
      * `Print each element along with its index in the reversed list.`

**`Example Output:`**

`Index 0: elderberry`  
`Index 1: date`  
`Index 2: cherry`  
`Index 3: banana`  
`Index 4: apple`

`Consider checking on enumerate built-in function`

---

### **`Task 6: Modify Values in a Nested List`**

#### **`Problem:`**

`You are given a nested list that represents a grid of numbers. Your task is to use nested loops to modify some of the values in the grid based on specific conditions.`

**`Input:`** `A 2D list (nested list) containing integers. Example:`

`grid = [`  
    `[1, 2, 3],`  
    `[4, 5, 6],`  
    `[7, 8, 9]`  
`]`

**`Conditions:`**

1. `If a number is even, double its value.`  
2. `If a number is odd, replace it with 0.`

**`Output:`** `The modified grid after applying the changes.`  
`Example output for the given grid:`

`[`   
    `[0, 4, 0],`   
    `[8, 0, 12],`   
    `[0, 0, 0]`   
`]`

---

### **`Task 7: Modify a List Using a While Loop`**

#### **`Problem:`**

`You are given a list of integers. Use a while loop to iterate through the list and modify the values based on the following conditions:`

**`Conditions:`**

* `If a number is negative, set it to 0.`  
  * `If a number is positive, double its value.`  
  * `If a number is 0, skip it without making any changes.`

**`Input:`**

`numbers = [-3, 5, 0, -1, 8, 2]`

**`Expected Output:`**  
`After applying the conditions, the output should be:`

`[0, 10, 0, 0, 16, 4]`

---

### **`Bonus Task 8: Simulate a Do-While Loop in Python`**

#### **`Problem:`**

`Python does not have a built-in do-while loop, but you can simulate one. Write a program that repeatedly asks the user to input a number until they enter a value between 1 and 10. Ensure the first prompt executes at least once, even if the user enters an invalid value.`

**`Input/Output Example:`**

`Enter a number between 1 and 10: -5`  
`Invalid input. Try again.`  
`Enter a number between 1 and 10: 12`  
`Invalid input. Try again.`  
`Enter a number between 1 and 10: 7`  
`Thank you! Your number is 7.`

---

**`Hint for Implementation:`**

1. `Use an infinite while True loop to simulate the "do" part.`  
2. `Break the loop when the condition is satisfied.`

---

