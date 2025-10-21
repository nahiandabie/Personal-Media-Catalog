# 🎬 Personal Media Catalog

A Python console application that manages a personal collection of books, movies, and video games using **XML** for data persistence and **XSLT** for reporting.

---

## 🚀 Features
- Add, view, and save media items (books, movies, games)
- Data stored in `catalog.xml` and validated by `media_catalog.xsd`
- Dynamic object creation using the **Factory Pattern**
- Single instance catalog management via **Singleton Pattern**
- Persistent XML storage with the **Repository Pattern**
- Generate HTML reports using **XSLT transformations**
- Fully version-controlled with Git and GitHub
---

## 🗂️ Project Structure
Personal-Media-Catalog/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── media.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── catalog_repository.py
│   └── services/
│       ├── __init__.py
│       ├── catalog_manager.py
│       ├── media_factory.py
│       └── report_generator.py
├── data/
│   ├── catalog.xml
│   ├── media_catalog.xsd
│   ├── catalog_to_html.xsl
│   └── movies_only.xsl
├── docs/
│   └── FINAL_REPORT.md
├── requirements.txt
└── README.md
---

## 🧩 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/codecrafters-org/personal-media-catalog.git
   cd personal-media-catalog
2. Create a virtual environment:
   python -m venv venv
   venv\Scripts\activate  # for Windows
3. Install dependencies:
   pip install -r requirements.txt

▶️ Usage
Run the application from the root folder:
python -m src.main

Use the console menu to:
1. Add media items
2. View all media
3. Generate HTML reports
4. Save and exit

🧱 Design Patterns Used

| Pattern        | Purpose                                                |
| -------------- | ------------------------------------------------------ |
| **Factory**    | Dynamically creates Book, Movie, and VideoGame objects |
| **Singleton**  | Ensures only one instance of CatalogManager            |
| **Repository** | Handles XML persistence (load and save operations)     |

🧾 Reporting

Generate HTML reports directly from the console:
Full Catalog Report: catalog_to_html.xsl
Movies Only Report: movies_only.xsl
The output HTML files are saved under the data/ directory and can be opened in any browser.

🧠 Contributors
| Name             | Role                               |
| ---------------- | ---------------------------------- |
| Nahom Aychiluhum | Team Lead & Python Developer       |
| Hana Kebede      | XML/XSLT Designer                  |
| Yonas Mekonnen   | Repository & Documentation Manager |

🧰 Tools & Technologies
. Python 3.x
. XML / XSD / XSLT
. lxml library
. Git & GitHub
