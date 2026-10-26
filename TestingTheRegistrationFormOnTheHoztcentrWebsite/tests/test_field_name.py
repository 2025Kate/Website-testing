import re
import pytest
from playwright.sync_api import expect, Page

def positive_name_registration(page, pos_name_value):
    page.goto("https://hozcentr.com/")
    page.locator("[id='btn_reg']").click()
    name = page.locator("[id='usname']")
    name.click()
    name.press_sequentially(pos_name_value, delay=25)
    name.press("Tab")
    page.get_by_text("Я хочу", exact=False).click()
    page.locator("dd", has_text="Я ознакомился и согласен").click(position={"x": 5, "y": 5})
    page.locator("[id='sr_submit']").click()
    page.wait_for_timeout(1000)


@pytest.mark.positive_tests
@pytest.mark.parametrize("pos_name_value", [
    'Ирина',
    'Василий2007',
    'Анна-Мария',
    'Пользователь сайта',
    'Иван_Иванов',
    'Max',
    'ЕГОР',
    'павел',
    'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзывалпосые',
    'ватиожеофидсорвафутвыисоврафрфмдчгрвоадлыоррыдвоид',
    ''
], ids = [
    'Five Cyrillic characters',
    'A name containing numbers',
    'A name containing a hyphen',
    'A name containing a space',
    'A name containing an underscore',
    'A name composed of 3 Latin letters',
    'A name consisting of uppercase letters',
    'A name made up of lowercase letters',
    'A name consisting of 49 characters',
    'A name consisting of 50 characters',
    'Empty field'
])

def test_positive_valid_name(page, pos_name_value):
    positive_name_registration(page, pos_name_value)
    count_message = page.get_by_text(re.compile(r"имя пользователя", re.IGNORECASE)).count()
    assert count_message == 0



def negative_name_registration(page, neg_name_value):
    page.goto("https://hozcentr.com/")
    page.locator("[id='btn_reg']").click()
    name = page.locator("[id='usname']")
    name.click()
    name.press_sequentially(neg_name_value, delay=25)
    name.press("Tab")
    page.get_by_text("Я хочу", exact=False).click()
    page.locator("dd", has_text="Я ознакомился и согласен").click(position={"x": 5, "y": 5})
    page.locator("[id='sr_submit']").click()
    page.wait_for_timeout(1000)


@pytest.mark.negative_tests
def test_name_consisting_of_51_characters(page):
    negative_name_registration(page, 'лмоаплдыяослрдыгкпеаыорвплсорвораплдыгрцунвавлорагк')
    count_message = page.get_by_text("Слишком длинное имя пользователя!").count()
    assert count_message == 1

@pytest.mark.negative_tests
def test_name_consisting_of_1_character(page):
    negative_name_registration(page, 'Я')
    count_message = page.get_by_text("Имя пользователя менее 3-х символов!").count()
    assert count_message == 1

@pytest.mark.negative_tests
def test_name_consisting_of_2_character(page):
    negative_name_registration(page, 'ОН')
    count_message = page.get_by_text("Имя пользователя менее 3-х символов!").count()
    assert count_message == 1

@pytest.mark.positive_tests
@pytest.mark.parametrize("neg_name_value", [
    'авлоп!',
    "смл'",
    'Ан#ия#',
    'Богач$',
    'Иван%',
    'Привет&Пока',
], ids = [
    'Name containing !',
    "Name containing '",
    'Name containing #',
    'Name containing $',
    'Name containing %',
    'Name containing &',
])

def test_negative_valid_name(page, neg_name_value):
    negative_name_registration(page, neg_name_value)
    count_message = page.get_by_text(re.compile(r"имя пользователя", re.IGNORECASE)).count()
    assert count_message == 1