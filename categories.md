---
layout: default
title: Categories
permalink: /categories/
---

<div class="category-page">

  <h1>Categories</h1>

  {% assign categories = site.categories | sort %}

  {% for category in categories %}

    <div class="category-section">

      <h2>
        {{ category[0] }}
      </h2>

      {% assign category_posts = category[1] %}

      {% assign topics = category_posts
        | map: "topic"
        | compact
        | uniq
        | sort
      %}

      {% for topic in topics %}

        <div class="topic-section">

          <h3>
            {{ topic }}
          </h3>

          <ul>

            {% for post in category_posts %}

              {% if post.topic == topic %}

                <li>
                  <a href="{{ post.url | relative_url }}">
                    {{ post.title }}
                  </a>
                </li>

              {% endif %}

            {% endfor %}

          </ul>

        </div>

      {% endfor %}

    </div>

  {% endfor %}

</div>