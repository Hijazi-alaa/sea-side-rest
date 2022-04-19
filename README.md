# Sea Side Restaurant

## [Sea Side](https://seaside-rest.herokuapp.com/)

<img src="readme-images/responsive.png">

<br>

This is a restaurant app that allows users to book a table at a certain time,
the site owner or admin can approve or dismiss the bookings. <br>
The site also has a menu page where Admin can add, edit, or delete menu items for visitors to see. <br>

<ul>
Technologies and libraries used:
<li>Python</li>
<li>Django.</li>
<li>Bootstrap</li>
<li>HTML/CSS</li>
<li>JavaScript</li>
<li>Cloudinary-storage</li>
<li>PostgreSQL</li>
</ul>
Sea Side consists of 3 separated apps: reservation, menu and announcement
<hr>
Additionally, the admin can use the admin panel to publish new events and announcements wish then displayed in a section called announcements on the home page. <br>
Provided with Django's built-in user model, the app requires users to register or log in in order to create a booking, edit their own existing booking, or even delete their bookings. Bookings are only available to see for the user that created them.

The application is fully responsive on all devices.
<img>

Sea Side Restaurant is a full-stack application developed using agile methodology.
below are the issues that were defined before starting the applications with acceptance criteria

### mock up
I created a mock up of the home page using [Figma.com](https://www.figma.com/)
<img src="readme-images/mockup.png">
Worth to know that changes made to the homepage design while developing.

## Features <hr>
Through out development, I followed the issues' acceptance criteria on every issue

### stage 1
<img src="readme-images/1.png">

#### User Story View booking
<img src="readme-images/issue13.png">

#### User Story Add a booking
<img src="readme-images/issue1.png">

#### User Story Booking confirmation
<img src="readme-images/issue14.png">

#### User Story Authorization
<img src="readme-images/issue2.png">
<hr>

### stage 2
<img src="readme-images/2.png">

#### User Story Booking page
<img src="readme-images/issue7.png">

#### User Story Booking Authentication
<img src="readme-images/issue5.png">

#### User Story Authenticate to edit a booking
<img src="readme-images/issue6.png">
<hr>

### stage 3
<img src="readme-images/3.png">

#### User Story Delete Booking
<img src="readme-images/issue4.png">

#### User Story Edit booking
<img src="readme-images/issue3.png">

#### User Story Oppening Hours
<img src="readme-images/issue9.png">

<hr>

### stage 4
<img src="readme-images/4.png">

#### User Story Menu
<img src="readme-images/issue8.png">

#### User Story Address 
<img src="readme-images/issue10.png">

#### User Story Announcements
<img src="readme-images/issue12.png">

#### User Story Map
<img src="readme-images/issue11.png">

<hr>

### Other Features

<ul>
<li>Navbar contains a restaurant's logo and links to all relevant pages, Booking only appears for logged-in users, instead, a none logged-in user would see a sign-up and sign-in links</li>
<img src="readme-images/navbar.png"> <br>
<img src="readme-images/navbar2.png">

<li>The hero image on the home page contains 2 buttons 1 for creating a booking, that redirects non logged-in users to log in first in order to book.</li>
<br>
<img src="readme-images/hero-btn.png">
<br>

<li>View menu button available to all visitors.</li>

<li>About us section on the home page showcase the restaurant's services.</li>

<li>Google map API provided on the home page showing the location of the restaurant.</li>

<li>Menu page provided with an introduction of Kitchen chefs with social media links for each chef.</li>
<br>

<img src="readme-images/chefs.png">
<br>

<li>Feedback provided to all users actions in the form of messages, messages will disappear after 3 seconds of appearing.</li>

<li>Responsive footer at the bottom of every page, provided with social media links.</li>
<br>
<img src="readme-images/footer.png">
<br>
</ul>
<hr>

### Potential features to implement:
<ul>
<li>Ability for admin to change opening hours.</li>
<li>Check availability of tables and auto accept bookings according to it.</li>
</ul>

## Testing
<hr>
<ul>Manual Testing:
<li>Booking data model tested: all of its CRUD functionality for the admin and users</li>
<li>Tested confirm bookings by admin.</li>
<li>Menu data model tested: create and read functionality for admin, and only view for users</li>
<li>Announcements data model: tested create and read functionality for the admin and only view for users</li>
<li>Sign-up/ Sign-in forms and links all tested to confirm working as intended</li>
<li>Tested Booking page links and all its functionality</li>
<li>Tested User Authorisations to ensure role-based functions such as Booking page access, edit or deleting bookings</li>
</ul>

### Validator Testing
<ul>
<li>All Python code ran through PEOP8 checker succesfully without any problem.</li>

<li>All CSS files ran through CSS jigsaw validator with no errors</li>

[CSS JIGSAW](https://jigsaw.w3.org/css-validator/) passed with no erros.
<img src="readme-images/css-jigsaw.png">

<li>All HTML files ran through W3C validator with no errors</li>

[HTML W3C validator](https://validator.w3.org/)
</ul>

<hr>

## Deployment
At the start of making the project I the made the first deployment to Heroku after setting up the environment by doing the following steps:
<ol>
<li>Installing Django and supporting libraries</li>
    <ul>
        <li>Installed Django and gunicorn</li>
        <li>Installed supporting libraries</li>
        <li>Installed Cloudinary Libraries</li>
        <li>Created project and app</li>
        <li>Ran server to test</li>
    </ul>
<li>Deploying an app to Heroku</li>
    <ul>
    <li>Created an app on Heroku</li>
    <li>Attached the database</li>
    <li>Prepared environment and settings.py file</li>
    <li>Got my statc and media files stored on Cloudinary</li>
    <li>Deplyed the app (empty) by linking my Github and chose deploy branch.</li>
    </ul>
<li>Final deployment after finishing the project:</li>
    <ul>
    <li>Installed heroku in gitpod using the command: npm install -g heroku</li>
    <li>Logged in to heroku in the terminal window used command: login -i</li>
    <li>Entred command heroku git:remote -a seaside-rest to select the heroku app I created before remotly</li>
    <li>Added and commited all changes to github</li>
    <li>pushed to github and heroku using commands:
    <ul>
        <li>git push origin main</li>
        <li>git push heroku main</li>
    </ul>
    </li>
    </ul>
</ol>
End of deployment

## Credits
<hr>

Hero Image was taken by a google search, Original site owner is:
https://www.ahusseaside.com/

Images of chefs and hero sections buttons style are taken from a boot strap template:

[Bootstrapmade](https://bootstrapmade.com/delicious-free-restaurant-bootstrap-theme/)

Html elemnts main responsivenes are [Bootstrap](https://getbootstrap.com/)

all icons used in the projects are [FontAwsome](https://fontawesome.com/)

Fonts from by [Google Fonts](https://fonts.google.com/)

Map API from [Google map platform](https://mapsplatform.google.com/)

Used the lessons videos of (I think therefore I blog) for reference on deployment and creating a model.

Recived help from Daniel_c_5p on slack in :
<ul>
<li>restrict booking views to the user that owns the booking</li>
<li>Help with menu view function to view menu items in 4 seperate categories</li>
</ul>

Code institute tutor support helped me get back on track on several occasions when I had errors or any problems throughout the project.