import pymysql.cursors

def connect():
    #try:
        cnx = pymysql.connect(
            user='Main',
			password = 'Pasbot20!8',
            host = 'localhost',
            db='Users'
        )
        return cnx

def set_user(table_name,connection,ID_VK):
    if search_field(table_name, connection, ID_VK , "id_vk")==False:
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO " + table_name + " (id_vk) VALUES (%s)"
                print(sql)
                str = cursor.execute(sql,(ID_VK))
                connection.commit()
                return True
        except:
            return False
    else:
         return False

def search_field(table_name,connection,value, field):
        with connection.cursor() as cursor:
            sql = "SELECT * FROM " + table_name + " WHERE " + field + " = %s"
            str = cursor.execute(sql,(value))
            if str==0:
                return False
            else:
                return True

def get_field(connection,table_name,select_field,field,value):
        with connection.cursor() as cursor:
            sql = "SELECT " + select_field + " FROM " + table_name + " WHERE " + field + " = %s"
            cursor.execute(sql,(value))
            return list(cursor.fetchone())

def set_field(connection, table_name, ID_VK, field, value):
    with connection.cursor() as cursor:
        sql = "UPDATE " + table_name + " SET " + field + " = " + value + " WHERE id_vk = %s"
        str = cursor.execute(sql, (ID_VK))
        connection.commit()
def get_fields(connection,table_name,select_field,field,value):
    with connection.cursor() as cursor:
            sql = "SELECT " + select_field + " FROM " + table_name + " WHERE " + field + " = %s"
            cursor.execute(sql,(value))
            return list(cursor.fetchone())

#def get_field(connection, table_name, ID_VK, field):
#    with connection.cursor() as cursor:
#        sql = "SELECT " + field + " FROM " + table_name + " WHERE id_vk = %s"
#        cursor.execute(sql,(ID_VK))
#        return list(cursor.fetchone())[0]
