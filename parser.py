import requests
from bs4 import BeautifulSoup

#https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4052
def get_html(faculty, direction):
    #FACE - Faculty of automation and computer engineering (АВТФ)
        #FACE_1 - Software for computer systems and networks
        #FACE_2 - Networked information technology
        #FACE_3 - Information systems in industry and business
        #FACE_4 - Software development technologies
        #FACE_5 - Complex protection of Informatization objects
        #FACE_6 - Information security of automated systems of critical objects
        #FACE_7 - Information and measuring technologies
        #FACE_8 - Bioengineering and robot systems
        #FACE_9 - Automation and control
        #FACE_10 - Applied Informatics in Economics
    if faculty == "FACE":
        if direction == "FACE_1":
            return requests.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=3983").text
        elif direction == "FACE_2":
            return  requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4014").text
        elif direction == "FACE_3":
            return  requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=3984").text
        elif direction == "FACE_4":
            return  requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=3985").text
        elif direction == "FACE_5":
            return  requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=3986").text
        elif direction == "FACE_6":
            return  requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=3987").text
        elif direction == "FACE_7":
            return  requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=3988").text
        elif direction == "FACE_8":
            return  requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=3989").text
        elif direction == "FACE_9":
            return  requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=3990").text
        elif direction == "FACE_10":
            return  requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=3991").text
    #FA - Faculty of aircraft (ФЛА)
        #FA_1 - Ecological safety
        #FA_2 - Dynamics and strength
        #FA_3 - Climate and refrigeration equipment
        #FA_4 - Autonomous control systems of the means of destruction
        #FA_5 - Ammunition
        #FA_6 - Safety of technological processes and production
        #FA_7 - Environmental engineering
        #FA_8 - Aerohydrodynamics
        #FA_9 - Aircraft and helicopter
        #FA_10 - Life support systems and aircraft equipment
        #FA_11 - Maintenance of aircraft and aircraft engines
        #FA_12 - Autonomous information and control systems
    if faculty == "FA":
        if direction == "FA_1":
            return requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4032").text
        elif direction == "FA_2":
            return requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4034").text
        elif direction == "FA_3":
            return requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4035").text
        elif direction == "FA_4":
            return requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4036").text
        elif direction == "FA_5":
            return requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4037").text
        elif direction == "FA_6":
            return requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4038").text
        elif direction == "FA_7":
            return requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4040").text
        elif direction == "FA_8":
            return requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4041").text
        elif direction == "FA_9":
            return requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4042").text
        elif direction == "FA_10":
            return requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4043").text
        elif direction == "FA_11":
            return requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4044").text
        elif direction == "FA_12":
            return requsts.get("https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4045").text


def get_html_by_url(url):
    res = requests.get(url)
    return res.text

def get_position_in_list_by_name(html, name):
    soup = BeautifulSoup(html, 'lxml')
    persons = soup.find_all('td', class_ = 'tdbr')
    for person in persons:
        if person.text == name:
            for i in range(0,5):
                person = person.previous
            return person

def main():
    #res = get_html('https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4052')
    #person = get_position_in_list_by_name(res, "Гладких Иван Евгеньевич")
    a = '(1,)'
    print(a)
    print(a[0])


if __name__== '__main__':
    main()
