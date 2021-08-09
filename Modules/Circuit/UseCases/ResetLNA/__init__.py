from Modules.Circuit.Entities.Source import Source
from Modules.Circuit.Entities.LNA import LNA
from Modules.Circuit.Entities.Circuit import Circuit


class ResetLNAUseCase:
    def execute(self, circuit: Circuit) -> None:

        circuit.lna_block = LNA(
            "LNA",
            nfet_type="sky130_fd_pr__nfet_01v8",
            pfet_type="sky130_fd_pr__pfet_01v8",
        )

        circuit.source_block = Source(
            "SourceCircuit",
            signal_amplitude=0.5,
            v_pol_1=1.10,
            v_pol_2=0.68,
            vcc=1.8,
            vdd=1.8,
        )
