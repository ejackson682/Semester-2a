from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z
stairBlock = 53
step = 0
while step < 10:
 mc.setblock(x + step, y + step, z, stairBlock)
 step += 1
