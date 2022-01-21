import flask 

app = flask.Flask(__name__)

@app.route('/')
def index():
   return flask.render_template("index.html")

@app.route('/callback', methods=['POST'])
def callback():    
   return 'Hello Python'


if __name__ == '__main__':
   app.run()
   
   