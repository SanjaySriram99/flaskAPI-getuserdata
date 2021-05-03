# flaskAPI-getuserdata
Basic flask API to get user data from excel spreadsheet
login.html is the basic HTML for taking email as input.
It then gives a POST request to the API, which then searches the given Excel Spreadsheet for the email.
The Excel Spreadsheet has been converted to Pandas DataFrame for ease of earching and utilisation.
Once the email has been checked in Excel, the whole row data is passed back to the HTML page as JSON.
