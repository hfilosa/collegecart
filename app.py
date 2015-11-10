from flask import Flask, render_template, request, session, redirect
import utils.py

app=Flask(__name__)

@app.route('/')
def home():
    """
    our only route, it loads a page full of stuff
    """
    return render_template('base.html', s=session)

if __name__=="__main__":
    app.debug = True
    app.run('0.0.0.0', port=8000)
