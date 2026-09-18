# CyberSec Blog

A personal cybersecurity blog where I document my learning journey, practical labs, security concepts, and hands-on experiments.

🌐 **Live Blog:** https://nidhisaini-0.github.io/

## About

This blog focuses on learning cybersecurity through practical exploration and hands-on labs.

Topics currently covered include:

* Web Security
* SQL Injection
* Cross-Site Scripting (XSS)
* PortSwigger Web Security Academy labs
* Practical cybersecurity concepts
* Security tools and techniques

## Blog Structure

The blog is built using **Jekyll** and hosted with **GitHub Pages**.

```text
Nidhisaini-0.github.io/
├── _layouts/          # Jekyll page layouts
├── _posts/            # Blog posts
├── assets/            # Images and other assets
├── _config.yml        # Jekyll configuration
├── about.md           # About page
├── categories.md      # Categories page
├── tags.md            # Tags page
├── index.md           # Home page
└── web-security.md    # Web Security category
```

## Technologies

* Jekyll
* Markdown
* HTML
* CSS
* Git
* GitHub Pages

## Content

Most posts are based on hands-on cybersecurity labs and experiments. The writeups focus on documenting:

1. The vulnerability or security concept
2. The vulnerable behavior
3. The exploitation process
4. Practical observations and key takeaways

## Running Locally

To run the blog locally, make sure Ruby and Jekyll are installed.

Clone the repository:

```bash
git clone https://github.com/Nidhisaini-0/Nidhisaini-0.github.io.git
cd Nidhisaini-0.github.io
```

Install the required dependencies:

```bash
bundle install
```

Start the Jekyll development server:

```bash
bundle exec jekyll serve
```

Then open:

```text
http://localhost:4000
```

## Adding a New Post

Create a Markdown file inside `_posts/` using the Jekyll naming format:

```text
YYYY-MM-DD-post-title.md
```

Example:

```text
2026-09-18-example-security-lab.md
```

A typical post starts with front matter such as:

```yaml
---
layout: post
title: "Example Security Lab"
date: 2026-09-18
categories: [Web Security]
topic: SQL Injection
tags: [sql-injection, web-security, cybersecurity]
toc: true
---
```

Then add the writeup below the front matter.

## Disclaimer

All security testing documented on this blog is intended for **educational purposes and authorized environments only**.

Do not use the techniques described here against systems or applications without permission.

## Author

**Nidhi Saini**

Cybersecurity learner documenting practical security research, labs, and projects.

---

⭐ If you find the content useful, feel free to explore the blog and follow the repository.
