from typing import List, Union

import config
import devices.base.obj
from devices.aqueduct.ohsa.constants import *


def instantiate_device(d_device, setup):
    return OHSA(**d_device)


class OHSA(devices.base.obj.Device):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def start(self, interval_s: float = 1., record: bool = False):
        """Start receiving data from the OHSA device at the specified ``interval_s`` in seconds.

        The OHSA device must be started to begin continuously updating readings from any attached
        balances. This method should be called in a Recipe prior to using the :py:func:`weight` method to read out data.

        This method has no effect if the OHSA device has already been started 
        and the py:func:`start` method is called again.

        :Example: start the :class:`OHSA` named `OHSASIM` with an update interval of 1 second:

        .. code-block:: python

            OHSASIM.start()

        To record data, set the ``record`` argument to ``True``. This will make the weight
        history available for plotting in the user interface.

        :Example: start the :class:`OHSA` named `OHSASIM` with an update interval of 1 second
        and record the data:

        .. code-block:: python

            OHSASIM.start(record=True)

        :param interval_s: number-like value to specify the update interval in seconds
            between the Hub and the OHSA Device Node
        :type interval_s: float, int, defaults to 1.
        :param record: record the data from each balance
        :type record: bool

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def stop(self):
        """Stop receiving data from the OHSA device.

        After stopping the OHSA device, data will no longer be accessible 
        through the :py:func:`weight` method .

        This method has no effect if the OHSA device has already been stopped 
        and the py:func:`stop` method is called again.

        :Example: stop the :class:`OHSA` named `OHSASIM`:

        .. code-block:: python

            OHSASIM.stop()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def clear_recorded(self):
        """Clear the recorded data for the OHSA device. The recordable data includes:

        ====================
          Recordable Data
        ====================
          weight
        ====================

        for each input.

        :Example: clear the recorded data for the OHSA device names OHSASIM:

        .. code-block:: python

            OHSASIM.clear_recorded()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def tare(self, index: int = 0):
        """Send a tare command to one of the four balance inputs.

        This is equivalent to pressing the `tare` button on the Ohaus Adventurer balance.

        :Example: tare input 1 of the :class:`OHSA` device named `OHSASIM`:

        .. code-block:: python

            OHSASIM.tare(input=1)

        :param index: number-like value to specify the input of the balance to tare
        :type index: int, {0:3}
            index 0: bottom left DB-9 connector on Device Node
            index 1: bottom right DB-9 connector on Device Node
            index 2: top right DB-9 connector on Device Node
            index 3: top left DB-9 connector on Device Node
        :return: command dictionary
        :rtype: dict
        """
        return {}

    def weight(self, index: int = 0):
        """
        Get a weight reading from one of the 4 possible Ohaus Adventurer balance inputs. The *input_num* argument
        selects the input channel (one of the 4 possible positions for an attached Ohaus Adventurer balance) to read.

        If no valid input is present or the weight reading is invalid, returns `None`.

        =====  =================
        Index    Input Location
        =====  =================
          0      bottom left
          1      bottom right
          2      top right
          3      top left
        =====  =================

        :Example: read weight from input 0:

        .. code-block:: python

            OHSA.weight(0)

        :Example: read weight from input 3:

        .. code-block:: python

            OHSA.weight(3)

        :param index: input to read from, `0` is first input
        :type index: int, {0:3}
        :return: weight in grams
        :rtype: float, None
        """
        return float(50)


    def get_weight(self, index: int = 0):
        """
        Alias for the py:func:`weight` method.

        :Example: read weight from input 3:

        .. code-block:: python

            OHSA.get_weight(3)

        :param index: input to read from, `0` is first input
        :type index: int, {0:3}
        :return: weight in grams
        :rtype: float, None
        """
        return self.weight(index)

    def get_all_weights(self) -> List[float]:
        """
        Get all of the weight readings from an OHSA Device Node.

        The method will always return a list of length 4. Inputs with valid weight
        readings will return a `float` value. Inputs without valid readings
        will return `None`.

        =====  ==========  =================
        Index  Input Num     Input Location
        =====  ==========  =================
          0        0          bottom left
          1        1          bottom right
          2        2           top right
          3        3           top left
        =====  ==========  =================

        :Example: read all balances:

        .. code-block:: python

            weights = OHSA.get_all_weights()
            len(weights) # 4

        :return: weight values
        :rtype: list
        """
        return tuple(50, 50, 50, 50)

    def set_sim_weight(self, value: float, index: int = 0):
        """
        In `Sim` mode, sets the simulated weight reading for a given balance input.

        Useful for checking logic based on feedback from a balance.

        :Example: set the simulated weight value of input 2 to 400 grams:

        .. code-block:: python

            OHSA.set_sim_weight(400, index=2)

        :param value: simulated value to assign
        :type value: float
        :param index: input to assign the value to, `0` is first input
        :type index: int, {0:3}
        :return: None
        """
        return

    def set_sim_weights(self, values: Union[dict, tuple, list]):
        """
        In `Sim` mode, sets the simulated weights of readings of multiple inputs.

        Pass a dict, tuple, or list to set the values.

        If a list or tuple is passed, each element should be a value to set the corresponding input to, eg.

        .. code-block:: python

            OHSASIM.set_sim_weights((4.5, , 0.3, ))

        would input 0 to 4.5 g and input 2 to 0.3 g. Inputs 1 and 3 would are not affected.

        If a dict is pass, the format should be:

        .. code-block:: python

            OHSASIM.set_sim_weights({
                '0': 4.5,
                 1: 25.
            })

        where each key is a str or int for an input number and the value of the key is the desired weight reading.

        :param values: simulated values to assign
        :type values: dict, tuple, list
        :return: None
        """
        return

    def set_sim_rates_of_change(self, values: Union[dict, tuple, list]):
        """
        In `Sim` mode, sets the simulated rate-of-change, in grams/s, for the weight readings.

        Pass a dict, tuple, or list to set the values.

        If a list or tuple is passed, each element should be a value to set the corresponding input to, eg.

        .. code-block:: python

            OHSASIM.set_sim_rates_of_change((0.05, , -0.13, ))

        would input 0's rate of change to 0.05 g/s and input 2's rate of change
        to -0.13 g/s. Inputs 1 and 3 would are not affected.

        If a dict is pass, the format should be:

        .. code-block:: python

            OHSASIM.set_sim_weights({
                '0': 4.5,
                 1: 25.
            })

        where each key is a str or int for an input number and the value of the key is the desired weight reading's
        rate of change.

        :param values: simulated rate-of-change values to assign
        :type values: dict, tuple, list
        :return: None
        """
        return

    def set_sim_noise(self, active: int = 1, values: Union[dict, tuple, list] = ()) -> None:
        """
        In `Sim` mode, simulated noise is added to the balance weight readings by default.

        Turn off the simulated noise by passing ``active = 0``

        Turn on the simulated noise by passing ``active = 1``

        Affects all inputs.

        :Example: turn off the simulated noise of the :class:`OHSA` device named `OHSASIM`:

        .. code-block:: python

            OHSASIM.set_sim_noise(active=0)

        Alternatively, adjust the simulated noise for individual inputs by passing
        a dict, tuple, or list as the `values` argument.

        If a list or tuple is passed, each element should be a value to set the corresponding input to, eg.

        .. code-block:: python

            OHSASIM.set_sim_noise((0.05, , 1.13, ))

        would set input 0's simulated noise to 0.05 g and input 2's simulated noise
        to 1.13 g. Inputs 1 and 3 would are not affected.
        
        The noise added to the reading during each simulated measurement acquisition
        is selected randomly from a uniform distribution in the range [-v, +v] where v is the noise value assigned.

        If a `dict` is passed, the format should be:

        .. code-block:: python

            OHSASIM.set_sim_noise({
                '0': 0.05,
                 1: 1.13.
            })

        where each key is a str or int for an input number and the value of the key is the desired input's
        simulated noise.

        :param active: noise control toggle
        :type active: int, {0,1}
        :param values: simulated values to assign
        :type values: dict, tuple, list
        :return: None
        """
        return










