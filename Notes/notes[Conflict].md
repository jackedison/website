<h1> Web Frameworks - Flask </h1>

A **web framework** is a code library that makes web development faster and easier by providing common patterns for building reliable, scalable, and maintainable  web applications.

Since the early 2000s professional web development projects almost always use an existing web framework.

They make it easier to reuse code for common HTTP operations and to structure projects in more readable ways.

Popular frameworks include:
* Django
* **Flask**
* Bottle
* Pyramidd
* Morepath
* Turbogears

Common functionalities they provide include:
* URL routing
* Input form handling and validation
* HTML, XML, JSON and other output formats with a 'templating engine'?
* Database connection configuration
* Web security (think SQL injection etc)
* Session storage and retrieval


<h2> Flask </h2>
Flask was written several years after Django taking into account learnings and improvements.

Flask mega-tutorial by Miguel Grinberg: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

<h3> Installing package </h3>

Can install Flask from **PyPI** (Python Package Index). Tool to do this is called **pip**.

This downloads the package from PyPI and then adds it to your local Python installation.

<h3> Virtual Environment </h3>

To avoid old projects being ruined by newer installations of Flask on the computer, we will use a venv to keep package iterations the same unless specifically updated for the project.

<h3> Creating a package </h3>

A sub=directory that includes a \_\_init\_\_.py file is considered a package, and can be imported. When the package is imported the \_\_init\_\_.py executes.

Here we have created a package with imports routes (view functions detailing how to handle URL requests). Using decorators if a request for / or /index is called we return our function.

<h3> Running the package - FLASK_APP environment variable </h3>

We can run the package by first specifying the FLASK_App environment variable:

`export FLASK_APP=web_framework.py`

And then running it with:

`flask run`

<h3> Localhost </h3>

By default in a development environment it will use the freely available port 5000.

We can connect to our route URLs with either:

1. http://localhost:5000/

2. http://localhost:5000/index

Both of these routes are decorated to our view function.

<h2> Chapter 2: Templates </h2>

We can now add some basic HTML to the web page.

<h3> A quick note on web pages: HTML, CSS, Javascriipt </h3>

Almost all web pages are made up of HTML, CSS, and Javascript. In the 1990s HTML was the only building block. Basic Jack summary:

* HTML: Foundation of page structure. Text and dividers etc. Hyper text markup language.
* CSS: Makes it look nice (ever notice a page only load in HTML?) 1996 release with idea to remove all formatting from HTML and add to CSS. 'Cascading Style Sheet'. Without defined sheet will default to web browser's (e.g. time new roman, size 12 font, etc.)
* Javascript: Logic based programming language that can be used to modify website content and users' interaction with it. e.g. confirmation boxes.

HTML can also embed some basic logic (at least with Flask and Jinja2) and formatting, so for now we will get by with that.


<h3> HTMLs with Flask </h3>

Keeping full HTML of webpages in return functions would get too complicated. So instead we can keep them as templates.

We keep these in a templates folder inside the application package.

flask.render_template can render in any variables into the html.

We can even render in conditional statements into HTML with 

`{% if title %}`

`{% else %}`

`{% endif %}`

Dynamic list sizes / loops with

`{% for post in posts %}`

`{% endfor %}`

This is all handled by **Jinja2** in the render_template call.

<h3> Template Inheritance </h3>

If we wanted to add a navigation bar which exists on every page we want to inherit rather than replicate the code in each HTML.

Jinja2 has template inheritance.

So we can derive a base template which we will call base.html. 

A block control statement defines the place where the derived templates can insert themselves into the base template.

`{% block content %}{% endblock %}`

Then just inherit with:

`{% extends "base.html" %}`

<h2> Chapter 3: Web Forms </h2>

"How do we accept inputs from users through web forms?"

One option is to use the **Flask-WTF** extension. This is a wrapper around the **WTForms** package that integrates well with Flask. Extensions are an important part of the Flask ecosystem.

`pip install flask-wtf`

<h3> Configuration </h3>

It can be quite useful to set up a config.py file to configurate certain configuration variables for the flask app.

For example, the SECRET_KEY configuration variable allows Flask and Flask extensions to use the value of the secret key as a cryptographic key to generate signatures or tokens. For the Flask-WTF extension is allows it to block against CSRF (Cross-Site Request Forgery).

<h3> Web forms </h3>

Using FLask-WTF we can create some forms. For code readability and future extensions we will create them in a new module forms.py.

We also take classes to represent the field types from the WTForms package.

Validators check that the fields submitted are not empty. Better to use pre-designed packages here with tons of prior testing than to code your own logic.

Once we have the form class we can create a form template in the HTML to render it to the web page. We will create a new login.html that inherits from the base to include the top naviation bar.

Our login.html expects to be fed in a form object of our LoginForm class in the forms.py module.

<h3> Receiving form data </h3>

We can update the view function to accept and validate data using Flask-WTF methods.

GET requests are those that return information to the client (web browser).
POST requests are when the browser submits form data to the server.

<h3> Generating links </h3>

To have better control of links in your routes or html its good to handle them with the Flask function url_for(). This generates URLs using its internal mappings of URLs to view functions. So url_for('login') can be set to map to (return) /login. Then we can change the url_for variable in the future if we want a new login url.

<h2> Chapter 4: Databases in Flask </h2>

*Flask does not support databases natively.*

So we can pick another database that best fits our application. Two groups:

1. Those that follow the *relational* model
2. Those that do not (NoSQL, i.e. do not implement the popular relational query language SQL)

The former being better for applications that have structured data such as lists of users, blog posts, etc, while the latter tends to be better for data with a less defined structure.

Here we will use a new package, **Flask-SQLAlchemy**. This is an extension that provides a Flask-friendly wrapper to the popular **SQLAlchemy** package. The SQLAlchemy package is an **ORM** (Object Relational Mapper). ORMs allow applications to manage a database using high-level entities such as classes, objects, and methods instead of table and SQL. The ORM will translate these high level operations into database commands.

SQLAlchemy supports several database engines including MySQL, PostgreSQL, and SQLite. So here we could use an SQLite database without a server during production and then when we deploy move to a more robust MySQL server without much effort.

`pip install flask-sqlalchemy`

<h3> Database Migrations </h3>

Making updates to an existing database as the application changes or grows is hard because relational databases are centered around structured data. 



**question: how would we implement a relational database from ground up? what links in a class (like our linked list attempt)**


Sources:
1. Web frameworks usage overview: https://www.fullstackpython.com/web-frameworks.html
2. Flask tutorial https://www.fullstackpython.com/flask.html
3. Building your own Python web framework **COULD BE AN AWESOME THING TO IMPLEMENT** https://testdriven.io/courses/python-web-framework/?utm_source=fsp or this https://mattscodecave.com/posts/simple-python-framework-from-scratch.html or this https://rahmonov.me/posts/write-python-framework-part-one/



