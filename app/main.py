class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.spouse = None
        Person.people[name] = self
    pass


def create_person_list(people: list) -> list:
    person_list = []
    #Проходимо через список словників та створюємо екземпляр классу для кожного словника
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        person_list.append(person)
    #Отримуємо відповідний екземпляр Person із словника Person.people і призначае атрибут подружжя якщо можливо
    for person_dict in people:
        name = person_dict["name"]
        person = Person.people[name]
        spouse_name = person_dict.get("wife") or person_dict.get("husband")
        if spouse_name:
            spouse = Person.people.get(spouse_name)
            if "wife" in person_dict:
                person.wife = spouse
            elif "husband" in person_dict:
                person.husband = spouse

    return person_list
