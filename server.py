from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"


@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_hello(name):
    print(name)
    return "Hello," + name

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num,name):
    output = ''

    for i in range(0,num):
        output += f"<h1>{name}</h1>"
    
    return output

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Page Not Found</h1>"









if __name__=="__main__":
    app.run(debug=True)