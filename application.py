from flask import Flask, request, render_template, jsonify, redirect, url_for, session
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
application.secret_key = "your_secret_key_here"  # Use a strong random secret key

app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        data = CustomData(
            no_of_dependents=int(request.form.get('no_of_dependents')),
            education=request.form.get('education'),
            self_employed=request.form.get('self_employed'),
            income_annum=int(request.form.get('income_annum')),
            loan_amount=int(request.form.get('loan_amount')),
            loan_term=int(request.form.get('loan_term')),
            cibil_score=int(request.form.get('cibil_score')),
            residential_assets_value=int(request.form.get('residential_assets_value')),
            commercial_assets_value=int(request.form.get('commercial_assets_value')),
            luxury_assets_value=int(request.form.get('luxury_assets_value')),
            bank_asset_value=int(request.form.get('bank_asset_value')),
        )

        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)

        # Save result in session and redirect to avoid form resubmission
        result = "Accepted" if pred[0] == 1 else "Rejected"
        session['final_result'] = result

        return redirect(url_for('predict_datapoint'))

    # GET request - show form with result if available
    final_result = session.pop('final_result', None)
    return render_template('form.html', final_result=final_result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
