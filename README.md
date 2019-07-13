# Django-Application
<h4>
Create a superUser account before interacting with User, Account, Model and Admin Privilages
</h4>
<h2>
Main Features :
</h2>
<ul>
<li>Blog Page Featured With Backend Dashboard</li>
  <li>Category Based Post with title,content and image </li>
<li>User Profile Page with Update Feature</li>
<li>Registration,login,logout Page</li>
<li>Frondend and Backend Validation</li>
<li>After Login, User can Create, Update and Delete Their Posts</li>
<li>After Login, User can update Their Profile Info Like (E-mail , Username and Profile Pictures) </li>
<li>Number of Posts By a Specific User </li>
  <li>Number of Posts By a Specific Category  </li>

</ul>

<h2>
Used Technolgies :
</h2>
<ul>
<li>Python</li>
<li>Django v2.2.1</li>
<li>SQLite3</li>
<li>HTML</li>
<li>CSS</li>
<li>Bootstrap</li>
<li>Crispy Form</li>
<li>Font-Awesome</li>
<li>JavaScript</li>
</ul>

<h2>Installation</h2>
<h4>Create WebBlog virtual environment & goto the directory.
</h4>

<h4>
Linux -->
</h4>
<div>
virtualenv -p /usr/bin/python3 dj
cd dj
</div>



<h4>
Windows -->
</h4>
<div>
virtualenv dj
cd .\dj\
</div>


<h2>Activate virtualenv :</h2>
<h4>Linux -->
</h4>
<div>
source bin/activate
</div>


<h4>Windows--></h4>
<div>
.\Scripts\activate
</div>

<h2>
clone the project in the dj directory.
</h2>

<div>
git clone https://github.com/sohanur-it/Django-Application.git
</div>

<h2>Install requirements.txt
</h2>
<div>
python -m pip install -r requirement.txt
</div>
<h2>
Now goto src/ directory and create db models.
</h2>


<div>
cd src/
python manage.py migrate
</div>

<h2>Run Server :</h2>
<div>
python manage.py runserver
</div>
Now go to<a href="http://127.0.0.1:8000/"><ul><li> http://127.0.0.1:8000/</li></ul> </a>

<h2>ScreenShots</h2>

<ol>
  <li>Registration Page : </li><br>
<img src="https://github.com/sohanur-it/Django-Blog/blob/master/src/screenshot/registration.png"><br><br>

  
 <li>Login Page : </li><br>
<img src="https://github.com/sohanur-it/Django-Blog/blob/master/src/screenshot/login.png"><br><br>

 <li>Home Page : </li><br>
<img src="https://github.com/sohanur-it/Django-Blog/blob/master/src/screenshot/home.png"><br><br>

 <li>Detail View of Post : </li><br>
<img src="https://github.com/sohanur-it/Django-Blog/blob/master/src/screenshot/detail_view.png"><br><br>
 
 <li>Profile Update  Page : </li><br>
<img src="https://github.com/sohanur-it/Django-Blog/blob/master/src/screenshot/profile.png"><br><br>

</ol>



