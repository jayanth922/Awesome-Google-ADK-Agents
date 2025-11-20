import sqlite3
import os

DB_FILE = "hotels.db"

def setup_database():
    """Initializes the SQLite database with sample data."""
    if os.path.exists(DB_FILE):
        return

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hotels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            location TEXT,
            price_per_night REAL,
            amenities TEXT,
            rating REAL
        )
    ''')
    
    # Sample Data
    hotels = [
        ("Grand Paris Hotel", "Paris", 180.0, "WiFi, Breakfast", 4.5),
        ("Eiffel View Inn", "Paris", 250.0, "View, WiFi, Pool", 4.8),
        ("Tokyo Tower Stay", "Tokyo", 120.0, "WiFi", 4.0),
        ("Sakura Hostel", "Tokyo", 50.0, "Shared Lounge", 3.5),
        ("NYC Luxury Suites", "New York", 450.0, "Pool, Gym, Spa", 5.0),
        ("Brooklyn Boutique", "New York", 200.0, "WiFi, Bar", 4.2),
        ("London Central", "London", 220.0, "WiFi, Breakfast", 4.3)
    ]
    
    cursor.executemany('INSERT INTO hotels (name, location, price_per_night, amenities, rating) VALUES (?, ?, ?, ?, ?)', hotels)
    conn.commit()
    conn.close()
    print(f"Database {DB_FILE} created and populated.")

def search_hotels(location: str, max_price: float = 1000.0, amenity: str = None):
    """
    Searches for hotels in the database.
    
    Args:
        location: The city/location to search in (e.g., 'Paris').
        max_price: Maximum price per night.
        amenity: Optional amenity to filter by (e.g., 'Pool').
    """
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    query = "SELECT * FROM hotels WHERE location LIKE ? AND price_per_night <= ?"
    params = [f"%{location}%", max_price]
    
    if amenity:
        query += " AND amenities LIKE ?"
        params.append(f"%{amenity}%")
        
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    
    results = []
    for row in rows:
        results.append({
            "name": row["name"],
            "location": row["location"],
            "price": row["price_per_night"],
            "amenities": row["amenities"],
            "rating": row["rating"]
        })
        
    return results

