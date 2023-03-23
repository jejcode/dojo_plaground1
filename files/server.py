from flask import Flask, render_template # render_template necessary for templates to work
app = Flask(__name__) # new instance of Flask

@app.route('/play/<int:num>/<string:color>')  # route that will load play.html
def play(num, color):
    #     ^ function arguments are passed from route line   v
    return render_template('play.html', num = num, color = color) 

if __name__ == '__main__':
    app.run(debug = True, port = 8000) # runs the app on port 8000