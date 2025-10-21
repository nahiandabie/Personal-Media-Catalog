from src.services.catalog_manager import CatalogManager
from src.services.media_factory import MediaFactory
from src.services.report_generator import ReportGenerator

def show_menu():
    print("\n=== Personal Media Catalog ===")
    print("1. Add Media")
    print("2. View All Media")
    print("3. Generate HTML Report")
    print("4. Save and Exit")

def add_media(manager):
    media_type = input("Enter media type (book/movie/videogame): ").strip().lower()
    title = input("Title: ")
    year = input("Year: ")
    genre = input("Genre: ")

    if media_type == "book":
        author = input("Author: ")
        pages = input("Pages: ")
        media = MediaFactory.create_media("book", title=title, year=year, genre=genre, author=author, pages=pages)
    elif media_type == "movie":
        director = input("Director: ")
        duration = input("Duration: ")
        media = MediaFactory.create_media("movie", title=title, year=year, genre=genre, director=director, duration=duration)
    elif media_type == "videogame":
        platform = input("Platform: ")
        developer = input("Developer: ")
        media = MediaFactory.create_media("videogame", title=title, year=year, genre=genre, platform=platform, developer=developer)
    else:
        print("Invalid media type.")
        return

    manager.add_media(media)
    print(f"{media_type.capitalize()} added successfully!")

def main():
    manager = CatalogManager()
    reporter = ReportGenerator()
    while True:
        show_menu()
        choice = input("Select option: ")
        if choice == "1":
            add_media(manager)
        elif choice == "2":
            for m in manager.view_all():
                print(vars(m))
        elif choice == "3":
            print("\n1. Full Catalog Report\n2. Movies Only Report\n3. Book Only Report")
            sub_choice = input("Select report type: ")
            if sub_choice == "1":
                reporter.generate_report("data/catalog_to_html.xsl", "data/full_catalog.html")
            elif sub_choice == "2":
                reporter.generate_report("data/movies_only.xsl", "data/movies_only.html")
            elif sub_choice == "3":
                reporter.generate_report("data/book_only.xsl", "data/book_only.html")
            else:
                print("Invalid choice.")
        elif choice == "4":
            manager.save()
            print("Catalog saved. Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
