import sqlite3

# Create connection to concrete.db
with sqlite3.connect('concrete.db') as conn:
    cursor = conn.cursor()

    # Create the table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS concrete_tests (
            test_id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT,
            test_date TEXT,
            required_strength INTEGER,
            actual_strength INTEGER,
            passed INTEGER
        )
    ''')
    conn.commit()

print("Database created!")
