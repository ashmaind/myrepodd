import sqlite3

def get_user_data(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    data = cursor.fetchone()
    conn.close()
    
    return data

# Example usage
user_input = input("Enter your username: ")
user_data = get_user_data(user_input)
print(user_data)
