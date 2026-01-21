from app.main import Person, create_person_list


def test_create_person_list():
    people = [
        {"name": "Ross", "age": 30, "wife": "Rachel"},
        {"name": "Joey", "age": 29, "wife": None},
        {"name": "Rachel", "age": 28, "husband": "Ross"},
    ]

    result = create_person_list(people)

    ross = Person.people["Ross"]
    joey = Person.people["Joey"]
    rachel = Person.people["Rachel"]

    assert ross.wife is rachel
    assert rachel.husband is ross
    assert not hasattr(joey, "wife")
    assert ross.wife.name == "Rachel"
    assert rachel.husband.name == "Ross"
    assert ross.wife.husband is ross
