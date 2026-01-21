class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None  # Inicializamos com None
        self.husband = None  # Inicializamos com None
        Person.people[name] = self

    def set_spouse(self) -> None:
        if self.wife:
            self.wife = Person.people.get(self.wife)
        if self.husband:
            self.husband = Person.people.get(self.husband)


def create_person_list(people: list) -> list:
    person_list = [
        Person(person["name"], person["age"]) for person in people
    ]

    for person in people:
        person_instance = Person.people.get(person["name"])
        # Atribuir wife ou husband, se existirem
        person_instance.wife = Person.people.get(
            person.get("wife")
        )  # Usando get() aqui
        if not person.get("wife"):
            # Se não houver "wife", removemos o atributo
            if hasattr(person_instance, "wife"):
                del person_instance.wife

        person_instance.husband = Person.people.get(
            person.get("husband")
        )  # Usando get() aqui
        if not person.get("husband"):
            # Se não houver "husband", removemos o atributo
            if hasattr(person_instance, "husband"):
                del person_instance.husband

    return person_list
