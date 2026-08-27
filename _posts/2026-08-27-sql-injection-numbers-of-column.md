---
layout: post
title: "SQL Injection — Determining the numbers of column"
date: 2026-08-27

categories:
  - Web Security

topic: SQL Injection

tags:
  - PortSwigger
  - SQL Injection
  - Web Security Academy

toc: true
---

# Lab: SQL injection UNION attack, determining the number of columns returned by the query

## Lab Information

- **Platform:** PortSwigger Web Security Academy
- **Difficulty:** Practitioner
- **Vulnerability:** SQL Injection
- **Status:** Solved ✓

## Lab Objective

This lab contains a SQl injection vulnerability in the product category filter.
The main objective of this lab is to determine the number the columns that are being returned by the query.
This is the very first step of UNION attack.

## Background knowledge about UNION operator in SQL

In sql, UNION operator is used for concatenating the result sets from two queries.

exa:
Let's take these two table:-

```text
     table-A                       table-B
  column-1  column-2            column-3 column-4
      a         b                  c          d
      e         f                  g          h 
``` 
The sql query is something like this-

```sql
SELECT column-1,column-2 FROM table-A UNION SELECT column-3,column-4 FROM table-B
```
result:
```text
a  b
e  f
c  d
g  h
```
Here, UNION operator combine these two query and return value from both table.


**Rule for UNION operator for combining the result set of two queries**

1. Number of column in both query should be same.
2. The data type must be compatible.
   

## Testing (How I know that this lab has sql-injection vulnerability?)

I put ``` ' ``` at the end of URL, it gave me **Internal server error** which specify that something is broke in backend. 
And I got to know that this product category field has sql-injection vulnerability. 


## Payload

sqli(way 1 UNION operator):

we put this payload at the end of URL and increase NULL iteratively until it gives 200 ok response 

```sql
'UNION select NULL--
```
Internally this payload changes to sql query something like 
```sql
select ? from table UNION select NULL,NULL,NULL--
```
According to the rule number 1 of UNION operator the number of column will be same as how many NULL we put in our payload.

sqli(way 2 order by clause):

we put this at the end of URL and increase the number of iteratively until the page is broke 

```text
'order by 1--
```
The number of column will be = number at which page broke - 1 

## Exploitation

1. I put, 
   ```sql
   'UNION select NULL--
   ```
   at the end of URL(category parameter). It gives me **Internal server error**, which means number of column is not 1.

2. Then I put one more NUll in URL and increase its value iteratively until it gives me 200 ok response. In this lab it is 3 NULL values.

3. According the rule of union operator, that the number of column in both query are same gives me answer that the number of column is 3.
   

## Result

After putting

```text
'UNION select NULL,NULL,NULL--
```
in the URL(category parameter) returns 200 ok response and the lab is solved.

![SQL Injection Determining Number of Columns - Solved](/assets/images/portswigger/sql-injection/Determining-numbers-of-column.png)

## Key Takeaways

- UNION-based SQL injection can be used to retrieve data from other database queries when the application is vulnerable.
- The number of columns in the original query must match the number of columns in the UNION SELECT query.
- Different numbers of NULL values can be tested to determine the correct column count.
- An error usually indicates that the number of columns in the UNION SELECT does not match the original query.
- Once the correct column count is identified, the same technique can be used to determine which columns can display text/data in the application response.


**Lab Status: Solved ✓**