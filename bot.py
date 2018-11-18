#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import vk_api
import time
import json
import sys
import requests
import database as data

vk = vk_api.VkApi(token="d00a1318d5f9182d89e56612d1df321e3413ca74c2b6cb6a6fe443cb0782adbcbf089960703bfda62658b")
vk._auth_token()
WAIT_FILLING_POINTS = "-3"
WAIT_FILLING = "-2"
TEMP_FILLING = "-1"


def get_button(label, color,payload=""):
    return{
        "action":{
            "type":"text",
            "payload":json.dumps(payload),
            "label":label
        },
        "color": color
    }

def add_subject(id,connection,field,know_points):
    if data.get_field(connection=connection, table_name="Status",select_field="status", field="id_vk", value=id)[0]==True:
        if know_points=="yes":
            vk.method("messages.send", {"user_id": id, "message": "Введи баллы:"}) #убрал клавиатуру, тк можно нажать Главное меню и в базе останется -2
            data.set_field(connection=connection, table_name="Graduates", ID_VK=id, field=field, value=WAIT_FILLING)
        else:
            vk.method("messages.send", {"user_id": id, "message": "Выбор сделан", "keyboard":keyboard_exams}) #убрал клавиатуру, тк можно нажать Главное меню и в базе останется -2
            data.set_field(connection=connection, table_name="Graduates", ID_VK=id, field=field, value=TEMP_FILLING)
    else:
        vk.method("messages.send", {"user_id": id, "message": 'Предмет добавлен в список', "keyboard":keyboard_exams})
        data.set_field(connection=connection, table_name="Schoolchildren", ID_VK=id, field=field, value=True)

def search_subject(id,connection,table_name,flag):
    mas=["russian","math","biology","geography","foreign_language","informatics","history","literature","social_science","physics","chemistry"]
    for i in mas:
        if data.get_field(connection=connection, table_name=table_name,select_field=i,field="id_vk", value=id)[0]==int(flag):
            return i
    return 0

def use_menu(status):
    if status==True:
        vk.method("messages.send", {"user_id": id, "message": "Выбери нужную функцию", "keyboard":keyboard_menu_enrollee})
    else:
        vk.method("messages.send", {"user_id": id, "message": "Выбери нужную функцию", "keyboard":keyboard_menu_schoolchild})

def use_exams():
    vk.method("messages.send", {"user_id": id, "message": "Выбери нужный предмет", "keyboard":keyboard_exams})

def use_cabinet(status):
    if status==True:
        vk.method("messages.send", {"user_id": id, "message": "Выбери нужную функцию", "keyboard":keyboard_cabinet_enrollee})
    else:
        vk.method("messages.send", {"user_id": id, "message": "Выбери нужную функцию", "keyboard":keyboard_cabinet_schoolchild})

def use_data():
    vk.method("messages.send", {"user_id": id, "message": "Выбери нужную функцию", "keyboard":keyboard_data})

def info_about_nstu():
    try:
        str = open('/home/Main/Project/git/bot/info_files/about_nstu.txt', 'r')
    except IOError:
        vk.method("messages.send", {"user_id": id, "message": "Оу... Кажется у нас проблемы, попробуйте позже.", "keyboard":keyboard_default})
    finally:
        data_file = str.read()
        str.close()
        vk.method("messages.send", {"user_id": id, "message": data_file, "keyboard":keyboard_default})

def subscribe():
    if data.get_field(connection=connection, table_name="Status",select_field="subscribe", field="id_vk", value=id)[0]==False:
        data.set_field(connection = connection, table_name = "Status", ID_VK = id, field = "subscribe", value = "1")
        vk.method("messages.send", {"user_id": id, "message": "Теперь ты подписан на уведомления"})
    else:
        data.set_field(connection = connection, table_name = "Status", ID_VK = id, field = "subscribe", value = "0")
        vk.method("messages.send", {"user_id": id, "message": "Теперь ты отписан от уведомлений"})
    use_menu(status=data.get_field(connection=connection, table_name="Status",select_field="subscribe", field="id_vk", value=id)[0])

