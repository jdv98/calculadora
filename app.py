from flask import Flask, render_template, jsonify, json
from config import DevelopmentConfig
import ipAddress as ac
import subnetMask as sm
import difusion as df
import segmentos as nh
import  networkAddress as na
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.errorhandler(404)
def page_not_found(e): #recibe como parametro el error
    return render_template('404.html'),404

@app.route('/ip-address-class/<x1>')
def ip_address_class(x1=None):
	if x1:
		data = {'ipaddressclass':ac.ipAddress(x1)}
		response = app.response_class(
			response=json.dumps(data),
			status=200,
			mimetype='application/json'
		)
		return response
	
@app.route('/subnet-mask/<x1>')
@app.route('/subnet-mask/<int:x2>')
def prefix_to_mask(x1=None, x2=None):
	if x1:
		return jsonify({'masktoprefix':sm.maskToPrefix(x1)})
	if x2:
		return jsonify({'prefixtomask':sm.prefixToMask(x2)})

@app.route('/difusion/<x1>')
def ip_difusion(x1=None):
	if x1:
		return jsonify({'ipaddressdifusion':df.difusionIp(x1)})

@app.route('/network-host/<x1>')
def network_host(x1=None):
	if x1:
		return jsonify({'networkhost':nh.networkHost(x1)})		

@app.route('/network-address/<x1>')
def network_address(x1=None):
	if x1:
		return jsonify({'networkaddress':na.networkAddress(x1)})		


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8999)