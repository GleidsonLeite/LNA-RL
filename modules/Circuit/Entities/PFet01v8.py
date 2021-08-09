from PySpice.Spice.Netlist import SubCircuit


class PFet01v8(SubCircuit):

    NODES = ("DRAIN", "GATE", "SOURCE", "SUBSTRATE")

    def __init__(self, name: str, fet_type: str, length: float, width: float) -> None:
        super().__init__(name, *self.NODES)
        self.X(
            "M1",
            fet_type,
            "DRAIN",
            "GATE",
            "SOURCE",
            "SUBSTRATE",
            L=length,
            W=width,
            ad="'W*0.29'",
            pd="'2*(W+0.29)'",
            as_="'W*0.29'",
            ps="'2*(W+0.29)'",
            nrd="'0.29/W'",
            nrs="'0.29/W'",
            sa=0,
            sb=0,
            sd=0,
            nf=1,
            mult=1,
        )
