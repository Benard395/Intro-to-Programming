import csv
import os
DATA_FILE = os.path.join(os.path.dirname(__file__), "deniro.csv")
with open(DATA_FILE, newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    headers = next(reader)
    movies = [
        {
            "year": int(row[0]),
            "score": int(row[1]),
            "title": row[2].strip('"'),
        }
        for row in reader
        if row
    ]
lowest = min(movies, key=lambda m: m["score"])
highest = max(movies, key=lambda m: m["score"])
average = sum(m["score"] for m in movies) / len(movies)
longest_title = max(movies, key=lambda m: len(m["title"]))
years = sorted(movie["year"] for movie in movies)
longest_gap = max(
    years[i] - years[i - 1] for i in range(1, len(years))
)
print(f"Lowest rated movie: {lowest['title']} ({lowest['score']})")
print(f"Highest rated movie: {highest['title']} ({highest['score']})")
print(f"Average rating: {average:.2f}")
print(f"Longest movie title: {longest_title['title']}")
print(f"Longest gap between movies: {longest_gap} years")
