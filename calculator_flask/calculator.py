from flask import Flask, render_template, request
import numpy as np

Flask_App = Flask(__name__)

@Flask_App.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@Flask_App.route('/operation_result/', methods=['POST'])
def operation_result():
	sm_input = request.form['soilmoisture']
	soil_type = request.form['soiltype']

	try:
		soilmoisture = float(sm_input)

		if soil_type == 'SW' or soil_type == 'SP':
			rci = np.exp(3.987 + (.815 * np.log(soilmoisture)))
		elif soil_type == 'SM' or soil_type == 'SC' or soil_type == 'SM-SC':
			rci = np.exp(12.542 - (2.955 * np.log(soilmoisture)))
		elif soil_type == 'CL':
			rci = np.exp(15.506 - (3.530 * np.log(soilmoisture)))
		elif soil_type == 'ML':
			rci = np.exp(11.936 - (2.407 * np.log(soilmoisture)))
		elif soil_type == 'CL-ML':
			rci = np.exp(14.236 - (3.137 * np.log(soilmoisture)))
		elif soil_type == 'CH':
			rci = np.exp(13.686 - (2.705 * np.log(soilmoisture)))
		elif soil_type == 'MH':
			rci = np.exp(23.641 - (5.191 * np.log(soilmoisture)))
		elif soil_type == 'OL':
			rci = np.exp(17.399 - (3.584 * np.log(soilmoisture)))
		elif soil_type == 'OH':
			rci = np.exp(12.189 - (1.942 * np.log(soilmoisture)))

	
		return render_template(
			'index.html',
			soiltype=soil_type,
			soilmoisture=soilmoisture,
			result=int(rci),
			calculation_success=True
		)

	except NoSMorST:
		return render_template(
			'index.html',
			soiltype=soil_type,
			soilmoisture=soilmoisture,
			result="Error",
			calculation_success=True,
			error="Input Soil Type or Soil Moisture"
		)


if __name__ == '__main__':
	Flask_App.debug = True
	Flask_App.run()

