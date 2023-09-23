![logo](https://telegra.ph/file/ca3d4122c2b981b5df2e8.png)

# szThings 
is a personal web task manager that helps you plan your day, manage projects and make real progress towards your goals.

![python-version](https://img.shields.io/badge/python-3.9-blue.svg)

## Run
```shell
git clone https://github.com/szerel/szThings
```
```shell
pip install - r requirements.txt
```
```shell
python3 manage.py runserver
```
```shell
python3 manage.py showmigrations
```
```shell
python3 manage.py migrate
```
```shell
python3 manage.py makemigrations main
```
```shell
python3 manage.py migrate
```
```shell
python3 manage.py createsuperuser
```

```
Go to the administration page and log in
http://127.0.0.1:8000/adminszereladmin/

Go to AUTHENTICATION AND AUTHORIZATION > Groups > add Group 
            name group = "view_add_task"
            permissions = all "main" 
            save

Go to http://127.0.0.1:8000/profile/
            name project = "Inbox"
            add

```
## Screenshots
### Start Page
![menu](https://telegra.ph/file/ae304f15c062b2205ebf3.png)
### Web tasks
![task1](https://telegra.ph/file/04ddaf7b4288550c704d0.png)


## Disclaimer
This code, is riddled with humor and satire. Please don't take it too seriously or take it personally. After all, programming is an art that allows us to express ourselves, even if it's in a funny and ironic way. Use code with a smile on your face, and remember that true programming prowess also includes the ability to handle the nuances of life with ease and good humor. Happy coding!