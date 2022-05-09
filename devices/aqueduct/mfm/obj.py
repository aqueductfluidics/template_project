import typing
from typing import List, Union, Tuple

import devices.base.obj
from devices.aqueduct.mfm.constants import *


def instantiate_device(d_device, setup):
    return MFM(**d_device)


class MFM(devices.base.obj.Device):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def start(self, interval_s: float = 1., record: bool = False):
        """Start receiving data from the MFM device at the specified ``interval_s`` in seconds.

        The MFM device must be started to begin continuously updating readings from any attached
        SciLog modules. This method should be called in a Recipe prior to using the :py:func:`get_pressure` 
        method to read out data.

        This method has no effect if the MFM device has already been started 
        and the py:func:`start` method is called again.

        :Example: start the :class:`MFM` named `MFMSIM` with an update interval of 1 second:

        .. code-block:: python

            MFMSIM.start()

        :param interval_s:
            | number-like value to specify the update interval in seconds between the Hub and the MFM Device Node
            | numbers less than `1` will be set to 1
        :type interval_s: float, int, defaults to 1.
        :param record: record the data from each transducer
        :type record: bool

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def stop(self):
        """Stop receiving data from the MFM device.

        After stopping the MFM device, data will no longer be accessible 
        through the :py:func:`get_pressure` method .

        This method has no effect if the OHSA device has already been stopped 
        and the py:func:`stop` method is called again.

        :Example: stop the :class:`MFM` named `MFMSIM`:

        .. code-block:: python

            MFMSIM.stop()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def clear_recorded(self):
        """Clear the recorded data for the MFM device. The recordable data includes:

        ====================
          Recordable Data
        ====================
          pressure
        ====================

        for each input.

        :Example: clear the recorded data for the MFM device names MFMSIM:

        .. code-block:: python

            MFMSIM.clear_recorded()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def get_mass_flow(self, index: int = 0) -> Union[float, None]:
        """
        Get a pressure reading from one of the MFM Device Node's 4 possible transducer inputs.
        The *index* argument selects the input channel.

        If no valid input or transducer is present, returns `None`.

        :Example: read transducer input 0:

        .. code-block:: python

            MFMSIM.get_mass_flow(0)

        :param index: input to read from, `0` is first input
        :type index:
            | An integer value
            | Value must be between 0 and 3
            | input_num 0: bottom left DB-9 connector on Device Node
            | input_num 1: bottom right DB-9 connector on Device Node
            | input_num 2: top right DB-9 connector on Device Node
            | input_num 3: top left DB-9 connector on Device Node

        :return: pressure value
        :rtype: float, None
        """
        return 5.

    def get_all_mass_flow_values(self) -> List[float]:
        """
        Get all of the pressure readings a SciLog Device Node.

        The method will always return a list of length 12. Inputs with valid pressure
        readings will return a `float` value. Inputs without valid readings
        will return `None`.

        =====  ==========  =================
        Index  Input Num     Input Location
        =====  ==========  =================
          0        0          bottom left
          1        1          bottom left
          2        2          bottom left
          3        3         bottom right
        =====  ==========  =================

        :Example: read all transducers:

        .. code-block:: python

            pressures = MFMSIM.get_all_mass_flow_values()
            len(pressures) # 4

        :return: pressure values
        :rtype: list
        """
        return (5, 7, 45, 67)

    def set_sim_mass_flow(self, value: float = 0., input_num: int = 0) -> None:
        """
        Set the simulated pressure reading for one of the MFM's 4 possible transducer inputs.

        Only functions in Sim Mode.

        The *input_num* argument selects the input channel (one of the 4 possible positions for
        an attached MFM device).

        :Example: set transducer input 0 to 25 ml/min:

        .. code-block:: python

            MFMSIM.set_sim_mass_flow(25,1)

        :param value: pressure value
        :type value: float, int
        :param input_num: input to read from, `0` is first input
        :type input_num: int, {0:3}
        :return: pressure value
        :rtype: float, None
        """
        return {}

    def set_sim_mass_flow_values(self, values: Union[tuple, list]):
        """
        In `Sim` mode, sets the simulated mass flow readings of multiple inputs.

        Pass a tuple or list to set the values.

        If a list or tuple is passed, each element should be a value to set the corresponding input to, eg.

        .. code-block:: python

            MFMSIM.set_sim_mass_flow_values((4.5, , 0.3, ))

        would set input 0 to 4.5 ml/min and input 2 to 0.3 ml/min. Inputs 1 and 3 are not affected.

        where each key is a str or int for an input number and the value of the key is the desired pressure reading.

        :param values: simulated values to assign
        :type values: tuple, list
        :return: None
        """
        return {}

    def set_sim_rates_of_change(self, values: Union[dict, tuple, list]):
        """
        In `Sim` mode, sets the simulated rate-of-change, in grams/s, for the weight readings.

        Pass a dict, tuple, or list to set the values.

        If a list or tuple is passed, each element should be a value to set the corresponding input to, eg.

        .. code-block:: python

            MFMSIM.set_sim_rates_of_change((0.05, , -0.13, ))

        would input 0's rate of change to 0.05 ml/min/s and input 2's rate of change
        to -0.13 ml/min/s. Inputs 1 and 3 are not affected.

        If a dict is pass, the format should be:

        .. code-block:: python

            MFMSIM.set_sim_rates_of_change({
                '0': 4.5,
                 1: 25.
            })

        where each key is a str or int for an input number and the value of the key is the desired weight reading's
        rate of change.

        :param values: simulated rate-of-change values to assign
        :type values: dict, tuple, list
        :return: None
        """
        return {}

    def set_sim_noise(self, active: int = 1, values: Union[dict, tuple, list] = ()) -> None:
        """
        In `Sim` mode, simulated noise is added to the pressure readings by default.

        Turn off the simulated noise by passing ``active = 0``

        Turn on the simulated noise by passing ``active = 1``

        Affects all inputs.

        :Example: turn off the simulated noise of the :class:`MFM` device named `MFMSIM`:

        .. code-block:: python

            MFMSIM.set_sim_noise(active=0)

        Alternatively, adjust the simulated noise for individual inputs by passing
        a dict, tuple, or list to set the `values` argument.

        If a list or tuple is passed, each element should be a value to set the corresponding input to, eg.

        .. code-block:: python

            MFMSIM.set_sim_noise((0.05, , -0.13, ))

        would set input 0's simulated noise to 0.05 g and input 2's simulated noise
        to -0.13 g. Inputs 1 and 3 would are not affected.

        If a `dict` is passed, the format should be:

        .. code-block:: python

            MFMSIM.set_sim_noise({
                '0': 4.5,
                 1: 25.
            })

        where each key is a str or int for an input number and the value of the key is the desired input's
        simulated noise.

        :param active: noise control toggle
        :type active: int, {0,1}
        :param values: simulated values to assign
        :type values: dict, tuple, list
        :return: None
        """
        return {}

