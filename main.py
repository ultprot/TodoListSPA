# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import jsonify
from flask import json
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
		print(request)
		print(request.json)
		json_data={
			'id':global_id,
			'subject':request.json['subject'],
			'content':request.json['content'],
			'priority':request.json['priority'],
			'expiration':request.json['expiration']
		}
		print(json_data)
		response=app.response_class(
			response=json.dumps(json_data),
			status=200,
			mimetype='application/json; charset=utf-8'
		)
		global_id+=1
		print(response)
		return response

@app.route('/item/<int:id>',methods=['PUT'])
def updateItem(id):
	if request.method=='PUT':
		print("item "+str(id)+" updated")
		print(request)
		print(request.json)
	return app.send_static_file('index.html')

@app.route('/item/<int:id>',methods=['DELETE'])
def deleteItem(id):
	if request.method=='DELETE':
		print("item "+str(id)+" deleted")
		print(request)
		json_data={
			'id':id,
		}
		response=app.response_class(
			response=json.dumps(json_data),
			status=200,
			mimetype='application/json; charset=utf-8'
		)
	return response

@app.route('/item/<int:id>/priority',methods=['PUT'])
def updatePriority(id):
	if request.method=='PUT':
		print("item "+str(id)+" priority updated")
		print(request)
	return app.send_static_file('index.html')

@app.route('/item/<int:id>/done',methods=['PUT'])
def updateDone(id):
	if request.method=='PUT':
		print("item"+str(id)+" done updated")
		print(request)
	return app.send_static_file('index.html')


if __name__=='__main__':
	app.run(host='0.0.0.0',port=26530)
