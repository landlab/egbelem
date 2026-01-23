"""
test_egbe_lem.py: external unit tests for EgbeLem and associated code.
"""

import os
from egbelem import EgbeLem


def test_run_with_default_params_cl():
    os.system("python ../src/egbelem/egbelem.py")

def test_run_with_default_params():
    model = EgbeLem()
    model.run()


if __name__ == "__main__":
    test_run_with_default_params_cl()
    test_run_with_default_params()
