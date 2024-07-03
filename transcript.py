import sys
import traceback
from nxpython import *
createProject("/home/desktop/Projects/large-blinker")
getProject().loadNative("/home/desktop/Projects/large-blinker/large-blinker.nym")
getProject().setDescription("")
getProject().save("/home/desktop/Projects/large-blinker/large-blinker.nym")
getProject().save("/home/desktop/Projects/large-blinker/native-auto.nym")
getProject().progress("Synthesize", 3)
getProject().clearPads()
getProject().addPad("clk", differential=False, drive="2mA", inputDelayLine=0, inputSignalSlope=0, location="IOB0_D01P", outputCapacity=0, outputDelayLine=0, slewRate="Medium", standard="LVCMOS", terminationReference="VT", turbo=False, weakTermination="PullUp")
getProject().addPad("led", differential=False, drive="2mA", inputDelayLine=0, inputSignalSlope=0, location="IOB11_D05N", outputCapacity=0, outputDelayLine=0, slewRate="Medium", standard="LVCMOS", terminationReference="VT", turbo=False, weakTermination="PullUp")
getProject().clearBanks()
getProject().clearPins()
getProject().clearWFGs()
getProject().progress("Place", 5)
getProject().progress("Route", 3)
getProject().generateBitstream("/home/desktop/Projects/large-blinker/output/large-blinker.nxb")
getProject().destroy()
