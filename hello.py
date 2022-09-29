from datetime import datetime
from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?')
    email= EmailField('What is your UofT Email address?', validators=[Email()])
    submit = SubmitField('Submit')
    
csrf=CSRFProtect()
csrf.exempt(NameForm)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html',
                           current_time=datetime.utcnow(), form=NameForm())

if __name__ == '__main__':
    manager.run()
