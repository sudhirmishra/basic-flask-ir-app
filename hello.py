from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():

	return render_template('index.html')

@app.route('/rating',methods=['GET','POST'])
def hello_world():
	movies = {}
	if request.method == "POST":
		message = "Processed Data!"
		
		for item in request.form:
			if item == "singlebutton":
				continue
			movies[item] = request.form[item]

			"""
			Structure
			
			movies = { "movie-name-1":"rating" }
			"""
		for key, value in movies.items():
			print("Movie name: "+key+" rated "+value)

		# To see the above print statements, look at linux bash/shell/command prompt

		return message

	else:

		movies = [["A B"],["B"],["C"],["D"],["E"]]

		return render_template('hello.html', movies=movies)
	
@app.route('/tagging',methods=['GET','POST'])
def tagging():

	movies = {}
	if request.method == "POST":
		message = "Processed Data!"
		
		for item in request.form:
			if item == "singlebutton":
				continue
			movies[item] = request.form[item].split(',')

		"""
		Structure
		
		movies = { "movie-name-1":["tag-1","tag-2"] }
		"""

		for key,value in movies.items():
			print("Movie name "+key+" tags "+ "|".join(value))

		# To see the above print statements, look at linux bash/shell/command prompt

		print(movies)

		return message

	else:

		movies = [["A B"],["B"],["C"],["D"],["E"]]
		return render_template('tagging.html', movies=movies)
	
