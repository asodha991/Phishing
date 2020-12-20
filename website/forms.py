from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL


class AcceptURL(FlaskForm):

	url = StringField('Enter the URL', validators = [URL(require_tld=True, message="Enter valid URL")])

	submit = SubmitField('Check Status')