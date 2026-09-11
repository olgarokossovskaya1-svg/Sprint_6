import pytest
import allure
from pages.main_page import MainPage
from data.questions_data import QUESTIONS_DATA


class TestQuestions:
    @pytest.mark.parametrize("index, expected_answer", 
                             [(q["index"], q["answer"]) for q in QUESTIONS_DATA],
                             ids=[q["question"] for q in QUESTIONS_DATA])
    @allure.title("Проверка соответствия вопроса и ответа")
    def test_question_opens_corresponding_answer(self, driver, index, expected_answer):
        page = MainPage(driver)
        page.open()
        page.accept_cookies()
        page.click_question(index)
        assert page.get_answer_text(index) == expected_answer