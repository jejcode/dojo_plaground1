from flask import Flask, render_template # render_template necessary for templates to work
app = Flask(__name__) # new instance of Flask

@app.route('/play')  # route that will load play.html
def play(num = 3, color = "rgb(144,192,243)"):
    #     ^ function arguments are passed from route line   v
    return render_template('play.html', num = num, color = color) 

@app.route('/play/<int:num>')  # route that will load play.html
def play_num(num, color = "rgb(144,192,243)"):
    #     ^ function arguments are passed from route line   v
    return render_template('play.html', num = num, color=color) 

@app.route('/play/<int:num>/<string:color>')  # route that will load play.html
def play_num_color(num, color):
    #     ^ function arguments are passed from route line   v
    return render_template('play.html', num = num, color = color) 

if __name__ == '__main__':
    app.run(debug = True, port = 8000) # runs the app on port 8000