class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        # if no instance is created , then create one
        if cls._instance is None:
            cls._instance = super(DatabaseConnection,cls).__new__(cls)
            print("New Database Connection is Created!")
        return cls._instance
    
#Testing
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(f"is db1 and db2 is same? {db1 is db2}")





















