from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_selene(open_browser):
    browser.open('/')

    s(".search-input").click()
    s("#query-builder-test").send_keys("allure-framework/allure2")
    s("#query-builder-test").submit()

    s(by.link_text("allure-framework/allure2")).click()

    s("#issues-tab").click()

    s(by.partial_text("#2200")).should(be.visible)
