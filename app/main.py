class Person:
    people = {}

    def __init__(self, name: str, age: int) -> dict:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self

    def repr(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people: list) -> list:

    Person.people = {}

    for one_person in people:
        Person(one_person["name"], one_person["age"])

    for one_person in people:
        person_instance = Person.people[one_person["name"]]
        spouse_name = one_person.get("wife") or one_person.get("husband")

        if spouse_name:
            spouse_instance = Person.people.get(spouse_name)
            if "wife" in one_person:
                if one_person["wife"] is not None:
                    person_instance.wife = spouse_instance
                else:
                    None
            elif "husband" in one_person:
                person_instance.husband = spouse_instance

    return list(Person.people.values())


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

# new_person_list = create_person_list(people)
# print(Person.people)
