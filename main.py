# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import jsonify
from flask import json
import pymysql
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
with open('./mysql.json') as credential:
	cred=json.load(credential)



def connection():
	return pymysql.connect(
	host='localhost',
	user='todoer',
	password=cred['password'],
	charset='utf8mb4',
	db='todolist',
	cursorclass=pymysql.cursors.DictCursor
	)

def dataList():
	conn=connection()
	try:
		with conn.cursor() as cursor:
			sql='select * from todo;'
			cursor.execute(sql)
			recs=cursor.fetchall()
	finally:
		conn.close()
	return recs

def toMysqlDateTime(datetime):
	splited=datetime.split('T')
	converted=splited[0]+' '+splited[1]
	return converted
def dataPost(subject,content,priority,expiration):
	conn=connection()
	if not(str(type(expiration))=='<class \'NoneType\'>'):
		expiration=toMysqlDateTime(expiration)
	try:
		with conn.cursor() as cursor:
			if str(type(priority))=='None':
				if str(type(expiration))=='<class \'NoneType\'>':
					sql='insert into todo(subject, content) values(%s,%s);'
					cursor.execute(sql,(subject,content))
					conn.commit()
					print('다 없다')
				else:
					sql='insert into todo(subject, content, expiration) values(%s,%s,%s);'
					cursor.execute(sql,(subject,content,expiration))
					conn.commit()
					print('p없다')
			else:
				if str(type(expiration))=='<class \'NoneType\'>':
					sql='insert into todo(subject, content, priority) values(%s,%s,%s);'
					cursor.execute(sql,(subject,content,priority))
					conn.commit()
					print('e 없다')
				else:
					sql='insert into todo(subject, content, priority, expiration) values(%s,%s,%s,%s);'
					cursor.execute(sql,(subject,content,priority,expiration))
					conn.commit()
					result=cursor.fetchall()
					print(result)
					print('다 있다')
			sql='select last_insert_id()'
			cursor.execute(sql)
			id=cursor.fetchone()
	finally:
		conn.close()
	id=id['last_insert_id()']
	return id
def dataUdate(id,subject,content,priority,expiration):
	conn=connection()
	if not(str(type(expiration))=='<class \'NoneType\'>'):
		expiration=toMysqlDateTime(expiration)
	try:
		with conn.cursor() as cursor:
			if str(type(priority))=='None':
				if str(type(expiration))=='<class \'NoneType\'>':
					sql='update todo set subject=%s, content=%s where id=%s;'
					cursor.execute(sql,(subject,content,id))
					conn.commit()
					print('다 없다')
				else:
					sql='update todo set subject=%s, content=%s, expiration=%s where id=%s;'
					cursor.execute(sql,(subject,content,expiration,id))
					conn.commit()
					print('p없다')
			else:
				if str(type(expiration))=='<class \'NoneType\'>':
					sql='update todo set subject=%s, content=%s, priority=%s where id=%s;'
					cursor.execute(sql,(subject,content,priority,id))
					conn.commit()
					print('e 없다')
				else:
					sql='update todo set subject=%s, content=%s, priority=%s expiration=%s where id=%s;'
					cursor.execute(sql,(subject,content,priority,expiration,id))
					conn.commit()
	finally:
		conn.close()
	return
def dataDelete(id):
	conn=connection()
	try:
		with conn.cursor() as cursor:
			sql='delete from todo where id=%s;'
			cursor.execute(sql,(id))
			conn.commit()
	finally:
		conn.close()
	return
def dataToggle(id,done):
	conn=connection()
	try:
		with conn.cursor() as cursor:
			sql='update todo set done=%s where id=%s;'
			cursor.execute(sql,(done,id))
			conn.commit()
	finally:
		conn.close()
	return
@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/list')
def getList():
	data=dataList()
	if isinstance(data,list):
		data.reverse()
	else:
		data=[]
	response=app.response_class(
		response=json.dumps(data),
		status=200,
		mimetype='application/json; charset=utf-8'
	)	
	return response

@app.route('/item',methods=['POST'])
def postItem():
	if request.method=='POST':
		print("item posted")
		print(request)
		print(request.json)
		id=dataPost(request.json['subject'],request.json['content'],request.json['priority'],request.json['expiration'])
		json_data={
			'id':id,
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
		print(response)
		return response

@app.route('/item/<int:id>',methods=['PUT'])
def updateItem(id):
	if request.method=='PUT':
		data=request.json
		dataUdate(id,data['subject'],data['content'],data['priority'],data['expiration'])
		json_data={
			'id':id,
		}
		response=app.response_class(
			response=json.dumps(json_data),
			status=200,
			mimetype='application/json; charset=utf-8'
		)
	return response

@app.route('/item/<int:id>',methods=['DELETE'])
def deleteItem(id):
	if request.method=='DELETE':
		dataDelete(id)
		json_data={
			'id':id,
		}
		response=app.response_class(
			response=json.dumps(json_data),
			status=200,
			mimetype='application/json; charset=utf-8'
		)
	return response

@app.route('/item/<int:id>/done',methods=['PUT'])
def updateDone(id):
	if request.method=='PUT':
		dataToggle(id,request.json['done'])
		json_data={
			'id':id,
		}
		response=app.response_class(
			response=json.dumps(json_data),
			status=200,
			mimetype='application/json; charset=utf-8'
		)
	return response


if __name__=='__main__':
	app.run(host='0.0.0.0',port=26530)
