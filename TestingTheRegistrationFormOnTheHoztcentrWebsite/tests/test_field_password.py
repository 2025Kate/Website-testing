import re
import pytest
from playwright.sync_api import Page, expect

def positive_password_registration(page, pos_password_value, pos_password_value_2):
    page.goto("https://hozcentr.com/")
    page.locator("[id='btn_reg']").click()
    password = page.locator("[id='uspass']")
    password.click()
    password.press_sequentially(pos_password_value, delay=25)
    password.press("Tab")
    password2 = page.locator("[id='uspass2']")
    password2.press_sequentially(pos_password_value_2, delay=25)
    page.get_by_text("Я хочу", exact=False).click()
    page.locator("dd", has_text="Я ознакомился и согласен").click(position={"x": 5, "y": 5})
    page.locator("[id='sr_submit']").click()
    page.wait_for_timeout(1000)

@pytest.mark.positive_tests
@pytest.mark.parametrize("pos_password_value, pos_password_value_2",[
    ('TrsdAfhy0gFuCHqeE4K9', ''),
    ('5Wg7Jt4OKnhd3oq9CVA', ''),
    ('J', ''),
    ('l5F#sLd~RV', ''),
    ('iPYDKmWOdN',''),
    ('741369654852', ''),
    ('xMSoukgyPq', 'xMSoukgyPq'),
    ('fkjg KJH dfkgjh', 'fkjg KJH dfkgjh'),
    (' sdkjfhk', ' sdkjfhk'),
    ('Lbkj ', 'Lbkj '),
], ids=[
    'A 20‑character password',
    'A 19‑character password',
    'A password consisting of 1 character',
    'A password consisting of numbers, special characters, and letters (10 characters)',
    'A password consisting of Latin letters',
    'A password made of numbers',
    'The password field and the confirm password field are filled with the same data',
    'A password containing spaces in the middle',
    'A password containing spaces at the beginning',
    'A password containing spaces at the end',
])

def test_positive_valid_password(page, pos_password_value, pos_password_value_2):
    positive_password_registration(page, pos_password_value, pos_password_value_2)
    count_message = page.get_by_text(re.compile(r"пароль содержит", re.IGNORECASE)).count()
    assert count_message == 0


def negative_password_registration(page, neg_password_value, neg_password_value_2):
    page.goto("https://hozcentr.com/")
    page.locator("[id='btn_reg']").click()
    password = page.locator("[id='uspass']")
    password.click()
    password.press_sequentially(neg_password_value, delay=25)
    password.press("Tab")
    password2 = page.locator("[id='uspass2']")
    password2.press_sequentially(neg_password_value_2, delay=25)
    page.get_by_text("Я хочу", exact=False).click()
    page.locator("dd", has_text="Я ознакомился и согласен").click(position={"x": 5, "y": 5})
    page.locator("[id='sr_submit']").click()
    page.wait_for_timeout(1000)

@pytest.mark.negative_tests
@pytest.mark.parametrize("neg_password_value, neg_password_value_2", [
        ('Пароль', 'Пароль'),
        ('JkiP65gKTDxFlW60gxUb0', 'JkiP65gKTDxFlW60gxUb0'),
        ('           ', '           '),
        ('', 'password'),
        ('word', ''),
        ('123456789', '987654321'),
],ids=[
    'A password containing Cyrillic characters',
    'A 21‑character password',
    'A password containing only spaces (11 of them)',
    'The password field is empty, the confirm password field is filled in',
    'The repeat password field is empty, the password field is filled in.',
    'The password field and the password repeat field are filled with different data'


])

def test_negative_valid_password(page, neg_password_value, neg_password_value_2):
    negative_password_registration(page, neg_password_value, neg_password_value_2)
    count_message = page.get_by_text("Пароли не совпадают").count()
    count_message_2 = page.get_by_text(re.compile(r"пароль содержит", re.IGNORECASE)).count()
    assert count_message == 1 or count_message_2 == 1

def test_empty_password_field(page):
    negative_password_registration(page, '', '')
    count_message = page.get_by_text("Пароль не может быть пустым.").count()
    assert count_message == 1
