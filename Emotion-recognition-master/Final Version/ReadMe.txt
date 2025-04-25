Tourism Agency Booking System

Project Overview
The Tourism Agency Booking System is a Python-based application designed to manage tourist data, tours, bookings, payments, and related functionalities using a SQLite database. The system provides a command-line interface (CLI) for managing and querying tables such as tourists, destinations, tours, bookings, payments, and reviews.

Features
- Table Management: Create, drop, and populate tables in the SQLite database.
- Data Queries: Query tourist data, bookings, payments, and reviews.
- User Interaction: Simple CLI interface for interacting with the system.

System Design
The application is organized into several Python modules:
- db_connection.py: Manages database connections.
- create_tables.py: Creates necessary tables in the SQLite database.
- drop_tables.py: Drops all tables in the database.
- populate_tables.py: Populates the tables with sample data.
- query_tables.py: Contains functions to query data from the tables.
- main.py: The main script that integrates all the modules and provides the CLI interface for user interaction.

Installation Requirements
- Python 3.6 or higher.
- SQLite (usually included with Python).
- Tabulate (used for formatting output):
  ```
  pip install tabulate
  ```

Installation Steps
1. Clone or download the project repository.

2. Install dependencies:
   ```
   pip install tabulate
   ```
3. Run the system:
   - Navigate to the project folder and run the system:
   ```
   python main.py
   ```

 User Instructions
1. Launch the System:
   To start the application, use the following command:
   ```
   python main.py
   ```
   
2. Main Menu: Upon launching, the system will display the following menu:
   ```
   1. Table Management
   2. Data Queries
   3. Exit
   ```
   - Table Management: Create, drop, or populate tables as needed.
   - Data Queries: Search and view data about tourists, tours, bookings, payments, and reviews.
   - Exit: Exit the system.
