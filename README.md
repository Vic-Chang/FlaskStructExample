# Flask 網站結構範例
一個使用Python Flask建立的簡易站。


Flask 結構以功能導向為主(Functional base structure)，建立一個使用flask-bootstrap4 package建立的頁面，擁有基本的路由以及Web API。

並上傳至Heroku運行。([Flask Demo])

## 部分文件說明
* manage.py > 使用 flask_script package ，可以使用shell控制網站啟動、下commad執行fuction。
* procfile > Heroku 網站使用文件，建立heroku container "dynos"

***

# FlaskStructExample

This project show how to builing a flask website with functional base structure.

Website contain a index page with bootstrap4 (flask-bootstrap4 package) and a Web Api.

And this project will publish to Heroku service.([Flask Demo])

## Some notes
* manage.py > Use package `flask_script`. You can use shell to run the web and use command to execute some fuction. 
* procfile > This is a required file for Heroku, use for build the Heroku's container "dynos".

[Flask Demo]: https://my-first-python-flask.herokuapp.com/
