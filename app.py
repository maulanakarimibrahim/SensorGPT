from flask import Flask, render_template
import json

app = Flask(__name__

@app.route('/')
def display_json():

    with open('mydata.json','r') as json_file:
        data = json.load(json_file)

# render the template with the json data
    return render_template('display_json.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
