#!/usr/bin/env python
"""
c4d.BaseView

Important: these are not real files. They are automatically generated to
ease code completion only.
"""

class BaseView(object):
    """
    CINEMA 4D view window.
    """
    def __init__(self, *args, **kwargs):
        pass


    def AddUserData(self, *args, **kwargs):
        """
        Add a user data.
        """
        pass

    def BackfaceCulling(self, *args, **kwargs):
        """
        Tests the face with center p and normal n for backface culling.
        """
        pass

    def CS(self, *args, **kwargs):
        """
        Camera to screen conversion.
        """
        pass

    def CW(self, *args, **kwargs):
        """
        Camera to world conversion.
        """
        pass

    def CW_V(self, *args, **kwargs):
        """
        World to camera vector conversion
        """
        pass

    def ChangeNBit(self, *args, **kwargs):
        """
        Sets bits in the 64-bit bitfield of the node.
        """
        pass

    def CheckType(self, *args, **kwargs):
        """
        Checks the type of a basetype.
        """
        pass

    def ClearKeyframeSelection(self, *args, **kwargs):
        """
        Clears the current keyframe selection.
        """
        pass

    def CopyTo(self, *args, **kwargs):
        """
        Copy an Atom object into another.
        """
        pass

    def DelBit(self, *args, **kwargs):
        """
        Deletes the object flags denoted by argument.
        """
        pass

    def Edit(self, *args, **kwargs):
        """
        Triggers the edit action for this object.
        """
        pass

    def FindCTrack(self, *args, **kwargs):
        """
        Returns a track.
        """
        pass

    def FindKeyframeSelection(self, *args, **kwargs):
        """
        Checks if id is included in the keyframe selection.
        """
        pass

    def GetAllBits(self, *args, **kwargs):
        """
        Returns all of the object's bits
        """
        pass

    def GetBit(self, *args, **kwargs):
        """
        Returns the state of the object flags denoted by mask.
        """
        pass

    def GetBubbleHelp(self, *args, **kwargs):
        """
        Returns the bubble help of the object
        """
        pass

    def GetCTrackRoot(self, *args, **kwargs):
        """
        Get the track root of this object.
        """
        pass

    def GetCTracks(self, *args, **kwargs):
        """
        Returns all tracks
        """
        pass

    def GetChildren(self, *args, **kwargs):
        """
        Returns all children in a tuple
        """
        pass

    def GetClassification(self, *args, **kwargs):
        """
        Returns the base type.
        """
        pass

    def GetClone(self, *args, **kwargs):
        """
        Returns a copy of the object.
        """
        pass

    def GetData(self, *args, **kwargs):
        """
        Returns the settings.
        """
        pass

    def GetDataInstance(self, *args, **kwargs):
        """
        Returns a reference to the original settings.
        """
        pass

    def GetDirty(self, *args, **kwargs):
        """
        Gets the dirty checksum for the object.
        """
        pass

    def GetDocument(self, *args, **kwargs):
        """
        Get the document for this node.
        """
        pass

    def GetDown(self, *args, **kwargs):
        """
        Get the first child GeListNode in the list
        """
        pass

    def GetDownLast(self, *args, **kwargs):
        """
        Returns the last child in the list.
        """
        pass

    def GetFirstCTrack(self, *args, **kwargs):
        """
        Returns the first CTrack.
        """
        pass

    def GetFirstShader(self, *args, **kwargs):
        """
        Returns the first shader of the object.
        """
        pass

    def GetFrame(self, *args, **kwargs):
        """
        Returns the dimensions in pixels.
        """
        pass

    def GetIcon(self, *args, **kwargs):
        """
        Returns the icon of the object.
        """
        pass

    def GetInfo(self, *args, **kwargs):
        """
        Returns the information flags.
        """
        pass

    def GetLayerData(self, *args, **kwargs):
        """
        Get the layer data for this object.
        """
        pass

    def GetLayerObject(self, *args, **kwargs):
        """
        Get the layer of this object.
        """
        pass

    def GetListHead(self, *args, **kwargs):
        """
        Get the list head for this node.
        """
        pass

    def GetMain(self, *args, **kwargs):
        """
        Goes one level up.
        """
        pass

    def GetMg(self, *args, **kwargs):
        """
        Returns the camera matrix.
        """
        pass

    def GetMi(self, *args, **kwargs):
        """
        Returns the inverse of the camera matrix.
        """
        pass

    def GetNBit(self, *args, **kwargs):
        """
        Returns bits in the 64-bit bitfield of the node.
        """
        pass

    def GetNLARoot(self, *args, **kwargs):
        """
        Private.
        """
        pass

    def GetName(self, *args, **kwargs):
        """
        Returns the name of the object.
        """
        pass

    def GetNext(self, *args, **kwargs):
        """
        Get the next GeListNode in the list
        """
        pass

    def GetNodeData(self, *args, **kwargs):
        """
        Get the nodedata type.
        """
        pass

    def GetPred(self, *args, **kwargs):
        """
        Get the previous GeListNode in the list
        """
        pass

    def GetProjection(self, *args, **kwargs):
        """
        Returns the projection.
        """
        pass

    def GetSafeFrame(self, *args, **kwargs):
        """
        The positiion in pixels of the render line.
        """
        pass

    def GetType(self, *args, **kwargs):
        """
        Get the type of the atom.
        """
        pass

    def GetTypeName(self, *args, **kwargs):
        """
        The name of the object category.
        """
        pass

    def GetUp(self, *args, **kwargs):
        """
        Get the upper GeListNode in the list
        """
        pass

    def GetUserDataContainer(self, *args, **kwargs):
        """
        Returns the user data container.
        """
        pass

    def GetViewParameter(self, *args, **kwargs):
        """
        Retrieves the parameters for the current projection.
        """
        pass

    def InsertAfter(self, *args, **kwargs):
        """
        Insert after object.
        """
        pass

    def InsertBefore(self, *args, **kwargs):
        """
        Insert before object.
        """
        pass

    def InsertShader(self, *args, **kwargs):
        """
        Inserts a shader in the object's shader list.
        """
        pass

    def InsertTrackSorted(self, *args, **kwargs):
        """
        Insert a new track.
        """
        pass

    def InsertUnder(self, *args, **kwargs):
        """
        Insert under object.
        """
        pass

    def InsertUnderLast(self, *args, **kwargs):
        """
        Insert this node as the last child.
        """
        pass

    def IsAlive(self, *args, **kwargs):
        """
        Returns if the object is still alive.
        """
        pass

    def IsDocumentRelated(self, *args, **kwargs):
        """
        Checks if can be insert into a document.
        """
        pass

    def KeyframeSelectionContent(self, *args, **kwargs):
        """
        Checks if there are any active keyframe selections.
        """
        pass

    def Message(self, *args, **kwargs):
        """
        Sends a message to the object.
        """
        pass

    def MultiMessage(self, *args, **kwargs):
        """
        Sends a message to the atom and to its children, parents or branches.
        """
        pass

    def Read(self, *args, **kwargs):
        """
        Reads to this atom.
        """
        pass

    def ReadObject(self, *args, **kwargs):
        """
        Reads to this atom.
        """
        pass

    def Remove(self, *args, **kwargs):
        """
        Remove this node from its list.
        """
        pass

    def RemoveUserData(self, *args, **kwargs):
        """
        Remove a user data.
        """
        pass

    def SC(self, *args, **kwargs):
        """
        Screen to camera conversion.
        """
        pass

    def SW(self, *args, **kwargs):
        """
        Screen to world conversion.
        """
        pass

    def Scale(self, *args, **kwargs):
        """
        Scales the object.
        """
        pass

    def SetAllBits(self, *args, **kwargs):
        """
        Set all of the object's bits
        """
        pass

    def SetBit(self, *args, **kwargs):
        """
        Each object contains a number of flags.
        """
        pass

    def SetData(self, *args, **kwargs):
        """
        Set the settings.
        """
        pass

    def SetDirty(self, *args, **kwargs):
        """
        Sets the dirty checksum for the object.
        """
        pass

    def SetKeyframeSelection(self, *args, **kwargs):
        """
        Sets the keyframe selection status.
        """
        pass

    def SetLayerData(self, *args, **kwargs):
        """
        Set the layer data for this object.
        """
        pass

    def SetLayerObject(self, *args, **kwargs):
        """
        Set the layer of this object.
        """
        pass

    def SetName(self, *args, **kwargs):
        """
        Set the name of the object
        """
        pass

    def SetUserDataContainer(self, *args, **kwargs):
        """
        Set the user data container.
        """
        pass

    def TestClipping3D(self, *args, **kwargs):
        """
        Tests if a bounding box is visible.
        """
        pass

    def TestPoint(self, *args, **kwargs):
        """
        Returns TRUE if the point is within the boundary.
        """
        pass

    def TestPointZ(self, *args, **kwargs):
        """
        Returns TRUE if the point is visible in the view.
        """
        pass

    def ToggleBit(self, *args, **kwargs):
        """
        Toggles the state of the object flags denoted by the argument.
        """
        pass

    def TransferGoal(self, *args, **kwargs):
        """
        Transfer goals from this object to dst.
        """
        pass

    def WC(self, *args, **kwargs):
        """
        World to camera conversion.
        """
        pass

    def WC_V(self, *args, **kwargs):
        """
        Camera to screen conversion.
        """
        pass

    def WS(self, *args, **kwargs):
        """
        World to screen conversion.
        """
        pass

    def Write(self, *args, **kwargs):
        """
        Writes this atom.
        """
        pass

    def WriteObject(self, *args, **kwargs):
        """
        Writes this atom.
        """
        pass

    def ZSensitiveFar(self, *args, **kwargs):
        """
        Indicates if the view has Z far clipping.
        """
        pass

    def ZSensitiveFarClipping(self, *args, **kwargs):
        """
        Returns the far clipping of Z sensitive view.
        """
        pass

    def ZSensitiveNear(self, *args, **kwargs):
        """
        Indicates if the view has Z near clipping.
        """
        pass

    def ZSensitiveNearClipping(self, *args, **kwargs):
        """
        Returns the near clipping of Z sensitive view.
        """
        pass
