import pytest
from playwright.sync_api import expect, Page

def positive_mail_registration(page, pos_email_value):
    page.goto("https://hozcentr.com/")
    page.locator("[id='btn_reg']").click()
    email = page.locator("[id='usemail']")
    email.click()
    email.press_sequentially(pos_email_value, delay=50)
    email.press("Tab")
    page.get_by_text("Я хочу", exact=False).click()
    page.locator("dd", has_text="Я ознакомился и согласен").click(position={"x": 5, "y": 5})
    page.locator("[id='sr_submit']").click()
    page.wait_for_timeout(1000)


@pytest.mark.positive_tests
@pytest.mark.parametrize("pos_email_value", [
    'KAt_2026-progRAMM@gmail.com',
    'user@gmail.com',
    'NAME@MAIL.RU',
    'MAX2024@GMAIL.COM',
    '2003anna@mail.ru',
    'MARIA@MAIL1.RU',
    'i@g2mail.com',
    'ANNA-MARIA@MAIL.RU',
    'new-user@gmail.com',
    'SKY@HELLO-WORLD.RU',
    'myemail@gmail-gmail.com',
    'pixene_sode@YANDEX.RU',
    'star_new@mail.ru',
    'filec.iyeho@YANDEX.RU',
    'zovajuc.efu@gmail.com',
    'dok@cuwun.ikuxi.RU',
    'ana@gedav.ucigu.com',
    'qwertyuiopasdfghjklzxcvbnmlkjhgfdsaqwert@yandex.ru',
    'QWERTYUQHJDFFGHJKLZXCVBNMLKJHGFDSAQWERT@GMAIL.COM'
    'rtyirtyoidfgbdsnbefggdgsdharhkjcnvbawbr@gmail.com',
    'RTGHGFHFGNSBCVKCVHERGGDGSDHARHKJCNVBAWBR@MAIL.RU'
], ids=[
    'test_with_all_permissible_characters_in_the_username',
    'test_lowercase',
    'test_uppercase',
    'test_uppercase_with_numbers_in_name',
    'test_lowercase_with_numbers_in_name',
    'test_uppercase_with_numbers_in_domain',
    'test_lowercase_with_numbers_in_domain',
    'test_uppercase_with_dash_in_name',
    'test_lowercase_with_dash_in_name',
    'test_uppercase_with_dash_in_domain',
    'test_lowercase_with_dash_in_domain',
    'test_uppercase_with_emphasis_in_name',
    'test_lowercase_with_emphasis_in_name',
    'test_uppercase_with_dot_in_name',
    'test_lowercase_with_dot_in_name',
    'test_uppercase_with_dot_in_domain',
    'test_lowercase_with_dot_in_domain',
    'test_the_maximum_allowed_number_of_characters_in_lowercase',
    'test_the_maximum_allowed_number_of_characters_in_uppercase'
    'test_lowercase_49‑character_email_address',
    'test_uppercase_49‑character_email_address'
])

def test_positive_valid_email(page, pos_email_value):
    positive_mail_registration(page, pos_email_value)
    count_message = page.get_by_text("Некорректная электронная почта").count()
    assert count_message == 0

def negative_email_registration(page, neg_email_value):
    page.goto("https://hozcentr.com/")
    page.locator("[id='btn_reg']").click()
    email = page.locator("[id='usemail']")
    email.click()
    email.press_sequentially(neg_email_value, delay=50)
    email.press("Tab")
    page.get_by_text("Я хочу", exact=False).click()
    page.locator("dd", has_text="Я ознакомился и согласен").click(position={"x": 5, "y": 5})
    page.locator("[id='sr_submit']").click()
    page.wait_for_timeout(1000)


@pytest.mark.negative_tests
@pytest.mark.parametrize("neg_email_value", [
    'nuyura@pop_2025.com',
    'GIGU@I_M.RU',
    'gamble56@gmail.ru',
    'IRIS@GMAIL.RU',
    ' ',
    'name@gmailcom',
    'FLOWERS@MAILRU',
    'ghjkfdknewrtdeovndfkjhrtoigjdlfkspdgfdopgp@mail.ru',
    'VCNKFJGSREHBXCWDSDENFKDJDFHQWEBJDFNZFJK@YANDEX.RU',
    'lau_delbert11hotmail.com',
    'MICKYMAIL.RU',
    'essie short@gmail.com',
    'KEELY MERRILL42@MAIL.RU',
    'cherry-shayna91@mail .ru',
    'ZEPEDARUTHANN51@YAND EX.RU',
    '@mail.ru',
    '@YANDEX.RU',
    'Linda',
    'BORIS',
    'login@домен.рф'

], ids=[
    'test_lowercase_with_emphasis_in_domain',
    'test_uppercase_with_emphasis_in_domain',
    'test_lowercase_domain_is_gmail.ru',
    'test_uppercasethe_domain_is_gmail.ru',
    'test_empty_field',
    'test_lowercase_email_without_dot_in_domain',
    'test_uppercase_email_without_dot_in_domain',
    'test_lowercase_exceeding_the_allowed_number_of_characters',
    'test_uppercase_exceeding_the_allowed_number_of_characters',
    'test_lowercase_email_without_@',
    'test_uppercase_email_without_@',
    'test_lowercase_space_in_name',
    'test_uppercase_space_in_name',
    'test_lowercase_space_in_domain',
    'test_uppercase_space_in_domain',
    'test_lowercase_without_username',
    'test_uppercase_without_username',
    'test_lowercase_without_domain',
    'test_uppercase_without_domain',
    'test_with_cyrillic_domain'
])

def test_negative_valid_email(page, neg_email_value):
    negative_email_registration(page, neg_email_value)
    count_message = page.get_by_text("Некорректная электронная почта").count()
    assert count_message == 1