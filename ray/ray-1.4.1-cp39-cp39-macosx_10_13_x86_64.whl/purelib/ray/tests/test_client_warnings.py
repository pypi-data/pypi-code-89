from ray.util.client.ray_client_helpers import ray_start_client_server
from ray.util.client.worker import TASK_WARNING_THRESHOLD
from ray.util.debug import _logged

import numpy as np
import pytest

import unittest
import warnings


@pytest.fixture(autouse=True)
def reset_debug_logs():
    """Resets internal state of ray.util.debug so that warning can be tested
    more than once in the same process"""
    _logged.clear()


class LoggerSuite(unittest.TestCase):
    """Test client warnings are raised when many tasks are scheduled"""

    def testManyTasksWarning(self):
        with ray_start_client_server() as ray:

            @ray.remote
            def f():
                return 42

            with self.assertWarns(UserWarning) as cm:
                for _ in range(TASK_WARNING_THRESHOLD + 1):
                    f.remote()
            assert f"More than {TASK_WARNING_THRESHOLD} remote tasks have " \
                "been scheduled." in cm.warning.args[0]

    def testNoWarning(self):
        with ray_start_client_server() as ray:

            @ray.remote
            def f():
                return 42

            with warnings.catch_warnings(record=True) as warn_list:
                for _ in range(TASK_WARNING_THRESHOLD):
                    f.remote()
            assert not any(f"More than {TASK_WARNING_THRESHOLD} remote tasks "
                           "have been scheduled." in str(w.args[0])
                           for w in warn_list)

    def testOutboundMessageSizeWarning(self):
        with ray_start_client_server() as ray:
            large_argument = np.random.rand(100, 100, 100)

            @ray.remote
            def f(some_arg):
                return some_arg[0][0][0]

            with self.assertWarns(UserWarning) as cm:
                for _ in range(50):
                    f.remote(large_argument)
            assert "More than 10MB of messages have been created to " \
                "schedule tasks on the server." in cm.warning.args[0]


if __name__ == "__main__":
    import sys
    import pytest
    sys.exit(pytest.main(["-v", __file__]))
