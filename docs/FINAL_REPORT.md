# 📘 Final Report — Personal Media Catalog

## 🧑‍🤝‍🧑 Team Members
- **Nahom Aychiluhum** – Team Lead & Developer  
- **Hana Kebede** – XML/XSLT Designer  
- **Yonas Mekonnen** – Repository & Documentation Manager  

---

## 🎯 Project Overview
The *Personal Media Catalog* is a Python-based console application that allows users to manage their personal collection of media (books, movies, and video games). It demonstrates the integration of XML technologies with software design principles and version control.

---

## 🧩 Design Patterns Implemented

| Pattern | Description | Implementation |
|----------|--------------|----------------|
| **Factory Pattern** | Creates media objects dynamically based on user input. | `MediaFactory.create_media()` |
| **Singleton Pattern** | Ensures only one `CatalogManager` instance handles media operations. | `CatalogManager` class |
| **Repository Pattern** | Separates XML persistence logic from business logic. | `CatalogRepository` class |

---

## 🧱 Technologies Used
- **Python 3.11+**
- **xml.etree.ElementTree**
- **lxml (for XSLT)**
- **Git & GitHub for version control**
- **VS Code IDE**

---

## 🧠 Challenges & Solutions

| Challenge | Solution |
|------------|-----------|
| XML parsing errors during validation | Validated XML against `media_catalog.xsd` early in development |
| Path errors when running `main.py` | Used `python -m src.main` to execute from root folder |
| XSLT formatting inconsistencies | Added inline CSS for consistent HTML rendering |
| Git push conflicts | Resolved by using `git pull --rebase` before pushing |

---

## 💡 Lessons Learned
- Importance of structuring projects with design patterns.
- How XML, XSD, and XSLT can work together with Python.
- Benefits of version control for collaborative development.
- Value of separating concerns through repositories and services.

---

## 🧾 Conclusion
This project successfully demonstrates software integration using XML technologies, design patterns, and Git collaboration. It serves as a practical implementation of the principles taught in the *Integrative Programming and Technologies* course.

---