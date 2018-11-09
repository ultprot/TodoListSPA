# todo-list

> A Vue.js project
> With Flask
## Build Setup

``` bash
# in vue directory
cd client

# build for production with minification
npm run build

#in python dir
cd ..

#python envinronment setting
virtualenv venv
source venv/bin/activate

#install packages
pip3 install -r requirements.txt

#runserver
python3 main.py
```
##  DB setting  
create user 'todoer'at mariadb  
execute mysql.init  
set DB's password in mysql.json  

## Sample
[Example](http://13.124.223.114:26530)
