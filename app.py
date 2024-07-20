from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    ip_address = request.form['ip_address']
    api_key = 'at_9A9QkgxTt7mBU2UgbgwqZ0pCCd72v'
    url = f'https://geo.ipify.org/api/v2/country,city,vpn?apiKey={api_key}&ipAddress={ip_address}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        data = {}
    return render_template('resultado.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
