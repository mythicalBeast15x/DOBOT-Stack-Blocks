import DobotDllType as dType

api = dType.load()

#connect Dobot
state = dType.ConnectDobot(api, "COM5", 115200)[0]

print('Dobot Connected...')
suction_cup = 1
enable_pump = 1
ctrl_mode = 1
pos = dType.GetPose(api)
x = pos[0]
y = pos [1]
z = pos[2]
rHead = pos[3]

print(x, y, z, rHead)


# SETUP------
dType.SetHOMEParams(api, x,  y,  z,  rHead)
dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200)
dType.SetPTPCommonParams(api, 100, 100)

ptpMode = 0

#dType.SetPTPCmd(api, 0, x, y, z, rHead, 0)
#dType.dSleep(2000)
# -----------
#b1
enable_pump = 1
dType.SetEndEffectorSuctionCup(api, suction_cup, enable_pump, ctrl_mode)

dType.SetPTPCmd(api, 2, x, y, z+30, rHead, 0)
dType.SetPTPCmd(api, 2, x, y-150, z+30, rHead, 0)
dType.SetPTPCmd(api, 2, x, y-150, z, rHead, 0)

enable_pump = 0
dType.SetEndEffectorSuctionCup(api, suction_cup, enable_pump, ctrl_mode)
dType.dSleep(4000)

dType.SetPTPCmd(api, 2, x, y-150, z+60, rHead, 0)
dType.SetPTPCmd(api, 2, x, y-40, z+30, rHead, 0)
dType.SetPTPCmd(api, 2, x, y-40, z, rHead, 0)

enable_pump = 1
dType.SetEndEffectorSuctionCup(api, suction_cup, enable_pump, ctrl_mode)
dType.SetPTPCmd(api, 2, x, y-40, z+60, rHead, 0)
dType.SetPTPCmd(api, 2, x, y-150, z+60, rHead, 0)
dType.SetPTPCmd(api, 2, x, y-150, z+30, rHead, 0)
enable_pump = 0
dType.SetEndEffectorSuctionCup(api, suction_cup, enable_pump, ctrl_mode)

dType.SetPTPCmd(api, 2, x, y-150, z+90, rHead, 0)
dType.SetPTPCmd(api, 2, x+10, y-80, z+90, rHead, 0)
dType.SetPTPCmd(api, 2, x+10, y-80, z, rHead, 0)

enable_pump = 1
dType.SetEndEffectorSuctionCup(api, suction_cup, enable_pump, ctrl_mode)
dType.dSleep(4000)

dType.SetPTPCmd(api, 2, x+10, y-80, z+90, rHead, 0)
dType.SetPTPCmd(api, 2, x, y-150, z+90, rHead, 0)
dType.SetPTPCmd(api, 2, x, y-150, z+60, rHead, 0)

enable_pump = 0
dType.SetEndEffectorSuctionCup(api, suction_cup, enable_pump, ctrl_mode)
dType.dSleep(4000)