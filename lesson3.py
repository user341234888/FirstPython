import mysql.connector

try:
    sql_connection = mysql.connector.connect(
        user='sql11665821', password='KbaxUxvqBS',
        host='sql11.freemysqlhosting.net', database='sql11665821')
except Exception as err:
    print(err)

try:
    query_str = 'insert into sql11665821.first_table (name1, number2) values ("hi dude", 1)'
    sql_cursor = sql_connection.cursor()
    sql_cursor.execute(query_str)

    # for (name1, number2) in sql_cursor:
    #     print(f'number: {number2} name: {name1}')
    sql_connection.close()
except Exception as err:
    print(err)
finally:
    sql_connection.close()
