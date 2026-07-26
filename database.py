from dotenv import load_dotenv
import os
import psycopg

load_dotenv()

db = os.getenv("DATABASE_URL")
print(db)
conn = psycopg.connect(db)
cursor = conn.cursor()

print("Connected to PostgreSQL!")