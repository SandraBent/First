from flask import Flask, render_template
from google.cloud import datastore
import os
app = Flask(__name__)

client = datastore.Client()
user_col        = ['Name', 'Password']
def google_get(entity, col):
    print("entity:" + entity)
    print("col:   " + str(col))
    result = client.query(kind=entity)
    return database_dict(col, result.fetch())
def database_dict(col, result):
	print("database_dict")
	output = []
	for entity in result:
		print(str(entity))
		test = {}
		for y in col:
			test[y] = entity[y]
		output.append(test)
		
	return output

@app.route('/')
def index():
	data=google_get("Users", user_col)
	print(data)
	return render_template("index.html")

@app.route('/sandy')
def sandy_page():
	return 'Hi Sandy!'

if __name__ == '__main__':
	server_port = os.environ.get('PORT', '8080')
	app.run(debug=False, port=server_port, host='0.0.0.0')	
