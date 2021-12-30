import local.lib.meha.methods
import local.lib.meha.classes

import random
import time

def test_data_class():
    devices = local.lib.meha.classes.Devices.generate_dev_devices()
    from recipe_runner.aqueduct import Aqueduct
    aqueduct = Aqueduct('G', None, None, None)

    def random_ph():
        return random.uniform(6, 8)

    def random_ml():
        return random.uniform(0, 1)

    devices.PH.get_ph = random_ph

    devices.PP.ml_pumped = random_ml

    data: local.lib.meha.classes.Data = local.lib.meha.classes.Data(devices, aqueduct)

    for _ in range(0, 10):
        data.update_data()
        time.sleep(1)

    print(data._cache._cache)

