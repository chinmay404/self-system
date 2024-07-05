import psycopg2

def create_table(conn, table_name):
    try:
        cursor = conn.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                word VARCHAR(255) PRIMARY KEY,
                meaning TEXT,
                pronunciation TEXT NULL,
                sentence1 TEXT NULL,
                sentence2 TEXT NULL,
                sentence3 TEXT NULL,
                sentence4 TEXT NULL,
                sentence5 TEXT NULL,
                type VARCHAR(50) NULL,
                notes TEXT NULL,
                added_date DATE DEFAULT CURRENT_DATE,
                last_seen_date DATE DEFAULT CURRENT_DATE,
                learned BOOLEAN DEFAULT TRUE,
                correct_answers INTEGER DEFAULT 0,
                incorrect_answers INTEGER DEFAULT 0,
                last_tested_date DATE NULL,
                tags TEXT NULL  -- Added tags field
            );
        """)

        try:
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f'Error in commit: {e}')
            return False

    except Exception as e:
        print(f'Error in create_table: {e}')
        return False
