---
layout: post
title: "Stored XSS into HTML context with nothing encoded"
date: 2026-09-14

categories:
  - Web Security

topic: Cross-site scripting

tags:
  - PortSwigger
  - Cross-site scripting
  - Web Security Academy

toc: true
---

# Lab: Stored XSS into HTML context with nothing encoded

## Lab Information

- **Platform:** PortSwigger Web Security Academy
- **Tool:** Burp Suite
- **Difficulty:** Apprentice
- **Vulnerability:** Cross-site scripting
- **Status:** Solved ✓

## Lab Objective

This lab contains a simple reflected cross-site scripting vulnerability in the search functionality.

To solve the lab, submit a comment that calls the ```alert``` function when the blog post is viewed.

## Cross-site scripting

Cross-site scripting is when a attacker injects malicious code/script into the website.It happens when website takes untrusted user input (like text from a form, URL parameter, search query, or comment field) and include it in page as it is without proper sanitization.
Now if an attacker upload any malicious code/script into website, it will not treat is as an plain text and put it in the codebase of website.

Common types are:

1. Stored(persistent) XSS
2. Reflected XSS
3. DOM-based XSS

## Exploitation

1. In this lab the comment box of any post is a vulnerable field. If I write something in comment box, the website treat it as the part of code not plain text/input.
   
2. Then I put some special character (like <, >, ") and the website still accepting it as input. It tells that the website have XSS vulnerability.

3. Now as the lab ask me to call a ```alert``` funcion to solve the lab, I put
 ```text
 <script> alert() </script>
```
in the comment box. And now when I go back the the post an alert message appears.

## Result

After putting 
```text
<script> alert() </script>
```
in the comment box, it shows an alert pop-up every time I visit the post.

![Reflected XSS into HTML context- Solved](/assets/images/portswigger/XSS/Stored-XSS.png)


## Key Takeaways

1. It doesn't need a victim to click anything
Unlike reflected XSS, the payload gets saved on the server (in a comment, profile field, post, etc.) and runs automatically for every user who views that page. No phishing link needed — just visiting the page is enough.

2. One injection can hit many victims
Since the malicious script lives in the database, a single successful injection can compromise every user who loads that page — including admins, which makes it especially dangerous for privilege escalation.

3. Persistence makes it harder to catch
The payload stays live until someone finds and removes it from the backend. It's not a one-time event like reflected XSS — it just sits there, quietly firing every time the page loads.

4. Same root cause, bigger blast radius
Just like reflected XSS, it comes down to unescaped user input being rendered as HTML. The difference isn't the vulnerability itself — it's where that input ends up (stored vs. thrown back immediately) that changes the severity.
  
**Lab Status: Solved ✓**
