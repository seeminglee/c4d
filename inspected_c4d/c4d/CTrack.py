#!/usr/bin/env python
"""
c4d.CTrack

Important: these are not real files. They are automatically generated to
ease code completion only.
"""

class CTrack(object):
    """
    Animation track base class.
    """
    def __init__(self, *args, **kwargs):
        pass


    def AddUserData(self, *args, **kwargs):
        """
        Add a user data.
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

    def FillKey(self, *args, **kwargs):
        """
        Fills key with default values.
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

    def FlushData(self, *args, **kwargs):
        """
        Flush the CTracks contents.
        """
        pass

    def GetAfter(self, *args, **kwargs):
        """
        Returns the pre loop type.
        """
        pass

    def GetAllBits(self, *args, **kwargs):
        """
        Returns all of the object's bits
        """
        pass

    def GetBefore(self, *args, **kwargs):
        """
        Returns the post loop type before.
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

    def GetCurve(self, *args, **kwargs):
        """
        Returns the CCurve.
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

    def GetDescriptionID(self, *args, **kwargs):
        """
        The description ID of this track.
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

    def GetHeight(self, *args, **kwargs):
        """
        Returns the height of the CTrack in pixels.
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

    def GetObject(self, *args, **kwargs):
        """
        Returns the host object.
        """
        pass

    def GetPred(self, *args, **kwargs):
        """
        Get the previous GeListNode in the list
        """
        pass

    def GetTLHeight(self, *args, **kwargs):
        """
        Returns the height of the MiniFCurve in pixels
        """
        pass

    def GetTrackCategory(self, *args, **kwargs):
        """
        Returns the track category.
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

    def GetUnit(self, *args, **kwargs):
        """
        Returns the unit and step.
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

    def GetValue(self, *args, **kwargs):
        """
        Gets the value of this track at time.
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

    def Remap(self, *args, **kwargs):
        """
        Remaps time.
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

    def Scale(self, *args, **kwargs):
        """
        Scales the object.
        """
        pass

    def SetAfter(self, *args, **kwargs):
        """
        Set the post loop type.
        """
        pass

    def SetAllBits(self, *args, **kwargs):
        """
        Set all of the object's bits
        """
        pass

    def SetBefore(self, *args, **kwargs):
        """
        Set the pre loop type.
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

    def SetDescriptionID(self, *args, **kwargs):
        """
        Set the description ID of this track.
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

    def SetTLHeight(self, *args, **kwargs):
        """
        Set the height of the MiniFCurve in pixels
        """
        pass

    def SetUserDataContainer(self, *args, **kwargs):
        """
        Set the user data container.
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
