class Person:
    people = {}  # Klasa atrybut do przechowywania wszystkich instancji

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Dodajemy instancję do słownika klasowego people
        Person.people[name] = self


def create_person_list(people_data):
    # Pierwszy przebieg: tworzymy wszystkie osoby bez ustawiania związków
    person_list = []
    for person_dict in people_data:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        person_list.append(person)

    # Drugi przebieg: ustawiamy żony/mężów
    for person_dict in people_data:
        name = person_dict["name"]
        person = Person.people[name]
        if "wife" in person_dict and person_dict["wife"]:
            person.wife = Person.people[person_dict["wife"]]
        if "husband" in person_dict and person_dict["husband"]:
            person.husband = Person.people[person_dict["husband"]]

    return person_list
