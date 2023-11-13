class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def find_partner(self, spouse: "Person", is_wife: bool) -> None:
        if is_wife:
            self.wife = spouse
            spouse.husband = self
        else:
            self.husband = spouse
            spouse.wife = self


def create_person_list(people: list) -> list:
    created_person_list = []

    for persona in people:
        name = persona["name"]
        age = persona["age"]
        person = Person(name, age)
        created_person_list.append(person)

    match_spouses(people)

    return created_person_list


def match_spouses(people_data: list) -> None:
    for persona in people_data:
        person = Person.people.get(persona["name"])
        if person:
            if "wife" in persona and persona["wife"]:
                spouse_name = persona["wife"]
                spouse = Person.people.get(spouse_name)
                if spouse:
                    person.find_partner(spouse, is_wife=True)
            if "husband" in persona and persona["husband"]:
                spouse_name = persona["husband"]
                spouse = Person.people.get(spouse_name)
                if spouse:
                    person.find_partner(spouse, is_wife=False)
