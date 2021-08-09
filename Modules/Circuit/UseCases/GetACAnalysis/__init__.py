from Modules.Circuit.DTOs.IACAnalysis import IACANalysis
from Modules.Circuit.DTOs.INGSPICE import INGSPICE
from Modules.Circuit.Entities.Circuit import Circuit


class GetACAnalysisUseCase:
    def execute(
        self,
        circuit: Circuit,
        start_frequency: float,
        stop_frequency: float,
        number_of_points: int = 1000,
        variation: str = "dec",
        temperature: float = 25,
        nominal_temperature: float = 25,
    ) -> IACANalysis:
        simulator = circuit.simulator(
            temperature=temperature, nominal_temperature=nominal_temperature
        )

        analysis: IACANalysis = simulator.ac(
            start_frequency=start_frequency,
            stop_frequency=stop_frequency,
            number_of_points=number_of_points,
            variation=variation,
        )

        ngspice: INGSPICE = simulator.factory(circuit).ngspice
        ngspice.remove_circuit()
        ngspice.destroy()

        return analysis
