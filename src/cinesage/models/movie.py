from pydantic import BaseModel, Field, field_validator

class MovieData(BaseModel):
    title:str = Field(
        min_length=1,
        max_length=200,
        description="Movie Title"
    )

    release_year: int | None = Field(
        default=None,
        ge=1888,
        le=2100
    )

    genres: list[str] = Field(
        min_length=1,
        max_length=10
    )

    director:str | None = Field(
        default=None,
        max_length=100
    )
    
    cast: list[str] = Field(
        default_factory=list,
        max_length=20
    )

    rating: float | None = Field(
        ge=0,
        le=10
    )

    summary:str | None = Field(
        default=None,
        max_length=1000
    )

# Custom title validation
@field_validator("title")
@classmethod
def validate_title(cls, value):
    if not value:
        raise ValueError("Movie title cannot be empty")

    value = value.strip()

    return value

# Custom genre validation
@field_validator("genres")
@classmethod
def validate_genre(cls, value):
    genres = [genre.strip() for genre in value]
    if any(not genre for genre in genres):
        raise ValueError("Genre names cannot be empty")
    return genres