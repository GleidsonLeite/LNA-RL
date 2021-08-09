from Modules.Circuit.Entities.Circuit import Circuit
from Modules.Circuit.UseCases.GetACAnalysis import GetACAnalysisUseCase

techology_directory = (
    "/edatools/opentools/skywater-pdk/libraries/sky130_fd_pr/latest"
)

technology_file_path = f"{techology_directory}/models/corners/tt.spice"

circuit = Circuit(
    title="LNA Test",
    technology_directory_path=technology_file_path,
    nfet_type="sky130_fd_pr__nfet_01v8",
    pfet_type="sky130_fd_pr__pfet_01v8",
)

getACAnalysisUseCase = GetACAnalysisUseCase()
analysis = getACAnalysisUseCase.execute(
    circuit=circuit, start_frequency=1, stop_frequency=1e9
)

print(analysis.nodes["out"].as_ndarray())
