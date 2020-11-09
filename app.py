from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

path = os.path.join("../Instructions/Resources/cities.csv")

cities_data = pd.read_csv(path)

print(cities_data)

print(cities_data.shape)

print(cities_data.columns.values)

cities = cities_data.to_dict(orient="record")
print(cities)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/graphics")
def graphic_pages():
    return render_template("visualization-pages.html")


@app.route("/analysis")
def analysis_page():
    return render_template("comparisons-page.html")

@app.route("/data")
def data_page():
    return render_template("data-page.html", cities=cities)


if __name__=="__main__":
    app.run(debug=True)

