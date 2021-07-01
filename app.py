from flask import Flask, render_template, request
import joblib
import numpy as np
app = Flask(__name__)

model = joblib.load('D:\Projects!\housing-price-prediction\my_model.pkl')

@app.route('/')
def student():
   return render_template('data.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      latitude = float(request.form.get('lat'))
      longitude = float(request.form.get('lon'))
      housing_age = float(request.form.get('age'))
      total_rooms = float(request.form.get('rooms'))
      total_bedrooms = float(request.form.get('bed'))
      population = float(request.form.get('pop'))
      households = float(request.form.get('holds'))
      income = float(request.form.get('inc'))
      ocean_proximity =  float(request.form.get('oceanp'))
      rph = total_rooms/households
      bpr = total_bedrooms/total_rooms
      pph = population/households
      a1 = [[longitude, latitude, housing_age, total_rooms, total_bedrooms, population, households, income, ocean_proximity, rph, bpr, pph]]
      prediction = int(model.predict(a1))
      prediction = "{:,}".format(prediction)
      return render_template('result.html', prediction = prediction)

if __name__ == '__main__':
   app.run(debug = True)
