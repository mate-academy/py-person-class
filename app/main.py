class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_data: list) -> list:
    Person.people = {}

    person_list = []

    for person_dict in people_data:
        person = Person(person_dict["name"], person_dict["age"])
        person_list.append(person)

    for person_dict in people_data:
        current_person = Person.people[person_dict["name"]]

        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            if wife_name in Person.people:
                current_person.wife = Person.people[wife_name]
            else:
                print(
                    f"Ostrzeżenie: Żona \"{wife_name}\" dla \"{current_person.name}\" nie została znaleziona w danych wejściowych.")

        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            if husband_name in Person.people:
                current_person.husband = Person.people[husband_name]
            else:
                print(
                    f"Ostrzeżenie: Mąż \"{husband_name}\" dla \"{current_person.name}\" nie został znaleziony w danych wejściowych.")

    return person_list