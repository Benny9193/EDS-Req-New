"""Connect to SQL Server using credentials from .env file."""
import pyodbc
from dotenv import load_dotenv
import os

# Load .env from parent directory
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE_CATALOG', 'EDS')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')

conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"TrustServerCertificate=yes;"
)

try:
    conn = pyodbc.connect(conn_str, timeout=10)
    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION")
    version = cursor.fetchone()[0]
    print("Connected successfully!")
    print(f"Server: {server}")
    print(f"Database: {database}")
    print(f"\nSQL Server Version:\n{version}")
    cursor.close()
    conn.close()
except pyodbc.Error as e:
    print(f"Connection failed: {e}")
