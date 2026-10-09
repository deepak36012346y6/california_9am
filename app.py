from flask import Flask, render_template, request
import joblib
import pandas as pd
import os

app = Flask(__name__)

folder = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(
    os.path.join(folder, "california.joblib")
)

columns = [
    "MedInc",
    "HouseAge",
    "AveRooms",
    "AveBedrms",
    "Population",
    "AveOccup",
    "Latitude",
    "Longitude"
]

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    error = None
    values = {}

    if request.method == "POST":

        try:
            for col in columns:

                values[col] = request.form.get(col, "").strip()

                if not values[col]:
                    raise ValueError(f"Enter {col}")

            data = [
                float(values[col])
                for col in columns
            ]

            df = pd.DataFrame(
                [data],
                columns=columns
            )

            prediction = float(
                model.predict(df)[0]
            ) * 100000

        except (ValueError, TypeError) as e:

            error = str(e)

    return render_template(
        "index.html",
        prediction=prediction,
        error=error,
        values=values
    )


if __name__ == "__main__":
    app.run(debug=True)
