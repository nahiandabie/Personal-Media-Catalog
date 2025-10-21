from src.models.media import Book, Movie, VideoGame

class MediaFactory:
    @staticmethod
    def create_media(media_type, **kwargs):
        if media_type.lower() == "book":
            return Book(**kwargs)
        elif media_type.lower() == "movie":
            return Movie(**kwargs)
        elif media_type.lower() == "videogame":
            return VideoGame(**kwargs)
        else:
            raise ValueError(f"Unknown media type: {media_type}")
