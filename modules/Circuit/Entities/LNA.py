from modules.Circuit.Entities.PFet01v8 import PFet01v8
from modules.Circuit.Entities.NFet01v8 import NFet01v8
from PySpice.Spice.Netlist import SubCircuit


class LNA(SubCircuit):
    NODES = ("IN", "OUT", "VCC", "VDD", "VPOL1", "VPOL2", "GND")

    def __init__(self, name: str, nfet_type: str, pfet_type: str):
        super().__init__(name, *self.NODES)

        self.nfet1 = NFet01v8(
            name="NFET1", fet_type=nfet_type, length=2.2, width=68.3
        )
        self.pfet2 = PFet01v8(
            name="PFET2", fet_type=pfet_type, length=39.9, width=1.1
        )
        self.nfet3 = NFet01v8(
            name="NFET3", fet_type=nfet_type, length=48, width=6.5
        )

        self.subcircuit(self.nfet1)
        self.subcircuit(self.pfet2)
        self.subcircuit(self.nfet3)

        self.L("LG", "IN", "PLG", 5.8e-9)
        self.R("RPOL1", "PLG", "VPOL1", 19939)
        self.X("M1", "NFETW1", "PRF", "PLG", "GND", "GND")
        self.C("C1", "PC1", "PLG", 19.7e-12)
        self.R("RF", "PC1", "PRF", 19540)
        self.X("M2", "PFET2", "VCC", "PC1", "PRF", "GND")
        self.C("CDEC", "VCC", "GND", 1e-6)
        self.C("CM1", "PRF", "PCM1", 4.7e-12)
        self.R("RPOL2", "PCM1", "VPOL2", 13548)
        self.X("M3", "NFETW3", "PM3", "PCM1", "GND", "GND")
        self.L("LPK", "VDD", "PM3", 7.6e-9)
        self.C("CM2", "PM3", "OUT", 0.65e-12)
        self.C("CM3", "PM3", "GND", 4.7e-12)

    @property
    def LG(self) -> float:
        inductance: float = self.element("LLG").inductance
        return inductance

    @LG.setter
    def LG(self, inductance: float) -> None:
        self.element("LLG").inductance = inductance

    @property
    def RPOL1(self) -> float:
        resistance: float = self.element("RRPOL1")
        return resistance

    @RPOL1.setter
    def RPOL1(self, resistance: float) -> None:
        self.element("RRPOL1").resistance = resistance

    @property
    def RPOL2(self) -> float:
        resistance: float = self.element("RRPOL2")
        return resistance

    @RPOL2.setter
    def RPOL2(self, resistance: float) -> None:
        self.element("RRPOL2").resistance = resistance

    @property
    def C1(self) -> float:
        capacitance: float = self.element("CC1").capacitance
        return capacitance

    @C1.setter
    def C1(self, capacitance: float) -> None:
        self.element("CC1").capacitance = capacitance

    @property
    def CM1(self) -> float:
        capacitance: float = self.circuit.element("CCM1").capacitance
        return capacitance

    @CM1.setter
    def CM1(self, capacitance: float) -> None:
        self.circuit.element("CCM1").capacitance = capacitance

    @property
    def CM2(self) -> float:
        capacitance: float = self.circuit.element("CCM2").capacitance
        return capacitance

    @CM2.setter
    def CM2(self, capacitance: float) -> None:
        self.self.circuit("CCM2").capacitance = capacitance

    @property
    def CM3(self) -> float:
        capacitance: float = self.circuit.element("CCM3").capacitance
        return capacitance

    @CM3.setter
    def CM3(self, capacitance: float) -> None:
        self.self.circuit("CCM3").capacitance = capacitance

    @property
    def RF(self) -> float:
        resistance: float = self.circuit.element("RRF").resistance
        return resistance

    @RF.setter
    def RF(self, resistance: float) -> None:
        self.circuit.element("RRF").resistance = resistance

    @property
    def CDEC(self) -> float:
        capacitance: float = self.circuit.element("CCDEC").capacitance
        return capacitance

    @property
    def LPK(self) -> float:
        inductance: float = self.circuit.element("LLPK").inductance
        return inductance

    @LPK.setter
    def LPK(self, inductance: float) -> None:
        self.circuit.element("LLPK").inductance = inductance
