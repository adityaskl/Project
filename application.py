import flask
from flask import render_template, request

import pickle
from training import prediction
import requests
application = flask.Flask(__name__)


model = pickle.load(open("model.pickle", 'rb'))


@application.route("/")
@application.route('/index.html')
def index() -> str:
    """Base page."""
    return flask.render_template("index.html")


@application.route('/plots.html')
def plots():
    return render_template('plots.html')

@application.route('/densityMaps.html')
def heatmaps():
    return render_template('densityMaps.html')



@application.route('/predictsdrought.html')
def predictsdrought():
    return render_template('predictsdrought.html')


@application.route('/predicts.html')
def predicts():
    return render_template('predicts.html', cityname="Information about the city")


@application.route('/predicts.html', methods=["GET", "POST"])
def get_predicts():
    try:
        cityname = request.form["city"]
        # print(cityname)
        URL = "https://geocode.search.hereapi.com/v1/geocode"
        location = cityname
        # Acquire from developer.here.com
        api_key = 'ftKvGdH2ItSBc6N3Jbh4TzpH6F57uHHqw4Us4Uoj0HM'
        PARAMS = {'apikey': api_key, 'q': location}
        # sending get request and saving the response as response object
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        latitude = data['items'][0]['position']['lat']
        longitude = data['items'][0]['position']['lng']
        final = prediction.get_data(latitude, longitude)

        final[4] *= 15
        if str(model.predict([final])[0]) == "0":
            pred = "Safe"
        else:
            pred = "Unsafe"

        return render_template('predicts.html', cityname="Information about " + cityname, temp=round(final[0], 2), maxt=round(final[1], 2), wspd=round(final[2], 2), cloudcover=round(final[3], 2), percip=round(final[4], 2), humidity=round(final[5], 2), pred=pred)
    except:
        return render_template('predicts.html', cityname="Oops, we weren't able to retrieve data for that city.")


if __name__ == "__main__":
    application.run(debug=True)
