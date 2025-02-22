import connection_handler as ch


def update_user():
    # Create a connection handler instance
    connection_handler = ch.ConnectionHandler()
    try:
        # Establish the connection
        conn, cursor = connection_handler.get_connection()

        display_all_users(cursor)

        name = input('User to update ')
        new_name = input('New user name')

        # Insert data into the 'users' table
        cursor.execute(f"update users set name = '{new_name}' where name = '{name}'")
        conn.commit()
        print("User is updated in the 'users' table")

    except Exception as e:
        # If an exception occurs, rollback the transaction
        print(f"Error occurred: {e}")
        conn.rollback()

    finally:
        # Close the connection
        connection_handler.close_connection()


def display_all_users(cursor):
    cursor.execute('select * from users')
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()


update_user()
