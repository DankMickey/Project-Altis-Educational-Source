from panda3d.core import *
from ToonHood import ToonHood
from toontown.town import CPTownLoader
from toontown.safezone import CPSafeZoneLoader
from toontown.toonbase.ToontownGlobals import *

class CPHood(ToonHood):
    ID = ChestnutPark
    SAFEZONELOADER_CLASS = CPSafeZoneLoader.CPSafeZoneLoader
    STORAGE_DNA = 'phase_6/dna/storage_CP.pdna'
    SKY_FILE = 'phase_6/models/modules/unpainted_sky.bam'
    SPOOKY_SKY_FILE = 'phase_3.5/models/props/BR_sky'
    TITLE_COLOR = (1.0, 0.5, 0.4, 1.0)

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.underwaterColor = Vec4(0, 0, 0.6, 1)

    def load(self):
        ToonHood.load(self)

        self.fog = Fog('OZFog')

    def enter(self, requestStatus):
        ToonHood.enter(self, requestStatus)

        base.camLens.setNearFar(SpeedwayCameraNear, SpeedwayCameraFar)

    def exit(self):
        base.camLens.setNearFar(DefaultCameraNear, DefaultCameraFar)

        ToonHood.exit(self)

    def setUnderwaterFog(self):
        if base.wantFog:
            self.fog.setColor(self.underwaterFogColor)
            self.fog.setLinearRange(0.1, 100.0)
            render.setFog(self.fog)
            self.sky.setFog(self.fog)

    def setWhiteFog(self):
        if base.wantFog:
            self.fog.setColor(self.whiteFogColor)
            self.fog.setLinearRange(0.0, 400.0)
            render.clearFog()
            render.setFog(self.fog)
            self.sky.clearFog()
            self.sky.setFog(self.fog)

    def setNoFog(self):
        if base.wantFog:
            render.clearFog()
            self.sky.clearFog()