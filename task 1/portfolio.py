from flask import Flask,render_template, url_for, redirect, request

app=Flask(__name__, static_url_path='/static')

@app.route('/')
def HOME():
    return render_template("HOME.html")


if(__name__=='__main__'):
    app.run(debug=True)
