---
layout: default
title: Tags
---

<div class="page">

  <h1 class="page-title">
    Tags
  </h1>


  <div class="tag-cloud">

    {% for tag in site.tags %}

      {% assign tag_name = tag[0] %}

      <a
        href="#{{ tag_name | slugify }}"
        class="tag tag-large"
      >
        #{{ tag_name }}
      </a>

    {% endfor %}

  </div>


  <div class="tag-results">

    {% for tag in site.tags %}

      {% assign tag_name = tag[0] %}
      {% assign posts = tag[1] %}

      <section
        class="tag-section"
        id="{{ tag_name | slugify }}"
      >

        <div class="section-header">

          <h2>
            #{{ tag_name }}
          </h2>

          <span class="category-count">
            {{ posts.size }} post{% if posts.size != 1 %}s{% endif %}
          </span>

        </div>


        <div class="post-list">

          {% for post in posts %}

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

            </a>

          {% endfor %}

        </div>

      </section>

    {% endfor %}

  </div>

</div>
