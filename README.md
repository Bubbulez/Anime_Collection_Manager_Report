# Anime Collection Manager and Recommendation System

## Project Overview

The Anime Collection Manager and Recommendation System is a web-based Python application developed using Flask, SQLite, HTML, and Jinja2 templates.

The system allows users to:

- Add anime to a personal collection
- View all anime entries
- Search for anime by title
- Edit existing anime records
- Delete anime records
- Receive genre-based recommendations
- View collection statistics
- Prevent duplicate anime entries using case-insensitive matching

The project was created for CPS 3320 Python Programming at Kean University.

---

## Features

### Home Page
Provides navigation to all areas of the application.

### Add Anime
Allows users to enter:

- Title
- Genre
- Episode Count
- Rating
- Watch Status

Duplicate anime titles are automatically detected regardless of capitalization.

Example:

- Attack on Titan
- ATTACK ON TITAN
- attack on titan

These are treated as the same title.

### View Collection

Displays all anime stored in the database.

Information shown:

- Title
- Genre
- Episodes
- Rating
- Watch Status

Users can also edit or delete entries.

### Search Anime

Allows users to search for anime using a title or partial title.

### Recommendation System

Users enter a genre and receive matching anime recommendations from the collection.

Example:

Input:

Fantasy

Output:

- Fairy Tail
- No Game No Life

### Statistics Dashboard

Displays:

- Total Anime Count
- Watching Count
- Completed Count
- Paused Count
- Dropped Count
- Plan to Watch Count

---

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- Jinja2
- GitHub
- VS Code

---

## Project Structure

```text
Anime_Collection_Manager_Report/
│
├── app.py
├── anime.db
│
├── home.html
├── add_anime.html
├── anime_list.html
├── edit_anime.html
├── search.html
├── recommend.html
├── stats.html
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Bubbulez/Anime_Collection_Manager_Report.git
```

### Move into Project Folder

```bash
cd Anime_Collection_Manager_Report
```

### Install Flask

```bash
pip install flask
```

---

## Running the Application

Run:

```bash
python app.py
```

Flask will start the local server.

Open:

```text
http://127.0.0.1:5000
```

in a web browser.

---

## Database

SQLite is used to store anime records.

Database file:

```text
anime.db
```

Main table:

```sql
Anime
```

Fields:

- id
- title
- genre
- episodes
- rating
- watch_status

---

## Testing Results

The final test database contained:

- 97 Anime Entries
- 5 Completed
- 2 Watching
- 1 Paused
- 1 Dropped
- 88 Plan to Watch

All CRUD operations were tested successfully.

---

## Future Improvements

Potential future enhancements include:

- User Accounts
- Login Authentication
- Anime API Integration
- Advanced Recommendation Algorithms
- Cloud Database Support
- User Ratings Analytics

---

## Author

Delali Doe

Kean University

CPS 3320 Python Programming

Summer 2026