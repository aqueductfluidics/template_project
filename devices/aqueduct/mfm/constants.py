import devices.base.constants
from enum import Enum
from devices.aqueduct.ohsa.constants import Active, ACTIVE_KEY

Active # noqa, avoid unused param

NUMBER_INPUTS: int = 4

TRANSDUCER_PREFIX = "txdcr_"

BASE = dict(
    type="MFM",
    number_icons=NUMBER_INPUTS,
    number_ports=NUMBER_INPUTS * 2,
)

BASE_DTYPES = dict(

)

BASE.update({
    ACTIVE_KEY: 0,
})

BASE_DTYPES.update({
    ACTIVE_KEY: int.__name__,
})

for i in range(0, NUMBER_INPUTS):
    BASE.update({
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + TRANSDUCER_PREFIX + str(i) + '_mf_value': 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + TRANSDUCER_PREFIX + str(i) + '_mf_units': "ml/min",
        '_connection_' + str(i) + '_length_mm': 30,
        '_connection_' + str(i) + '_id_mm': 6,
        '_connection_' + str(i) + '_material': 'polysulfone',
    })
    BASE_DTYPES.update({
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + TRANSDUCER_PREFIX + str(i) + '_mf_value': float.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + TRANSDUCER_PREFIX + str(i) + '_mf_units': str.__name__,
        '_connection_' + str(i) + '_length_mm': float.__name__,
        '_connection_' + str(i) + '_id_mm': float.__name__,
        '_connection_' + str(i) + '_material': str.__name__,
    })

for i in range(0, NUMBER_INPUTS):
    BASE.update({
        '_input_' + str(i) + '_active': 0,
    })
    BASE_DTYPES.update({
        '_input_' + str(i) + '_active': int.__name__,
    })

BASE = {**devices.base.constants.BASE, **BASE}
BASE_DTYPES = {**devices.base.constants.BASE_DTYPES, **BASE_DTYPES}

DEVICE_TYPE = BASE.get('type')

DISPLAY_NAME = "Ultrasonic Mass Flow Meter (" + DEVICE_TYPE + ")"

CATEGORY = "Mass Flow Transducers"

# value returned by the MFM device
# when one of the transducers is absent
NO_TRANSDUCER_VALUE = "-"

# value returned by the MFM device
# when one of the inputs is absent
NO_INPUT_VALUE = '?'
