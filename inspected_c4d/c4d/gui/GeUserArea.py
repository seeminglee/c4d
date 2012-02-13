#!/usr/bin/env python
"""
c4d.gui.GeUserArea

Important: these are not real files. They are automatically generated to
ease code completion only.
"""

class GeUserArea(object):
    """
    Used to create custom GUI components.
    """
    def __init__(self, *args, **kwargs):
        pass


    def CheckDropArea(self, *args, **kwargs):
        """
        Checks the drag position in a drag event message.
        """
        pass

    def ClearClippingRegion(self, *args, **kwargs):
        """
        Clears any clipping region.
        """
        pass

    def CoreMessage(self, *args, **kwargs):
        """
        Called when a C4D core messages is received.
        """
        pass

    def DrawBitmap(self, *args, **kwargs):
        """
        Draws a bitmap in the area.
        """
        pass

    def DrawBorder(self, *args, **kwargs):
        """
        Draws a border.
        """
        pass

    def DrawGetFontBaseLine(self, *args, **kwargs):
        """
        Returns the font base line.
        """
        pass

    def DrawGetFontHeight(self, *args, **kwargs):
        """
        Returns the height of the current font.
        """
        pass

    def DrawGetTextWidth(self, *args, **kwargs):
        """
        Returns the width in pixels of the string text.
        """
        pass

    def DrawLine(self, *args, **kwargs):
        """
        Draws a line with the current pen color.
        """
        pass

    def DrawMsg(self, *args, **kwargs):
        """
        Draw the userarea.
        """
        pass

    def DrawRectangle(self, *args, **kwargs):
        """
        Fills a rectangular area.
        """
        pass

    def DrawSetFont(self, *args, **kwargs):
        """
        Sets the text font.
        """
        pass

    def DrawSetPen(self, *args, **kwargs):
        """
        Sets the draw color.
        """
        pass

    def DrawSetTextCol(self, *args, **kwargs):
        """
        Sets the text foreground and background color.
        """
        pass

    def DrawSetTextRotation(self, *args, **kwargs):
        """
        Set the text rotatation.
        """
        pass

    def DrawText(self, *args, **kwargs):
        """
        Draws a rectangle in the area.
        """
        pass

    def FillBitmapBackground,(self, *args, **kwargs):
        """
        Draws a bitmap in the area.
        """
        pass

    def GetBorderSize(self, *args, **kwargs):
        """
        Retrieves the space required to draw a border.
        """
        pass

    def GetColorRGB(self, *args, **kwargs):
        """
        Gets the RGB values associated with a color code.
        """
        pass

    def GetDragObject(self, *args, **kwargs):
        """
        A convenience function to extract the data from a drag and drop message.
        """
        pass

    def GetDragPosition(self, *args, **kwargs):
        """
        A convenience function to extract local drag coordinates from a drag and drop event.
        """
        pass

    def GetHeight(self, *args, **kwargs):
        """
        Return the height.
        """
        pass

    def GetId(self, *args, **kwargs):
        """
        Return the ID.
        """
        pass

    def GetInputEvent(self, *args, **kwargs):
        """
        Gets the next input event for a certain device.
        """
        pass

    def GetInputState(self, *args, **kwargs):
        """
        Polls a certain channel of a device.
        """
        pass

    def GetMinSize(self, *args, **kwargs):
        """
        Specify a minimum size for the user area.
        """
        pass

    def GetWidth(self, *args, **kwargs):
        """
        Return the width.
        """
        pass

    def Global2Local(self, *args, **kwargs):
        """
        Transforms global coordinates.
        """
        pass

    def HasFocus(self, *args, **kwargs):
        """
        Indicates the focus state.
        """
        pass

    def Init(self, *args, **kwargs):
        """
        Called once when the user area is initialized.
        """
        pass

    def InitValues(self, *args, **kwargs):
        """
        Called after the layout is calculated.
        """
        pass

    def InputEvent(self, *args, **kwargs):
        """
        Called when an input event is received.
        """
        pass

    def IsEnabled(self, *args, **kwargs):
        """
        Indicates the enabled state.
        """
        pass

    def IsHotkeyDown(self, *args, **kwargs):
        """
        Checks the standard navigation hotkeys.
        """
        pass

    def KillEvents(self, *args, **kwargs):
        """
        Flushes all events from the window message queue.
        """
        pass

    def LayoutChanged(self, *args, **kwargs):
        """
        Tells the GUI element that the layout has changed.
        """
        pass

    def Local2Global(self, *args, **kwargs):
        """
        Transforms local coordinates.
        """
        pass

    def Local2Screen(self, *args, **kwargs):
        """
        Transforms local coordinates.
        """
        pass

    def Message(self, *args, **kwargs):
        """
        Override this function if you want to react to more messages.
        """
        pass

    def MouseDrag(self, *args, **kwargs):
        """
        Polls the mouse during a drag started MouseDragStart.
        """
        pass

    def MouseDragEnd(self, *args, **kwargs):
        """
        Ends a mouse drag.
        """
        pass

    def MouseDragStart(self, *args, **kwargs):
        """
        Starts a mouse drag.
        """
        pass

    def OffScreenOn(self, *args, **kwargs):
        """
        Enables double buffering to avoid blinking and flickering effects.
        """
        pass

    def Redraw(self, *args, **kwargs):
        """
        Forces the user area to redraw itself.
        """
        pass

    def Screen2Local(self, *args, **kwargs):
        """
        Transforms screen coordinates.
        """
        pass

    def ScrollArea(self, *args, **kwargs):
        """
        Scrolls the area.
        """
        pass

    def SendParentMessage(self, *args, **kwargs):
        """
        Send a custom message.
        """
        pass

    def SetClippingRegion(self, *args, **kwargs):
        """
        Set a clipping region.
        """
        pass

    def SetDragDestination(self, *args, **kwargs):
        """
        Sets the correct cursor during drag and drop handling.
        """
        pass

    def SetTimer(self, *args, **kwargs):
        """
        Initializes the timer clock.
        """
        pass

    def Sized(self, *args, **kwargs):
        """
        Called when the user area is resized.
        """
        pass

    def Timer(self, *args, **kwargs):
        """
        Called on timer subscription.
        """
        pass
