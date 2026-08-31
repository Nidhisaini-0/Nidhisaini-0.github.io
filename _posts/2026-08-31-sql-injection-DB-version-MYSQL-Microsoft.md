---
layout: post
title: "SQL Injection UNION attack - querying DB type and version on MYSQL and Microsoft"
date: 2026-08-31

categories:
  - Web Security

topic: SQL Injection

tags:
  - PortSwigger
  - SQL Injection
  - Web Security Academy

toc: true
---

# Lab: SQL injection attack, querying the database type and version on MySQL and Microsoft

## Lab Information

- **Platform:** PortSwigger Web Security Academy
- **Tool:** Burp Suite
- **Difficulty:** Practitioner
- **Vulnerability:** SQL Injection
- **Status:** Solved ✓

## Lab Objective

This lab contains a SQl injection vulnerability in the product category filter.

The main objective of this lab is to display the database version string.

   
## Testing (How I know that this lab has sql-injection vulnerability?)

I put ``` ' ``` in product category filter URL, it gave me **Internal server error** which specify that something is broke in backend. 
And I got to know that this product category field has sql-injection vulnerability. 


## Exploitation


### 1. Determine the number of columns
 The first step for UNION based attack is to determine the number of column.
 Query for determining column number is:

 ```sql
 'UNION SELECT NULL,NULL#
 ```
 **Note:** In SQL, **#** is also uses for commenting the query.

 To know more about determining number of column read my previous lab:
 [Read my determining number of columns post](/blog/2026/08/27/sql-injection-numbers-of-column/)

 In this lab the number of columns are **2**.

### 2. Determine the datatype of each column
 The second step is determining datatype of column, if it is text or number or NULL.
  
 ```sql
 'UNION SELECT 'text','text'#
 ```
 To know more about determining datatype of column read my previous lab:
 [Read my determining datatype of column post](/blog/2026/08/27/sql-injection-column-containing-text/)

 In this lab both column are of **text** datatype.

### 3. Querying database type and version on MySQL and Microsoft

 Query for determining database type and version on MySQL and Microsoft is 
 ```sql
 SELECT @@version
 ```
 To know more about querying Database version. Read 
  [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)

 The final payload for determine DB type and version on MySQL and Microsoft is: 

 ```sql
 'UNION SELECT NULL, @@version#
 ```
 This query returns database type and version in output field.


## Result

After putting

```sql
'UNION SELECT NULL, @@version#
```
in the URL(category parameter),it returns **8.0.42-0ubuntu0.20.04.1**. 

![SQL Injection retrieving data from other table - Solved](/assets/images/portswigger/sql-injection/DB-version-MYSQL-Microsoft1.png)

![SQL Injection retrieving data from other table - Solved](/assets/images/portswigger/sql-injection/DB-version-MYSQL-Microsoft2.png)


## Key Takeaways

- Different DBMS platforms such as MySQL and Microsoft SQL Server use different SQL syntax and functions.
- The @@version query can be used to retrieve version information in both MySQL and Microsoft SQL Server.
- Identifying the database type and version helps determine which SQL techniques and syntax are supported.
- Database-specific knowledge is important when constructing UNION-based SQL injection queries.
- Understanding the underlying DBMS makes it easier to adapt SQL injection techniques to the specific database environment.

**Lab Status: Solved ✓**