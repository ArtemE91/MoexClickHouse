from database.connection import client


if __name__ == "__main__":
    result = client.query('SELECT * FROM records')
    print(result.result_rows)
