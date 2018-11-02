# -*- coding: utf-8 -*-

from flask import Flask
import os
class VueFlask(Flask):
	jinja_options=Flask.jinja_options.copy()
	jinja_options.update(dict(
	    block_start_string='{%',
		block_end_string='%}',
		variable_start_string='((',
		variable_end_string='))',
		comment_start_string='{#',
		comment_end_string='#}'
	))

ROOT_PATH=os.path.dirname(os.path.abspath(__file__))
STATIC_PATH=os.path.join(ROOT_PATH,'client/dist')

app=VueFlask(__name__,static_folder=STATIC_PATH,static_url_path='')

@app.route('/')
def index():
	return app.send_static_file('index.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=26530)
