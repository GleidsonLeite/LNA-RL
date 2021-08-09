from PySpice.Spice.Netlist import SubCircuit


class Source(SubCircuit):
    NODES = ("IN", "VCC", "VDD", "VPOL1", "VPOL2", "GND")

    def __init__(
        self,
        name: str,
        signal_amplitude: float,
        v_pol_1: float,
        v_pol_2: float,
        vcc: float,
        vdd: float,
    ):
        super().__init__(name, *self.NODES)
        self.SinusoidalVoltageSource("signal", "IN", "GND", signal_amplitude)
        self.V("VCC", "VCC", "GND", vcc)
        self.V("VDD", "VDD", "GND", vdd)
        self.V("VPOL1", "VPOL1", "GND", v_pol_1)
        self.V("VPOL2", "VPOL2", "GND", v_pol_2)

    @property
    def vcc(self) -> float:
        dc_value: float = self.element("VVCC").dc_value
        return dc_value

    @vcc.setter
    def vcc(self, dc_value: float) -> None:
        self.element("VVCC").dc_value = dc_value

    @property
    def vdd(self) -> float:
        vdd_dc_value: float = self.element("VVDD").dc_value
        return vdd_dc_value

    @vdd.setter
    def vdd(self, dc_value: float) -> None:
        self.element("VVDD").dc_value = dc_value

    @property
    def polarization_source_1(self) -> float:
        dc_value: float = self.element("VVPOL1").dc_value
        return dc_value

    @polarization_source_1.setter
    def polarization_source_1(self, dc_value: float) -> None:
        self.element("VVPOL1").dc_value = dc_value

    @property
    def polarization_source_2(self) -> float:
        dc_value: float = self.element("VVPOL2").dc_value
        return dc_value

    @polarization_source_2.setter
    def polarization_source_2(self, dc_value: float) -> None:
        self.element("VVPOL2").dc_value = dc_value
