import pytest
from selene import have
from selene.support.shared import browser, config

full_name = 'Nevsky Alex Koteykovich'


@pytest.fixture(scope="class")
def size_window():
    config.window_width = 1200
    config.window_height = 1200


def test_form_filling_success():
    browser.open('https://demoqa.com/text-box')
    browser.element('[id="userName"]').send_keys(full_name)
    browser.element('[id="userEmail"]').send_keys('koteykovich@mail.ru')
    browser.element('[id="currentAddress"]').send_keys('Saint-Petersburg')
    browser.element('[id="permanentAddress"]').send_keys('All world')
    browser.execute_script("window.scrollTo(0, 800)")
    browser.element('[id="submit"]').click()

    assert browser.element('[id="name"]').should(have.text(full_name))
