from db_connection import get_connection

# Function to create the required tables in the database
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Create Tourists Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tourists (
    TouristID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    MiddleName TEXT,
    LastName TEXT,
    PhoneNumber TEXT,
    Email TEXT,
    Address TEXT,
    PassportNumber TEXT,
    PreferredDestinations TEXT
)
''')

    # Create Destinations Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Destinations (
        DestinationID INTEGER PRIMARY KEY,
        Name TEXT,
        Location TEXT
    )
    ''')

    # Create Tours Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tours (
        TourID INTEGER PRIMARY KEY,
        DestinationID INTEGER,
        Price REAL,
        Duration INTEGER,
        AvailableSlots INTEGER,
        FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID)
    )
    ''')

    # Create Bookings Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Bookings (
        BookingID INTEGER PRIMARY KEY,
        TourID INTEGER,
        TouristID INTEGER,
        NumberOfParticipants INTEGER,
        TotalCost REAL,
        FOREIGN KEY (TourID) REFERENCES Tours(TourID),
        FOREIGN KEY (TouristID) REFERENCES Tourists(TouristID)
    )
    ''')

    # Create Payments Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Payments (
        PaymentID INTEGER PRIMARY KEY,
        BookingID INTEGER,
        PaymentMethod TEXT,
        Amount REAL,
        PaymentStatus TEXT,
        FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID)
    )
    ''')

    # Create Reviews Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Reviews (
        ReviewID INTEGER PRIMARY KEY,
        TouristID INTEGER,
        DestinationID INTEGER,
        Rating INTEGER,
        Comments TEXT,
        ReviewDate TEXT,
        FOREIGN KEY (TouristID) REFERENCES Tourists(TouristID),
        FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID)
    )
    ''')

    # Create Promotions Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Promotions (
        PromotionID INTEGER PRIMARY KEY,
        Description TEXT,
        DiscountPercentage INTEGER,
        ApplicableTours TEXT
    )
    ''')

    # Create TourPromotions Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS TourPromotions (
        TourID INTEGER,
        PromotionID INTEGER,
        FOREIGN KEY (TourID) REFERENCES Tours(TourID),
        FOREIGN KEY (PromotionID) REFERENCES Promotions(PromotionID)
    )
    ''')

    # Create the 'Packages' table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Packages (
        package_id INTEGER PRIMARY KEY AUTOINCREMENT,
        package_name TEXT,
        price REAL,
        destination_id INTEGER,
        FOREIGN KEY (destination_id) REFERENCES Destinations(destination_id)
    )
    ''')

    # Create the 'PackageDetails' table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS PackageDetails (
        package_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
        package_id INTEGER,
        detail TEXT,
        FOREIGN KEY (package_id) REFERENCES Packages(package_id)
    )
    ''')

    # Create the 'Guides' table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Guides (
        guide_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        language_expertise TEXT,
        FOREIGN KEY (guide_id) REFERENCES Tours(tour_id)
    )
    ''')

    # Create the 'GuideDetails' table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS GuideDetails (
        guide_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
        guide_id INTEGER,
        experience_level TEXT,
        FOREIGN KEY (guide_id) REFERENCES Guides(guide_id)
    )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print("Tables created successfully.")
