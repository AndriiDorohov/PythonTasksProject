Practice \#9  
**`Chapter 24 (Python files management)`**

### **`Task 1: Write User Input to a File`**

#### **`Problem:`**

`Create a program that prompts the user to enter their name, age, and favorite color. Write this information to a file called user_info.txt in the following format:`

`Name: [User's Name]`    
`Age: [User's Age]`    
`Favorite Color: [User's Favorite Color]`

**`Example Input:`**

`Enter your name: Alice`    
`Enter your age: 25`    
`Enter your favorite color: Blue`

**`Expected Output in user_info.txt:`**

`Name: Alice`    
`Age: 25`    
`Favorite Color: Blue`

---

### **`Task 2: Count Words in a File`**

#### **`Problem Statement:`**

`Write a program that reads the content of a text file sample.txt, counts the number of words in it, and displays the total word count.`

1. `Create a text file sample.txt with any content (e.g., "Hello world! This is a file.").`  
2. `Open the file in read mode, count the words, and print the result.`

**`Example Input in sample.txt:`**

`Hello world! This is a file.`

**`Expected Output:`**

`The file contains 6 words.`

---

### **`Task 3: Append and Display File Content`**

#### **`Problem:`**

`Create a program that appends a new line to a file called log.txt with the current date and time. Then, read and display the entire file content.`

1. `If the file doesn't exist, create it.`  
2. `Append the current date and time in the format: YYYY-MM-DD HH:MM:SS.`  
3. `Print the entire content of the file after the new line is added.`

**`Example Execution:`**  
`On the first run:`

`log.txt created.`  
`Appended: 2024-12-26 15:00:00`

`On the second run:`

`Appended: 2024-12-26 15:01:00`

`File content:`  
`2024-12-26 15:00:00`  
`2024-12-26 15:01:00`

---

### **`Task 4: Reading and Writing a CSV File`**

#### **`Problem:`**

`Create a program that does the following:`

1. `Write a CSV file named students.csv with columns: Name, Age, and Grade.`  
   * `Populate it with at least 3 rows of sample data (e.g., "Alice", 25, "A").`  
2. `Read the file and calculate the average age of the students.`  
3. `Display the content of the CSV file along with the average age.`

**`Example Input (Data in students.csv):`**

`Name,Age,Grade`  
`Alice,25,A`  
`Bob,22,B`  
`Charlie,24,A`

**`Expected Output:`**

`File content:`  
`Name: Alice, Age: 25, Grade: A`  
`Name: Bob, Age: 22, Grade: B`  
`Name: Charlie, Age: 24, Grade: A`

`Average Age: 23.67`

---

