import pandas as pd
import mysql.connector

# Load data from CSV
file_path = "content_data.csv"  # Replace with your actual file path
data = pd.read_csv(file_path)

# Database connection
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "your_mysql_password",
    "database": "gti_database"
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Insert data into content_table
for _, row in data.iterrows():
    cursor.execute(
        "INSERT INTO content_table (gti, task_id) VALUES (%s, %s)",
        (row["gti"], row["task_id"]),
    )

conn.commit()
print("Data imported successfully!")
cursor.close()
conn.close()
