 AI-Powered Music Recommendation System

 Overview

This project is a web-based Music Recommendation System developed using Python and Flask. It recommends songs based on user input by applying Natural Language Processing (NLP) techniques such as TF-IDF Vectorization and Cosine Similarity.

The system analyzes song features including genre, mood, and keywords, then recommends the most relevant songs along with Spotify and YouTube search links.

 Features

* Personalized music recommendations
* Content-based filtering
* TF-IDF Vectorization
* Cosine Similarity matching
* Spotify search integration
* YouTube search integration
* User-friendly web interface

Technologies Used

* Python
* Flask
* Pandas
* Scikit-learn
* HTML
* CSS
* TF-IDF Vectorization
* Cosine Similarity

 Project Structure

text
Music-Recommendation-System/
│
├── app.py
├── songs.csv
├── REQUIREMENTS.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

 How It Works

1. Song data is loaded from the dataset.
2. Genre, mood, and keywords are combined into a feature column.
3. TF-IDF Vectorization converts text into numerical vectors.
4. User input is transformed using the same TF-IDF model.
5. Cosine Similarity calculates similarity scores.
6. The top matching songs are recommended.
7. Spotify and YouTube search links are generated for each recommendation.

 Installation

1. Clone the repository


git clone https://github.com/faizal-afk/MUSICRECOMMENDATION.git


2. Navigate to the project directory


cd MUSICRECOMMENDATION


3. Install dependencies


pip install -r REQUIREMENTS.txt


4. Run the application
python app.py


5. Open your browser and visit


http://127.0.0.1:5000


Future Improvements

* User authentication
* Hybrid recommendation system
* Real Spotify API integration
* Improved recommendation accuracy
* Larger music dataset

