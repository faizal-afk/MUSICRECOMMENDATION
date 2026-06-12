from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

songs = pd.read_csv("songs.csv")

songs["features"] = (
    songs["genre"] + " " +
    songs["mood"] + " " +
    songs["keywords"]
)

tfidf = TfidfVectorizer(stop_words="english")
matrix = tfidf.fit_transform(songs["features"])

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    if request.method == "POST":

        user_input = request.form["lyrics"]

        user_vector = tfidf.transform([user_input])

        similarity = cosine_similarity(user_vector, matrix)

        scores = list(enumerate(similarity[0]))

        scores = sorted(
            scores,
            key=lambda x: x[1],
            reverse=True
        )

        for i in scores:

            if i[1] > 0.10:

                recommendations.append({
                    "song": songs.iloc[i[0]]["song"],
                    "artist": songs.iloc[i[0]]["artist"],
                    "genre": songs.iloc[i[0]]["genre"],
                    "mood": songs.iloc[i[0]]["mood"],
                    "score": round(i[1] * 100, 2),

                    "spotify":
                    f"https://open.spotify.com/search/{songs.iloc[i[0]]['song']}",

                    "youtube":
                    f"https://www.youtube.com/results?search_query={songs.iloc[i[0]]['song']} {songs.iloc[i[0]]['artist']}"
                })

            if len(recommendations) == 6:
                break

    return render_template(
        "index.html",
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)