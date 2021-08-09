from modules.Circuit.Entities.Source import Source
from PySpice.Spice.Netlist import Circuit
from modules.Circuit.Entities.LNA import LNA

techology_directory = (
    "/edatools/opentools/skywater-pdk/libraries/sky130_fd_pr/latest"
)

circuit = Circuit("LNA Test")
circuit.include(f"{techology_directory}/models/corners/tt.spice")

lnaBlock = LNA(
    name="LNA",
    nfet_type="sky130_fd_pr__nfet_01v8",
    pfet_type="sky130_fd_pr__pfet_01v8",
)

sourceBlock = Source(
    name="SourceCircuit",
    signal_amplitude=0.5,
    v_pol_1=1.10,
    v_pol_2=0.68,
    vcc=1.8,
    vdd=1.8,
)

circuit.subcircuit(lnaBlock)

circuit.X(
    "amplifier", "LNA", "IN", "OUT", "VCC", "VDD", "VPOL1", "VPOL2", circuit.gnd
)
circuit.X(
    "source", "SourceCircuit", "IN", "VCC", "VDD", "VPOL1", "VPOL2", circuit.gnd
)
circuit.R("Rtest", "OUT", circuit.gnd, 50)


print(circuit)
