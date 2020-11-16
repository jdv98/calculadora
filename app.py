from flask import Flask, render_template, jsonify, json
from config import DevelopmentConfig
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
from principal import receive

@app.errorhandler(404)
def page_not_found(e): #recibe como parametro el error
    return render_template('404.html'),404

@app.route('/ipv4-calc/<x1>')
@app.route('/ipv4-calc/<x1>/<x2>')
def prefix_to_mask(x1=None, x2=None):
    return jsonify(receive(x1,x2))		

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8999)
