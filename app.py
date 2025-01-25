from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
  return "Hello, Harshit"

if __name__ == "__main__":
  print("I'm inside the if block")
  app.run(host='0.0.0.0', port=8080, debug=True)