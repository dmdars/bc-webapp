from configparser import ConfigParser
import psycopg2

def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config

def connect():
    """ Connect to the PostgreSQL database server """
    try:
        config = load_config()
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def select_cmd(sql):
    try:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
        
        cur.close()
        conn.close()

        return rows
    except (psycopg2.DatabaseError, Exception) as e:
        print(e)
        return False
        

def insert_cmd(sql):
    try:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute(sql)
        
        conn.commit()
        cur.close()
        conn.close()

        return True
    except (psycopg2.DatabaseError, Exception) as e:
        print(e)
        return False

# if __name__ == '__main__':
#    add_user("test1","testing","test12@gmail.com","testing123")