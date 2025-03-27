class Person:
    # Dicionário para armazenar instâncias por nome
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self

    def set_spouse(self, spouse: "Person", relationship: str):
        if spouse:
            if relationship == "wife" and not hasattr(self, "wife"):
                self.wife = spouse
                spouse.husband = self
            elif relationship == "husband" and not hasattr(self, "husband"):
                self.husband = spouse
                spouse.wife = self


def create_person_list(people: list) -> list:
    person_objects = []

    # Cria as instâncias de Person
    for person in people:
        name = person.get("name")
        age = person.get("age")
        person_objects.append(Person(name, age))

    # Cria os relacionamentos (depois de criar todas as instâncias)
    for person in people:
        person_instance = Person.people.get(person["name"])

        # Atribui esposa (se ela existir)
        wife_name = person.get("wife")
        if wife_name and wife_name in Person.people:
            wife = Person.people.get(wife_name)
            person_instance.set_spouse(wife, "wife")

        # Atribui marido (se ele existir)
        husband_name = person.get("husband")
        if husband_name and husband_name in Person.people:
            husband = Person.people.get(husband_name)
            person_instance.set_spouse(husband, "husband")

    return person_objects
