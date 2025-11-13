import sqlite3

with sqlite3.connect('concrete.db') as conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT project_name, test_date, required_strength, actual_strength, passed FROM concrete_tests')
    # 1. SHOW ALL TESTS
    print("ALL TESTS")
    while row:= cursor.fetchone():
        project_name = row['project_name']
        test_date = row['test_date']
        required_strength = row['required_strength']
        actual_strength = row['actual_strength']
        passed = row['passed']
        if passed:
            passed = str("PASS")
        else:
            passed = str("FAIL")
        print (project_name + ": " + str(actual_strength) + " PSI - " + passed)


    # 2. Show ONLY failed tests
    cursor = conn.cursor()
    cursor.execute('''
        SELECT project_name, test_date, required_strength, actual_strength
        FROM concrete_tests
        WHERE passed = 0
    ''')
    print("\nFAILED TESTS")
    while row:= cursor.fetchone():
        project_name = row['project_name']
        test_date = row['test_date']
        required_strength = row['required_strength']
        actual_strength = row['actual_strength']

        print(project_name + " on " + test_date)
        print("  Required: " + str(required_strength) + " PSI")
        print("  Actual: " + str(actual_strength) + " PSI")
        print("")

    # 3. Count tests by project
    cursor = conn.cursor()
    cursor.execute('''
        SELECT project_name,
               SUM(CASE WHEN passed = 1 THEN 1 ELSE 0 END) AS passed_count,
               COUNT(*) AS total_count
        FROM concrete_tests
        GROUP BY project_name
        ORDER BY project_name
    ''')
    print("TESTS PER PROJECT")
    while row:= cursor.fetchone():
        project_name = row['project_name']
        passed_count = row['passed_count']
        total_count = row['total_count']
        print(project_name + ": " + str(passed_count) + "/" + str(total_count) + " passed")