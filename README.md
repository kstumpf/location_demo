location_demo
=============

<h3>Proverb Database: Form Testing with jQuery & AJAX</h3>

<p>
This project was created with:
<ul>
    <li><a href="https://www.python.org/downloads/">Python 2.7.6</a></li>
    <li><a href="https://www.djangoproject.com/download/">Django 1.6.5</a></li>
    <li><a href="http://jquery.com/download/">jQuery 2.1.1</a></li>
</ul></p>

<h3>Installation and Configuration:</h3>
<p>
Download the .zip file located to the right.
From the command line, enter the project and sync the database by typing the following: 
        python manage.py syncdb
Then run the server with:
        python manage.py runserver
        
        To play with the project, add locations of different types (Continent, Country, Culture), and then create new proverbs.
</p>

<h3>Proverb Database Features Studied</h3>
<p>This project studied the loading of separate forms to one page and the submission of said forms without redirection, all done through the use of jQuery. It also focused on creating dependent drop-downs in Django forms. This work is best shown in proverbs/templates/master_create.html & proverbs/templates/prov_create.html. 

The following tutorials and resources were used:
<ul>
    <li><a href="https://docs.djangoproject.com/en/1.6/">The Official Django Docs</a></li>
    <li><a href="http://api.jquery.com/">The jQuery API</a></li>
    <li><a href="http://courses.tutsplus.com/courses/30-days-to-learn-jquery/lessons/hello-jquery">30 Days to Learn jQuery</a></li>
    <li><a href="http://www.devinterface.com/blog/en/2011/02/how-to-implement-two-dropdowns-dependent-on-each-other-using-django-and-jquery/">Stefano Mancini's Dependent Drop Downs Tutorial</a></li>
</ul></p>

<h3>Further Improvements that Could be Made</h3>
<p>
<ul>
    <li>Continents with spaces in their names prevent prov_create.html's javascript call to all_json_countries from going through properly.</li>
    <li>Merge the ProverbForm with the html form to create one cohesive Proverb form that can be properly submitted to create new Proverbs.</li>
    <li>When, on the master_create page, a location form is submitted, find a way to alert the proverb form so that it can reload to show the new location. Ideally, this reload would not delete the info that had already been entered in the proverb form.</li>
</ul></p>
