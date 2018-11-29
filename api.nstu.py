import requests
import json
import database as data
import getter
#sphere disc2 disc3
connection = data.connect()
subjects = {'Математика': "math",
'Биология': "biology",
'История': "history",
'Иностранный язык': "foreign_language",
'Литература': "literature",
'Информатика': "informatics",
'География': "geography",
'Физика': "physics",
'Химия': "chemistry",
'Обществознание': "social_science",
'Иностр. яз.': "foreign_language"}
def get_field(table_name,field1, field2, value):
    with connection.cursor() as cursor:
        sql = "SELECT " + field1 + " FROM " + table_name + " WHERE " + field2 + " = %s"
        print(sql)
        print(value)
        str = cursor.execute(sql,(value))
        print("////////////////////////////////////////")
        return list(cursor.fetchone())[0]
def search_field(table_name, field, value):
    if value != None:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Sphere WHERE + '" + str(field) + "' = " +"'"+ str(value)+"'"
            s = cursor.execute(sql)
            if s==0:
                return False
            else:
                return True
    else:
        return True
def set_line(table_name, values):
    print(values)
    res = 0
    if values["BALL_K"] == None:
        values["BALL_K"] = 0
    if values["BALL_B"] == None:
        values["BALL_B"] = 0
    if values["DESCR"] == None:
        values["DESCR"] = "null"
    if values["PROFILE_NAME"]==None:
        values["PRPFILE_NAME"] = "null"
    if values["data"][0]["SPHERE"] != None:
        for val in values["data"]:
            sphere = get_field("Sphere","SPHERE","NAME_SPHERE",val["SPHERE"])
            res = res*100 + sphere
    disc2 = get_field("DISC2","DISC2","NAME_SUB",subjects[values["DISC2"]])
    disc3 = get_field("DISC3","DISC3","NAME_SUB",subjects[values["DISC3"]])
    with connection.cursor() as cursor:
            if search_field("Directions", "ID_DIR", values["ID"]) == False:
                sql = "INSERT INTO " + table_name + "(DESCR, PROFILE_NAME, ID_DIR, FACULT, KEYS_PLUS, DIRECTION, SPHERE, DISC2, DISC3, BALL_K, BALL_B, URL) VALUES ( "+","+str(values['DESCR'])+"'"+", "+"'"+str(values['PROFILE_NAME'])+"'"+", "+str(values['ID']) +", '"+str(values['FACULT']) +"', "+" '"+str(values['KEYS_PLUS']) + "', " + " '"+ str(values['DIRECTION'])+"', "+str(res)+", "+str(disc2)+", "+str(disc3)+", "+" "+str(values['BALL_K'])+", "+" "+str(values['BALL_B']) +", "+" '"+"abc'"+")"
                print(sql)
                cursor.execute(sql)
                connection.commit()
            '''else:
                val = get_field("Directions","SPHERE","ID_DIR",values["ID"])
                val = val*100+values["SPHEPE"]
                sql = "UPDATE "+table_name+" SET SPHERE = '"+str(val)+"' WHERE ID_DIR = '" + str(values["ID"]) + "'"
                cursor.execute(sql)
                connection.commit()'''

def main():
    url = getter.get_nstu_url()
    html = requests.get(url)
    text = html.text
    text = bytes(text, 'utf-8').decode('unicode-escape')
    api = json.loads(text)
    i = 1
    for item in api:
            set_line("Directions",item)

if __name__== '__main__':
    main()
