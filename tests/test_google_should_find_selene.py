import pytest
from selene import browser, have
from selene.support.shared import config

base_url = 'https://google.com'


@pytest.fixture(scope="class")
def size_window():
    config.window_width = 1200
    config.window_height = 1000


class TestSearchInGoogle:

    # browser.open('https://google.com')
    # browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    # browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

    def test_should_success_field_filling(self, size_window):
        browser.open(base_url)
        browser.element('[id="APjFqb"]').send_keys('Stack overflow').press_enter()
        browser.element('[class="VuuXrf"]').should(have.text('Stack Overflow'))

    def test_should_fail_field_filling(self):
        browser.open(base_url)
        browser.element('[id="APjFqb"]').send_keys('aesrdtyuikujhfbgdfrsedassfdghgjkjlojkhjgfd').press_enter()
        browser.element('[class="card-section"]').should(have.text('ничего не найдено'))
