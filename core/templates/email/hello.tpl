{% extends "mail_templated/base.tpl" %}

{% block subject %}
Account Activations 
{% endblock %}

{% block html %}
{{token}}
{% endblock %}