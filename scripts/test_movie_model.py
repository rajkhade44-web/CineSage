from cinesage.models.movie import MovieData
from pydantic import ValidationError

# movie = MovieData(
#     title="Interstellar",
#     release_year=2014,
#     director="Christopher Nolan",
#     cast=["Matthew McConaughey", "Anne Hathaway"],
#     genres=["Sci-Fi", "Drama"],
#     summary="A journey through space and time.",
#     rating=8.7
# )

# print(f"Valid Movie: {movie.title}")

# # Invalid Rating 
# try:
#     MovieData(
#         title="Test Movie",
#         genres=['Action'],
#         rating=15
#     )
# except ValidationError as e:
#     print("\n Invalid Rating")
#     print(e)

# # Empty Title
# try:
#     MovieData(
#         title="",
#         genres=['Drama'],
#         rating=8.5
#     )
# except ValidationError as e:
#     print("\nInvalid Title")
#     print(e)

# # Empty Genre
# try:
#     MovieData(
#         title="Test Movie",
#         genres=[],
#         rating=8.0
#     )
# except ValidationError as e:
#     print("\nInvalid Genre")
#     print(e)



# print(f"Movie Title: {movie.title}")

# print("\nJSON OUTPUT: ")

# print(movie.model_dump_json(indent=2))

# Test 1 : Title and genre cleaning

movie = MovieData(
    title="   Interstellar   ",
    genres=[" Sci-Fi ", " Drama "],
    rating=8.7
)
print(movie.title)
print(movie.genres)

# Test 2 : Empty title

try:
    MovieData(
        title="   ",
        genres=["Drama"],
        rating=8.0
    )
except ValidationError as e:
    print("Title validation failed:", e)

# Test 3 : Empty genres
try:
    MovieData(
        title="Inception",
        genres=["Action", "  "],
        rating=8.8
    )
except ValidationError as e:
    print("Genre validation failed:", e)

print(movie.genres[0])