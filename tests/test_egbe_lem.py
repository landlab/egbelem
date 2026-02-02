"""
test_egbe_lem.py: external unit tests for EgbeLem and associated code.
"""

import os
from numpy.testing import assert_equal
from egbelem import EgbeLem


def test_run_with_default_params_cl():
    os.system("python ../src/egbelem/egbelem.py")
    os.system("python ../src/egbelem/egbelem.py ../src/egbelem/egbedefaults.yaml")

def test_run_with_default_params():
    model = EgbeLem()
    model.run()
    model = EgbeLem(input_file="../src/egbelem/egbedefaults.yaml")
    model.run()

def test_run_pause_continue():
    model = EgbeLem()
    model.update_until(200., dt=100.)
    assert_equal(model.current_time, 200.)
    model.update_until(400., dt=100.)
    assert_equal(model.current_time, 400.)


if __name__ == "__main__":
    test_run_with_default_params_cl()
    test_run_with_default_params()
    test_run_pause_continue()
