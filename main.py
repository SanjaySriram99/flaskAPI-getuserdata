from flask import Flask, request, render_template, url_for, redirect, jsonify
import json
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/data', methods=['GET', 'POST'])
def data():
    # print(request.body)
    email = request.form.get('email', False)
    # print(email)
    df = pd.read_excel('Dummy data V 1.2 tableau.xlsx')
    for i in range(df.shape[0]):
        if email == df['Email'][i]:
            user = df.loc[i]
    user_json = user.to_json()
    result = json.loads(user_json)
    return result


if __name__ == '__main__':
    app.run(debug=True)
