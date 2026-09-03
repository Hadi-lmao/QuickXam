from database.schema import initialize_database

def main():
    initialize_database()
    print("QuickXam database initialized successfully.")

if __name__ == "__main__":
    main()