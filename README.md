# Django App #1

Following this:

* https://docs.djangoproject.com/en/5.0/intro/tutorial01/

---

## My First Route:

![polls index view](./readme_images/polls_index_view.png)

## Interact with the SQLite3 Database:

```
sqlite3
```

```
SQLite version 3.43.2 2023-10-10 13:08:14
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> .open db.sqlite3
sqlite> .tables
```

Now you see whatever tables exist. Quick way to see the migrations:

```
SELECT * FROM django_migrations;
```

## Where You Left Off:

* https://docs.djangoproject.com/en/5.0/intro/tutorial02/#:~:text=in%20INSTALLED_APPS.-,Creating%20models,-%C2%B6
