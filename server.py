from flask import Flask
from flask import jsonify
from flask import request
from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def mlprediction():

   # data = request.get_json(force=True)
   # state = data['state']
   # district = data['district']
   
   state = request.form['name']
   district = request.form['email']
   response= requests.get("https://api.covid19india.org/state_district_wise.json")
   responsedata = response.json()
   # state = request.form['state']
   # district = request.form['district']

   

   # data = request.get_json(force=True)
   # state = data['state']
   # district = data['district']
  
   mysinput=state
   stateinput = " ".join([
      word.capitalize()
      for word in mysinput.split(" ")
   ])

   if stateinput in responsedata:
      statewise=responsedata[stateinput]
      mydinput=district
      distinput = " ".join([
         word.capitalize()
         for word in mydinput.split(" ")
      ])
      if distinput in statewise['districtData']:
         district=statewise['districtData'][distinput]
         return jsonify({'totalcases':district['confirmed'],
                        "active":district['active'],
                        "recovered":district['recovered'],
                        "death":district['deceased']})
      else:
         return jsonify()

   else:
       return jsonify()

if __name__ == '__main__':
    app.run(port=5002)
    app.debug = True
