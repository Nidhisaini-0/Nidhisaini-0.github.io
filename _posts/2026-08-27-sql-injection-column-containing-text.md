---
layout: post
title: "SQL Injection — Finding a column containing text"
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

# Lab: SQL injection UNION attack, finding a column containing text

## Lab Information

- **Platform:** PortSwigger Web Security Academy
- **Difficulty:** Practitioner
- **Vulnerability:** SQL Injection
- **Status:** Solved ✓

## Lab Objective

This lab contains a SQl injection vulnerability in the product category filter.
The main objective of this lab is to determine the datatype of columns.
 
Determining numbers of columns is the very first step of UNION attack.
The next step is to identify a column that is compatible with string data.

The lab will provide a random value that you need to make appear within the query results. To solve the lab, perform a SQL injection UNION attack that returns an additional row containing the value provided. This technique helps you determine which columns are compatible with string data. 


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

we put this payload at the end of URL and increase NULL iteratively until it gives 200 ok response 

```sql
'UNION select NULL--
```
Internally this payload changes to sql query something like 
```sql
select ? from table UNION select NULL,NULL,NULL--
```
According to the rule number 1 of UNION operator the number of column will be same as how many NULL we put in our payload.

Now as we know the number of column, we check datatype of column by putting text and number instead of NULL iteratively at each place.

```sql
'UNION select 'a',NULL,NULL--
```

If it gives error --> first column is not string 

If it doesn't give any error and shows 'a' in output --> first column is a string 

## Exploitation

1. I put, 
   ```sql
   'UNION select NULL,NULL,NULL--
   ```
   at the end of URL(category parameter). It tells me that numbers of column are 3.

2. Then I put random text 'a' instead of 1st NULL 
   ```sql
   'UNION select 'a',NULL,NULL--
   ```
   which gives me **internal server error** means 1st column is not text datatype.

3. Then I put 'a' at the place of 2nd NULL
    ```sql
    'UNION select NULL,'a',NULL--
    ```
    which print a in the output means the 2nd column is text datatype.


## Result

After putting

```text
'UNION select NULL,'iIK4rC',NULL--
```
in the URL(category parameter) returns 200 ok response and this random string 'iIK4rC' is listed in products output. 

![SQL Injection Determining Number of Columns - Solved](/assets/images/portswigger/sql-injection/Determining-column-datatype.png)

## Key Takeaways

- UNION-based SQL injection requires the injected values to be compatible with the data types of the target columns. 
  
- Different data types can be tested by placing values such as strings, numbers, or NULL in the UNION query.
  
- NULL is useful because it can often be converted to different data types by the database.
  
- By observing errors and application responses, you can identify which columns accept string or other data types.
  
- Determining the column data types helps construct a valid UNION query for retrieving data in a controlled lab environment.


**Lab Status: Solved ✓**