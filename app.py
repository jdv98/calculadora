from flask import Flask, render_template, jsonify, json
from config import DevelopmentConfig
import ipAddress as ac
import subnetMask as sm
import difusion as df
import segmentos as nh
import  networkAddress as na
import flIP as fl
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.errorhandler(404)
def page_not_found(e): #recibe como parametro el error
    return render_template('404.html'),404

@app.route('/ipv4-calc/<x1>')
@app.route('/ipv4-calc/<x1>/<int:x2>')
@app.route('/ipv4-calc/<int:x2>')
def prefix_to_mask(x1=None, x2=None):
	data={}
	if x1:
		data['ipaddressclass']=ac.ipAddressClass(x1)
		data['defaultmask']=ac.ipAddressMask(x1)
		data['networkhost']=nh.networkHost(x1)
		data['firstdirecction']=fl.calcFirstIP(x1)
		data['lastdirecction']=fl.calcLastIP(x1)
		data['networkaddress']=na.networkAddress(x1)
	if x1 and x2:
		data['subnetworkdirection']=fl.calcRed(x1,x2)
		data['ipaddressdifusion']=fl.calcDifusion(x1,x2)
	if x2:
		data['prefixtomask']=sm.prefixToMask(x2)
	return jsonify(data)		

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8999)