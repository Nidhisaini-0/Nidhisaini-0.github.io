---
layout: default
title: Categories
---

<div class="page">

  <h1 class="page-title">
    Categories
  </h1>

  <div class="category-list">

    {% for category in site.categories %}

      {% assign category_name = category[0] %}
      {% assign posts = category[1] %}

      <section
        class="category-section"
        id="{{ category_name | slugify }}"
      >

        <div class="section-header">

          <h2>
            {{ category_name }}
          </h2>

          <span class="category-count">
            {{ posts.size }} post{% if posts.size != 1 %}s{% endif %}
          </span>

        </div>


        {% if category_name == "Web Security" %}

          <!-- Web Security Topics -->

          {% assign topics = posts | map: "topic" | compact | uniq | sort %}

          {% for topic in topics %}

            <div class="topic-section">

              <h3>
                {{ topic }}
              </h3>

              <div class="post-list">

                {% for post in posts %}

                  {% if post.topic == topic %}

                    <a
                      href="{{ post.url | relative_url }}"
                      class="post-card"
                    >

                      <span class="post-date">
                        {{ post.date | date: "%d %B %Y" }}
                      </span>

                      <h4>
                        {{ post.title }}
                      </h4>

                      <p>
                        {{ post.excerpt
                           | strip_html
                           | strip_newlines
                           | truncate: 160
                        }}
                      </p>

                    </a>

                  {% endif %}

                {% endfor %}

              </div>

            </div>

          {% endfor %}


          <!-- Web Security posts without a topic -->

          {% assign untitled_posts = posts | where_exp: "post", "post.topic == nil" %}

          {% if untitled_posts.size > 0 %}

            <div class="post-list">

              {% for post in untitled_posts %}

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
                    {{ post.excerpt
                       | strip_html
                       | strip_newlines
                       | truncate: 160
                    }}
                  </p>

                </a>

              {% endfor %}

            </div>

          {% endif %}


        {% else %}

          <!-- Normal categories -->

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

                <p>
                  {{ post.excerpt
                     | strip_html
                     | strip_newlines
                     | truncate: 160
                  }}
                </p>

              </a>

            {% endfor %}

          </div>

        {% endif %}

      </section>

    {% endfor %}

  </div>

</div>