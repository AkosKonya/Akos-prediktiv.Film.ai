movies = [
  { "title": "Rush", "genre": "Action", "age": "15+", "runtime": "2:03" },
  { "title": "Rush Hour", "genre": "Comedy", "age": "13+", "runtime": "1:38" },
  { "title": "John Wick", "genre": "Action", "age": "17+", "runtime": "1:41" },
  { "title": "Cars", "genre": "Adventure", "age": "All ages", "runtime": "1:57" },
  { "title": "Puss in Boots", "genre": "Adventure", "age": "7+", "runtime": "1:30" },
  { "title": "The Terminator", "genre": "Action", "age": "17+", "runtime": "1:47" },
  { "title": "Terminator 2: Judgment Day", "genre": "Action", "age": "15+", "runtime": "2:17" },
  { "title": "Terminator 3: Rise of the Machines", "genre": "Action", "age": "13+", "runtime": "1:49" },
  { "title": "Cars 2", "genre": "Adventure", "age": "6+", "runtime": "1:46" },
  { "title": "The Matrix", "genre": "Action", "age": "15+", "runtime": "2:16" },
  { "title": "Mad Max: Fury Road", "genre": "Action", "age": "15+", "runtime": "2:00" },
  { "title": "Spider-Man: Into the Spider-Verse", "genre": "Adventure", "age": "10+", "runtime": "1:57" },
  { "title": "Gladiator", "genre": "Action", "age": "16+", "runtime": "2:35" },
  { "title": "Finding Nemo", "genre": "Adventure", "age": "All ages", "runtime": "1:40" },
  { "title": "Shrek", "genre": "Comedy", "age": "7+", "runtime": "1:30" },
  { "title": "Mission: Impossible", "genre": "Action", "age": "13+", "runtime": "1:50" },
  { "title": "The Dark Knight", "genre": "Action", "age": "13+", "runtime": "2:32" },
  { "title": "Kung Fu Panda", "genre": "Adventure", "age": "7+", "runtime": "1:32" },
  { "title": "Toy Story", "genre": "Adventure", "age": "All ages", "runtime": "1:21" },
  { "title": "Guardians of the Galaxy", "genre": "Action", "age": "13+", "runtime": "2:01" },
  { "title": "Jurassic Park", "genre": "Adventure", "age": "13+", "runtime": "2:07" },
  { "title": "Deadpool", "genre": "Comedy", "age": "17+", "runtime": "1:48" },
  { "title": "Avengers: Endgame", "genre": "Action", "age": "13+", "runtime": "3:01" },
  { "title": "How to Train Your Dragon", "genre": "Adventure", "age": "7+", "runtime": "1:38" },
  { "title": "Pirates of the Caribbean: The Curse of the Black Pearl", "genre": "Adventure", "age": "13+", "runtime": "2:23" },
  { "title": "Jumanji: Welcome to the Jungle", "genre": "Comedy", "age": "12+", "runtime": "1:59" },
  { "title": "Top Gun: Maverick", "genre": "Action", "age": "13+", "runtime": "2:11" },
  { "title": "The Incredibles", "genre": "Adventure", "age": "All ages", "runtime": "1:55" },
  { "title": "Men in Black", "genre": "Comedy", "age": "12+", "runtime": "1:38" },
  { "title": "Ready Player One", "genre": "Action", "age": "13+", "runtime": "2:20" }
]

while True:
    genre = input("What genre do you like? (Q or q to quit)\n")

    if genre.lower() == "q":
        print("Program stopped.")
        break

    age = input("What age restriction?\n")
    runtime = input("What's your desired movie length? (hours:min)\n")

    scored_movies = []

    for movie in movies:
        score = 0

        if movie["genre"] == genre:
            score += 2

        if movie["age"] == age:
            score += 1

        if movie["runtime"] == runtime:
            score += 1

        scored_movies.append((score, movie["title"]))

    # Den film som har mäst poäng liger högst upp i listan eftersom de är sorterade genom vilken som har högst poäng.
    scored_movies.sort(reverse=True)

    print("\nWe recommend these movies:")

    # Printar top 3 filmer som fick mest poäng efter frågorna som ställdes.
    for i in range(3):
        print(f"{i+1}. {scored_movies[i][1]}")

        #Idag har jag skrivit till 20 mer filmer, samt har jag försökt lösa att den ger mig 3 film rekommendationer på samma gång. Men det gick inte så bra så tillslut fick jag lite hjälp från en AI för att få en idé på vad för slags kod man skriver för att få 3 film rekommendationer.
        #Nästa gång behöver jag att lägga till mer frågor och försöka göra koden så fint som möjligt.