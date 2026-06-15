from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/add", methods=["GET", "POST"])
def add_anime():
    if request.method == "POST":
        title = request.form["title"].strip()
        genre = request.form["genre"]
        episodes = request.form["episodes"]
        rating = request.form["rating"]
        watch_status = request.form["watch_status"]

        connection = sqlite3.connect("anime.db")
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM Anime WHERE TRIM(LOWER(title)) = TRIM(LOWER(?))",
            (title,)
        )

        existing_anime = cursor.fetchone()

        if existing_anime:
            connection.close()
            return render_template(
                "add_anime.html",
                message="This anime is already in your collection."
            )

        cursor.execute(
            "INSERT INTO Anime (title, genre, episodes, rating, watch_status) VALUES (?, ?, ?, ?, ?)",
            (title, genre, episodes, rating, watch_status)
        )

        connection.commit()
        connection.close()

        return redirect("/list")

    return render_template("add_anime.html")


@app.route("/list")
def anime_list():
    connection = sqlite3.connect("anime.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Anime")
    anime_list = cursor.fetchall()

    connection.close()

    return render_template("anime_list.html", anime_list=anime_list)


@app.route("/search", methods=["GET", "POST"])
def search_anime():
    results = []

    if request.method == "POST":
        search_term = request.form["search_term"]

        connection = sqlite3.connect("anime.db")
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM Anime WHERE title LIKE ?",
            ("%" + search_term + "%",)
        )

        results = cursor.fetchall()
        connection.close()

    return render_template("search.html", results=results)


@app.route("/recommend", methods=["GET", "POST"])
def recommend_anime():
    recommendations = []

    if request.method == "POST":
        genre = request.form["genre"]

        connection = sqlite3.connect("anime.db")
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM Anime WHERE genre LIKE ?",
            ("%" + genre + "%",)
        )

        recommendations = cursor.fetchall()
        connection.close()

    return render_template("recommend.html", recommendations=recommendations)


@app.route("/stats")
def stats():
    connection = sqlite3.connect("anime.db")
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM Anime")
    total = cursor.fetchone()[0]

    cursor.execute("""
        SELECT watch_status, COUNT(*)
        FROM Anime
        GROUP BY watch_status
    """)

    status_counts = cursor.fetchall()

    connection.close()

    return render_template(
        "stats.html",
        total=total,
        status_counts=status_counts
    )


@app.route("/delete/<int:id>")
def delete_anime(id):
    connection = sqlite3.connect("anime.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM Anime WHERE id = ?", (id,))

    connection.commit()
    connection.close()

    return redirect("/list")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_anime(id):
    connection = sqlite3.connect("anime.db")
    cursor = connection.cursor()

    if request.method == "POST":
        title = request.form["title"]
        genre = request.form["genre"]
        episodes = request.form["episodes"]
        rating = request.form["rating"]
        watch_status = request.form["watch_status"]

        cursor.execute("""
            UPDATE Anime
            SET title = ?,
                genre = ?,
                episodes = ?,
                rating = ?,
                watch_status = ?
            WHERE id = ?
        """, (title, genre, episodes, rating, watch_status, id))

        connection.commit()
        connection.close()

        return redirect("/list")

    cursor.execute("SELECT * FROM Anime WHERE id = ?", (id,))
    anime = cursor.fetchone()

    connection.close()

    return render_template("edit_anime.html", anime=anime)


if __name__ == "__main__":
    app.run(debug=True)