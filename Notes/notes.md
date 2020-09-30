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

<h3> Database summary </h3>

A database is a collection of information organised to __provide efficient retrieval__.

There are Relational Database Management Systems (RDBMS), generally referred to as SQL databases (Oracle, MySQL, PostgreSQL, SQLite).

There are also Non-Relational Database Management Systems (NRDBMS) generally  referred to as NoSQL databases (MongoDB, Cassandra, Redis, Aerospike, Couchbase).

**CAP Theorem** defines requirements of databases. Brewer proposed that distributed data store can only ever provide two out of the three:

1. **C**onsistency: all nodes see the same data at the same time
2. **A**vailability: every request gets a response of success/failure
3. **P**artition Tolerant: continued functionality even if the instance of the database fails

SQL/RDBMS tend to focus on Consistency & Availability

NoSQL/NRDBMS focus on either Partition tolerance & Consistency or Partition tolerance & Availability.

SQL databases are very popular but aren't enough for huge datasets we deal with today.

In Non-relational Databases (NoSQL) information is stored in a more flexible way and designed to be distribtued more than relational.

Here they follow the **BASE System** -> **B**asically **A**vailble, **S**oft State, **E**ventual consistency.

**Four major types of Non-Relational Databases**

1. Key-Value - hash table of keys and values
2. Column oriented - 2d array where each key has one or more key/value pairs
3. Document stored - similar to key-value but with some structure and encoding i.e. JSON / XML
4. Graph based - edges, nodes, and properties for index-free adjacency


SQL is better for applications that have structured data such as lists of users, blog posts, etc, while NoSQL tends to be better for data with a less defined structure.

<h3> Our Flask database </h3>

Here we will use a new package, **Flask-SQLAlchemy**. This is an extension that provides a Flask-friendly wrapper to the popular **SQLAlchemy** package. The SQLAlchemy package is an **ORM** (Object Relational Mapper). ORMs allow applications to manage a database using high-level entities such as classes, objects, and methods instead of table and SQL. The ORM will translate these high level operations into database commands.

SQLAlchemy supports several database engines including MySQL, PostgreSQL, and SQLite. So here we could use an SQLite database without a server during production and then when we deploy move to a more robust MySQL server without much effort.

`pip install flask-sqlalchemy`

<h3> Database Migrations </h3>

Making updates to an existing database as the application changes or grows is hard because relational databases are centered around structured data. So when the structure changes all the old data needs to be *migrated* to the modified structure.

**Flask-Migrate** is an extension which acts as a Flask wrapper for **Alembic**, a database migration framework for SQLAlchemy. A bit more work upfront but makes for much easier changes in the future.

`pip install flask-migrate`

**WARNING THIS DATABASE MIGRATION WRAPPED IS NOT UP TO DATE SO NOT USING FOR MY PROJECT**

<h3> Which SQL database to use? </h3>

**SQLite** databases are the most convenient choice for developing small applications. Each database is stored in a single file on a disk so there is no need to run a database server like **MySQL** or **PostgreSQL**.

So we can add a new config item to our config.py file to configure the database. SQLALCHEMY_DATABASE_URI config variable to show Flask_SQLAlchemy where the database is.

Then create an instance of our flask_sqlalchemy and flask_migrate in \_\_init\_\_.py.

<h3> What database model do we want to implement? </h3>

| data | datatype
|------	|----- |
| id | int |
| username | varchar (64) |
| email | varchar (120) |
| password_hash | varchar (128) |

Unique id assigned as the primary key of the database.

Other fields as strings (VARCHAR in database syntax) with max length defined for memory alllocation.

Note passwords stored as a hash. Proper security practice.

We can create this into code in a models.py file.

For our second database we will create a posts data type. The schema for this will link to the user_id of our users data type.

| data | datatype
|------	|----- |
| id | int |
| body | varchar (140) |
| timestamp | datetime |
| user_id | int |

Here the user_id field is called a *foreign key*. This is also a *one-to-many* relationship where one user_id can refer to many posts.

We will add this new class Post to our models.py.

In Python prompt to add users/posts:

`python`

`from my_package import db`

`from my_package.models import User, Post`

`db.create_all()` - create any new tables into db. Will not attempt to create any tables if they already exist. Note db.drop_all() to remove.

`u = User(username='Jack', email='jack.edison95@gmail.com')`

`db.session.add(u)`

`db.session.commit()`

You can query all users with:

`User.query.all()` - *note can access .id and .username parameters of users etc.*

To add a post:

`u = User.query.get(1)` - gets 1st user stored

`p = Post(body='my first post!', author=u)`

`db.session.add(p)`

`db.session.commit()`

You could get all the users posts with:

`u.posts.all()`

The [Flask SQLAlchemcy documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) can be helpful in finding syntax.

To erase the users database:

`users = User.query_all()`

