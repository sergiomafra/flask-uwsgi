from flask import Flask

app = Flask(__name__)

## Hello World
@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'

## Creating another unique route
@app.route('/information')
def info():
    return '<h1>Puppies are cute!</h1>'

## Example of dynamic route
@app.route('/puppy/<name>')
def puppy(name):
    return f'<h1>This is a page for {name.upper()}</h1>'

if __name__ == '__main__':
    app.run()
