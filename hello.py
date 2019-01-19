#to run file call: export FLASK_APP=hello.py
#flask run
from flask import Flask, render_template, request
from prolog.index import getMyFriends, getMySuggestions, addNewFriend

import sys
import logging

# every python has attribute __name__ which is set to '__main__' when
# module run as main program (run in terminal e.g. python hello.py)
# flask constructor takes the name of current module from static variable __name__
app = Flask(__name__)
default_user = 'martina'

# that will run when we run python program from
# here we exeminate if script is being run directly
# or being imported by something else
if __name__ == "__main__":
    logging.basicConfig(filename=__name__, level=logging.DEBUG)
    logging.info('Application started')

    # run web aplication server
    app.run(debug=True)

# app.route is decorator to function that represents URL that is binded to function
@app.route('/')
def hello_world():
    myfriends = getMyFriends(default_user)
    suggestions = getMySuggestions(default_user)

    newSuggestions = removeFriendsFromSuggestions(myfriends, suggestions, default_user)

    return render_template('index.html', name=default_user, users=myfriends, suggestions=newSuggestions)

@app.route('/<user>')
def username_profile(user):
    user = "\'%s\'" % user

    myfriends = getMyFriends(user)
    suggestions = getMySuggestions(user)

    newSuggestions = removeFriendsFromSuggestions(myfriends, suggestions, user)

    return render_template('index.html', name=user, users=myfriends, suggestions=newSuggestions)

@app.route('/add/new-user', methods=['POST'])
def add_friend():
    result = request.form.to_dict()
    
    if len(result.keys()) > 0:
        user = result.keys()[0]
        friend = result[user]

    addNewFriend(user, friend)
    myfriends = getMyFriends(default_user)
    suggestions = getMySuggestions(default_user)

    newSuggestions = removeFriendsFromSuggestions

    return render_template('index.html', name=user, users=myfriends, suggestions=newSuggestions)


def removeFriendsFromSuggestions(myfriends, suggestions, username) :
    newSuggestions = []
    
    for user in suggestions:
        if user not in myfriends and user != username:
            newSuggestions.append(user)
            
    return newSuggestions
