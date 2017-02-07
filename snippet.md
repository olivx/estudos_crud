
# examples for snippets

#### if want know whats the url you access , you may do this

{% if  request.resolver_match.url_name == 'home'  %}


#### pagination with search and bootstrap class on links

 {% if book_list.has_other_pages %}
<ul class="pagination">
    <!-- navega para traz  -->
    {% if book_list.has_previous %}
    <li><a href="?page={{ book_list.previous_page_number }}{% if request.GET.search %}&search={{ request.GET.search }}{% endif %}">&laquo;</a></li>
    {% else %}
    <li class="disabled"><span>&laquo;</span></li>
    {% endif %}
    <!-- cria lista de pagina -->
    {% for i in book_list.paginator.page_range %}
    {% if book_list.number == i %}
    <li class="active"><span>{{ i }} <span class="sr-only">(current)</span></span></li>
    {% else %}
    <li><a href="?page={{ i }}{% if request.GET.search %}&search={{ request.GET.search }}{% endif %}">{{ i }}</a></li>
    {% endif %}
    {% endfor %}
    <!-- navega para frente-->
    {% if book_list.has_next %}
    <li><a href="?page={{ book_list.next_page_number }}{% if request.GET.search %}&search={{ request.GET.search }}{% endif %}">&raquo;</a></li>
    {% else %}
    <li class="disabled"><span>&raquo;</span></li>
    {% endif %}
</ul>
{% endif %}

#### form with widget_tweaks
{% load widget_tweaks %}

<!-- loop  -->
{% for field in form %}
<div class="control-group {% if field.errors%} has-error {% endif %}">
    <label for="{{ field.id_for_label }}"> {{ field.label }}  </label>
    {% render_field field class="form-control" %}
    {% for error in field.errors %}
    <p class="help-block">{{ error }}</p>
    {% endfor %}

</div>
{% endfor  %}

#### simple login
<div class="modal fade" id="login-modal" tabindex="-1" role="dialog"

     aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">

    <div class="modal-dialog">

        <div class="loginmodal-container">

            <h1>Faça o Login </h1><br>

            <form method="post" action="{% url 'login' %}">
                {% csrf_token %}

                <input type="text" name="username" placeholder="Usuario ">
                <input type="password" name="password" placeholder="Senha ">
                <input type="submit" name="login" class="login loginmodal-submit" value="Login">

            </form>

            <!--<div class="login-help">-->
                <!--<a href="#">Register</a> - <a href="#">Forgot Password</a>-->
            <!--</div>-->

        </div>
    </div>
</div>


#### simple logout
{% extends 'base.html' %}


{% block container %}
<div class="col-md-4 col-md-offset-4">
    <h1 class="page-header text-center text-primary"> Thanks for your visit  !</h1>
</div>

{% endblock %}


#### base.html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>{% block title %} Books {% endblock%}</title>

    <!-- Bootstrap -->
    <link href="{%  static 'css/bootstrap.min.css' %}" rel="stylesheet">
    <link href="{%  static 'css/books.css' %}" rel="stylesheet">
    <link href="{%  static 'css/jquery-ui.min.css' %}" rel="stylesheet">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  {% include 'partial/menu.html'%}

  <body>

    <div class="container">
        {% block container %}
        {% endblock %}
    </div>


    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="{% static 'js/jquery-3.1.1.min.js' %}"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="{% static 'js/bootstrap.min.js' %}"></script>
    <script src="{% static 'js/bootstrap-datepicker.js' %}"></script>
    <script src="{% static 'js/locales/bootstrap-datepicker.pt-BR.js' %}"></script>

    {% block java_script_app %}
    {% endblock %}
  </body>
</html>


#### generic modal
<!-- modal generic -->
<div class="modal fade" id="modal-book">
    <div class="modal-dialog">
        <div class="modal-content">



        </div><!-- modal content  -->
    </div>
</div>


#### form on modal

<form action="{% url 'book_save' %}" method="post" class="js-create-form">

    <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true"> x </button>
        <h4 class="modal-title"> ADD New Book </h4>
    </div>

    <div class="modal-body">
        {% csrf_token %}

        {% include 'partial/book_form.html'%}

    </div>
    <div class="modal-footer">
        <button class="btn" data-dismiss="modal" aria-hidden="true">Fechar</button>
        <button class="btn btn-primary">Salvar</button>
    </div>


</form>
