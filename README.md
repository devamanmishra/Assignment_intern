# **EzyMetrics Backend Project**

## Overview

This project is a **backend API service** for EzyMetrics, built using **Flask** and **MongoDB**. It focuses on **data integration** with dummy CRM and marketing platforms, **data storage**, **report generation** (in PDF and CSV), and sending **email alerts** when specific conditions are met.

### **Features:**
1. **API Service Development** for integrating with dummy CRM and Marketing platforms.
2. **Data Storage** in MongoDB and performing ETL (Extract, Transform, Load) operations.
3. **Dynamic Report Generation** in PDF and CSV formats.
4. **Email Alerts** triggered by specified conditions.
5. Easy deployment and integration using **Flask**.

## **Tech Stack**
- **Python** (v3.9 or higher)
- **Flask** (Web framework)
- **MongoDB** (NoSQL database)
- **Flask-Mail** (For email alerts)
- **pdfkit** (For PDF generation)
- **pandas** (For CSV generation)


## **Prerequisites**

1. **Python 3.9+**: Make sure you have Python installed on your system.
2. **MongoDB**: Ensure you have MongoDB installed locally or use **MongoDB Atlas** (cloud version). recommended - (MongoDB Atlas)
3. **wkhtmltopdf**: Required for generating PDF reports.
4. **Flask-Mail**: You will need an SMTP server to send email alerts. For Gmail, ensure you have an **app-specific password** if 2-factor authentication is enabled.


## **Installation**

1. **Clone the repository**:
   git clone https://github.com/devamanmishra/Assignment_intern.git

2. **Create a virtual environment** (optional but recommended):
3. **Install dependencies**:
   Install the necessary Python packages using `requirements.txt`.
  
   **pip install -r requirements.txt**

4. **Configure Flask-Mail**:
   Update the **SMTP server** settings in `app.py` for sending email alerts.

   Example for Gmail:
   
   - app.config['MAIL_SERVER'] = 'smtp.gmail.com'
   - app.config['MAIL_PORT'] = 587
   - app.config['MAIL_USE_TLS'] = True
   - app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
   - app.config['MAIL_PASSWORD'] = 'your-app-password'  # Use an app-specific password
   - app.config['MAIL_DEFAULT_SENDER'] = 'yourmail@gmail.com'

6. **Setup MongoDB**:
   Ensure that MongoDB is running locally or connect to MongoDB Atlas by updating the MongoDB connection string in `app.py` if needed:
   

## **API Endpoints**

### **1. Fetch Data**
- **Endpoint**: `/fetch-data`
- **Method**: `GET`
- **Description**: Simulates fetching data from dummy CRM and Marketing platforms, and stores it in MongoDB.
- **Response**:
  {
    "message": "Data fetched and stored successfully!"
  }
 
### **2. Transform Data**
- **Endpoint**: '/transform-data'
- **Method**: 'POST'
- **Description**: Performs ETL operations, transforming raw data into meaningful metrics (e.g., lead conversion rates).
- **Response**:
  {
    "total_leads": 200,
    "converted_leads": 50,
    "conversion_rate": 25.0
  }
  
### **3. Generate CSV Report**
- **Endpoint**: `/report/csv`
- **Method**: `GET`
- **Description**: Generates a CSV report from the CRM data stored in MongoDB.
- **Response**: Returns a CSV file.

### **4. Generate PDF Report**
- **Endpoint**: `/report/pdf`
- **Method**: `GET`
- **Description**: Generates a PDF report from the CRM data stored in MongoDB.
- **Response**: Returns a PDF file.

### **5. Send Email Alert**
- **Endpoint**: `/send-alert`
- **Method**: `POST`
- **Description**: Sends an email alert if a certain condition is met.
- **Request Body**:
  {
    "condition": "true",
    "recipient": "recipient@example.com"
  }
- **Response**:

  {
    "message": "Alert sent to recipient@example.com!"
  }


## **How to Run**
if  you are using the Virtual env then First Activate the Virtual env

1. **Run the Flask App**:
   Start the Flask development server:

   python app.py

2. **Access the API**:
   The Flask app will run at `http://127.0.0.1:5000/`.

3. **Use Postman** to test the endpoints.
