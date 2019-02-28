# pitch

## Author: Carine Izere

## Description

        Pitches is a web application that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them. The pitches are organized by category. You can have different categories like pickup lines, interview pitch , product pitch, promotion pitch.

## View Live Site here

        To use this application, visit the live application link at:
        https://newshighlightc.herokuapp.com/

## User Requirements

        user should see the pitches other people have posted.
        user should vote on the pitch they liked and give it a downvote or upvote.
        user should comment on the different pitches and leave feedback.
        user should submit a pitch in any category.
        user should view the different categories.

## Features

        Create and display pitches based on categories
        Create category for pitches
        Display trending pitches based on day, week, month, year.
        Display the latest pitches and comments.
        Create user accounts with roles
        Send email verification to users with secret token that expires after sometime
        Send email to admin user when a new user signs up.
        Generate gravatars
        Editing user profiles
        Admin and moderator user with admin roles : create/delete/edit pitches topics, other users pitches and user's roles.
        User's messaging capability
        Show user's with the most pitches upvotes
        Multiple language support using flask-babel

## Specifications

### Setup & Requirements

        Clone the repository
        install all the requirements in the file > requirements.txt
        open terminal and go to the project folder, run \$ ./start.sh

# first initialize the database if the migrations folder does not exist

        python manage.py db init

# create a migration

        python manage.py db migrate -m "initial migration"

# upgrade

        python manage.py db upgrade

### Cloning

        \_In your terminal:

        \_\$ git clone https://github.com/CarineIzere/Pitch.

        \*\$ cd Pitch

## Technologies used

        - Python 3.6
        - Flask Framework
        - HTML, CSS and Bootstrap
        - JavaScript
        - Git
        - Postgres db

## License

      [![License: MIT]

## copyright

      ©2019 [Carine Izere]

## Support and contact details

      tel:+250783706421 E_mail : carizeree@gmail.com

## Bugs

      No bugs have been identified as far but incase of any contact author

## Contribution

      pull requests are encouraged

## Acknowledge

      It will be a great pressure for anyone will use my code.
