---
layout: default
title: SQL Injection
permalink: /web-security/sql-injection/
---

<div class="category-page">

  <h1>SQL Injection</h1>

  <p>
    PortSwigger Web Security Academy labs covering
    SQL injection vulnerabilities and exploitation techniques.
  </p>

  <h2>Labs</h2>

  <div class="post-list">

    {% assign sql_posts = site.posts | where_exp: "post", "post.topic == 'SQL Injection'" %}

    {% for post in sql_posts %}

      <article class="post-card">

        <h3>
          <a href="{{ post.url | relative_url }}">
            {{ post.title }}
          </a>
        </h3>

        <p>
          {{ post.excerpt | strip_html | truncate: 160 }}
        </p>

        <small>
          {{ post.date | date: "%B %d, %Y" }}
        </small>

      </article>

    {% else %}

      <p>No SQL Injection labs documented yet.</p>

    {% endfor %}

  </div>

</div>
