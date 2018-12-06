#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import json


class keyboard:
    def __init__(self):
        pass
    def get_button(label, color,payload=""):
    return{
        "action":{
            "type":"text",
            "payload":json.dumps(payload),
            "label":label
        },
        "color": color
    }
    def convertToString():
        keyboard = json.dumps(keyboard, ensure_ascii = False)
    keyboard

keyboard_start = keyboard()
keyboard_start.keyboard = {
    "one_time": True,
    "buttons":[
        [get_button(label="Начать",color="default", payload="admin")]
    ]
}
keyboard_start.convertToString()


keyboard_main_menu = keyboard()
keyboard_main_menu.keyboard = {
    "one_time": True,
    "buttons":[
        [get_button(label="Подписаться/отписаться",color="default",payload="subscribe")],
        [get_button(label="Подбор направления",color="default",payload="directions")],
        [get_button(label="Конкурсные списки",color="primary",payload="lists")]
    ]
}
keyboard_main_menu.convertToString()


keyboard_subscribe = keyboard()
keyboard_subscribe.keyboard={
    "one_time": True,
    "buttons":[
        [get_button(label="Для школьника",color="default", payload="schollchild")],
        [get_button(label="Для поступающего",color="default",payload="enrollee")]
    ]
}
keyboard_subscribe.convertToString()


keyboard_direction_selection = keyboard()
keyboard_direction_selection.keyboard = {
    "one_time": True,
    "buttons":[
        [get_button(label="По предметам",color="default",payload="name_dir")],
        [get_button(label="По сфере",color="default",payload="sphere")],
        [get_button(label="Главное меню",color="primary",payload="main_menu")]
    ]
}
keyboard_direction_selection.convertToString()

keyboard_list = keyboard()
keyboard_list.keyboard = {
    "one_time": True,
    "buttons":[
        [get_button(label="Ввести код из ЛК НГТУ",color="default",payload="lk_code")],
        [get_button(label="Частота уведомлений",color="default",payload="frequency")],
        [get_button(label="Главное меню",color="primary",payload="main_menu")]
    ]
}
keyboard_list.convertToString()


keyboard_sphere = keyboard()
keyboard_sphere.keyboard = {
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
            get_button(label="Главное меню",color="primary",payload="main_menu"),
            get_button(label = "Найти", color = "primary", payload = "search")
        ]
    ]
}
keyboard_sphere.convertToString()


keyboard_subjects = keyboard()
keyboard_subjects.keyboard = {
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
            get_button(label="Главное меню",color="primary",payload="main_menu")
        ]
    ]
}
keyboard_subjects.convertToString()


keyboard_frequency = keyboard()
keyboard_frequency.keyboard = {
    "one_time": True,
    "buttons":[
        [get_button(label="Один раз в день",color="default",payload="one_per_day")],
        [get_button(label="Два раза в день",color="default",payload="two_per_day")],
        [get_button(label="Один раз в два дня",color="primary",payload="one_per_two_day")]
    ]
}
keyboard_frequency.convertToString()