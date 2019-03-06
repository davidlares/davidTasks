# DavidTasks

This repo is a simple demo with a professional approach on how to use Flask Framework and other complementary modules for a single Task CRUD web app. (workshop)

## Flask Libraries

Please refer to the `requirements.txt` for the python dependencies, most of its implementations are placed on the `app` module `__init__.py` file

### Virtualenv

Simply: `virtualenv [your_env_name]`

### Config.py

This file separates ENV variables for each development phase (intended), it contains the `KEY` for the `CSRF`, `MAIL` credential setups, and also the MySQL DB string connections

### Singleton Pattern

Is a software pattern that restricts multiple object instances of a class. This project uses this pattern for integration support for external scripts or commands. Check the `Flask-Script` package for instructions

### MySQL Integration

This project works with a SQL database called `flask_tasks` it contains two tables, the `users` who handle login/register users and his relations 1-M with the `tasks` (title and description) with the `user_id` relation on it

Check the `models.py`, the field structure of every one

Actually works with DB migrations, you can extend the structure filling the model structure and run the migration command placed on the `manage.py` file, like this:

  `python manage.py db migrate` and after `python manage.py db upgrade`

### Frontend

Is not quite the best approach, but it uses the `Flask-Bootstrap4` package

### Run project

`python manage.py runserver`

## Credits

  - [David Lares](https://twitter.com/davidlares3)

## Licence

  - [MIT](https://opensource.org/licenses/MIT)
