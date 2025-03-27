class Person:
    # Dicionário para armazenar instâncias por nome
    people = {}

<<<<<<< HEAD
    def __init__(self, name: str, age: int) -> None:
=======
    def __init__(self, name: str, age: int):
>>>>>>> 9f977e8746bce585ec424697f12762a39e6a3b99
        self.name = name
        self.age = age
        Person.people[name] = self

<<<<<<< HEAD
    def set_spouse(self, spouse: "Person", relationship: str) -> None:
        if (spouse and relationship in ("wife", "husband") and
            ((relationship == "wife" and not getattr(self, "wife", None) and
              not getattr(spouse, "husband", None)) or
             (relationship == "husband" and not getattr(self, "husband", None) and
              not getattr(spouse, "wife", None)))):
            if relationship == "wife":
                self.wife = spouse
                spouse.husband = self
            else:
=======
    def set_spouse(self, spouse: "Person", relationship: str):
        if spouse:
            if relationship == "wife" and not hasattr(self, "wife"):
                self.wife = spouse
                spouse.husband = self
            elif relationship == "husband" and not hasattr(self, "husband"):
>>>>>>> 9f977e8746bce585ec424697f12762a39e6a3b99
                self.husband = spouse
                spouse.wife = self


<<<<<<< HEAD
def create_person_list(people: list[dict[str, str | int]]) -> list[Person]:
    person_objects = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person in people:
        person_instance = Person.people.get(person["name"])

        if (wife_name := person.get("wife")) and (
                wife := Person.people.get(wife_name)):
            person_instance.set_spouse(wife, "wife")

        if (husband_name := person.get("husband")) and (
                husband := Person.people.get(husband_name)):
            person_instance.set_spouse(husband, "husband")

    return person_objects

=======
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
>>>>>>> 9f977e8746bce585ec424697f12762a39e6a3b99
