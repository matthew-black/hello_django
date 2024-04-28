# Environment Set-Up:

## Create and Instantiate a Virtual Environment:

From [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

#### Create:

* `python3 -m venv .venv`
  * `-m venv` = use the `venv` module
  * `.venv` = the name of the virtual environment folder

### Instantiate:

* `source .venv/bin/activate`

#### Verify:

* `which python`
  * should output `/Users/..../.venv/bin/python`

#### Deactivate:

* `deactivate`

---

## Do Django Things:

From [here](https://docs.djangoproject.com/en/5.0/intro/tutorial01/).

#### Install:

* `pip install django`
  * installs django in `.vent/lib/python3.12/site-packages/`
* `pip freeze > requirements.txt`
  * creates a `requirements.txt` file in root dir

#### Instantiate Django Project:

* `django-admin startproject name_of_project`
  * creates:
    ```
    name_of_project/
      manage.py
      name_of_project/
          __init__.py
          settings.py
          urls.py
          asgi.py
          wsgi.py
    ```

#### Start the Server:

* `python manage.py runserver`
