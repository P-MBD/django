{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ name }}
{% endblock %}

{% block html %}
This is an <strong>html</strong> message.
<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZ_AxHyJTfxcxpt0bn313ReGPqfSCNkqEhuQ&usqp=CAU'>
{% endblock %}