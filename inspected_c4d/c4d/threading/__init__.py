# Functions --------------------------------------------------

def GeCheckBackgroundThreadsRunning(*args, **kwargs):
    """
    Stops all running background threads of the give typeclass.
    """
    pass

def GeGetCPUCount(*args, **kwargs):
    """
    Get the number of CPUs in the system.
    """
    pass

def GeGetCurrentThread(*args, **kwargs):
    """
    Returns the current thread.
    """
    pass

def GeGetCurrentThreadId(*args, **kwargs):
    """
    Returns a unique ID for the current thread.
    """
    pass

def GeIsMainThread(*args, **kwargs):
    """
    Checks if you are in the main thread.
    """
    pass

def GeProcessBackgroundThreads(*args, **kwargs):
    """
    This is called by CINEMA 4D when it is idle.
    """
    pass

def GeStopBackgroundThreads(*args, **kwargs):
    """
    Allows you to see if any of the threads matching typeclass is running.
    """
    pass

def GeThreadLock(*args, **kwargs):
    """
    Lock global semaphore.
    """
    pass

def GeThreadUnlock(*args, **kwargs):
    """
    Unlock global semaphore.
    """
    pass

def IdentifyThread(*args, **kwargs):
    """
    Identifies a thread's type.
    """
    pass
# Classes ----------------------------------------------------
'''
BaseThread
C4DThread
'''
# Everything else --------------------------------------------
__doc__ = "Returns a unique ID for the current thread. Usally you don't have to care about this."
__name__ = 'c4d.threading'
__package__ = None