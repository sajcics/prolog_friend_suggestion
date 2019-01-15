#to run file call: export FLASK_APP=hello.py
#flask run
from flask import Flask, render_template
from prolog.index import callProlog

import sys
import logging

# every python has attribute __name__ which is set to '__main__' when
# module run as main program (run in terminal e.g. python hello.py)
# flask constructor takes the name of current module from static variable __name__
app = Flask(__name__)

# fortmat logging data and availability to call logger outside main class
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(name)s - %(message)s'))
app.logger.addHandler(handler)

# that will run when we run python program from
# here we exeminate if script is being run directly
# or being imported by something else
if __name__ == "__main__":
    # run web aplication server
    app.run(debug=True)

# app.route is decorator to function that represents URL that is binded to function
@app.route('/')
def hello_world(name=None):
    app.logger.error("executing path /")
    callProlog()
    return render_template('index.html', name="anica")

#@app.route('/<username>')
#def username_profile(username):
#    return render_template('index.html', name=username)


#def prikazi_prijatelje(name):
#    return x.query('prijatelj('+name+', X)')*/
