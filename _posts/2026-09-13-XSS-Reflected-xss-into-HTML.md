---
layout: post
title: "Reflected XSS into HTML context with nothing encoded"
date: 2026-09-13

categories:
  - Web Security

topic: Cross-site scripting

tags:
  - PortSwigger
  - Cross-site scripting
  - Web Security Academy

toc: true
---

# Lab: Reflected XSS into HTML context with nothing encoded

## Lab Information

- **Platform:** PortSwigger Web Security Academy
- **Tool:** Burp Suite
- **Difficulty:** Apprentice
- **Vulnerability:** Cross-site scripting
- **Status:** Solved ✓

## Lab Objective

This lab contains a simple reflected cross-site scripting vulnerability in the search functionality.

To solve the lab, preform a cross-site scripting attack that calls the alert function.

## Cross-site scripting

Cross-site scripting is when a attacker injects malicious code/script into the website.It happens when website takes untrusted user input (like text from a form, URL parameter, search query, or comment field) and include it in page as it is without proper sanitization.
Now if an attacker upload any malicious code/script into website, it will not treat is as an plain text and put it in the codebase of website.

Common types are:

1. Stored(persistent) XSS
2. Reflected XSS
3. DOM-based XSS

## Exploitation

1. First I write a random string in the search bar and that string renders directly on the webpage. This behavior of website shows that the website is not handling the user input properly and storing it in webpage code.

2. Then I put some special character (like <, >, ") and the website still accepting it as input. It tells that the website have XSS vulnerability.

3. Now as the lab ask me to call a ```alert``` function to solve the lab, I put
 ```text
 <script> alert() </script>
```
in the search bar. And it shows an alert pop-up on the screen.

## Result

After putting 
```text
<script> alert() </script>
```
in the search bar, it shows an alert pop-up on the screen.

![Reflected XSS into HTML context- Solved](/assets/images/portswigger/XSS/Reflected-XSS.png)


## Key Takeaways

1. Unfiltered input = open door
This lab shows what happens when a website takes what you type and puts it straight into the page — no filtering, no encoding, nothing. Whatever you send, it shows.

2. No escaping needed to break in
Since the input lands right in the HTML body, you don't need any fancy tricks to close tags or escape quotes. A basic 
```text
 <script>alert(1)</script>
 ``` 
 just works.

3. It only fires when someone clicks
Reflected XSS isn't stored anywhere — it only runs when a victim opens a specially crafted link. So the real-world attack usually involves tricking someone into clicking it (phishing, basically).

4. View-source is your best friend
Before writing any payload, just check the page source. If you see your input sitting there untouched in the HTML, that's your confirmation the vuln is real.

5. The real fix is encoding, not blocking
Filtering out words like "script" doesn't really help — attackers just find workarounds. The actual fix is encoding output properly so the browser treats it as text, not code.
  
**Lab Status: Solved ✓**
