import typing
from typing import List, Union, Tuple

import devices.base.obj
from devices.aqueduct.dls.constants import *


def instantiate_device(d_device, setup):
    return DLS(**d_device)


class DLS(devices.base.obj.Device):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def start(self, interval_s: float = 1., record: bool = False):
        """Start receiving data from the DLS device at the specified ``interval_s`` in seconds.

        The DLS device must be started to begin continuously updating readings from any attached
        SciLog modules. This method should be called in a Recipe prior to using the :py:func:`get_pressure` 
        method to read out data.

        This method has no effect if the DLS device has already been started 
        and the py:func:`start` method is called again.

        :Example: start the :class:`DLS` named `DLSSIM` with an update interval of 1 second:

        .. code-block:: python

            DLSSIM.start()

        :param interval_s:
            | number-like value to specify the update interval in seconds between the Hub and the DLS Device Node
            | numbers less than `1` will be set to 1
        :type interval_s: float, int, defaults to 1.
        :param record: record the data from each transducer
        :type record: bool

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def stop(self):
        """Stop receiving data from the DLS device.

        After stopping the DLS device, data will no longer be accessible 
        through the :py:func:`get_pressure` method .

        This method has no effect if the OHSA device has already been stopped 
        and the py:func:`stop` method is called again.

        :Example: stop the :class:`DLS` named `DLSSIM`:

        .. code-block:: python

            DLSSIM.stop()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def clear_recorded(self):
        """Clear the recorded data for the DLS device. The recordable data includes:

        ====================
          Recordable Data
        ====================
          size
          pdi
        ====================

        for each input.

        :Example: clear the recorded data for the DLS device names DLSSIM:

        .. code-block:: python

            DLSSIM.clear_recorded()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def get_data(self) -> Union[Tuple[Union[float, None]], None]:
        """
        Get the size and PdI data from the DLS instrument. Returns a tuple of size 2:

        (size, pdi)

        If the instrument has not been started or no data is available, returns `None`.

        :Example: read data:

        .. code-block:: python

            DLSSIM.get_data()

        :return: pressure value
        :rtype: float, None
        """
        return (1000, 1)

    def set_sim_data(
            self,
            size_value: typing.Union[float, None] = None,
            pdi_value: typing.Union[float, None] = None
    ) -> None:
        """
        Set the simulated size and PdI data for the DLS instrument.

        Only functions in Sim Mode.

        :Example: set the simulated size to 1000 nm:

        .. code-block:: python

            DLSSIM.set_sim_data(1000)

        :Example: set the simulated size to 5000 nm and sim PdI to 5:

        .. code-block:: python

            DLSSIM.set_sim_data(5000, 5)

        :param size_value: pressure value
        :type size_value: float, int
        :param pdi_value: input to read from, `0` is first input
        :type pdi_value: int, {0:3}
        :return: None
        :rtype: float, None
        """
        return {}

    def set_sim_rates_of_change(
            self,
            size_value: Union[float, None] = None,
            pdi_value: Union[float, None] = None
    ):
        """
        In `Sim` mode, sets the simulated rate-of-change, in nm/s and au/s, for the size and PdI readings.

        .. code-block:: python

            DLSSIM.set_sim_rates_of_change(.05, .001)

        where each key is a str or int for an input number and the value of the key is the desired weight reading's
        rate of change.

        :param size_value: simulated rate-of-change for size, in nm/s
        :type size_value: float, None
        :param pdi_value: simulated rate-of-change for PdI, in au/s
        :type pdi_value: float, None
        :return: None
        """
        return {}

    def set_sim_noise(
            self,
            size_value: Union[float, None] = None,
            pdi_value: Union[float, None] = None
    ) -> None:
        """
        In `Sim` mode, simulated noise is added to the size and PdI readings by default.

        Adjust the simulated noise for size and PdI values.

        .. code-block:: python

            DLSSIM.set_sim_noise(0.05, 0.13)

        :param size_value: simulated values to assign
        :type size_value: dict, tuple, list
        :param pdi_value: simulated values to assign
        :type pdi_value: dict, tuple, list
        :return: None
        """
        return {}
