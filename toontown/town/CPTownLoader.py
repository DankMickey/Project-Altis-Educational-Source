import TownLoader
import CPStreet

class CPTownLoader(TownLoader.TownLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        TownLoader.TownLoader.__init__(self, hood, parentFSM, doneEvent)
        self.streetClass = CPStreet.CPStreet
        self.musicFile = 'phase_6/audio/bgm/CP_SZ.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/CP_SZ_activity.ogg'
        self.townStorageDNAFile = 'phase_6/dna/storage_CP_town.pdna'

    def load(self, zoneId):
        TownLoader.TownLoader.load(self, zoneId)
        dnaFile = 'phase_6/dna/chestnut_park_' + str(self.canonicalBranchZone) + '.pdna'
        self.createHood(dnaFile)

    def unload(self):
        TownLoader.TownLoader.unload(self)