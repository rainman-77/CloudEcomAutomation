import random
from datetime import datetime
import pytest


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BaseTest:
    @staticmethod
    def generate_mail():
        cur_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + str(random.randint(1, 99))
        return f"test_ash_{cur_time}@gmail.com"


