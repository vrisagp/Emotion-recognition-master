from create_tables import create_tables
from drop_tables import drop_tables
from populate_tables import populate_tables
from query_tables import query_tables

# Function to display the main menu
def show_main_menu():
    print("\n=== Tourism Agency Booking System ===")
    print("1. Table Management")
    print("2. Data Queries")
    print("3. Exit")

# Function to display the table management menu
def show_table_management_menu():
    print("\n=== Table Management ===")
    print("1. Create Tables")
    print("2. Drop Tables")
    print("3. Populate Tables")
    print("4. Back to Main Menu")

# Function to display the data queries menu
def show_data_queries_menu():
    print("\n=== Data Queries ===")
    print("1. Query Tourists")
    print("2. Query Tours")
    print("3. Query Payments")
    print("4. Back to Main Menu")

def main():
    while True:
        show_main_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            while True:
                show_table_management_menu()
                table_choice = input("Enter your choice (1-4): ")

                if table_choice == '1':
                    create_tables()
                elif table_choice == '2':
                    drop_tables()
                elif table_choice == '3':
                    populate_tables()
                elif table_choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == '2':
            while True:
                show_data_queries_menu()
                query_choice = input("Enter your choice (1-4): ")

                if query_choice == '1':
                    query_tables()
                elif query_choice == '2':
                    query_tables()  # You can replace this with other specific queries
                elif query_choice == '3':
                    query_tables()  # You can replace this with other specific queries
                elif query_choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == '__main__':
    main()
