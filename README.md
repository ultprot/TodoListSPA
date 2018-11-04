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
