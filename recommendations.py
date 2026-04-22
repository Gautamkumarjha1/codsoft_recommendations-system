# Simple movie dataset
movies = {
    "Avengers": "action",
    "Iron Man": "action",
    "Batman": "action",
    "Joker": "drama",
    "Titanic": "romance",
    "Notebook": "romance",
    "Superman": "action",
    "La La Land": "romance"
}

# Recommendation function
def recommend(movie_name):
    if movie_name not in movies:
        return "Movie not found!"

    genre = movies[movie_name]
    recommendations = []

    for movie in movies:
        if movies[movie] == genre and movie != movie_name:
            recommendations.append(movie)

    return recommendations

# Main program
print("Available Movies:")
for m in movies:
    print("-", m)

user_movie = input("\nEnter a movie you like: ")

result = recommend(user_movie)

print("\n🎯 Recommended Movies:")
print(result)
