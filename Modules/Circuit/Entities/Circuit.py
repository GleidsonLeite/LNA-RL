from Modules.Circuit.Entities.Source import Source
from Modules.Circuit.Entities.LNA import LNA
from typing import Iterable
from PySpice.Spice.Netlist import Circuit as PySpiceCircuit

test: Iterable[str] = ("oi", "teste")


class Circuit(PySpiceCircuit):
    def __init__(
        self,
        title: str,
        technology_directory_path: str,
        nfet_type: str,
        pfet_type: str,
        ground: int = 0,
        global_nodes: Iterable[str] = (),
    ):
        super().__init__(title, ground=ground, global_nodes=global_nodes)

        self.include(technology_directory_path)

        self.lna_block = LNA("LNA", nfet_type=nfet_type, pfet_type=pfet_type)

        self.source_block = Source(
            "SourceCircuit",
            signal_amplitude=0.5,
            v_pol_1=1.10,
            v_pol_2=0.68,
            vcc=1.8,
            vdd=1.8,
        )

        self.subcircuit(self.lna_block)
        self.subcircuit(self.source_block)

        self.X(
            "amplifier",
            "LNA",
            "IN",
            "OUT",
            "VCC",
            "VDD",
            "VPOL1",
            "VPOL2",
            self.gnd,
        )

        self.X(
            "source",
            "SourceCircuit",
            "IN",
            "VCC",
            "VDD",
            "VPOL1",
            "VPOL2",
            self.gnd,
        )

        self.R("Rtest", "OUT", self.gnd, 50)
