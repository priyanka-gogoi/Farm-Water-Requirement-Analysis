from flask import Flask, render_template, request

import predictor

app = Flask(__name__)

@app.route('/')
def home_page():
  return render_template("index.html")

@app.route('/results', methods = ['POST'])
def results():
  input_values = [x for x in request.form.values()]
  input_values.pop(-1)
  inputs = list(map(float, input_values))
  pred_res = predictor.predict_wr([inputs])
  
  return render_template("index.html", results = "Water Required by the Crop:- {:0.3f} mm/day". format(pred_res[0]))

if __name__ == "__main__":
  app.run()