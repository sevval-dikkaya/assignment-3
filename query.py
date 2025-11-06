import sqlite3

with sqlite3.connect('concrete.db') as conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 1. SHOW ALL TESTS


    # 2. Show ONLY failed tests


    # 3. Count tests by project
