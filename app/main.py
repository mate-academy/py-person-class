# main.py

from person import Person


def create_person_list(people_data: list) -> list:
    # Primeiro, cria todas as instâncias sem relacionamentos
    for data in people_data:
        Person(data["name"], data["age"])

    # Depois, adiciona os relacionamentos (wife/husband)
    for data in people_data:
        person = Person.people[data["name"]]
        if "wife" in data and data["wife"]:
            person.wife = Person.people[data["wife"]]
        elif "husband" in data and data["husband"]:
            person.husband = Person.people[data["husband"]]

    return list(Person.people.values())