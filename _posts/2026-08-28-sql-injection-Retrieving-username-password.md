---
layout: post
title: "SQL Injection — Retrieving username and password from users table"
date: 2026-08-28

categories:
  - Web Security

topic: SQL Injection

tags:
  - PortSwigger
  - SQL Injection
  - Web Security Academy

toc: true
---

# Lab: SQL injection UNION attack, retrieving data from other tables

## Lab Information

- **Platform:** PortSwigger Web Security Academy
- **Difficulty:** Practitioner
- **Vulnerability:** SQL Injection
- **Status:** Solved ✓

## Lab Objective

This lab contains a SQl injection vulnerability in the product category filter.

The database contains a different table called users, with column called username and password.

The main objective of this lab is to retrieves all usernames and passwords, and use the information to log in as the administrator user.

   
## Testing (How I know that this lab has sql-injection vulnerability?)

I put ``` ' ``` in product category filter URL, it gave me **Internal server error** which specify that something is broke in backend. 
And I got to know that this product category field has sql-injection vulnerability. 


## Exploitation


### 1. Determine the number of columns
 The first step for UNION based attack is to determine the number of column.
 Query for determining column number is:

 ```sql
 'UNION SELECT NULL,NULL--
 ```
 To know more about determining number of column read my previous lab:

 [Read my determining number of columns post](/blog/2026/08/27/sql-injection-numbers-of-column/)

 In this lab the number of columns are 2.

### 2. Determine the datatype of each column
 The second step is determining datatype of column, if it is text or number or NULL.
  
 ```sql
 'UNION SELECT 'text','text'--
 ```
 To know more about determining datatype of column read my previous lab:

 [Read my determining datatype of column post](/blog/2026/08/27/sql-injection-column-containing-text/)

 In this lab both column contain text.

### 3. Retrieve the username and password
 In 3rd step I retrieve username and password from users table by the query:

 ```sql
 'UNION SELECT username,password from users--
 ```
 This query returns usernames and passwords and from that list I took administrator user and It's password. 
 Using this information I successfully log in as the administrator user.


## Result

After putting

```sql
'UNION SELECT username,password from users--
```
in the URL(category parameter) returns lists of username and password. 
With the help of that list I retrieve administrator user and it's password and log in as administrator user.


![SQL Injection retrieving data from other table - Solved](/assets/images/portswigger/sql-injection/Retrieving-username-password1.png)


![SQL Injection retrieving data from other table - Solved](/assets/images/portswigger/sql-injection/Retrieving-username-password2.png)


## Key Takeaways

- UNION-based SQL injection can be used to combine the results of the original query with data from another table.
- The injected UNION SELECT must have the same number of columns as the original query.
- The selected columns must have compatible data types with the corresponding columns in the original query.
- Once the query structure is understood, data from other database tables can potentially be retrieved through the application's response.
- Proper input validation and parameterized queries are important defenses against UNION-based SQL injection.


**Lab Status: Solved ✓**