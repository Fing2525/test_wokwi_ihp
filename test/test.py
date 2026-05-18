
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def and_gate_test(dut):

    dut.ui_in.value = 0b00000011
    await Timer(1, units="ns")

    assert dut.uo_out.value & 1 == 1

    dut.ui_in.value = 0b00000010
    await Timer(1, units="ns")

    assert dut.uo_out.value & 1 == 0
