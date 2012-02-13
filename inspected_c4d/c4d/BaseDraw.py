#!/usr/bin/env python
"""
c4d.BaseDraw

Important: these are not real files. They are automatically generated to
ease code completion only.
"""

class BaseDraw(object):
    """
    CINEMA 4D view window.
    """
    def __init__(self, *args, **kwargs):
        pass


    def AddToPostPass(self, *args, **kwargs):
        """
        Adds the object op to DRAWPASS_XRAY.
        """
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

    def CheckColor(self, *args, **kwargs):
        """
        Check color to background
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

    def ConvertColor(self, *args, **kwargs):
        """
        Color conversion.
        """
        pass

    def ConvertColorReverse(self, *args, **kwargs):
        """
        Reverse color conversion.
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

    def DoUndo(self, *args, **kwargs):
        """
        Performs an undo operation in the view.
        """
        pass

    def DrawArrayEnd(self, *args, **kwargs):
        """
        Forces end DrawPolygon operation.
        """
        pass

    def DrawBox(self, *args, **kwargs):
        """
        Draws a box.
        """
        pass

    def DrawCircle(self, *args, **kwargs):
        """
        Draws an ellipse in the current pen color.
        """
        pass

    def DrawCircle2D(self, *args, **kwargs):
        """
        Draws a circle in the current pen color.
        """
        pass

    def DrawHandle(self, *args, **kwargs):
        """
        Draws a handle.
        """
        pass

    def DrawHandle2D(self, *args, **kwargs):
        """
        Draws a standard handle (orange dot).
        """
        pass

    def DrawLine(self, *args, **kwargs):
        """
        Draws a 3d line in the current pen color.
        """
        pass

    def DrawLine2D(self, *args, **kwargs):
        """
        Draws a 2d line in the current pen color.
        """
        pass

    def DrawObject(self, *args, **kwargs):
        """
        Draws an object into the view.
        """
        pass

    def DrawPoint2D(self, *args, **kwargs):
        """
        Draws a point in the current pen color.
        """
        pass

    def DrawPoints(self, *args, **kwargs):
        """
        Draws a point list.
        """
        pass

    def DrawPolygon(self, *args, **kwargs):
        """
        Draws a polygon in the view.
        """
        pass

    def DrawPolygonObject(self, *args, **kwargs):
        """
        Draws a polygon object into the view.
        """
        pass

    def DrawScene(self, *args, **kwargs):
        """
        Draw a scene into the framebuffer.
        """
        pass

    def DrawSphere(self, *args, **kwargs):
        """
        Draw a sphere.
        """
        pass

    def DrawTexture(self, *args, **kwargs):
        """
        Draws a texture.
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

    def GetDisplayFilter(self, *args, **kwargs):
        """
        Returns the current display filter.
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

    def GetDrawParam(self, *args, **kwargs):
        """
        Get draw parameters.
        """
        pass

    def GetEditState(self, *args, **kwargs):
        """
        Returns the current edit state.
        """
        pass

    def GetEditorCamera(self, *args, **kwargs):
        """
        Returns the camera editor.
        """
        pass

    def GetEditorWindow(self, *args, **kwargs):
        """
        Get the EditorWindow of the BaseDraw.
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

    def GetFrameScreen(self, *args, **kwargs):
        """
        Used in the Extended GL mode.
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

    def GetObjectColor(self, *args, **kwargs):
        """
        Draws a box.
        """
        pass

    def GetParameterData(self, *args, **kwargs):
        """
        Convenience function for getting parameters.
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

    def GetReductionMode(self, *args, **kwargs):
        """
        Return the reduction mode.
        """
        pass

    def GetSafeFrame(self, *args, **kwargs):
        """
        The positiion in pixels of the render line.
        """
        pass

    def GetSceneCamera(self, *args, **kwargs):
        """
        Returns the current scene camera.
        """
        pass

    def GetTransparency(self, *args, **kwargs):
        """
        Returns the transparency for polygons.n
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

    def HasCameraLink(self, *args, **kwargs):
        """
        Indicates if the camera link is enabled.
        """
        pass

    def InitClipbox(self, *args, **kwargs):
        """
        Used to render into a framebuffer.
        """
        pass

    def InitUndo(self, *args, **kwargs):
        """
        Called before a change is made.
        """
        pass

    def InitView(self, *args, **kwargs):
        """
        Used to render into a framebuffer.
        """
        pass

    def InitializeView(self, *args, **kwargs):
        """
        Used after rendering into a framebuffer.
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

    def IsViewOpen(self, *args, **kwargs):
        """
        Checks if the view is open.
        """
        pass

    def KeyframeSelectionContent(self, *args, **kwargs):
        """
        Checks if there are any active keyframe selections.
        """
        pass

    def LineZOffset(self, *args, **kwargs):
        """
        Line Z Offset.
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

    def PointInRange(self, *args, **kwargs):
        """
        Returns TRUE if the screen point (x,y) is within a hit range.
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

    def SetDepth(self, *args, **kwargs):
        """
        Set depth
        """
        pass

    def SetDirty(self, *args, **kwargs):
        """
        Sets the dirty checksum for the object.
        """
        pass

    def SetDrawParam(self, *args, **kwargs):
        """
        Sets draw parameters.
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

    def SetLightList(self, *args, **kwargs):
        """
        Sets the lighting used by the draw functions.
        """
        pass

    def SetMatrix_Camera(self, *args, **kwargs):
        """
        Sets the transformation matrix to the camera system.
        """
        pass

    def SetMatrix_Matrix(self, *args, **kwargs):
        """
        Sets the transformation matrix to the given matrix mg.
        """
        pass

    def SetMatrix_Projection(self, *args, **kwargs):
        """
        For internal use only.
        """
        pass

    def SetMatrix_Screen(self, *args, **kwargs):
        """
        Sets the transformation matrix to screen coordinates.
        """
        pass

    def SetName(self, *args, **kwargs):
        """
        Set the name of the object
        """
        pass

    def SetPen(self, *args, **kwargs):
        """
        Sets the pen color for following drawing operations.
        """
        pass

    def SetPointSize(self, *args, **kwargs):
        """
        Set point size.
        """
        pass

    def SetSceneCamera(self, *args, **kwargs):
        """
        Set the scene camera.
        """
        pass

    def SetTexture(self, *args, **kwargs):
        """
        Set a texture used by the vertex buffer.
        """
        pass

    def SetTransparency(self, *args, **kwargs):
        """
        Set the transparency for polygons.n
        """
        pass

    def SetUserDataContainer(self, *args, **kwargs):
        """
        Set the user data container.
        """
        pass

    def SimpleShade(self, *args, **kwargs):
        """
        Quick shading algorithm.
        """
        pass

    def TestBreak(self, *args, **kwargs):
        """
        Checks for thread breaks in the draw.
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
