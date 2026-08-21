---
layout: default
title: Home
---

# CyberSec Blog

### Learn. Experiment. Understand. Secure.

Welcome to my cybersecurity blog.

Here I document my journey through cybersecurity, web security, networking, Linux, and ethical hacking.

## Latest Posts

{% for post in site.posts %}
### [{{ post.title }}]({{ post.url }})

{{ post.excerpt }}

[Read more →]({{ post.url }})

---
{% endfor %}
