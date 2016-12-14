from phonebook import Phonebook

def test__add_and_lookup():
    phonebook = Phonebook()
    phonebook.add("Bob", "123")
    assert "123" == phonebook.lookup("Bob")


def test_phonebook_given_access_to_names_and_numbers():
    phonebook = Phonebook()
    phonebook.add("Alice", "12345")
    phonebook.add("Bob", "123")
    assert set(phonebook.names()) == {"Alice", "Bob"}
