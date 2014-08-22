from zsenda import Mars
import pytest


def test_init():
    mars = Mars('jsonfile.json', 'jsonfile2.json')
    assert mars


def test_send():
    mars = Mars('jsonfile.json', 'jsonfile2.json')
    jdict = {'name': 'Suhail', 'age': '21', 'place': 'Palakkad'}
    assert mars.send(jdict) == 1
    assert mars.send('sd') is None


def test_receive():
    mars = Mars('jsonfile.json', 'jsonfile2.json')
    data = mars.receive()
    assert data['name'] == 'Suhail'
    cars = Mars('sa', 'sda')
    assert cars.receive() is None
