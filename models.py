# Import get_connection from database.py
from database import get_connection

# Create Tables
def create_tables():
    conn = get_connection()
    
    # Get cursor to be able to read and write from the database
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id SERIAL PRIMARY KEY,
            user_id INTEGER  NOT NULL,
            title VARCHAR(255) NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            category VARCHAR(255) NOT NULL,
            note VARCHAR(255),
        
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