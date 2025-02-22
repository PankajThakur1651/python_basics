import connection_handler as ch

# Create a connection handler instance
connection_handler = ch.ConnectionHandler()


def create_user(user="Pankaj", age=35):
    try:
        # Establish the connection
        conn, cursor = connection_handler.get_connection()
        # Insert data into the 'users' table
        cursor.execute(f"INSERT INTO users (name, age) VALUES('{user}', '{age}')")
        conn.commit()
        print("User is inserted into the 'users' table")

    except Exception as e:
        # If an exception occurs, rollback the transaction
        print(f"Error occurred: {e}")
        conn.rollback()

    finally:
        # Close the connection
        connection_handler.close_connection()


age =0
while 18 <= age <= 58:
    user = input('Add the user to add into users DB ')
    age = int(input(f'Add age of {user} to insert '))
    if 18 <= age <= 58:
        create_user(user, age)
