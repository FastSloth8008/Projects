from flask import Flask, render_template, request
import joblib
import pandas as pd

# Initialize the Flask application
app = Flask(__name__, static_folder='static')

# Load the serialized XGBoost model outside the route handler
xgb_model = joblib.load('Backend/xgb_model.pkl')

# Define route for the index page
@app.route('/')
def index():
    return render_template('webpage2.html')

# Define route for handling form submission
@app.route('/webpage1', methods=['POST'])
def webpage1():
    # Retrieve the form data
    form_data = request.form

    # Ensure all required fields are present in the form data
    if all(field in form_data for field in ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']):
        try:
            # Convert form data to float values
            amount = float(form_data['amount'])
            oldbalanceOrg = float(form_data['oldbalanceOrg'])
            newbalanceOrig = float(form_data['newbalanceOrig'])
            oldbalanceDest = float(form_data['oldbalanceDest'])
            newbalanceDest = float(form_data['newbalanceDest'])

            # Create a DataFrame from the form data
            input_data = pd.DataFrame([[amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]], 
                                      columns=['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest'])

            # Make prediction using the XGBoost model
            prediction = xgb_model.predict(input_data)

            # Determine the prediction result
            result = "Fraudulent Transaction" if prediction[0] == 1 else "Legitimate Transaction"

            # Pass the prediction result to the template
            return render_template('webpage1.html', prediction=result)
        except ValueError:
            # Handle invalid input (e.g., non-numeric values)
            return render_template('error.html', message="Invalid input. Please enter numeric values.")
    else:
        # Handle missing fields in the form data
        return render_template('error.html', message="Missing form fields.")

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True, port=8080)
