from flask import Flask, jsonify, request, render_template, redirect, url_for ,request
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "razi"
password = "123"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Ali"]



@app.route('/', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		name=request.form["username"]
		ps =request.form["password"]
		print("Post")
		if name==username and ps == password :
			return redirect(url_for('home'))
		else:
			return render_template('login.html')
	return render_template('login.html')


@app.route("/home")
def home():
	return render_template("home.html", fc=facebook_friends)



@app.route("/friend_exist/<string:name>")
def friend_exist(name):
	s=False
	for x in facebook_friends :
		if x == name:
			s=True
	print(s)
	print(name)
	return render_template("friend_exists.html" ,n = name ,send = s)






if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