`for u in users:`
`   db.session.delete(u)`

`db.session.commit()`

Can do the same with Post.

You can also add shell_context_processors to your code to auto import into Python shell (see tutorial) but I won't bother with this. i.e. means you wouldn't need to do import my_package each time.

<h2> Chapter 5: User Logins </h2>

<h3> Password hashing </h3>

In our user data we have a field for a hashed password. To implement password hashing we will use the **Werkzeug** package. *Note: in future could import my own SHA hashing but for now will use standard package for robustness.* Werkzeug is already installed with Flask as it is a core dependency.

We can hash with:

`from werkzeug.security import generate_password_hash`

`hash = generate_password_hash('foobar')`

We can check the hash with:

`check_password_hash(hash, 'foobar')`

We will add this to our models.py for when a user inputs a password for the database.

Now from python shell we could do `u.set_password('foobar')` and `u.check_password('foobar')` etc.

<h3> Flask-Login </h3>

This extension manages the user logged-in state which will remember while users browse pages. It also provides remember me functionality.

`pip install flask-login`

And then initialise in the \_\_init\_\_.py module.

Flask-Login works with a user model provided it has certain properties and methods. These four are:

1. is_authenticated: True if valid credentials else false.
2. is_active: True if account is active else false.
3. is_anonymous: False for regular users, True for special users.
4. get_id(): a method that returns unique identifier for user.

We could implement these but as they are generic Flask-Login provides a **UserMixin** class that includes generic implementations. We can add this to our User model in models.py as a parameter to feed in.

We will also add a **user loader function** to the models.py. This will allow flask-login to retrieve the user's id when called.

We can now add a full login function to our routes on the login page.

To log users out we can use Flask-Login's logout_user() function.

We will add a view function into routes.py to logout to logout user and redirect to index.

We will also add a logout option on the base.html naviation bar.

Required logins to view a page can be handled by the Flask-Login extension. By telling Flask-Login the view functions that handles logins (in \_\_init\_\_.py) we can use flask_login's login_required method as a decorator over routing in routes.py. A user will be redircted to the login page if they try to access the route without being logged in.

We can now login with user=Jack, pwd=foobar !

<h3> User registration </h3>

Till now the only way to create new users is through Python shell. So lets create a user registration form page.

Start by creating a RegistrationForm in forms.py to send to the HTML. For the email validator field we will `pip install email-validator`.

We will also create a register.html to display the form, a new-user query in the login.html form, and a new route function to the register page in routes.py.

<h2> Chapter 6: Profile Page and Avatars </h2>

To create a user profile page we will create a view function that maps /user/\<username\> to a URL.

Here we will want a page which shows any comments on past blog articles I suppose. Maybe account age too, last online, etc. Allow profile photos to be shown when posting.

So create a new route and html template for user's homepage. We will also add a link in the naviation bar.

<h3> Avatars </h3>

Instead of allowing users to upload custom avatars for now we will use Gravatar. We can generate a random image from a hash (hash of user in this instance) and assign it to their profile.

Build this into the User class in models.

Then adjust the user.html profile page to include the avatar.

We can improve the backend implementation of this post layout by creating a post sub-template to refer to under a blog or on the user's page. To create a sub template we will create the file _post.html.

With jinja2 we can include this with `{% include '_post/html' %}`

<h3> Adding new columns to database without migration </h3>

To make user's pages a bit more interesting we will add an about_me and last_see section. These will be added to the User model first which will require a database update.

To database update as we don't have a migration framework set up we will have to manually add these two new columns to our user table in the website_data.db database.

