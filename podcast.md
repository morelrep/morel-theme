---
title: Sóngoro cosongo
tagline: A podcast on Afro-Latin American music and literature
layout: post-index
---
<ul>
  {% for post in site.posts %}
    <li>
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <div class="ficha-metadata">
          Posted on <span class="metadata-input">{{ post.date | date_to_string }}</span><!-- here we will add tags that organize blog posts by content-->        
      </div>
    </li>
  {% endfor %}
</ul>