
# Keeno. A ticket for endless memories

## About
Keeno is a django based cinema ticket web-store.
Link: [keenoticket.pythonanywhere.com](http://keenoticket.pythonanywhere.com) (**adblock recommended**)

Implemented features:
- Movie poster slider
- Showtime table
- Cinema info webpage with an ability to book available seats via a modern conveinient interface
- Seat booking uses Rest API for a seemless experience
- All the information is stored in a SQLite database that consists of 3 tables: movie, theater, showtime
- Website has an admin page accessible at /admin. Login: admin, password: admin
- Website is adapted for all kinds of screens

# Setup

The first thing to do is to clone the repository:

$ git clone [https://github.com/petosbratok/keeno](https://github.com/petosbratok/keeno)

$ cd keeno

Install Python and Pip.
Install the dependencies:

$ pip install -r requirements.txt

Once  `pip`  has finished downloading the dependencies:

$ cd project
$ python manage.py runserver

Home page will be at  `http://127.0.0.1:8000/`
Shotimes link: `http://127.0.0.1:8000/post/<post_id>`
Admin page: `http://127.0.0.1:8000/admin`

# Walkthrough

After loading the homepage, user is greeted with a poster slider showing recent movie additions. 
Below the slider you can find a showtimes table. Click on the **book here** button to get to the showtime page. 
Showtime page consists of all the necesarry movie info and a user interface required to book a seat

