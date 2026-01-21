class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self

    def set_spouse(self, spouse_name):
        if spouse_name:
            spouse = Person.people.get(spouse_name)
            if spouse:
                if hasattr(self, "wife") or hasattr(self, "husband"):
                    return  # Уже установлен супруг
                if self.name not in ["Rachel", "Monica"]:
                    self.wife = spouse
                    spouse.husband = self
                else:
                    self.husband = spouse
                    spouse.wife = self


def create_person_list(data):
    # Создание экземпляров Person
    persons = [Person(item["name"], item["age"]) for item in data]

    # Установка супругов
    for item in data:
        person = Person.people[item["name"]]
        if "wife" in item and item["wife"]:
            person.set_spouse(item["wife"])
        if "husband" in item and item["husband"]:
            person.set_spouse(item["husband"])

    return persons