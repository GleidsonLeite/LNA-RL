from modules.Circuit.Entities.NFet01v8 import NFet01v8


fet = NFet01v8(name="test", length=0.15, width=1, fet_type="sky130_fd_pr__nfet_01v8")
fet.length = -1
