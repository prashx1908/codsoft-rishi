def get_movie_ratings():
    # This function simulates a database of movie ratings.
    # In a real-world scenario, you would retrieve this data from a database.
    return {
        'Movie1': 4.5,
        'Movie2': 3.0,
        'Movie3': 5.0,
        'Movie4': 2.5,
        'Movie5': 4.0,
        'Movie6': 3.5,
    }

def recommend_movies(user_ratings, threshold=3.5):
    recommended_movies = []

    for movie, rating in user_ratings.items():
        if rating >= threshold:
            recommended_movies.append(movie)

    return recommended_movies

def main():
    print("Welcome to the Movie Recommendation System!")

    # Simulate user ratings (you can replace this with user input or a real user database)
    user_ratings = {
        'Movie1': 4.0,
        'Movie2': 2.5,
        'Movie4': 3.5,
    }

    print("Your Ratings:")
    for movie, rating in user_ratings.items():
        print(f"{movie}: {rating}")

    # Get all movie ratings from the database
    all_movie_ratings = get_movie_ratings()

    # Recommend movies based on user ratings
    threshold = 3.0  # You can adjust this threshold based on your preference
    recommendations = recommend_movies(user_ratings, threshold)

    print("\nRecommended Movies:")
    for movie in recommendations:
        print(movie)

if __name__ == "__main__":
    main()
