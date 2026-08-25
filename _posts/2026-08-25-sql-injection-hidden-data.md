---

layout: post
title: "SQL Injection — Retrieving Hidden Data"
date: 2026-08-24
category: Web Security
topic: SQL Injection
tags:

* PortSwigger
* Burp Suite
* SQL Injection
* Web Security Academy
  toc: true

---

# SQL Injection — Retrieving Hidden Data

This was my first hands-on lab from **PortSwigger Web Security Academy**, and it was a good introduction to understanding how SQL Injection actually works.

The goal of this lab was to find a SQL injection vulnerability in a product category filter and use it to make the application display products that were normally hidden.

---

## Lab Information

* **Platform:** PortSwigger Web Security Academy
* **Difficulty:** Apprentice
* **Vulnerability:** SQL Injection
* **Category:** Web Security
* **Topic:** SQL Injection
* **Tool:** Burp Suite
* **Status:** Solved ✓

---

## Lab Objective

The application is an online shopping website where products can be filtered by category.

Some products are hidden because they have not been released yet.

The application uses a SQL query similar to:

```sql
SELECT * FROM products
WHERE category = 'Gifts'
AND released = 1
```

The important part is:

```sql
AND released = 1
```

This means that only products where `released` is set to `1` are normally displayed.

My goal was to find a way to manipulate the query and make the application return the hidden products as well.

---

## Finding the Vulnerability

I started by looking at the product category filter.

The category was being sent to the server as a parameter, which made it a good place to test for SQL Injection.

Instead of immediately trying a complicated payload, I started with a simple single quote:

```text
'
```

After submitting it, the application returned an **Internal Server Error**.

This was interesting because a single quote can affect the structure of an SQL query.

The error suggested that my input was reaching the database query without being handled properly.

So at this point, I had a good reason to suspect that the category parameter might be vulnerable to SQL Injection.

---

## Understanding What Was Happening

The application was working with a query similar to:

```sql
SELECT * FROM products
WHERE category = 'Gifts'
AND released = 1
```

Normally, the database needs to satisfy both conditions:

```text
category = 'Gifts'
        AND
released = 1
```

The second condition is what keeps unreleased products hidden.

If I could change the SQL logic so that the condition was always true, I could potentially make the application return more products than it was supposed to.

---

## Exploiting the SQL Injection

I then tried the following payload:

```text
' OR 1=1--
```

When sent through the URL, the spaces were represented using `+`:

```text
'+or+1=1--
```

The interesting part of the payload is:

```sql
' OR 1=1--
```

There are three important parts here.

### 1. Closing the original string

The first single quote:

```sql
'
```

closes the string that the application originally created around the category value.

### 2. Adding an always-true condition

Next is:

```sql
OR 1=1
```

The expression `1=1` is always true.

So instead of only checking the original category, the database is also given a condition that will always evaluate to true.

### 3. Commenting out the rest

Finally:

```sql
--
```

starts an SQL comment.

This means the remaining part of the original SQL query is ignored.

That is important because the original query still contained:

```sql
AND released = 1
```

By commenting out the remaining part of the query, I could bypass that restriction.

---

## What Changed?

The original query was approximately:

```sql
SELECT * FROM products
WHERE category = 'Gifts'
AND released = 1
```

After injecting the payload, the logic was changed to something similar to:

```sql
SELECT * FROM products
WHERE category = ''
OR 1=1
```

Because:

```sql
1=1
```

is always true, the database can return products that would normally be excluded.

This is why the hidden products became visible.

---

## Using Burp Suite

I used Burp Suite to inspect and modify the HTTP request sent by the application.

The basic process was:

```text
Browser
   ↓
Product category filter
   ↓
HTTP request
   ↓
Modify category parameter
   ↓
Send request
   ↓
Server processes the SQL query
   ↓
Hidden products are returned
```

Burp Suite made it easy to change the parameter and observe how the application's response changed.

This was also a good reminder that parameters which look harmless, such as a product category, can become dangerous if the application directly places their values into SQL queries.

---

## Result

After sending the modified request containing:

```text
' OR 1=1--
```

the application returned the hidden products.

This confirmed that the SQL injection was successful.

The PortSwigger lab was then marked as **solved**.

### Successful Lab

![SQL Injection Lab - Successfully Solved](/assets/images/portswigger/sql-injection/sql-injection-hidden-data-solved.png)

*The lab was successfully solved after manipulating the vulnerable category parameter.*

---

## Why Did This Work?

The main problem was that the application was allowing user input to influence the SQL query directly.

The application expected the category parameter to contain normal data, such as:

```text
Gifts
```

But instead, I supplied SQL syntax:

```sql
' OR 1=1--
```

The application did not properly separate the user input from the SQL command.

As a result, my input changed the logic of the database query itself.

This is the fundamental idea behind **SQL Injection**:

> An attacker is able to turn data supplied to an application into part of the SQL command being executed.

---

## What I Learned

This lab helped me understand the basic process of testing for SQL Injection.

The most useful part for me was seeing how a very simple test could reveal a vulnerability.

I started with:

```text
'
```

and received an error.

That gave me a clue that the input was interacting with the SQL query.

I then tested:

```text
' OR 1=1--
```

and the application returned the hidden products.

So the basic process was:

```text
Find an interesting parameter
        ↓
Test with a single quote
        ↓
Observe the error
        ↓
Suspect SQL Injection
        ↓
Test the SQL logic
        ↓
Modify the query
        ↓
Observe the result
```

This was a simple lab, but it gave me a much better understanding of what SQL Injection looks like in a real web application.

---

## How Can This Be Prevented?

The application should never directly combine user input with an SQL query.

One of the main defenses against SQL Injection is using **parameterized queries** or **prepared statements**.

For example, instead of directly inserting the category into the SQL statement, the application can use a parameter:

```sql
SELECT * FROM products
WHERE category = ?
AND released = 1
```

The category value is then supplied separately from the SQL statement.

This prevents the database from interpreting the user's input as SQL code.

Other security practices include:

* Using parameterized queries
* Using prepared statements
* Giving database users only the permissions they actually need
* Handling database errors safely
* Avoiding unnecessary exposure of database information

---

## Key Takeaways

* A simple single quote can sometimes reveal SQL injection behavior.
* User-controlled input should never be trusted.
* `OR 1=1` creates an always-true condition.
* `--` can comment out the remaining SQL query.
* SQL Injection can allow attackers to bypass application logic.
* Parameterized queries and prepared statements are important defenses.

---

## Final Thoughts

This was my first SQL Injection lab on PortSwigger, and it was a simple but useful introduction to the vulnerability.

What I found most interesting was that the attack did not require a complicated exploit.

A small change to a single parameter was enough to change the behavior of the database query and expose information that the application was supposed to hide.

This is why understanding how applications process user input is so important in web security.

**Lab Status: Solved ✓**