def other_event(msg):
    if data.get_field(connection=connection, table_name="Graduates",select_field="name", field="id_vk", value=id)[0]=="-2":#обрабатываем ФИО
        msg="'"+msg+"'"
        data.set_field(connection = connection, table_name = "Graduates", ID_VK = id, field = "name", value = msg)
        vk.method("messages.send", {"user_id": id, "message": "ФИО сохранены"})
        use_cabinet(status=True)
    elif data.get_field(connection=connection, table_name="Status",select_field="status", field="id_vk", value=id)[0]==1 and search_subject(id=id,connection=connection,table_name="Graduates",flag=WAIT_FILLING)!=0:#обрабатываем баллы
        try:
            points=int(msg)
        except:
            vk.method("messages.send", {"user_id": id, "message": "Баллы введены не верно"})
            data.set_field(connection=connection, table_name="Graduates", ID_VK=id, field=search_subject(id=id,connection=connection,table_name="Graduates",flag=WAIT_FILLING), value=0)
            use_exams()
        finally:
            if points>=0 and points <=100:
                data.set_field(connection=connection, table_name="Graduates", ID_VK=id, field=search_subject(id=id,connection=connection,table_name="Graduates",flag=WAIT_FILLING), value=msg)
                vk.method("messages.send", {"user_id": id, "message": "Баллы учтены"})
            else:
                vk.method("messages.send", {"user_id": id, "message": "Баллы введены не верно"})
                data.set_field(connection=connection, table_name="Graduates", ID_VK=id, field=search_subject(id=id,connection=connection,table_name="Graduates",flag=WAIT_FILLING), value=0)
            use_exams()
   #elif: #обрабатываем код направления
    else:
        vk.method("messages.send", {"user_id": id, "message": "Используй клавиатуру. Я тебя не понимаю"})
        use_menu(status=data.get_field(connection=connection, table_name="Status",select_field="status", field="id_vk", value=id)[0])

#def select_direction(field, id):


connection=data.connect()
#print(connection)
keyboard_start={
    "one_time": True,
    "buttons":[
        [get_button(label="Я выпускник",color="default", payload="enrollee")],
        [get_button(label="Я учусь в школе",color="default",payload="schoolchild")]
    ]
}

keyboard_menu_enrollee={
    "one_time": True,
    "buttons":[
        [get_button(label="Узнать информацию",color="default",payload="information")],
        [get_button(label="Личный кабинет",color="default",payload="cabinet")],
        [get_button(label="Подписаться/отписаться",color="default",payload="subscribe")]
    ]
}

keyboard_info={
    "one_time": True,
    "buttons":[
        [
            get_button(label="О НГТУ",color="default",payload="about_nstu"),
            get_button(label="Факультеты/Направления",color="default",payload="faculties"),
            get_button(label="??",color="default",payload="")
        ],
        [
            get_button(label="???",color="default",payload=""),
            get_button(label="???",color="default",payload=""),
            get_button(label="???",color="default",payload=""),
        ],
        [
            get_button(label="???",color="default",payload=""),
            get_button(label="???",color="default",payload=""),
            get_button(label="???",color="default",payload="")
        ],
        [get_button(label="Главное меню",color="primary",payload="main_menu")]
    ]
}

keyboard_cabinet_enrollee={
    "one_time": True,
    "buttons":[
        [get_button(label="Личные данные",color="default",payload="personal_info")],
        [get_button(label="Посмотреть место в списках",color="default",payload="position_in_list")],
        [get_button(label="Подбор направления",color="default",payload="direction_selection")],
        [get_button(label="Главное меню",color="primary",payload="main_menu")]
    ]
}

keyboard_data={
    "one_time": True,
    "buttons":[
        [get_button(label="ФИО",color="default",payload="name")],
        [get_button(label="Баллы за ЕГЭ",color="default",payload="exam_points")],
        [get_button(label="Дополнительная информация",color="default",payload="other_information")],
        [
            get_button(label="Назад",color="primary",payload="cabinet"),
            get_button(label="Главное меню",color="primary",payload="main_menu")
        ]
    ]
}

keyboard_direction_selection={
    "one_time": True,
    "buttons":[
        [get_button(label="По предметам",color="default",payload="name")], #keyboard_data already contained payload "name"
        [get_button(label="По сфере",color="default",payload="sphere")],
        [get_button(label="Главное меню",color="primary",payload="main_menu")]
    ]
}

