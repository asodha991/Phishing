from flask import Flask, render_template, url_for, flash, redirect
from forms import AcceptURL
from features_for_new_data import predict

app = Flask(__name__)

app.config['SECRET_KEY'] = '612202c1ba464e2083b8287e8a1f5554'

@app.route("/", methods = ['GET', 'POST'])
@app.route("/home", methods = ['GET', 'POST'])
def home():
	form = AcceptURL()

	if form.validate_on_submit():
		u = form.url.data
		p = predict(u)
		p = int(p[0])
		if p == 1:
			p = "Legitimate Website"
			flash(f'Predicted Status: {p}', 'success')
		else:
			p = "Phishing Website"
			flash(f'Predicted Status: {p}', 'danger')
		
		
		return redirect(url_for('home'))
	return render_template("home.html", form = form)

# @app.route("/statistics")
# def stats():
# 	return render_template("stats.html")

if __name__ == "__main__":
	app.run(debug = True)