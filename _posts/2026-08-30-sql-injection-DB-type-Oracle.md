---
layout: post
title: "SQL Injection UNION attack - querying DB type and version on Oracle"
date: 2026-08-30

categories:
  - Web Security

topic: SQL Injection

tags:
  - PortSwigger
  - SQL Injection
  - Web Security Academy

toc: true
---

# Lab: SQL injection attack, querying the database type and version on Oracle

## Lab Information

- **Platform:** PortSwigger Web Security Academy
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
 'UNION SELECT NULL,NULL from dual--
 ```
 To know more about determining number of column read my previous lab:
 [Read my determining number of columns post](/blog/2026/08/27/sql-injection-numbers-of-column/)

 In this lab the number of columns are **2**.

### 2. Determine the datatype of each column
 The second step is determining datatype of column, if it is text or number or NULL.
  
 ```sql
 'UNION SELECT 'text','text' from dual--
 ```
 To know more about determining datatype of column read my previous lab:
 [Read my determining datatype of column post](/blog/2026/08/27/sql-injection-column-containing-text/)

 In this lab both column are of **text** datatype.

### 3. Querying database type and version on Oracle

 Query for determining database type and version on Oracle is 
 ```sql
 SELECT banner FROM v$version
 ```
 To know more about querying Database version. Read 
  [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)

 The final payload for determine DB type and version on Oracle is: 

 ```sql
 'UNION SELECT NULL, banner FROM v$version--
 ```
 This query returns database type and version in output field.


## Result

After putting

```sql
'UNION SELECT NULL, banner FROM v$version--
```
in the URL(category parameter) returns database type and version. 

![SQL Injection retrieving data from other table - Solved](/assets/images/portswigger/sql-injection/Querying-DB-type-Oracle.png)


## Key Takeaways

- Oracle provides built-in views and functions that can be used to identify the database type and version.
- The v$version view can be queried to retrieve Oracle database version information.
- Knowing the database type and version helps determine which SQL syntax and features are supported.
- SQL injection techniques can vary depending on the underlying database management system.
- Identifying the DBMS is an important step when analyzing a SQL injection vulnerability in a controlled lab environment.


**Lab Status: Solved ✓**