from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
	movies = {}
	if request.method == "POST":
		message = "Processed Data!"
		
		for item in request.form:
			if item == "singlebutton":
				continue
			movies[item] = request.form[item]

		print(movies)

		return message

	else:

		movies = [["A B"],["B"],["C"],["D"],["E"]]

		return render_template('hello.html', movies=movies)
	



