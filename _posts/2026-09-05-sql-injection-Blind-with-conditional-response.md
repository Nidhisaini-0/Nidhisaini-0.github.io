---
layout: post
title: "Blind SQL injection with conditional responses"
date: 2026-09-05

categories:
  - Web Security

topic: SQL Injection

tags:
  - PortSwigger
  - SQL Injection
  - Web Security Academy

toc: true
---

# Lab: Blind SQL injection with conditional responses

## Lab Information

- **Platform:** PortSwigger Web Security Academy
- **Tool:** Burp Suite
- **Difficulty:** Practitioner
- **Vulnerability:** SQL Injection
- **Status:** Solved ✓

## Lab Objective
This lab contains a blind SQL injection vulnerability in tracking cookie section. 
The result of the SQL query are not returned, and no error messages are displayed. But the application includes a  ``` Welcome back``` message in the page if the query return any rows.

The database contains a different table called ```users``` , with columns called ```username``` and ```password```. You need to find out the password for ```administrator``` user and log in as the ```administrator``` user.


## Exploitation

The application contains a sql-injection vulnerability in tracking cookie section.
In backend the query for retrieving tracking Id from database is something like 
```sql
SELECT tracking_id from tracking_table where trackingId = 'RvLfBu6s9EZRlVYN'
```
If the tracking-id condition is true it return ```Welcome back!``` message which can be exploited.

### 1. Confirmation that the tracking id parameter is vulnerable to blind sqli
 
 At first I append tracking id section with 
 ```sql
 ' AND 1=1 --
 ```
 it returns ```Welcome back!``` 
 As 1=1 is always true both condition become true and it tells that tracking id parameter is vulnerable to sqli.

### 2. Confirmation that there is **users** table in database
 
 This payload tells that there is **users** table:
 ```sql
 ' AND (SELECT 'a' from users LIMIT 1) = 'a'--
 ```
 as it is true condition and return ```Welcome back!``` message.

### 3. Confirmation that there is a administrator in users table
 The payload confirm that there is administrator user
 ```sql
 ' AND (SELECT username from users where username = 'administrator') = 'administrator'--
 ```
 with this query it still returns ```Welcome back!``` message.

### 4. Enumerate the password for administrator user
 First we check the length of the password with the help of payload:
 ```sql
 ' AND (SELECT 'a' from users where username = 'administrator' AND LENGTH(password)>1) = 'a'--
 ```
 now we increase the number of 1. Do it sequentially or by binary search method technique. 
 And at the point it start giving false and application doesn't return ```Welcome back!``` message, it is the length of password. Here it is **20**.

 Now we enumerate the character of password with the query
 ```sql
 'AND (SELECT SUBSTRING(password,1,1) from users where username = 'administrator') = 'a'--
 ```
 In this payload I change the value of **a** to all lowercase alphanumeric character (a-z and 0-9). Then whichever character satisfies the condition is the first character of the password.

 After that I change the **SUBSTRING(password,1,1)** to **SUBSTRING(password,2,1)** and repeat the same process for second character of the password. 

 Then I increase the value 2 to 3 and so on to the all 20 character of password.
 This is a very hard task to do manually. So I did it with the help of **Burp Intruder**. **Burp Intruder** checks out the all possible combination for password.

 After retrieving the password I successfully login as administrator user.


## Result

After filling 

administrator user and its password **kizbiaigwists5jd6ikm** in login function I successfully login as administrator user.


![SQL Injection retrieving data from other table - Solved](/assets/images/portswigger/sql-injection/Blind-sql-injection-conditional-response.png)


## Key Takeaways

- Blind SQL injection occurs when the application does not directly display the results of the injected query.
- A conditional response can be used to determine whether an injected SQL condition is true or false.
- Changes in the application's response can act as a Boolean indicator for testing SQL conditions.
- SQL functions such as SUBSTRING() can be used to test individual characters of a value.
- By repeating these true/false tests, information can be inferred from the application's behavior even when query results are not directly visible.
  
**Lab Status: Solved ✓**