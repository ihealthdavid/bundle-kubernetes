---
layout: default
title: Juju Resources
category: Informational Pages
permalink: /info/juju.html
---

Juju is a service orchestration tool developed and sponsored by Canonical. It
interfaces with with existing configuration management solutions in a language
agnostic way, and drives system deployments with a declarative, event driven
model.

If you are new to Juju, it may be helpful to begin with the Documentation for
Juju, hosted at [juju.ubuntu.com/docs](http://juju.ubuntu.com/docs)

#### Juju User Documentation

<ul class="col-sm-6 col-md-4 ">
{% for link in site.data.jujucharms_usernav %}
    <p><a href="{{ link.url }}"><i class="fa fa-angle-right"></i> {{ link.title }}</a></p>
{% endfor %}
</ul>

#### Juju Developer Documentation

<ul class="col-sm-6 col-md-4 ">
{% for link in site.data.jujucharms_devnav %}
    <p><a href="{{ link.url }}"><i class="fa fa-angle-right"></i> {{ link.title }}</a></p>
{% endfor %}
</ul>