The code is implemented in db_manip.py for future functionality. SQLite3 datatypes for this process can be found [here](https://www.w3resource.com/sqlite/sqlite-data-types.php#:~:text=SQLite%20Date%20and%20Time%20Data,SSS%22).)

Next two steps are to update the user.html to show our new statistics and to ensure we are recording them correctly.

To log last_field we want to update the database whenever the user sends a request to the server. Instead of checking every request Flask offers a native feature .before_request we can add as a decorator over a function to run code before every request in routes.py.

Profile editor to allow a user to edit their about_me. I will try and implement this myself. I know I will need:

1. A form to fill that will update the db
2. An html page to fill in an about me
3. A route to that page

4. A link on their profile page to edit the profile

Successfully done (with some referencing :P).

<h2> Chapter 7: Error Handling </h2>

You can run Flask in debug mode to better understand errors in the browser by setting:

`export FLASK_DEBUG=1`

<h3> Custom error pages </h3>

We can create our own custom error handler pages with an @app.errorhandler(404) decorator for HTTP errors 404 for example.

We will create an error.py instead of putting in routes for our custom error handlers. We can then create some custom htmls 404.html and 500.html to inherit from base and keep the feel of the website. Finally, add import errors from my_package in \_\_init.\_\_py.

<h3> Emailing and logging errors locally </h3>

I'm not going to bother setting up emails but I will create log files locally using our old friend the logging package.

We will add this into \_\_init\_\_.py again.

<h2> Chapter 8: Followers </h2>

Databases many-to-many relationships are more complex in the back-end. For example, a user could have many followers and be following many other users. This is non trivial to show using relational databases and must use an auxiliary table called an **association table**.

Here we could have a big association table of all relationships such as:

| follower_id | followed_id |
| ---- | ---- |
| 1 | 2 |
| 1 | 3 |
| 1 | 4 |
| 2 | 3 |
| 3 | 4 |

This is the most efficient way to store all the data memory wise, and then could be queried for specific followers or following.

We could add this to our database but since I don't need this feature for my site I won't bother.

<h3> Unit Testing </h3>

A fundamental part to any large program when comple features are added.

Python includes a very useful `unittest` package that makes it easy to write and execute unit tests.

We can create a tests.py module to implement some rests for our User class.

These can be easily run with `python tests.py` from terminal. Or vscode implements inbuilt features to run.

If we had implemented followers we could add a form to follow on the user's page and update their profile to show the number of followers. We have done pretty similar stuff already so only new feature here would be a many to many database set up.

<h2> Chapter 9: Pagination </h2>

Submission of new posts.

To submit new posts to our blog we could build a method in browser (form class) instead of doing it directly from terminal.

<h2> Actually lets convert this into my website now then go back to tutorial and add anything else </h2>

**LETS TRY BUILD A PROPER MY PROJECTS AREA FIRST - Blog later**

1. A 'Projects' page. We will need routing to it, an html of it, a table for my projects in the db that the page displays.

2. Page that shows all my projects thumbnails and can click through. Should link to github or another web page ig, no need for default blog post page for now.
- database of projects
- html for project in projects display title, body, image, date, etc.

3. Projects link on toolbar

4. Create a project and see how it all works. Data storage etc.

5. Consider implementing web form to do so (pagination)

N/A blog only?. Default my blog page with title, text, pictures?

<h2> CSS & HTML notes </h2>

CSS (Cascading Style Sheets) is best practice for adding formatting to the HTML structure.

HTML should include content, CSS styling. This makes it easier to edit later.

CSS stylesheets are considered static files - there is no interaction with their code like there is with HTML templates.

Flask reserves a separate folder where you should put static files such as CSS, Javascript, images, or other files. That folder should be named *static*. It is also good practice to have a sub-folder *css*.

CSS refers to the HTML tags and div class names, applying fonts, colours, text, size, padding, margins, and background colours to those HTML elements.

Our HTML file then has to inherit the css page. We can do this with our *base.html* page as our other pages will inherit from it.

CSS can be added to an HTML document in 3 ways:

1. Inline by using the `style` attribute inside HTML elements
2. Internal by using a `<style>` element in the `<head>` section
**3. External by using a `<link>` element to link to an external CSS file in the `<head>` section** It should be added to the `<head>` section to be  called upon website load and decrease loading times. *(note: javascript should be inverse and placed at the cloding of the `<body>` tag.)*

In html you can use `meta` tags to assign meta data to the website. A title for google to scrape, a description, keywords, etc.

**Lets create a proper home page**:

* Photo of me
* About section of me
* Side links of images to linkedin etc

Literally just copy Tristan Hume.

Favicon: https://favicon.io/favicon-generator/ - kumbh sans font 110

KISS - {keep it simple stupid}

<h3> Colour scheme </h3>

Colour scheme taken from advice and recommendation on colour picking here: https://blog.datawrapper.de/beautifulcolors/

* color: black;
* color: rgb(100, 181, 192);
* color: rgb(28, 75, 117);
* color: rgb(244, 175, 92);
* color: rgb(174, 93, 33);


We have our colour scheme, lets create super basic template with quality content now.

In html by adding target="_blank" to urls we can set browser to open them in new tab. We will use this for all external webpages in the header.


What next?:

* comb through html and css any more best practices
* photo to about section: speech circled and coming out to left of about
* smaller project photos to index
* start adding projects database - include key projects column. Add languages and make nicer
* projects page nicer
* proper about me section
* push to github again!
* host online


**question/to do: how would we implement a relational database from ground up? what links in a class (like our linked list attempt)**

**add an API to databse for REST learning?**


Sources:
1. Web frameworks usage overview: https://www.fullstackpython.com/web-frameworks.html
2. Flask tutorial https://www.fullstackpython.com/flask.html
3. Building your own Python web framework **COULD BE AN AWESOME THING TO IMPLEMENT** https://testdriven.io/courses/python-web-framework/?utm_source=fsp or this https://mattscodecave.com/posts/simple-python-framework-from-scratch.html or this https://rahmonov.me/posts/write-python-framework-part-one/



