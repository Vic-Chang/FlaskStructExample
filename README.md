# Flask 網站結構範例
一個使用Python Flask建立的簡易站。


Flask 結構以功能導向為主(Functional base structure)，建立一個使用flask-bootstrap4 package建立的頁面，擁有基本的路由以及Web API。

並上傳至Heroku運行。([Flask Demo])

## 部分文件說明
* manage.py > 使用 flask_script package ，可以使用shell控制網站啟動、下commad執行fuction。
* procfile > Heroku 網站使用文件，建立heroku container "dynos"

## 其他說明
使用 `python manage.py runserver` 啟動伺服器。

或是可以使用 `python manage.py api reset` or `python manage.py test` 進行 command 管理。

***

# FlaskStructExample

This project show how to builing a flask website with functional base structure.

Website contain a index page with bootstrap4 (flask-bootstrap4 package) and a Web Api.

And this project will publish to Heroku service.([Flask Demo])

## Some notes
* manage.py > Use package `flask_script`. You can use shell to run the web and use command to execute some fuction. 
* procfile > This is a required file for Heroku, use for build the Heroku's container "dynos".

Use `python manage.py runserver` to run the server. 

And use shell command to adjust server like `python manage.py api reset` or `python manage.py test` (not implement yet)

[Flask Demo]: https://my-first-python-flask.herokuapp.com/
