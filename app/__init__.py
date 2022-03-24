from flask import Flask

app = Flask(__name__)
app.secret_key= 'lasdkslk1213'

from app.controllers import default
