from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load('model.h5')



def extract_client_from_request(req_data):
    client = []
    client.append(req_data['Processor'])
    client.append(req_data['Screen_Size_inch'])
    client.append(req_data['RAM_GB'])
    client.append(req_data['Graphics_Card'])
    client.append(req_data['SSD_GB'])
    client.append(req_data['HDD_GB'])
    client.append(req_data['OS'])
    client.append(req_data['Normal'])
    
    return client

@app.route('/test')
def test():
    print("Test")
    return "test"


@app.route('/hi', methods=['GET', 'POST'])
def hi():
    extract_client_from_request = []
    extract_client_from_request.append(request.args['Processor'])
    extract_client_from_request.append(request.args['Screen_Size_inch'])
    extract_client_from_request.append(request.args['RAM_GB'])
    extract_client_from_request.append(request.args['Graphics_Card'])
    extract_client_from_request.append(request.args['SSD_GB'])
    extract_client_from_request.append(request.args['HDD_GB'])
    extract_client_from_request.append(request.args['OS'])
    extract_client_from_request.append(request.args['Normal'])
    client = [extract_client_from_request]
    prediction = model.predict(client)[0]
    return jsonify({'price is': prediction})

@app.route('/predict', methods=['POST'])
def predict():
    client = [extract_client_from_request(request.json)]
    prediction = model.predict(client)[0]
    return jsonify({'price is': prediction})


if __name__ == '__main__':
    app.run(debug=True)
