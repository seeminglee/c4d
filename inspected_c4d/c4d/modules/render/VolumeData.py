#!/usr/bin/env python
"""
c4d.modules.render.VolumeData

Important: these are not real files. They are automatically generated to
ease code completion only.
"""

class VolumeData(object):
    """
    Base volume data information class.
    """
    def __init__(self, *args, **kwargs):
        self.alpha = None
        self.ambient = None
        self.back_delta = None
        self.back_p = None
        self.bumpn = None
        self.calc_illum = None
        self.calc_mip = None
        self.calc_refl = None
        self.calc_shadow = None
        self.calc_trans = None
        self.col = None
        self.cosc = None
        self.ddu = None
        self.ddv = None
        self.delta = None
        self.dispn = None
        self.dist = None
        self.fps = None
        self.global_mip = None
        self.lhit = None
        self.n = None
        self.nn = None
        self.orign = None
        self.p = None
        self.par_u = None
        self.par_v = None
        self.pp = None
        self.ray = None
        self.raybits = None
        self.raydepth = None
        self.recursion_id = None
        self.refl = None
        self.rray = None
        self.sid = None
        self.time = None
        self.trans = None
        self.tray = None
        self.uvw = None
        self.version = None


    def CalcArea(self, *args, **kwargs):
        """
        Sample area lights.
        """
        pass

    def CalcFgBg(self, *args, **kwargs):
        """
        Calculates the foreground or background.
        """
        pass

    def CalcShadow(self, *args, **kwargs):
        """
        Computes the shadow.
        """
        pass

    def CalcVisibleLight(self, *args, **kwargs):
        """
        Return the mixed color of all visible lights on a given ray span.
        """
        pass

    def CameraToScreen(self, *args, **kwargs):
        """
        Transform screen to camera coordinates.
        """
        pass

    def CopyTo(self, *args, **kwargs):
        """
        Copy this to another VolumeData.
        """
        pass

    def FindVideoPost(self, *args, **kwargs):
        """
        Returns a video post effect for this render process by ID.
        """
        pass

    def GetCPUCount(self, *args, **kwargs):
        """
        The cpu count.
        """
        pass

    def GetCurrentCPU(self, *args, **kwargs):
        """
        The current cpu.
        """
        pass

    def GetLight(self, *args, **kwargs):
        """
        Get the light source.
        """
        pass

    def GetLightCount(self, *args, **kwargs):
        """
        The light count.
        """
        pass

    def GetLightFalloff(self, *args, **kwargs):
        """
        Calculate the light falloff function.
        """
        pass

    def GetObjCount(self, *args, **kwargs):
        """
        The object count.
        """
        pass

    def GetRS(self, *args, **kwargs):
        """
        Calculate the R/S parameters for a point.
        """
        pass

    def GetRay(self, *args, **kwargs):
        """
        Generate the view ray for a position.
        """
        pass

    def GetSkyCount(self, *args, **kwargs):
        """
        The sky count.
        """
        pass

    def GetSmoothedNormal(self, *args, **kwargs):
        """
        Returns the phong normal for a point.
        """
        pass

    def GetVideoPost(self, *args, **kwargs):
        """
        Returns the n-th video post effect for this render process.
        """
        pass

    def GetWeights(self, *args, **kwargs):
        """
        Returns barycentric coordinates for a point on the surface of a polygon.
        """
        pass

    def GetXY(self, *args, **kwargs):
        """
        Returns the current X/Y pixel position in render resolution.
        """
        pass

    def IlluminanceAnyPoint(self, *args, **kwargs):
        """
        Used for custom illumination models.
        """
        pass

    def IlluminateSurfacePoint(self, *args, **kwargs):
        """
        Calculate the intensity of incoming light for a given light and surface point.
        """
        pass

    def Init(self, *args, **kwargs):
        """
        Initializes the values of this object with values from another object.
        """
        pass

    def OutOfMemory(self, *args, **kwargs):
        """
        Notify on out of memory.
        """
        pass

    def ScreenToCamera(self, *args, **kwargs):
        """
        Transform camera to screen coordinates.
        """
        pass

    def SetXY(self, *args, **kwargs):
        """
        Sets the current X/Y pixel position.
        """
        pass

    def SkipRenderProcess(self, *args, **kwargs):
        """
        Skip the render process.
        """
        pass

    def StatusSetBar(self, *args, **kwargs):
        """
        Set the progress bar
        """
        pass

    def StatusSetSpinMode(self, *args, **kwargs):
        """
        Set the render progress bar spinning.
        """
        pass

    def StatusSetText(self, *args, **kwargs):
        """
        Set the status bar text
        """
        pass
