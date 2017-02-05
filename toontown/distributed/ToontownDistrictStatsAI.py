from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.toon import DistributedToonAI
from toontown.toonbase import ToontownGlobals

class ToontownDistrictStatsAI(DistributedObjectAI):
    notify = directNotify.newCategory('ToontownDistrictStatsAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.districtId = 0
        self.avatarCount = 0
        self.newAvatarCount = 0
        self.invasionStatus = 0
        groupToonCount = [0] * 10 # we have 10 group types

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

        # We want to handle shard status queries so that a ShardStatusReceiver
        # being created after we're generated will know where we're at:
        self.air.netMessenger.accept('queryShardStatus', self, self.handleShardStatusQuery)
        taskMgr.doMethodLater(20, self.__checkGroups, self.uniqueName('checkGroups'))
        
    def delete(self):
        taskMgr.remove(self.uniqueName('checkGroups'))
        DistributedObjectAI.delete(self)

    def handleShardStatusQuery(self):
        # Send a shard status update containing our population:
        self.air.netMessenger.send('shardStatus', [self.air.ourChannel, {'population': \
            self.avatarCount}])

    def settoontownDistrictId(self, districtId):
        self.districtId = districtId

    def d_settoontownDistrictId(self, districtId):
        self.sendUpdate('settoontownDistrictId', [districtId])

    def b_settoontownDistrictId(self, districtId):
        self.settoontownDistrictId(districtId)
        self.d_settoontownDistrictId(districtId)

    def gettoontownDistrictId(self):
        return self.districtId

    def setAvatarCount(self, avatarCount):
        self.avatarCount = avatarCount

        # Send a shard status update containing our population:
        self.air.netMessenger.send('shardStatus', [self.air.ourChannel, {'population': \
            self.avatarCount}])

    def d_setAvatarCount(self, avatarCount):
        self.sendUpdate('setAvatarCount', [avatarCount])

    def b_setAvatarCount(self, avatarCount):
        self.d_setAvatarCount(avatarCount)
        self.setAvatarCount(avatarCount)

    def getAvatarCount(self):
        return self.avatarCount

    def setNewAvatarCount(self, newAvatarCount):
        self.newAvatarCount = newAvatarCount

    def d_setNewAvatarCount(self, newAvatarCount):
        self.sendUpdate('setNewAvatarCount', [newAvatarCount])

    def b_setNewAvatarCount(self, newAvatarCount):
        self.setNewAvatarCount(newAvatarCount)
        self.d_setNewAvatarCount(newAvatarCount)

    def getNewAvatarCount(self):
        return self.newAvatarCount

    def setInvasionStatus(self, invasionStatus):
        self.invasionStatus = invasionStatus

    def d_setInvasionStatus(self, invasionStatus):
        self.sendUpdate('setInvasionStatus', [invasionStatus])

    def b_setInvasionStatus(self, invasionStatus):
        self.setInvasionStatus(invasionStatus)
        self.d_setInvasionStatus(invasionStatus)

    def getInvasionStatus(self):
        return self.invasionStatus
        
    def setGroupToonCount(self, groupToonCount):
        self.groupToonCount = groupToonCount
        
    def d_setGroupAvCount(self, groupToonCount):
        self.sendUpdate('setGroupToonCount', [groupToonCount])
        
    def b_setGroupToonCount(self, groupToonCount):
        self.setGroupToonCount(groupToonCount)
        self.d_setGroupToonCount(groupToonCount)
        
    def getGroupToonCount(self):
        return self.groupToonCount
        
    def __checkGroups(self, task)
        groupAllowedAreas = [11000, 11100, 11200, 12000, 12100, 13000, 13100, 13200, 10000, 10100]
        self.groupToonCount = [0] * 10
        
        for av in self.air.doId2do.values()
            if isinstance(av, DistributedToonAI.DistributedToonAI) and av.isPlayerControlled() and av.zoneId in groupAllowedAreas:
                self.groupToonCount[groupAllowedAreas.index(av.zoneId)] += 1
                
        taskMgr.doMethodLater(20, self.__checkGroups, self.uniqueName("checkGroups"))
        self.b_setGroupToonCount(self.groupToonCount)