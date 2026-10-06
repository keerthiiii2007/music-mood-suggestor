from flask import Flask, render_template, request

app = Flask(__name__)

songs = {

    "Happy": [
        "Happy - Pharrell Williams",
        "Good Time - Owl City",
        "Best Day Of My Life - American Authors",
        "Can't Stop the Feeling - Justin Timberlake",
        "Walking on Sunshine - Katrina & The Waves",
        "Uptown Funk - Mark Ronson"
    ],

    "Sad": [
        "Someone You Loved - Lewis Capaldi",
        "Lovely - Billie Eilish",
        "Let Her Go - Passenger",
        "Photograph - Ed Sheeran",
        "The Night We Met - Lord Huron",
        "When I Was Your Man - Bruno Mars"
    ],

    "Chill": [
        "Sunflower - Post Malone",
        "Ocean Eyes - Billie Eilish",
        "Until I Found You - Stephen Sanchez",
        "Golden Hour - JVKE",
        "Perfect - Ed Sheeran",
        "Here With Me - d4vd"
    ],

    "Energetic": [
        "Believer - Imagine Dragons",
        "Counting Stars - OneRepublic",
        "On Top Of The World - Imagine Dragons",
        "Thunder - Imagine Dragons",
        "Hall of Fame - The Script",
        "Dance Monkey - Tones and I"
    ],

    "Romantic": [
        "Perfect - Ed Sheeran",
        "All of Me - John Legend",
        "A Thousand Years - Christina Perri",
        "Until I Found You - Stephen Sanchez",
        "Just the Way You Are - Bruno Mars",
        "Love Story - Taylor Swift"
    ]
}  


@app.route("/", methods=["GET", "POST"])
def home():

    selected_mood = None
    recommended_songs = []

    if request.method == "POST":
        selected_mood = request.form["mood"]
        recommended_songs = songs[selected_mood]

    return render_template(
        "index.html",
        selected_mood=selected_mood,
        recommended_songs=recommended_songs
    )


app.run(debug=True)