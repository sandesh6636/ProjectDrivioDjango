<style>
    .asteriskField{
        color: red;
    }
</style>

{% extends 'layout.html' %}
{% load crispy_forms_tags %}
{% load static %}



{% block main_content %}
<div class="container">
    <div class="d-flex justify-content-center">
        <div class="col-md-6">
            <h2 class="text-success text-center">Update Product Form</h2>
            {% for msg in messages %}
            {% if msg.level == DEFAULT_MESSAGE_LEVELS.SUCCESS%}
            <div class="alert alert-success">
                {{msg}}
            </div>
            {% endif %}
            
            {% if msg.level == DEFAULT_MESSAGE_LEVELS.ERROR%}
            <div class="alert alert-danger">
                {{ msg }}
            </div>
            {% endif %}
            {% endfor%}
            <form action="" method="POST" class="shadow-lg p-3" enctype="multipart/form-data">
                {% csrf_token %}
                {{ form | crispy }}
                <div class="mt-3">
                    <input type="submit" name="submit" value="Update Product" class="btn btn-primary">
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}
