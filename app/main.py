class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []  # Список для хранения объектов Person

    for person in people:
        # Создаем объект Person для каждого словаря
        person_obj = Person(person["name"], person["age"])

        # Если у человека есть супруга, устанавливаем соответствующую ссылку
        if person.get("wife"):
            wife = Person.people.get(person["wife"])
            if wife:
                person_obj.wife = wife
                wife.husband = person_obj  # Устанавливаем взаимную ссылку

        if person.get("husband"):
            husband = Person.people.get(person["husband"])
            if husband:
                person_obj.husband = husband
                husband.wife = person_obj  # Устанавливаем взаимную ссылку
        # Добавляем объект в список
        person_list.append(person_obj)

    return person_list
