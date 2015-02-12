---
layout: default
title: Kubernetes Resources
category: Informational Pages
permalink: /info/kubernetes.html
---

Kubernetes is an open source system for managing containerized applications
across multiple hosts, providing basic mechanisms for deployment, maintenance,
and scaling of applications.




#### User Documentation

<ul>
{% for link in site.data.kubernetes_usernav %}
    <p><a href="{{ link.url }}"><i class="fa fa-angle-right"></i> {{ link.title }}</a></p>
{% endfor %}
</ul>


#### Developer Documentation
<ul>
{% for link in site.data.kubernetes_devnav %}
    <p><a href="{{ link.url }}"><i class="fa fa-angle-right"></i> {{ link.title }}</a></p>
{% endfor %}
</ul>