keyboard_exams={
    "one_time": True,
    "buttons":[
        [
            get_button(label="Русский язык",color="default",payload="russian"),
            get_button(label="Математика",color="default",payload="math")
        ],
        [
            get_button(label="Биология",color="default",payload="biology"),
            get_button(label="География",color="default",payload="geography"),
            get_button(label="Иностранный язык",color="default",payload="foreign_language")
        ],
        [
            get_button(label="Информатика",color="default",payload="informatics"),
            get_button(label="История",color="default",payload="history"),
            get_button(label="Литература",color="default",payload="literature")
        ],
        [
            get_button(label="Обществознание",color="default",payload="social_science"),
            get_button(label="Физика",color="default",payload="physics"),
            get_button(label="Химия",color="default",payload="chemistry")
        ],
        [
            get_button(label="Назад",color="primary",payload="personal_info"),
            get_button(label="Главное меню",color="primary",payload="main_menu")
        ]
    ]
}

keyboard_menu_schoolchild={
    "one_time": True,
    "buttons":[
        [get_button(label="Узнать информацию",color="default",payload="information")],
        [get_button(label="Подобрать напрваление",color="default",payload="direction_selection_schoolchild")],
        [get_button(label="Подписаться/отписаться",color="default",payload="subscribe")],
    ]
}

keyboard_cabinet_schoolchild={
    "one_time": True,
    "buttons":[
        [get_button(label="Личные данные",color="default",payload="personal_info")],
        [get_button(label="Посмотреть место в списках",color="default",payload="position_in_list")],
        [get_button(label="???",color="default",payload="")],
        [get_button(label="Главное меню",color="primary",payload="main_menu")]
    ]
}

keyboard_know_points={
    "one_time": True,
    "buttons":[
        [
            get_button(label="Да",color="primary",payload="yes"),
            get_button(label="Нет",color="primary",payload="no")
        ]

    ]
}

keyboard_sphere={
    "one_time": True,
    "buttons":[
        [
            get_button(label="Машиностроение",color="default",payload="Машиностроение"),
            get_button(label="Безопасность",color="default",payload="Безопасность")
        ],
        [
            get_button(label="Энергетика",color="default",payload="Энергетика"),
            get_button(label="IT",color="default",payload="IT-технологии"),
            get_button(label="Электроника",color="default",payload="Электроника")
        ],
        [
            get_button(label="Авиация",color="default",payload="Авиация"),
            get_button(label="Общество",color="default",payload="Общество"),
            get_button(label="Экономика",color="default",payload="Экономика")
        ],
        [
            get_button(label="Химия",color="default",payload="Химия"),
            get_button(label="Языки",color="default",payload="Языки"),
            get_button(label="Физика",color="default",payload="Физика")
        ],
        [
            get_button(label="Назад",color="primary",payload="direction_selection"),
            get_button(label="Главное меню",color="primary",payload="main_menu")
        ]
    ]
}

keyboard_default={
    "one_time": True,
    "buttons":[[get_button(label="Главное меню",color="primary",payload="main_menu")]]
}

keyboard_null={
    "one_time": True,
    "buttons":[[get_button(label="Начать",color="primary",payload="admin")]]
}

