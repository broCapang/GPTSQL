from flask import Flask, render_template, request
from nlp import nlp
import sqlite3
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    connection = sqlite3.connect("test.db")
    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Drop each table
    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table[0]}")

    # Define the SQL command to create the table
    create_table_sql = """
    CREATE TABLE staff (
        staff_id INTEGER PRIMARY KEY,
        staff_first_name TEXT,
        staff_last_name TEXT
    );
    """
    # Execute the SQL command to create the table
    cursor.execute(create_table_sql)

    create_table_sql = """
    CREATE TABLE student (
        student_id INTEGER PRIMARY KEY,
        student_first_name TEXT,
        student_last_name TEXT,
        student_department TEXT
    );
    """
    # Execute the SQL command to create the table
    cursor.execute(create_table_sql)
    # Commit the changes to the database
    connection.commit()
    if request.method == 'POST':
        text_input = request.form['text_input']
        
        return render_template('index.html', text_input=nlp(text_input))
    else:
        return render_template('index.html')

if __name__ == '__main__':

    app.run(debug=True)
