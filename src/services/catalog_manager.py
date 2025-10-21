from src.repositories.catalog_repository import CatalogRepository

class CatalogManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.repository = CatalogRepository()
            cls._instance.catalog = cls._instance.repository.load_from_xml()
        return cls._instance

    def add_media(self, media):
        self.catalog.append(media)

    def view_all(self):
        return self.catalog

    def save(self):
        self.repository.save_to_xml(self.catalog)
