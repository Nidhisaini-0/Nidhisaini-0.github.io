---
layout: post
title: "SQL Injection — Login Bypass"
date: 2026-08-26

categories:
  - Web Security

topic: SQL Injection

tags:
  - PortSwigger
  - SQL Injection
  - Web Security Academy

toc: true
---

# Lab: SQL injection vulnerability allowing login bypass

## Lab Information

- **Platform:** PortSwigger Web Security Academy
- **Difficulty:** Apprentice
- **Vulnerability:** SQL Injection
- **Status:** Solved ✓

## Lab Objective

This lab contains a SQL injection vulnerability in the login function.
Main objective of the lab is to login into user account as the **administrator** without password.

## Understanding the Vulnerability

This lab has SQL vulnerability in login page. 
Internally the login page must be using a payload something like 

```sql
SELECT firstname FROM users where username= 'admin' and password= 'password'
```
we wants to login into user account only using username as **administrator**.

## Testing (How I know that this lab has sql-injection vulnerability?)

I put ``` ' ``` in username field and it gave me **Internal server error** which specify that something is broke in backend. 
And I got to know that this login page has sql-injection vulnerability. 

According to sql payload,
```
 username= 'admin' 
 ```
 is expecting username but when I put single quote(') in username field sql query become 
 ``` 
 username= '' 
 ```
  which give empty username to server and it shows an error.


## Payload

Expected Payload

```text
SELECT firstname FROM users where username= 'admin' and password= 'password'
```

What it become after sql-injection

```text
SELECT firstname FROM users where username= 'administrator'
```


## Exploitation

1. I put administrator in username field followed by single quote(') and double dash(--).
2. Single Quote(') closes the username field. 
3. In SQL double dash(--) uses to comment the line.
4. Double dash(--) comments out the remaining query and there is no need to check the correct password.
5. I put some random password in password field. 
6. Then I logged in as a administrator in user account and the sql vulnerability is exploitated successfully.
   
what I add in username field is:

```text
administrator'--
```

## Result

After putting

```text
administrator'--
```
in username field and some random password in password field, I got to logged in user account as administrator.

![SQL Injection Login Bypass - Solved](/assets/images/portswigger/sql-injection/sql-injection-login-bypass-solved.png)

## Key Takeaways

- SQL Injection can be used to bypass authentication when user input is directly included in an SQL query.
- Login forms should never trust or directly concatenate user-supplied input into database queries.
- SQL operators such as `OR` can change the logic of the original query.
- Testing unusual input in login parameters can help identify authentication-related SQL Injection vulnerabilities.
- Parameterized queries and prepared statements are important ways to prevent SQL Injection attacks.


**Lab Status: Solved ✓**