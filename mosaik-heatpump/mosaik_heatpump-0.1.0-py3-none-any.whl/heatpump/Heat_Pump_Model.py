"""
This module contains a simulation model of a Heat Pump based on the library TESPy.
"""

# from ..model import Model
from mosaik_heatpump.heatpump.Heat_Pump_Des import Heat_Pump_Des


class Heat_Pump_Design():
    """Design of the Heat Pump based on the initial parameters"""
    def __init__(self, params, COP_m_data):
        self.Heat_Pump = Heat_Pump_Des(params, COP_m_data)


class Heat_Pump_State():
    """Attributes that define the state of the Heat_Pump"""
    def __init__(self):
        self.P_Required = 0
        """Power consumption of the heat pump in W"""
        self.COP = 0
        """COP of the heat pump"""
        self.Q_Demand = 0
        """The heat demand of the consumer in W"""
        self.Q_Supplied = 0
        """The heat supplied to the consumer in W"""
        self.cons_T = 0
        """The temperature at which heat is supplied to the consumer (in °C)"""
        self.cond_in_T = 0
        """The temperature at which the water reenters the condenser (in °C)"""
        self.heat_source = 0
        """The source of heat for the heat pump ('water' or 'air')"""
        self.heat_source_T = 0
        """The temperature of the heat source (in °C)"""
        self.cond_m_in = 0
        """The mass flow rate on the condenser side inlet of the heat pump (in kg/s)"""
        self.cond_m_out = 0
        """The mass flow rate on the condenser side outlet of the heat pump (in kg/s)"""


class Heat_Pump_Inputs():
    """Inputs variables to the heat pump for each time step"""
    __slots__ = ['Q_Demand', 'heat_source', 'heat_source_T', 'cons_T', 'step_size', 'cond_in_T']

    def __init__(self, params):
        self.Q_Demand = params.get('Q_Demand')
        """The heat demand of the consumer in W"""

        self.heat_source = params.get('heat_source')
        """The source of heat ('water' or 'air')"""

        self.heat_source_T = params.get('heat_source_T')
        """The temperature of the heat source (in °C)"""

        # self.cons_T = params.get('cons_T')
        # """The temperature at which heat is supplied to the consumer (in °C)"""

        self.cond_in_T = params.get('cond_in_T')
        """The temperature at which the water reenters the condenser (in °C)"""

        self.step_size = None
        """step size in seconds"""


class Heat_Pump():
    """
    Simulation model of a heat pump based on the library TESPy.

    You have to provide the *params* dictionary that contains the parameters
    required for the design of the heat pump. It will look like this::

        {
            'cons_T': 35,
            'heat_source_T': 12,
            'heat_source': 'water' or 'air'
        }

    -*cons_T* is the temperature, in °C, at which heat is supplied to the consumer. This can
    be changed later in the simulation as well.

    -*heat_source_T* is the temperature, in °C, at which the ambient fluid (water or air)
    is available as the heat source.

    -*heat_source* is the fluid, either 'water' or 'air', that acts as the heat source for
    the system.
    """

    __slots__ = ['design', 'state', 'inputs']

    def __init__(self, params, COP_m_data):
        self.design = Heat_Pump_Design(params, COP_m_data)
        """stores the design of the heat pump in a
        :class:`.Heat_Pump_Model.Heat_Pump_Design` object"""
        self.state = Heat_Pump_State()
        """stores the state variables of the heat pump in a
        :class:`.Heat_Pump_Model.Heat_Pump_State` object"""
        self.inputs = Heat_Pump_Inputs(params)
        """stores the input parameters of the heat pump model in a
        :class:`.Heat_Pump_Model.Heat_Pump_Inputs` object"""

    def step(self):
        """
        perform simulation step

        The power consumption of the heat pump in the offdesign mode
        is calculated based on the consumer heat demand and the ambient
        fluid temperature.

        """

        step_inputs = {'heat_source_T': self.inputs.heat_source_T,
                       'Q_Demand': self.inputs.Q_Demand,
                       # 'cons_T': self.inputs.cons_T,
                       'cond_in_T': self.inputs.cond_in_T
                       }

        if self.inputs.Q_Demand is not None:
            self.state.Q_Demand = self.inputs.Q_Demand

        if self.inputs.heat_source_T is not None:
            self.state.heat_source_T = self.inputs.heat_source_T

        if self.inputs.cond_in_T is not None:
            self.state.cond_in_T = self.inputs.cond_in_T

        self.design.Heat_Pump.step(step_inputs)

        self.state.P_Required = self.design.Heat_Pump.P_cons
        self.state.COP = self.design.Heat_Pump.COP
        self.state.Q_Supplied = self.design.Heat_Pump.Q_Supplied
        self.state.cond_m_out = self.design.Heat_Pump.cond_m
        self.state.cond_m_in = - self.design.Heat_Pump.cond_m
        self.state.cons_T = self.design.Heat_Pump.cons_T
