from flask import Flask, jsonify, request, send_file
from pymongo import MongoClient
from etl.data_transform import transform_data
from services.crm_services import get_crm_data
from services.marketing_services import get_marketing_data
import pdfkit
import pandas as pd
from flask_mail import Mail, Message
import os

app = Flask(__name__)


client = MongoClient('mongodb://localhost:27017/') ## if you are using mongodb atlas add your connection string
db = client['ezyMetricsDB']


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'yourmail@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'yourmail@gmail.com'

mail = Mail(app)

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    crm_data = get_crm_data()
    marketing_data = get_marketing_data()
    
    
    db.crm.insert_many(crm_data)
    db.marketing.insert_many(marketing_data)
    
    return jsonify({"message": "Data fetched and stored successfully!"}), 200


@app.route('/transform-data', methods=['POST'])
def transform_data_endpoint():
    result = transform_data()
    return jsonify(result), 200

@app.route('/report/csv', methods=['GET'])
def generate_csv_report():
    
    data = list(db.crm.find({}))
    df = pd.DataFrame(data)
    
    
    csv_path = 'reports/report.csv'
    df.to_csv(csv_path, index=False)
    
    return send_file(csv_path, as_attachment=True)

@app.route('/report/pdf', methods=['GET'])
def generate_pdf_report():
    
    data = list(db.crm.find({}))
    df = pd.DataFrame(data)
    
    
    html = df.to_html()
    pdf_path = 'reports/report.pdf'
    pdfkit.from_string(html, pdf_path)
    
    return send_file(pdf_path, as_attachment=True)

@app.route('/send-alert', methods=['POST'])
def send_alert():
    data = request.get_json() 
    condition = data.get('condition')  
    recipient = data.get('recipient')  
    
    if not recipient:
        return jsonify({"error": "Recipient email is required"}), 400

    if condition == 'true':  
        msg = Message("Alert!", recipients=[recipient])  
        msg.body = "The condition has been met."
        mail.send(msg)
        return jsonify({"message": f"Alert sent to {recipient}!"}), 200
    return jsonify({"message": "Condition not met, no alert sent."}), 200


if __name__ == '__main__':
    if not os.path.exists('reports'):
        os.makedirs('reports')
    app.run(debug=True)