#я выпускник/школьник
keyboard_start = json.dumps(keyboard_start, ensure_ascii = False)
#меню выпускника
keyboard_menu_enrollee = json.dumps(keyboard_menu_enrollee, ensure_ascii = False)
#меню школьника
keyboard_menu_schoolchild = json.dumps(keyboard_menu_schoolchild, ensure_ascii = False)
#меню информации
keyboard_info = json.dumps(keyboard_info, ensure_ascii = False)
keyboard_know_points=json.dumps(keyboard_know_points, ensure_ascii = False)
keyboard_cabinet_enrollee = json.dumps(keyboard_cabinet_enrollee, ensure_ascii = False)
keyboard_cabinet_schoolchild = json.dumps(keyboard_cabinet_schoolchild, ensure_ascii = False)
keyboard_data = json.dumps(keyboard_data, ensure_ascii = False)
keyboard_exams = json.dumps(keyboard_exams, ensure_ascii=False)
keyboard_default = json.dumps(keyboard_default, ensure_ascii = False)
keyboard_null = json.dumps(keyboard_null, ensure_ascii = False)
keyboard_sphere = json.dumps(keyboard_sphere, ensure_ascii = False)
keyboard_direction_selection = json.dumps(keyboard_direction_selection,ensure_ascii = False)

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 100, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            msg = messages["items"][0]["last_message"]["text"]
            if "payload" in messages["items"][0]["last_message"]:
                pay = messages["items"][0]["last_message"]["payload"][1:-1]
            else:
                pay = "0"
            print(pay)
            if data.search_field(table_name="Status",connection=connection,value=id, field="id_vk")==False:
                data.set_user(table_name="Status", connection=connection,ID_VK=id)
            if pay=={"command":"start"} or pay == "admin":
                vk.method("messages.send", {"user_id": id, "message": "Привет! Чем я могу тебе помочь?", "keyboard":keyboard_start})
            elif msg=="admin":
                vk.method("messages.send", {"user_id": id, "message": "Начинаю с начала:", "keyboard":keyboard_null})
            elif pay=="enrollee":
                data.set_field(connection=connection, table_name="Status", ID_VK=id, field="status", value="True")
                data.set_user(table_name="Graduates", connection=connection,ID_VK=id)
                use_menu(status=True)
            elif pay=="schoolchild":
                data.set_field(connection=connection, table_name="Status", ID_VK=id, field="status", value="False")
                data.set_user(table_name="Schoolchildren", connection=connection,ID_VK=id)
                use_menu(status=False)
            elif pay=="information":
                vk.method("messages.send", {"user_id": id, "message": "Что ты хочешь узнать?", "keyboard":keyboard_info})
            elif pay=="cabinet":
                use_cabinet(status=data.get_field(connection=connection, table_name="Status",select_field="status", field="id_vk", value=id)[0])
            elif pay=="personal_info":
                use_data()
            elif pay=="exam_points":
                use_exams()
            elif pay=="main_menu":
                use_menu(status=(data.get_field(connection=connection, table_name="Status",select_field="status", field="id_vk", value=id))[0])
            elif pay=="biology" or pay=="geography" or pay=="foreign_language" or pay=="informatics" or pay=="history" or pay=="literature" or pay=="social_science" or pay=="physics" or pay=="chemistry" or pay=="russian" or pay=="math":
                vk.method("messages.send", {"user_id": id, "message": "Знаешь ли ты свои баллы?", "keyboard":keyboard_know_points})
                data.set_field(connection = connection, table_name = "Graduates", ID_VK = id, field = pay, value = WAIT_FILLING_POINTS)
            elif pay=="direction_selection":
                vk.method("messages.send", {"user_id": id, "message": "Как подобрать напрваление?", "keyboard":keyboard_direction_selection})
            elif pay=="sphere":
                vk.method("messages.send", {"user_id": id, "message": "Выберите сферу:", "keyboard":keyboard_sphere})
            elif pay=="Машиностроение" or pay=="Безопасность" or pay=="Энергетика" or pay=="IT-технологии" or pay=="Электроника" or pay=="Авиация" or pay=="Общество" or pay=="Экономика" or pay=="Химия" or pay=="Языки" or pay=="Физика":
                sphere = get_field(select_field = "SPHERE",table_name = "Sphere",connection= connection,value=pay, field="NAME_SPHERE")
            elif pay=="yes" or pay=="no":
                str=search_subject(id=id,connection=connection,table_name="Graduates",flag=WAIT_FILLING_POINTS)
                #print(str)
                if str!=0:
                    add_subject(id=id,connection=connection,field=str, know_points=pay)
            elif pay=="subscribe":
                subscribe()
            elif pay == "about_nstu":
                info_about_nstu()
            elif pay=="name":
                data.set_field(connection = connection, table_name = "Graduates", ID_VK = id, field = "name", value = WAIT_FILLING)
                vk.method("messages.send", {"user_id": id, "message": "Введите свое ФИО:"})
            elif pay=='"position_in_list"':
                vk.method("messages.send", {"user_id": id, "message": "Введите код напрваления"})
                vk.method("messages.send", {"user_id": id, "message": "Посмотреть его можно на https://www.nstu.ru/enrollee/exams"})
            else:
                other_event(msg=msg)

    except Exception:
        time.sleep(0.1)
