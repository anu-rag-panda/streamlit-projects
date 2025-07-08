import pandas as pd
import sqlite3
from dataclasses import dataclass
from typing import List

@dataclass
class Flight:
    flight_number: str
    source: str
    destination: str
    fare: float
    duration: float

class FlightManager:
    def __init__(self, db_path: str = "flights.db"):
        """Initialize FlightManager with database path."""
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self) -> None:
        """Initialize the SQLite database with flights table."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS flights (
                    flight_number TEXT PRIMARY KEY,
                    source TEXT NOT NULL,
                    destination TEXT NOT NULL,
                    fare REAL NOT NULL,
                    duration REAL NOT NULL
                )
            """)
    
    def add_flight(self, flight: Flight) -> None:
        """Add or update a flight in the database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT OR REPLACE INTO flights 
                (flight_number, source, destination, fare, duration)
                VALUES (?, ?, ?, ?, ?)
            """, (flight.flight_number, flight.source, flight.destination, 
                 flight.fare, flight.duration))
    
    def filter_flights(self, max_fare: float, max_duration: float) -> List[Flight]:
        """Filter flights by maximum fare and duration."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                SELECT * FROM flights 
                WHERE fare <= ? AND duration <= ?
            """, (max_fare, max_duration))
            
            return [Flight(*row) for row in cursor.fetchall()]
    
    def to_dataframe(self) -> pd.DataFrame:
        """Convert all flights to a pandas DataFrame."""
        with sqlite3.connect(self.db_path) as conn:
            return pd.read_sql_query("SELECT * FROM flights", conn)