#!/usr/bin/env python
"""
c4d.documents.BaseDocument

Important: these are not real files. They are automatically generated to
ease code completion only.
"""

class BaseDocument(object):
    """
    Represents a document.
    """
    def __init__(self, *args, **kwargs):
        pass


    def AddUndo(self, *args, **kwargs):
        """
        Perform a redo on this document (undo the last undo).
        """
        pass

    def AddUserData(self, *args, **kwargs):
        """
        Add a user data.
        """
        pass

    def AnimateObject(self, *args, **kwargs):
        """
        Animate a node in this document.
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

    def DoRedo(self, *args, **kwargs):
        """
        Perform a redo on this document (undo the last undo).
        """
        pass

    def DoUndo(self, *args, **kwargs):
        """
        Perform an undo operation.
        """
        pass

    def Edit(self, *args, **kwargs):
        """
        Triggers the edit action for this object.
        """
        pass

    def EndUndo(self, *args, **kwargs):
        """
        End the building of multiple undo actions into a single user undo.
        """
        pass

    def ExecutePasses(self, *args, **kwargs):
        """
        Animate the current frame of the document.
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

    def FindSceneHook(self, *args, **kwargs):
        """
        Finds a scene hook by ID.
        """
        pass

    def Flush(self, *args, **kwargs):
        """
        Empties the document.
        """
        pass

    def ForceCreateBaseDraw(self, *args, **kwargs):
        """
        Makes sure that GetBaseDraw(0) is accessible.
        """
        pass

    def GetAction(self, *args, **kwargs):
        """
        Get the current tool in the editor.
        """
        pass

    def GetActiveBaseDraw(self, *args, **kwargs):
        """
        Get the activate BaseDraw in the editor.
        """
        pass

    def GetActiveMaterial(self, *args, **kwargs):
        """
        Get the first object BaseMaterial of the document.
        """
        pass

    def GetActiveMaterials(self, *args, **kwargs):
        """
        Inserts the material into the document's material list.
        """
        pass

    def GetActiveObject(self, *args, **kwargs):
        """
        Get the currently active object in this document.
        """
        pass

    def GetActiveObjects(self, *args, **kwargs):
        """
        Returns the BaseTag selection.
        """
        pass

    def GetActiveObjectsFilter(self, *args, **kwargs):
        """
        Returns the active objects filter list.
        """
        pass

    def GetActiveRenderData(self, *args, **kwargs):
        """
        Get the active render settings for the document.
        """
        pass

    def GetActiveTag(self, *args, **kwargs):
        """
        Get the currently active tag in this document.

        """
        pass

    def GetActiveTags(self, *args, **kwargs):
        """
        Returns the BaseTag selection.
        """
        pass

    def GetActiveToolData(self, *args, **kwargs):
        """
        Returns the current active tool.
        """
        pass

    def GetAllBits(self, *args, **kwargs):
        """
        Returns all of the object's bits
        """
        pass

    def GetAllTextures(self, *args, **kwargs):
        """
        Returns all textures in the document.
        """
        pass

    def GetBaseDraw(self, *args, **kwargs):
        """
        Get the BaseDraw from one of the editor views.
        """
        pass

    def GetBaseDrawCount(self, *args, **kwargs):
        """
        Get the BaseDraw count in the editor view.
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

    def GetChanged(self, *args, **kwargs):
        """
        Check if the document was changed since last time saved.
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
        Returns the document settings.
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

    def GetDocumentName(self, *args, **kwargs):
        """
        Returns the document name
        """
        pass

    def GetDocumentPath(self, *args, **kwargs):
        """
        Returns the document path
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

    def GetDrawTime(self, *args, **kwargs):
        """
        Get the editor redraw time.
        """
        pass

    def GetFirstCTrack(self, *args, **kwargs):
        """
        Returns the first CTrack.
        """
        pass

    def GetFirstMaterial(self, *args, **kwargs):
        """
        Get the first object BaseMaterial of the document.
        """
        pass

    def GetFirstObject(self, *args, **kwargs):
        """
        Get the first object BaseObject of the document
        """
        pass

    def GetFirstRenderData(self, *args, **kwargs):
        """
        Get the first render settings for the document.
        """
        pass

    def GetFirstShader(self, *args, **kwargs):
        """
        Returns the first shader of the object.
        """
        pass

    def GetFps(self, *args, **kwargs):
        """
        Get frames per second
        """
        pass

    def GetHelperAxis(self, *args, **kwargs):
        """
        The helper axis for the current multi selection.
        """
        pass

    def GetHighest(self, *args, **kwargs):
        """
        The first object in object manager hierarchy of type type.
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

    def GetLOD(self, *args, **kwargs):
        """
        Returns the LOD.
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

    def GetLayerObjectRoot(self, *args, **kwargs):
        """
        Returns the list of layers of the document.
        """
        pass

    def GetListHead(self, *args, **kwargs):
        """
        Get the list head for this node.
        """
        pass

    def GetLoopMaxTime(self, *args, **kwargs):
        """
        Returns the right boundary of the document's preview range.
        """
        pass

    def GetLoopMinTime(self, *args, **kwargs):
        """
        Returns the left boundary of the document's preview range.
        """
        pass

    def GetMain(self, *args, **kwargs):
        """
        Goes one level up.
        """
        pass

    def GetMaterials(self, *args, **kwargs):
        """
        Returns a tuple of materials stored in the object manager.
        """
        pass

    def GetMaxTime(self, *args, **kwargs):
        """
        Returns the max time
        """
        pass

    def GetMinTime(self, *args, **kwargs):
        """
        Returns the min time
        """
        pass

    def GetMode(self, *args, **kwargs):
        """
        Get the main mode of the editor.
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

    def GetObjects(self, *args, **kwargs):
        """
        Returns a tuple of objects stored in the object manager.
        """
        pass

    def GetOrderedActiveObjects(self, *args, **kwargs):
        """
        Returns the active objects in an ordered list.
        """
        pass

    def GetParticleSystem(self, *args, **kwargs):
        """
        Returns the particlesystem.
        """
        pass

    def GetPred(self, *args, **kwargs):
        """
        Get the previous GeListNode in the list
        """
        pass

    def GetRenderBaseDraw(self, *args, **kwargs):
        """
        This is the BaseDraw belonging to the view.
        """
        pass

    def GetRenderLod(self, *args, **kwargs):
        """
        Returns the right boundary of the document's preview range.
        """
        pass

    def GetSelection(self, *args, **kwargs):
        """
        Returns the current selection.
        """
        pass

    def GetSettingsInstance(self, *args, **kwargs):
        """
        Get the BaseContainer setting of the specified type.
        """
        pass

    def GetSplinePlane(self, *args, **kwargs):
        """
        Get the spline plane.
        """
        pass

    def GetTime(self, *args, **kwargs):
        """
        Returns the time
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

    def GetUndoPtr(self, *args, **kwargs):
        """
        Returns the element of the last undo action.
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

    def InsertMaterial(self, *args, **kwargs):
        """
        Inserts the material into the document's material list.
        """
        pass

    def InsertObject(self, *args, **kwargs):
        """
        Inserts the object into the document's object hierarchy.
        """
        pass

    def InsertRenderData(self, *args, **kwargs):
        """
        Inserts a renderdata into the document's renderdata list.
        """
        pass

    def InsertRenderDataLast(self, *args, **kwargs):
        """
        Inserts the renderdata as last child into the document's render data list.
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

    def IsEditMode(self, *args, **kwargs):
        """
        Check if the editor is in an editable mode. 
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

    def Polygonize(self, *args, **kwargs):
        """
        Make a clone of the document.
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

    def Scale(self, *args, **kwargs):
        """
        Scales the object.
        """
        pass

    def SearchMaterial(self, *args, **kwargs):
        """
        Search for a material with the same case sensitive name.
        """
        pass

    def SearchMaterialInc(self, *args, **kwargs):
        """
        Search for a material with the same case sensitive name.
        """
        pass

    def SearchObject(self, *args, **kwargs):
        """
        Search for an object with the same case sensitive name.
        """
        pass

    def SearchObjectInc(self, *args, **kwargs):
        """
        Search for an object with the same case sensitive name.
        """
        pass

    def SetAction(self, *args, **kwargs):
        """
        Set the current tool in the editor.
        """
        pass

    def SetActiveMaterial(self, *args, **kwargs):
        """
        Sets a material to active within this document.
        """
        pass

    def SetActiveObject(self, *args, **kwargs):
        """
        Modifies the current multi selection with op, depending on mode.
        """
        pass

    def SetActiveRenderData(self, *args, **kwargs):
        """
        Set the active render settings for the document.
        """
        pass

    def SetActiveTag(self, *args, **kwargs):
        """
        Set the active tags for the document.
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

    def SetChanged(self, *args, **kwargs):
        """
        Set the change document flag.
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

    def SetDocumentName(self, *args, **kwargs):
        """
        Set the filename of the document.
        """
        pass

    def SetDocumentPath(self, *args, **kwargs):
        """
        Get previous Basedocument off list
        """
        pass

    def SetFps(self, *args, **kwargs):
        """
        Set frames per second.
        """
        pass

    def SetKeyframeSelection(self, *args, **kwargs):
        """
        Sets the keyframe selection status.
        """
        pass

    def SetLOD(self, *args, **kwargs):
        """
        Set the LOD.
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

    def SetLoopMaxTime(self, *args, **kwargs):
        """
        Sets the right boundary of the document's preview range.
        """
        pass

    def SetLoopMinTime(self, *args, **kwargs):
        """
        Sets the left boundary of the document's preview range.
        """
        pass

    def SetMaxTime(self, *args, **kwargs):
        """
        Set the end time for the timeline of this document.
        """
        pass

    def SetMinTime(self, *args, **kwargs):
        """
        Set the starting time for the timeline of this document.
        """
        pass

    def SetMode(self, *args, **kwargs):
        """
        Set the main mode of the editor.
        """
        pass

    def SetName(self, *args, **kwargs):
        """
        Set the name of the object
        """
        pass

    def SetRenderLod(self, *args, **kwargs):
        """
        Sets the right boundary of the document's preview range.
        """
        pass

    def SetRewind(self, *args, **kwargs):
        """
        C4D rewinds the whole document.
        """
        pass

    def SetSelection(self, *args, **kwargs):
        """
        Set the current selection.
        """
        pass

    def SetTime(self, *args, **kwargs):
        """
        Set the current time for this documents timeline.
        """
        pass

    def SetUserDataContainer(self, *args, **kwargs):
        """
        Set the user data container.
        """
        pass

    def StartUndo(self, *args, **kwargs):
        """
        Tell CINEMA 4D to start building a list of undos.
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
