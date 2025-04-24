**`SQL course`**

### **`Database Recap`**

#### **`Customers Table`**

| `customer_id` | `first_name` | `last_name` | `age` | `country` |
| :---: | :---: | :---: | :---: | :---: |
| `1` | `John` | `Doe` | `31` | `USA` |
| `2` | `Robert` | `Luna` | `22` | `USA` |
| `3` | `David` | `Robinson` | `22` | `UK` |
| `4` | `John` | `Reinhardt` | `25` | `UK` |
| `5` | `Betty` | `Doe` | `28` | `UAE` |

#### 

#### **`Orders Table`**

| `order_id` | `item` | `amount` | `customer_id` |
| :---: | :---: | :---: | :---: |
| `1` | `Keyboard` | `400` | `4` |
| `2` | `Mouse` | `300` | `4` |
| `3` | `Monitor` | `12000` | `3` |
| `4` | `Keyboard` | `400` | `1` |
| `5` | `Mousepad` | `250` | `2` |

#### 

#### **`Shippings Table`**

| `shipping_id` | `status` | `customer` |
| :---: | :---: | :---: |
| `1` | `Pending` | `2` |
| `2` | `Pending` | `4` |
| `3` | `Delivered` | `3` |
| `4` | `Pending` | `5` |
| `5` | `Delivered` | `1` |

### 

### 

### **`Tasks with Example Outputs`**

### ---

#### **`1. List All Customers`**

### **`Query:`** `Retrieve all details of the customers.`

### **`Expected Output:`**

| `customer_id` | `first_name` | `last_name` | `age` | `country` |
| :---: | :---: | :---: | :---: | :---: |
| `1` | `John` | `Doe` | `31` | `USA` |
| `2` | `Robert` | `Luna` | `22` | `USA` |
| `3` | `David` | `Robinson` | `22` | `UK` |
| `4` | `John` | `Reinhardt` | `25` | `UK` |
| `5` | `Betty` | `Doe` | `28` | `UAE` |

**`Tip`**`:`

* `Use the SELECT * syntax to retrieve all columns from a table.`  
* `Always verify the structure of the table with DESCRIBE Customers; to understand the schema.`

### ---

#### **`2. Find Customers from the USA`**

### **`Query:`** `Find all customers whose country is "USA".`

### **`Expected Output:`**

| `customer_id` | `first_name` | `last_name` | `age` | `country` |
| :---: | :---: | :---: | :---: | :---: |
| `1` | `John` | `Doe` | `31` | `USA` |
| `2` | `Robert` | `Luna` | `22` | `USA` |

**`Tip`**`:`

* `Use the WHERE clause to filter rows based on specific criteria.`  
* `Remember to match text values exactly, including case sensitivity depending on your SQL dialect. Use single quotes 'USA'.`

### ---

#### **`3. List All Pending Shipments`**

### **`Query:`** `Retrieve all details of shipments with the status "Pending".`

### **`Expected Output:`**

| `shipping_id` | `status` | `customer` |
| :---: | :---: | :---: |
| `1` | `Pending` | `2` |
| `2` | `Pending` | `4` |
| `4` | `Pending` | `5` |

### **`Tip:`**

* ### `Filtering works similarly across tables. Identify the column (status) that holds the condition ('Pending').`

* ### `Run SELECT DISTINCT status FROM Shippings; to see all unique statuses.`

### 

### ---

#### **`4. Join Customers with Orders`**

### **`Query:`** `List all customers along with the items they have ordered. Include customers even if they haven’t placed any orders.`

### **`Expected Output:`**

| `customer_id` | `first_name` | `last_name` | `item` | `amount` |
| :---: | :---: | :---: | :---: | :---: |
| `1` | `John` | `Doe` | `Keyboard` | `400` |
| `2` | `Robert` | `Luna` | `Mousepad` | `250` |
| `3` | `David` | `Robinson` | `Monitor` | `12000` |
| `4` | `John` | `Reinhardt` | `Keyboard` | `400` |
| `4` | `John` | `Reinhardt` | `Mouse` | `300` |
| `5` | `Betty` | `Doe` | `NULL` | `NULL` |

