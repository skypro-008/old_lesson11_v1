import re
from lesson1.utils import SkyproTestCase
from task import app

class TestCase(SkyproTestCase):

    def get_key(self):
        return "143401"  # это код, который отправится на платформу.

    def test_jinja2(self):
        with app.app_context():
            address = "/books"
            app.testing = True
            response = app.test_client().get(address)

        self.assertEqual(response.status_code, 200, msg="Запрос не обрабатывается")
        etalon = '<!doctypehtml><htmllang="en"><head><metacharset="utf-8"><title>title</title></head><body><ul><li>title:harrypotter</li><li>year:1996</li><li>author:джоанроалинг</li></ul><ul><li>title:корольартур</li><li>year:1485</li><li>author:томасмэлори</li></ul></body></html>'
        user_result: str = response.data.decode('utf-8').replace("\n", " ").replace("\r", "").lower()
        user_result = re.sub(r'\s+', '', user_result)
        self.assertEqual(user_result, etalon, msg="Проверьте что вы скопировали верстку и никак ее не изменяли, "
                                                  "ничего не добавили и не изменили (кроме вставки шаблонов Jinja2)")
