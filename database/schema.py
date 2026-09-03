from database.connection import get_connection
def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()
    # QUESTIONS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            chapter TEXT,
            question_text TEXT NOT NULL,
            question_type TEXT NOT NULL,
            option_a TEXT,
            option_b TEXT,
            option_c TEXT,
            option_d TEXT,
            correct_option TEXT,
            marks REAL NOT NULL DEFAULT 1,
            negative_marks REAL NOT NULL DEFAULT 0
        )
    """)
    # TESTS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            subject TEXT,
            duration_minutes INTEGER NOT NULL,
            total_questions INTEGER NOT NULL,
            positive_marks REAL NOT NULL DEFAULT 1,
            negative_marks REAL NOT NULL DEFAULT 0,
            start_time TEXT,
            end_time TEXT,
            created_at TEXT NOT NULL
        )
    """)
    # TEST <--> QUESTION
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_questions (
            test_id INTEGER NOT NULL,
            question_id INTEGER NOT NULL,
            question_number INTEGER NOT NULL,
            PRIMARY KEY (test_id, question_id),
            FOREIGN KEY (test_id)
                REFERENCES tests(id)
                ON DELETE CASCADE,
            FOREIGN KEY (question_id)
                REFERENCES questions(id)
                ON DELETE CASCADE
        )
    """)
    # ATTEMPTS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_id INTEGER NOT NULL,
            started_at TEXT NOT NULL,
            submitted_at TEXT,
            score REAL NOT NULL DEFAULT 0,
            FOREIGN KEY (test_id)
                REFERENCES tests(id)
                ON DELETE CASCADE
        )
    """)
    # ANSWERS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS answers (
            attempt_id INTEGER NOT NULL,
            question_id INTEGER NOT NULL,
            selected_option TEXT,
            is_correct INTEGER NOT NULL DEFAULT 0,
            marks_awarded REAL NOT NULL DEFAULT 0,
            PRIMARY KEY (attempt_id, question_id),
            FOREIGN KEY (attempt_id)
                REFERENCES attempts(id)
                ON DELETE CASCADE,
            FOREIGN KEY (question_id)
                REFERENCES questions(id)
                ON DELETE CASCADE
        )
    """)
    connection.commit()
    connection.close()