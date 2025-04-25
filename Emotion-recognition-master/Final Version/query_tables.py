from db_connection import get_connection
from tabulate import tabulate

# Function to query and display all tourists
def get_all_tourists(cursor):
    cursor.execute('SELECT * FROM Tourists')
    return cursor.fetchall()

# Function to update tourist details
def update_tourist_email(cursor, tourist_id, new_email):
    try:
        cursor.execute('''UPDATE Tourists SET Email = ? WHERE TouristID = ?;''', (new_email, tourist_id))
        if cursor.rowcount == 0:
            print(f"Error: No tourist found with ID {tourist_id}.")
            return
        cursor.connection.commit()
        print(f"Tourist ID {tourist_id}'s email updated to {new_email}.")
    except Exception as e:
        print(f"Error: {e}")

# Function to delete a tourist
def delete_tourist(cursor, tourist_id):
    try:
        cursor.execute('''DELETE FROM Tourists WHERE TouristID = ?;''', (tourist_id,))
        if cursor.rowcount == 0:
            print(f"Error: No tourist found with ID {tourist_id}.")
            return
        cursor.connection.commit()
        print(f"Tourist ID {tourist_id} deleted.")
    except Exception as e:
        print(f"Error: {e}")

# Function to search tourists by name
def search_tourists_by_name(cursor, name):
    cursor.execute('''SELECT * FROM Tourists WHERE FirstName || ' ' || LastName LIKE ?;''', ('%' + name + '%',))
    return cursor.fetchall()

# Function to get tours in a specific destination
def get_tours_by_destination(cursor, destination_name):
    cursor.execute('''SELECT Tours.TourID, Tours.Price, Tours.Duration
                      FROM Tours
                      JOIN Destinations ON Tours.DestinationID = Destinations.DestinationID
                      WHERE Destinations.Name = ?;''', (destination_name,))
    return cursor.fetchall()

# Function to get tourist bookings
def get_tourist_bookings(cursor):
    cursor.execute('''SELECT * FROM Bookings
                      JOIN Tourists ON Bookings.TouristID = Tourists.TouristID''')
    return cursor.fetchall()

# Function to get payments for bookings
def get_payments_for_bookings(cursor):
    cursor.execute('''SELECT Payments.PaymentID, Payments.Amount, Payments.PaymentStatus
                      FROM Payments
                      JOIN Bookings ON Payments.BookingID = Bookings.BookingID''')
    return cursor.fetchall()

# Function to display results in a user-friendly format
def display_results(title, data):
    print(f"\n{'='*40}")
    print(f"{title}:")
    if not data:
        print("No results found.")
    else:
        print(tabulate(data, headers="keys", tablefmt="pretty"))
    print(f"{'='*40}")

# Main function to handle user input and execute queries
def query_tables():
    conn = get_connection()
    cursor = conn.cursor()

    while True:
        print("\n=== Tourism Agency Booking System ===")
        print("1. Display all tourists")
        print("2. Update tourist email")
        print("3. Delete tourist")
        print("4. Search tourists by name")
        print("5. Get tours in a destination")
        print("6. View tourist bookings")
        print("7. View payments for bookings")
        print("8. Return to Main Menu")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            tourists = get_all_tourists(cursor)
            display_results("All Tourists", tourists)

        elif choice == '2':
            try:
                tourist_id = int(input("Enter Tourist ID to update: "))
                new_email = input("Enter new email address: ")
                update_tourist_email(cursor, tourist_id, new_email)
            except ValueError:
                print("Invalid input. Please enter a valid tourist ID.")

        elif choice == '3':
            try:
                tourist_id = int(input("Enter Tourist ID to delete: "))
                delete_tourist(cursor, tourist_id)
            except ValueError:
                print("Invalid input. Please enter a valid tourist ID.")

        elif choice == '4':
            name = input("Enter tourist name to search for: ")
            tourists = search_tourists_by_name(cursor, name)
            display_results(f"Search results for '{name}'", tourists)

        elif choice == '5':
            destination_name = input("Enter destination name to get tours: ")
            tours = get_tours_by_destination(cursor, destination_name)
            display_results(f"Tours in {destination_name}", tours)

        elif choice == '6':
            bookings = get_tourist_bookings(cursor)
            display_results("Tourist Bookings", bookings)

        elif choice == '7':
            payments = get_payments_for_bookings(cursor)
            display_results("Payments for Bookings", payments)

        elif choice == '8':
            break

        elif choice == '9':
            print("\nThank you for using the Tourism Agency system. Exiting...")
            break

        else:
            print("\nInvalid choice. Please try again.")

    conn.close()
