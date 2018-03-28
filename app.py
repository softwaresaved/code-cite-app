"""
Simple flask app
"""
import os
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
app = Flask(__name__)

class GetPapersQuery(FlaskForm):
    name = SelectField(
        'Select Query',
        choices = [('github', 'github'),('zenodo', 'zenodo')],
        validators=[DataRequired()])

# Set the app secret key to prevent CSRF

app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def root():
    """
    Root page of site
    """
    form = GetPapersQuery()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

