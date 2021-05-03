from flask import Flask, request, jsonify
import json
import pandas as pd

app = Flask(__name__)
# Excel sheet is converted to DataFrame using Pandas command
df = pd.read_excel("Dummy data V 1.2 tableau.xlsx")


@app.route('/', methods=['GET'])
# Home route which returns basic HTML output
def home():
    return '''<h1>Get User Data from Dummy Excel Sheet</h1>
    <p>A prototype API to get user data from Email ID</p>'''


@app.route('/data', methods=['POST', 'GET'])
# Main 'data' route which on taking POST or GET request
# stores email of a user, searches for its presence in
# the given dataframe, converts to JSON and sent to the HTML page
def data():
    user_json = ''
    if request.method == 'POST':
        email = request.form.get('email')
    else:
        email = request.args.get('email')
    user = df.loc[df[df['Email'] == email].index[0]]
    user_json = user.to_json(orient='index')

    parsed = json.loads(user_json)
    return jsonify(parsed)


if __name__ == '__main__':
    app.run(debug=True) # Running the main function with Debug ON in order to point out any errors
