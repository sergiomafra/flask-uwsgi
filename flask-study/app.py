from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

## Hello World
@app.route('/')
def index():
    return ('<h1>Hello Puppy!</h1><br /><h2>Move to /puppy-latin/<name> to see '
            'your name in latin</h2>')

## Creating another unique route
@app.route('/information')
def info():
    return '<h1>Puppies are cute!</h1>'

## Example of dynamic route
@app.route('/puppy/<name>')
def puppy(name):
    return f'<h1>This is a page for {name.upper()}</h1>'

## Example of DEBUG - Return 100th letter of the name
@app.route('/100/<name>')
def r100(__name__):
    return f'<h1>This is the 100th letter: {name[100]}</h1>'

## Exercise 01 - Puppy Latin
@app.route('/puppy-latin/<name>')
def puppy_latin(name):
    if name[-1] != 'y':
        return f'<h1>Your latin puppy name is {name}y.</h1>'
    else:
        return f'<h1>Your latin puppy name is {name[:-1]}iful.</h1>'

## Template to static file
@app.route('/welcome_static')
def welcome_static():
    return render_template('basic.html')

if __name__ == '__main__':
    app.run()
