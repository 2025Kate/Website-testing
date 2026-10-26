import pytest
from playwright.sync_api import Page, expect

def positive_phone_registration(page, pos_phone_value):
    page.goto("https://hozcentr.com/")
    page.locator("[id='btn_reg']").click()
    phone = page.locator("[id='usphone']")
    phone.click()
    phone.fill(pos_phone_value)
    phone.press("Tab")
    page.get_by_text("Я хочу", exact=False).click()
    page.locator("dd", has_text="Я ознакомился и согласен").click(position={"x": 5, "y": 5})
    page.locator("[id='sr_submit']").click()
    page.wait_for_timeout(1000)

@pytest.mark.positive_tests
@pytest.mark.parametrize("pos_phone_value", [
    '9824800337',
    '3843569874',
], ids=[
    'Enter a 10‑digit phone number without spaces',
    'Entering a landline phone number without spaces'
])

def test_positive_valid_phone(page, pos_phone_value):
    positive_phone_registration(page, pos_phone_value)
    count_message = page.get_by_text("Некорректный номер телефона!").count()
    assert count_message == 0

def test_enter_21_digits(page):
    page.goto("https://hozcentr.com/")
    page.locator("[id='btn_reg']").click()
    phone = page.locator("[id='usphone']")
    phone.click()
    phone.fill('965471235469852434671')
    phone.press("Tab")
    page.get_by_text("Я хочу", exact=False).click()
    page.locator("dd", has_text="Я ознакомился и согласен").click(position={"x": 5, "y": 5})
    page.locator("[id='sr_submit']").click()
    page.wait_for_timeout(1000)
    actual_value = phone.input_value()
    print()
    print(f"В поле записалось: {actual_value}")
    print("В поле ожидалось: +7(965) 471-23-54")
    count_message = page.get_by_text("Некорректный номер телефона!").count()
    assert count_message == 0



def negative_phone_registration(page, neg_phone_value):
    page.goto("https://hozcentr.com/")
    page.locator("[id='btn_reg']").click()
    phone = page.locator("[id='usphone']")
    phone.click()
    phone.press_sequentially(neg_phone_value, delay=25)
    phone.press("Tab")
    page.get_by_text("Я хочу", exact=False).click()
    page.locator("dd", has_text="Я ознакомился и согласен").click(position={"x": 5, "y": 5})
    page.locator("[id='sr_submit']").click()
    page.wait_for_timeout(1000)

@pytest.mark.positive_tests
@pytest.mark.parametrize("neg_phone_value", [
    '3',
    ''
], ids=[
    'Enter 1 digit',
    ''
])

def test_negative_valid_phone(page, neg_phone_value):
    negative_phone_registration(page, neg_phone_value)
    count_message = page.get_by_text("Некорректный номер телефона!").count()
    assert count_message == 1

