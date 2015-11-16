from flask import Flask, render_template, request, redirect
import utils

app=Flask(__name__)

@app.route('/')
def home():
    """
    our only route, it loads a page full of stuff
    """
    colleg={}
    basket={}
    college=utils.get_random_college()
    basket=utils.get_basket(college['cost'])
    s={}
    c={}
    return render_template('base.html',c=college,s=basket)

if __name__=="__main__":
    app.debug = True
    app.run('0.0.0.0', port=8000)
