import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_dynamic_test(open_browser):
    with allure.step('Открываем главную страницу'):
        browser.open('/')

    with allure.step('Ищем репозиторий'):
        s(".search-input").click()
        s("#query-builder-test").send_keys("allure-framework/allure2")
        s("#query-builder-test").submit()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text("allure-framework/allure2")).click()

    with allure.step('Открываем таб Issues'):
        s("#issues-tab").click()

    with allure.step('Проверяем наличие Issue с номером 2200'):
        s(by.partial_text("#2200")).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.TRIVIAL)
@allure.label("owner", "Ilya Chukov")
@allure.feature("Задачи в репозитории")
@allure.story("Проверка необходимого Issue")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps(open_browser):
    open_main_page()
    search_for_repository("allure-framework/allure2")
    go_to_repository("allure-framework/allure2")
    open_issue_tab()
    should_see_issue_with_number('#2200')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('/')


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s(".search-input").click()
    s("#query-builder-test").send_keys(repo)
    s("#query-builder-test").submit()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем таб Issues')
def open_issue_tab():
    s("#issues-tab").click()


@allure.step('Проверяем наличие Issue с номером {number}')
def should_see_issue_with_number(number):
    s(by.partial_text(number)).should(be.visible)
