---
layout: default
title: Home
---

<section class="hero">

  <div class="terminal-label">
    root@cybersec:~$
  </div>

  <h1>
    Learn.
    <span>Break.</span>
    Secure.
  </h1>

  <p class="hero-description">
    A cybersecurity blog documenting practical learning,
    security concepts, tools, experiments, and everything
    in between.
  </p>

</section>


<section>

  <div class="section-header">

    <h2>
      Latest Posts
    </h2>

  </div>


  <div class="post-list">

    {% for post in site.posts %}

      <a
        href="{{ post.url | relative_url }}"
        class="post-card"
      >

        <span class="post-date">
          {{ post.date | date: "%d %B %Y" }}
        </span>

        <h3>
          {{ post.title }}
        </h3>

        <p>
          {{ post.excerpt | strip_html | truncate: 180 }}
        </p>


        {% if post.categories %}

          <div class="tags">

            {% for category in post.categories %}

              <span class="tag">
                #{{ category }}
              </span>

            {% endfor %}

          </div>

        {% endif %}

      </a>

    {% endfor %}

  </div>

</section>
