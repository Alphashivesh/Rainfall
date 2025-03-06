from flask import render_template, Flask, request
import pickle

app = Flask(__name__)  # unique name
file = open("model.pkl", "rb")
random_Forest = pickle.load(file)
file.close()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        myDict = request.form
        Month = int(myDict["Month"])
        Year = int(myDict["Year"])

        # Validate the inputs
        if Month < 1 or Month > 12:
            return render_template('index.html', error="Invalid month. Please enter a month between 1 and 12.")
        if Year < 1901 or Year > 2015:
            return render_template('index.html', error="Invalid year. Please enter a year between 1901 and 2015.")

        pred = [Year, Month]
        res = random_Forest.predict([pred])[0]
        res = round(res, 2)
        return render_template('result.html', Month=Month, Year=Year, res=res)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
