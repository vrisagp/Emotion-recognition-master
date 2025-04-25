from db_connection import get_connection

# Function to drop all tables from the database
def drop_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''DROP TABLE IF EXISTS Tourists''')
    cursor.execute('''DROP TABLE IF EXISTS Destinations''')
    cursor.execute('''DROP TABLE IF EXISTS Tours''')
    cursor.execute('''DROP TABLE IF EXISTS Bookings''')
    cursor.execute('''DROP TABLE IF EXISTS Payments''')
    cursor.execute('''DROP TABLE IF EXISTS Reviews''')
    cursor.execute('''DROP TABLE IF EXISTS Promotions''')
    cursor.execute('''DROP TABLE IF EXISTS TourPromotions''')
    cursor.execute('''DROP TABLE IF EXISTS Packages''')
    cursor.execute('''DROP TABLE IF EXISTS PackageDetails''')
    cursor.execute('''DROP TABLE IF EXISTS Guides''')
    cursor.execute('''DROP TABLE IF EXISTS GuideDetails''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print("Tables dropped successfully.")
