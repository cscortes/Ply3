from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'



@app.route('/callback/', methods=['POST'])
def callback():
    
   return 'Hello Python'


if __name__ == '__main__':
   app.run()
   
   