# Anime Collection Manager and Recommendation System

## Overview

The Anime Collection Manager and Recommendation System is a web-based Python application developed using Flask and SQLite. The application allows users to organize and manage anime collections through a user-friendly interface while providing recommendation and statistical analysis features.

This project was developed for CPS 3320 Python Programming at Kean University.

---

## Features

### Home Page
Provides navigation to all areas of the application.

### Add Anime
Allows users to add anime records including:

- Title
- Genre
- Episode Count
- Rating
- Watch Status

### Duplicate Detection
Prevents duplicate anime titles from being added.

Examples:

- Attack on Titan
- ATTACK ON TITAN
- attack on titan

All are recognized as the same title using case-insensitive matching.

### View Collection
Displays all anime currently stored in the database.

Users can:

- View anime details
- Edit entries
- Delete entries

### Search Anime
Allows searching by title or partial title.

### Recommendation System
Provides genre-based recommendations.

Example:

Input:

```text
Fantasy
```

Output:

```text
Fairy Tail
No Game No Life
```

### Statistics Dashboard
Displays collection statistics including:

- Total Anime
- Watching
- Completed
- Paused
- Dropped
- Plan to Watch

---

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- Jinja2
- GitHub
- Visual Studio Code
- Overleaf (IEEE Report)

---

## Project Structure

```text
Anime_Collection_Manager_Report/
│
├── app.py
├── anime.db
├── README.md
│
└── templates/
    ├── home.html
    ├── add_anime.html
    ├── anime_list.html
    ├── edit_anime.html
    ├── search.html
    ├── recommend.html
    └── stats.html
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Bubbulez/Anime_Collection_Manager_Report.git
```

Move into the project folder:

```bash
cd Anime_Collection_Manager_Report
```

Install Flask:

```bash
pip install flask
```

---

## Running the Application

Start the Flask application:

```bash
python app.py
```

Open a browser and visit:

```text
http://127.0.0.1:5000
```

---

## Database Design

The application uses SQLite for data storage.

Database File:

```text
anime.db
```

Main Table:

```text
Anime
```

Fields:

| Field | Description |
|---------|---------|
| id | Unique identifier |
| title | Anime title |
| genre | Anime genre |
| episodes | Episode count |
| rating | User rating |
| watch_status | Viewing status |

---

## Application Pages

### Home
Landing page and navigation hub.

### Add Anime
Create new anime records.

### View Collection
View all anime stored in the database.

### Edit Anime
Modify existing anime information.

### Delete Anime
Remove anime from the collection.

### Search Anime
Locate anime titles quickly.

### Recommendations
Receive recommendations based on genre.

### Statistics
View collection summaries and watch-status counts.

---

## Testing Results

The final test database contained:

| Metric | Value |
|----------|----------|
| Total Anime | 97 |
| Completed | 5 |
| Watching | 2 |
| Paused | 1 |
| Dropped | 1 |
| Plan to Watch | 88 |

Testing verified:

- Create functionality
- Read functionality
- Update functionality
- Delete functionality
- Search operations
- Duplicate detection
- Recommendation system
- Statistics generation

---

## Future Improvements

Potential enhancements include:

- User login system
- Multi-user support
- Anime API integration
- Cloud database deployment
- Personalized recommendation algorithms
- Data visualization dashboards

---

## Author

**Delali Doe**

Kean University

CPS 3320 Python Programming

Summer 2026

---

## GitHub Repository

Repository:

```text
https://github.com/Bubbulez/Anime_Collection_Manager_Report
```
