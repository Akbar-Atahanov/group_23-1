import re

data = open('MOCK_DATA.txt', 'r')
content = data.read()
data.close()


class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def __str__(self):
        return f"emails - {email_mock}\n" \
               f" colors - {colors_mock} \n" \
               f"full_names - {full_name_mock} \n" \
               f"file_names - {file_name_mock}"
with open("MOCK_DATA.txt", "r", encoding='UTF-8') as file:
    file.read()
    colors_mock = re.findall(r"#[0-9A-Fa-f]{6}", content)
    with open("colors", "w", encoding='UTF-8') as file:
        for i in colors_mock:
            file.write(f"{i}\n")

    email_mock = re.findall(r"\b([\w\-]+)(@)[\w]+(\.[\w]+)+", content)
    with open("emails", "w", encoding='UTF-8') as file:
        for i in email_mock:
            file.write(f"{i}\n")
            #print(i)
    full_name_mock = re.findall(r"\b[A-Z][A-Za-z-]+\s[A-Za-z\' ]+\b", content)
    with open("full_names", "w", encoding='UTF-8') as file:
        for i in full_name_mock:
            file.write(f"{i}\n")
            #print(i)
    file_name_mock = re.findall(r"\t[A-Za-z][a-zA-Z]+\.[a-z]+", content)
    with open("fil_names", "w", encoding='UTF-8') as file:
        for i in file_name_mock:
            file.write(f"{i[1:]}\n")
           # print(i)


mock_data = Data(full_name_mock, email_mock, file_name_mock, colors_mock)
print(mock_data)