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

@app.route('/list')
def getList():
	print("list")
	return app.send_static_file('index.html')

@app.route('/item',methods=['POST'])
def postItem():
	if request.method=='POST':
		print("item posted")
	return app.send_static_file('index.html')

@app.route('/item/<int:id>',methods=['PUT'])
def updateItem():
	if request.methods=='POST':
		print("item "+id+" updated")
	return app.send_static_file('index.html')

@app.route('/item/<int:id>',methods=['DELETE'])
def deleteItem():
	if request.methods=='DELETE':
		print("item "+id+" deleted")
	return app.send_static_file('index.html')

@app.route('/item/<int:id>/priority',methods=['PUT'])
def updatePriority():
	if request.methods=='PUT':
		print("item "+id+" priority updated")
	return app.send_static_file('index.html')

@app.route('/item/<int:id>/done',methods=['PUT'])
def updateDone():
	if request.methods=='PUT':
		print("item"+id+" done updated")
	return app.send_static_file('index.html')


if __name__=='__main__':
    app.run(host='0.0.0.0',port=26530)