**`Tip`**`:`

* `Use LEFT JOIN to include all customers, even if they have no orders.`  
* `Always specify the join condition (ON c.customer_id = o.customer_id) to avoid a Cartesian product.`

### ---

#### **`5. Calculate Total Orders per Customer`**

### **`Query:`** `Calculate the total order amount for each customer. Include customers even if they haven’t placed any orders.`

### **`Expected Output:`**

| `customer_id` | `first_name` | `last_name` | `total_amount` |
| :---: | :---: | :---: | :---: |
| `1` | `John` | `Doe` | `400` |
| `2` | `Robert` | `Luna` | `250` |
| `3` | `David` | `Robinson` | `12000` |
| `4` | `John` | `Reinhardt` | `700` |
| `5` | `Betty` | `Doe` | `0` |

**`Tip`**`:`

* `Use SUM() for aggregate calculations and GROUP BY to group rows by customer.`  
* `Handle customers with no orders by using COALESCE(SUM(...), 0) to replace NULL with 0.`

### ---

#### **`6. List Customers with Delivered Shipments`**

### **`Query:`** `Find the names of customers who have at least one shipment with the status "Delivered".`

### **`Expected Output:`**

| `first_name` | `last_name` |
| :---: | :---: |
| `David` | `Robinson` |
| `John` | `Doe` |

### **`Tip:`**

* ### `Use DISTINCT to remove duplicate entries from your results.`

* ### `When working across multiple tables, use table aliases (c, s) to improve readability and avoid ambiguity.`

### 

### ---

#### **`7. Find Top Spending Customer`**

### **`Query:`** `Find the customer who has spent the most money on orders.`

### **`Expected Output:`**

| `customer_id` | `first_name` | `last_name` | `total_spent` |
| :---: | :---: | :---: | :---: |
| `3` | `David` | `Robinson` | `12000` |

**`Tip`**`:`

* `Use ORDER BY to sort results, and apply LIMIT to fetch only the top record.`  
* `Double-check the SUM(o.amount) to ensure it's aggregated per customer with GROUP BY.`

### ---

#### **`8. Count Pending Shipments by Country`**

### **`Query: Count the number of pending shipments for each country.`**

### **`Expected Output:`**

| `country` | `pending_shipments` |
| :---: | :---: |
| `USA` | `1` |
| `UK` | `1` |
| `UAE` | `1` |

### **`Tip:`**

* ### `Combine joins and group operations to summarize data from multiple tables.`

* ### `Use COUNT() to count specific rows and group them by a categorical field like country.`

### 

### ---

#### **`9. Match Orders with Shipping Status`**

### **`Query:`** `List each order along with the shipping status of the customer who placed the order.`

### **`Expected Output:`**

| `order_id` | `item` | `amount` | `customer_id` | `status` |
| :---: | :---: | :---: | :---: | :---: |
| `1` | `Keyboard` | `400` | `4` | `Pending` |
| `2` | `Mouse` | `300` | `4` | `Pending` |
| `3` | `Monitor` | `12000` | `3` | `Delivered` |
| `4` | `Keyboard` | `400` | `1` | `Delivered` |
| `5` | `Mousepad` | `250` | `2` | `Pending` |

**`Tip`**`:`

* `To match data across tables, use a JOIN that connects the related fields (o.customer_id = s.customer).`  
* `Think about whether you want to use INNER JOIN (only matching records) or LEFT JOIN (keep all orders even without matching shipments).`

### ---

#### **`10. Youngest Customers with Orders`**

### **`Query:`** `Retrieve the youngest customers who have placed an order. Include their age and order details.`

### **`Expected Output:`**

| `customer_id` | `first_name` | `last_name` | `age` | `item` | `amount` |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2` | `Robert` | `Luna` | `22` | `Mousepad` | `250` |
| `3` | `David` | `Robinson` | `22` | `Monitor` | `12000` |

**`Tip`**`:`

* `Use a subquery (SELECT MIN(age)) to dynamically find the condition for filtering.`  
* `When dealing with age comparisons, ensure all rows with the minimum value are included, not just the first match.`

### ---

