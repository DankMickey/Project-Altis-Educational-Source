from pandac.PandaModules import *
from toontown.toon.DistributedNPCToon import *

class DistributedNPCCog(DistributedNPCToon):

    def __init__(self, cr):
        DistributedNPCToon.__init__(self, cr)
        self.npcType = "Cog"

    def initPos(self):
        self.putOnSuit('f')