import devices.base.constants
from enum import Enum


NUMBER_INPUTS: int = 1
ACTIVE_KEY = "active"
MEAN_SIZE_NM_KEY = devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + "mean_size_nm"
PDI_KEY = devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + "pdi"


class Active(Enum):
    NOT_ACTIVE = 0
    IS_ACTIVE = 1


BASE = dict(
    type="DLS",
)

BASE_DTYPES = dict(

)

BASE.update({
    ACTIVE_KEY: 0,
    MEAN_SIZE_NM_KEY: 0.,
    PDI_KEY: 0.,
})

BASE_DTYPES.update({
    ACTIVE_KEY: int.__name__,
    MEAN_SIZE_NM_KEY: str.__name__,
    PDI_KEY: str.__name__,
})

BASE = {**devices.base.constants.BASE, **BASE}
BASE_DTYPES = {**devices.base.constants.BASE_DTYPES, **BASE_DTYPES}

DEVICE_TYPE = BASE.get('type')

DISPLAY_NAME = "Inline DLS (" + DEVICE_TYPE + ")"

CATEGORY = "Particle Sizers"

# value returned by the DLS device
# when the device is not active
NO_INPUT_VALUE = '?'
