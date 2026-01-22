class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(data_list: list) -> list:
    Person.people.clear()

    # Cria todas as pessoas
    [Person(data.get("name"), data.get("age")) for data in data_list]

    # Relaciona cônjuges
    for data in data_list:
        person = Person.people.get(data.get("name"))
        wife_name = data.get("wife")
        husband_name = data.get("husband")

        if wife_name:
            wife = Person.people.get(wife_name)
            if wife:
                person.wife = wife
                wife.husband = person  # link reverso

        if husband_name:
            husband = Person.people.get(husband_name)
            if husband:
                person.husband = husband
                husband.wife = person  # link reverso

    # Retorna a lista de objetos Person na mesma ordem
    return [Person.people.get(data.get("name")) for data in data_list]
