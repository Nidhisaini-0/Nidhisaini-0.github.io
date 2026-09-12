---
layout: post
title: "Blind SQL injection with conditional errors"
date: 2026-09-07

categories:
  - Web Security

topic: SQL Injection

tags:
  - PortSwigger
  - SQL Injection
  - Web Security Academy

toc: true
---

# Lab: Blind SQL injection with conditional errors

## Lab Information

- **Platform:** PortSwigger Web Security Academy
- **Tool:** Burp Suite
- **Difficulty:** Practitioner
- **Vulnerability:** SQL Injection
- **Status:** Solved ✓

## Lab Objective
This lab contains a blind SQL injection vulnerability in tracking cookie section. 
The result of the SQL query are not returned, and the application doesn't respond any differently based on whether the query returns any rows.
But if the sql query causes an error, then the application returns a custom error message.

The database contains a different table called ```users``` , with columns called ```username``` and ```password```. You need to find out the password for ```administrator``` user and log in as the ```administrator``` user.


## Exploitation

The application contains a sql-injection vulnerability in tracking cookie section. And it doesn't return any error or message but if the sql query itself causes an error then it gives error. So we check it by generating error manually.

In backend the query for retrieving tracking Id from database is something like 
```sql
SELECT tracking_id from tracking_table where trackingId = 'RvLfBu6s9EZRlVYN'
```

### 1. Confirmation that the tracking id parameter is vulnerable to blind sqli
 
 At first I append tracking id section with: 
 ```sql
 ' || (select '' from dual) ||'
 ```
 it doesn't give any error indicating the sql query is correct and also ```from dual``` means that the database is Oracle.

 Here ```||``` is used for concatenation of the string.

### 2. Confirmation that there is **users** table in database
 
 This payload tells that there is **users** table:
 ```sql
 ' || (select '' from users where rownum = 1) ||'
 ```
 it gives no error means the sql query is correct. So there is a users table in database.

### 3. Confirmation that there is a administrator in users table
 The payload confirm that there is administrator user
 ```sql
 ' || (select '' from users where username = 'administrator') ||'
 ```
 This query doesn't returns any error. But if we change username to something else even if that username doesn't exist it still doesn't gives any error.

 So we generate our own custom error using **CASE-THEN-ELSE**.

 The payload,
 ```sql
 ' || (select CASE WHEN(1=1) THEN TO_CHAR(1/0) ELSE '' END from users where username = 'administrator') || '
 ```
 generate error means administrator user exist.

 In the payload, first it checks if the administrator user exist. If the condition is true the ```CASE WHEN...``` parts run and ```TO_CHAR(1/0)``` generate errors. And if the administrator does not exist ```ELSE...``` part execute and it generates no error.


### 4. Enumerate the password for administrator user
 First we check the length of the password with the help of payload:
 ```sql
 ' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END from users where username = 'administrator' and length(password) > 1) ||'
 ```
 now we increase the number of 1. Do it sequentially or by binary search method technique. 
 And at the point it stop giving error it is the length of password. Here it is **20**.

 Now we enumerate the character of password with the query
 ```sql
 '|| (select CASE WHEN(1=1) THEN TO_CHAR(1/0) ELSE '' END from users where username = 'administrator' and SUBSTR(password,1,1) = 'a') ||'
 ```
 In this payload I change the value of **a** to all lowercase alphanumeric character (a-z and 0-9). Then whichever character satisfies the condition, is the first character of the password.

 After that I change the **SUBSTR(password,1,1)** to **SUBSTR(password,2,1)** and repeat the same process for second character of the password. 

 Then I increase the value 2 to 3 and so on to the all 20 character of password.
 This is a very hard task to do manually. So I did it with the help of **Burp Intruder**. **Burp Intruder** checks out the all possible combination for password.

 After retrieving the password I successfully login as administrator user.


## Result

After filling 

administrator user and its password **uayabgzjc9ln61ivwhge** in login function I successfully login as administrator user.


![SQL Injection retrieving data from other table - Solved](/assets/images/portswigger/sql-injection/Blind-sql-conditional-errors.png)


## Key Takeaways

- Blind SQL injection with conditional errors relies on database errors to determine whether an injected condition is true or false.
- In Oracle, expressions can be combined using the || concatenation operator to construct conditional payloads.
- A deliberate error can be triggered when a specific condition is true, creating a detectable difference in the application's response.
- Functions such as SUBSTR() can be used to test individual characters of a value.
- By repeating these conditional tests, information can be inferred even when the application does not directly display database results.
  
**Lab Status: Solved ✓**


## Python Automation

For automating the password extraction, I used a Python script originally written by **Rana Khalil** and published in the [Web-Security-Academy-Series repository](https://github.com/rkhal101/Web-Security-Academy-Series/blob/main/sql-injection/lab-12/sqli-lab-12.py).

I modified the original implementation to work with my setup, including updating the HTTP client to handle HTTP/2 communication and making other changes required for my environment.

**Original source:** [Rana Khalil — sqli-lab-12.py](https://github.com/rkhal101/Web-Security-Academy-Series/blob/main/sql-injection/lab-12/sqli-lab-12.py)

The original implementation belongs to its respective author. My changes are my own modifications to the original script.


[View the complete Python script](../scripts/blind-sqli-conditional-errors.py)