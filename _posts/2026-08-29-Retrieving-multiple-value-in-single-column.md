---
layout: post
title: "SQL Injection UNION attack — Retrieving multiple value in single column"
date: 2026-08-29

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

The main objective of this lab is to retrieves all usernames and passwords in a single column, and use the information to log in as the administrator user.

   
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
 'UNION SELECT NULL,'text'--
 ```
 To know more about determining datatype of column read my previous lab:
 [Read my determining datatype of column post](/blog/2026/08/27/sql-injection-column-containing-text/)

 In this lab only second column is of text datatype.

### 3. Retrieve the username and password using single column
 In this lab only second column is of text datatype. But username and password are two column, even if we retrieve both separately we will not find out which username have what password.

 Here, string concatenation comes into picture. 
 String concatenation concatenate multiple string together and returns it as a single value.
 Different database has different syntax for string concatenation.
 
 Now the workflow is as follow:

 1. First I found out the database type using 
     ```sql
     'UNION SELECT NULL, version()--
     ```
     This query is for PostgreSQL database, which indicates that database is PostgreSQL.
 
 2. Then I use the string concatenation query to concatenate the string.
    For PostgreSQL it is 
     ```text
     'foo' || 'bar'
     ```
  
 To Know more about string concatenation and finding database version read SQL injection cheet sheet at Portswigger website.

 [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)

 The final payload for Retrieving username and password in single column is: 

 ```sql
 'UNION SELECT NULL,username || '*' || password from users--
 ```
 This query returns all usernames and passwords separated by '*'(we include * by ourself for distinction).

 Using this information I successfully log in as the administrator user.


## Result

After putting

```sql
'UNION SELECT NULL,username || '*' || password from users--
```
in the URL(category parameter) returns lists of username and password. 
With the help of that list I retrieve administrator user and it's password and log in as administrator user.


![SQL Injection retrieving data from other table - Solved](/assets/images/portswigger/sql-injection/Retrieving-multiple-value-in-one-column1.png)


![SQL Injection retrieving data from other table - Solved](/assets/images/portswigger/sql-injection/Retrieving-multiple-value-in-one-column2.png)


## Key Takeaways

- String concatenation can be used to combine multiple database values into a single output column.
- When only one column is available for displaying text, multiple values can be joined into one string.
- A separator can be added between concatenated values to make the retrieved data easier to read.
- The database-specific concatenation syntax must be used for the query to work correctly.
- UNION-based SQL injection can therefore be used to retrieve multiple pieces of information through a single reflected column in a vulnerable application.


**Lab Status: Solved ✓**