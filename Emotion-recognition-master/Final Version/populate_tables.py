from db_connection import get_connection

def populate_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Insert sample data into Tourists table
    tourists_data = [
        ('John', 'A.', 'Doe', '123-456-7890', 'john.doe@email.com', '123 Main St, Toronto, Canada', 'A1234567', 'Paris, Rome'),
        ('Jane', 'B.', 'Smith', '987-654-3210', 'jane.smith@email.com', '456 Oak St, Vancouver, Canada', 'B7654321', 'London, Tokyo'),
        ('Alice', 'C.', 'Johnson', '555-123-4567', 'alice.johnson@email.com', '789 Pine St, Montreal, Canada', 'C9876543', 'New York, Sydney'),
        ('Bob', 'D.', 'Williams', '666-234-5678', 'bob.williams@email.com', '101 Maple St, Ottawa, Canada', 'D6543210', 'Paris, Berlin'),
        ('Charlie', 'E.', 'Brown', '777-345-6789', 'charlie.brown@email.com', '202 Birch St, Calgary, Canada', 'E3217654', 'Rome, Bangkok'),
    ]
    cursor.executemany('''
    INSERT INTO Tourists (FirstName, MiddleName, LastName, PhoneNumber, Email, Address, PassportNumber, PreferredDestinations)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', tourists_data)

    # Insert sample data into Destinations table
    destinations_data = [
        (1, 'Paris', 'France'),
        (2, 'Rome', 'Italy'),
        (3, 'London', 'UK'),
        (4, 'Tokyo', 'Japan'),
        (5, 'New York', 'USA'),
    ]
    cursor.executemany('''
    INSERT INTO Destinations (DestinationID, Name, Location)
    VALUES (?, ?, ?)
    ''', destinations_data)

    # Insert sample data into Tours table
    tours_data = [
        (1, 1, 500.00, 7, 30),
        (2, 2, 600.00, 5, 20),
        (3, 3, 700.00, 10, 25),
        (4, 4, 800.00, 8, 15),
        (5, 5, 900.00, 12, 50),
    ]
    cursor.executemany('''
    INSERT INTO Tours (TourID, DestinationID, Price, Duration, AvailableSlots)
    VALUES (?, ?, ?, ?, ?)
    ''', tours_data)

# Insert sample data into Bookings table
    bookings_data = [
    (1, 1, 1, 2, 1000.00),  # BookingID, TourID, TouristID, NumberOfParticipants, TotalCost
    (2, 2, 2, 1, 600.00),
    (3, 3, 3, 4, 2800.00),
    (4, 4, 4, 3, 2400.00),
    (5, 5, 5, 5, 4500.00),
]
    cursor.executemany('''
INSERT INTO Bookings (BookingID, TourID, TouristID, NumberOfParticipants, TotalCost)
VALUES (?, ?, ?, ?, ?)
''', bookings_data)


    # Insert sample data into Payments table
    payments_data = [
    (1, 1, 'Credit Card', 1000.00, 'Completed'),
    (2, 2, 'Debit Card', 600.00, 'Pending'),
    (3, 3, 'PayPal', 2800.00, 'Completed'),
    (4, 4, 'Credit Card', 2400.00, 'Completed'),
    (5, 5, 'Cash', 4500.00, 'Pending'),
]
    cursor.executemany('''
INSERT INTO Payments (PaymentID, BookingID, PaymentMethod, Amount, PaymentStatus)
VALUES (?, ?, ?, ?, ?)
''', payments_data)

   
    # Insert sample data into Reviews table
    reviews_data = [
        (1, 1, 1, 5, 'Amazing experience, would love to come back!', '2024-11-01'),
        (2, 2, 2, 4, 'Great food and sightseeing, but a bit rushed.', '2024-11-05'),
        (3, 3, 3, 5, 'The best tour ever! Loved every moment of it.', '2024-11-10'),
        (4, 4, 4, 3, 'Good, but the weather wasn’t great during the tour.', '2024-11-12'),
        (5, 5, 5, 4, 'Enjoyed it a lot, but a bit more time could be given for shopping.', '2024-11-15'),
    ]
    cursor.executemany('''
    INSERT INTO Reviews (ReviewID, TouristID, DestinationID, Rating, Comments, ReviewDate)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', reviews_data)

    # Insert sample data into Promotions table
    promotions_data = [
        (1, 'Summer Sale', 20, 'Tour 1, Tour 2'),
        (2, 'Winter Discount', 15, 'Tour 3, Tour 4'),
        (3, 'Holiday Special', 10, 'Tour 5'),
    ]
    cursor.executemany('''
    INSERT INTO Promotions (PromotionID, Description, DiscountPercentage, ApplicableTours)
    VALUES (?, ?, ?, ?)
    ''', promotions_data)

    # Insert sample data into TourPromotions table
    tour_promotions_data = [
        (1, 1),
        (2, 2),
        (3, 3),
    ]
    cursor.executemany('''
    INSERT INTO TourPromotions (TourID, PromotionID)
    VALUES (?, ?)
    ''', tour_promotions_data)

    # Insert sample data into Packages table
    packages_data = [
        ('Luxury Tour', 1000.00, 1),
        ('City Break', 600.00, 2),
        ('Adventure Tour', 1200.00, 3),
        ('Relaxing Vacation', 1500.00, 4),
        ('Holiday Package', 1800.00, 5),
    ]
    cursor.executemany('''
    INSERT INTO Packages (package_name, price, destination_id)
    VALUES (?, ?, ?)
    ''', packages_data)

    # Insert sample data into PackageDetails table
    package_details_data = [
        (1, '5-star hotel stay, private guide, and luxury transport'),
        (2, '2-day city tour, free meals, and airport transfers'),
        (3, 'Mountain trekking, camping, and guided nature tour'),
        (4, 'Beach resort stay, spa treatment, and all-inclusive services'),
        (5, 'Guided shopping tour, cultural experiences, and sightseeing'),
    ]
    cursor.executemany('''
    INSERT INTO PackageDetails (package_id, detail)
    VALUES (?, ?)
    ''', package_details_data)

    # Insert sample data into Guides table
    guides_data = [
        ('John Smith', 'English, French'),
        ('Alice Brown', 'English, Spanish'),
        ('David Green', 'German, English'),
        ('Maria White', 'Italian, English'),
        ('Emily Black', 'Chinese, English'),
    ]
    cursor.executemany('''
    INSERT INTO Guides (name, language_expertise)
    VALUES (?, ?)
    ''', guides_data)

    # Insert sample data into GuideDetails table
    guide_details_data = [
        (1, 'Expert in historical tours with 10+ years of experience'),
        (2, 'Fluent in multiple languages, specializes in city tours'),
        (3, 'Has experience in both rural and urban tours for over 5 years'),
        (4, 'Specializes in art history and architecture tours'),
        (5, 'Known for nature and cultural immersion tours with high ratings'),
    ]
    cursor.executemany('''
    INSERT INTO GuideDetails (guide_id, experience_level)
    VALUES (?, ?)
    ''', guide_details_data)

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print("Tables populated successfully.")
