# Import get_connection from database.py
from database import get_connection

# Create Tables
def create_tables():
    conn = get_connection()
    
    # Get cursor to be able to read and write from the database
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            user_id VARCHAR(255) NOT NULL,
            title VARCHAR(255) NOT NULL,
            amount VARCHAR(255) NOT NULL,
            category VARCHAR(255) NOT NULL,
            note VARCHAR(255) NOT NULL,
            advice VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            
            
            
         )           
    """)
    # Save the changes to the database
    conn.commit()
    cursor.close()
    conn.close()
    print("Greetings Mr Madikgetla your data tables have been created.")
    if __name__ == "__main__":
        create_tables()