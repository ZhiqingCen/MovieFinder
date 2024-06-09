# Project User Story

## Epic Story
- Search Function
- Movie Information
- Review & Rate Function
- Browse Function
- Account
    - Wishlist Function
    - Banlist Function
    - Email Confirmation Function
    - Password Reset Function

---

### Movie Information Page
As a movie finder, I want to have a detailed information page about the movie, so that I can tell if I am interested in this movie.
- Each movies has a poster
- Each movies has an information section which includes its name, description, genre, cast
- Each movies has rate and review section which includes its latest average rating of the site, all associated reviews, and a textbox to rate and write review
- The movie without ratings should be rated 0
- time
    - backend - 1h
    - frontend - 5h
- priority
    - backend - first?
    - frontend - after dashboard and link of movies created

As a movie finder, I want to have movie recommendations based on my wish-list and rating, so that I can explore more movies of my interest.
- Each movies has a recommendations section which list recommended movies' name based on user's wish-list and rating of that movie
- Each recommended movies has a link to this movie's information page
- Recommended movies is sorted in rating order and then sorted alphabetically
- time
    - backend - 2h
    - frontend - 2h
- priority
    - backend - after movie database created
    - frontend - after movie page implemented

---

### Review & Rate
As a movie fan, I want to rate and comment on the movie, so that I can express my thoughts on it.
- Each movie has a rate and review section
- Each movie can be rate between 0-5, with 0 being the worst and 5 being the best
- User cannot modified their own rating, once rated, rating buttons are disabled
- Each movie has a textbox for user to enter comment with a submit button
- Before submitting a comment, user must rate the movie
- Comments are sorted according to comment submission time
- Each user can leave multiple comments about a movie
- Each review will be check by automatic bots or admin (TBC) before displaying publicly at the movie page
- time
    - backend - 2h
    - frontend - 2h
- priority
    - backend - after movie database created and user account function implemented
    - frontend - after movie page and user account implemented

As a movie fan, I want to reply to others' reviews, so that I can interact with others.
- Each review has a like and dislike buttons
- After clicking the like button, like button is coloured/filled red and dislike button is disabled
- After clicking the dislike button, dislike button is coloured/filled red and like button is disabled
- time
    - backend - 1h
    - frontend - 1h
- priority
    - backend - after rating and comment function
    - frontend - after movie page, user account and rate & review section implemented

As a movie fan, I want to delete any comment that I have made in case there is a typo or it is inappropriate
- Each review has a delete button
- Once the delete button is click, this comment is deleted from the database and disappear from the frontend
- Once the delete button is click, alert of successfully deleted a comment is shown to the user
- time
    - backend - 1h
    - frontend - 1h
- priority
    - backend - after rating and comment function,
    - frontend - after movie page, user account and rate & review section implemented

---

### Dashboard
As a user, I want to have a dashboard which I can navigate through and back from any other pages.
- A header bar consist of
    - an icon and name of website which is a link towards the dashboard
    - a username which is a link to the user's profile page
    - a search section which allow user to type with a search button
- The dashboard has a movie section which show a list of movies
- Each movies shown has a poster, clickable movie name which link to the movie page, and its rating
- A footer bar consist of a link to the automatic bot
- time
    - frontend - 4h(frontend only）
- priority
    - frontend - first

As a movie finder, I want to browse through high rated movies of different categories.
- A genre selection panel which allow user to click on genre buttons and display relevant high rated movies in the movie section
- Movies of each genre are display from the highest rating to the lowest rating with alphabetical order
- The movie section will display 20 movies, with a page selection panel for user to navigate to the rest of the movies
- time
    - frontend - 3h (frontend only)
- priority
    - frontend - after dashboard implemented


---

## Database Structure

movies: {
    id:
    name:

}

account: {
    movies: {[
        {id:
        rating:
        comments: []
        }
    ]}
}


---
