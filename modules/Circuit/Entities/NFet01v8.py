from Errors.InvalidComponentValueError import InvalidComponentValueError
from PySpice.Spice.Netlist import SubCircuit


class NFet01v8(SubCircuit):
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

    @property
    def length(self) -> float:
        component_length: float = self.element("XM1").parameters["L"]
        return component_length

    @length.setter
    def length(self, new_length: float) -> None:
        if new_length <= 0:
            raise InvalidComponentValueError(
                value=new_length, message="You should provide a positive value"
            )
        self.element("XM1").parameters["L"] = new_length

    @property
    def width(self) -> float:
        component_width: float = self.element("XM1").parameters["W"]
        return component_width

    @width.setter
    def width(self, new_width: float) -> None:
        if new_width <= 0:
            raise InvalidComponentValueError(
                value=new_width, message="You should provide a positive value"
            )
        self.element("XM1").parameters["W"] = new_width
