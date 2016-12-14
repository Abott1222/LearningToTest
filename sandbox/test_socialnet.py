from socialnet import SocialNet
from socialnet import Profile


def test_create_and_add_socialnet():
    socialnet = SocialNet("test")
    person1 = Profile("Alex")
    socialnet.add(person1)
    assert True == socialnet.lookup("Alex")


