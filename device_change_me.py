# name=change_me
# TODO: Change the name of the device to something more descriptive
# Everywhen you see change_me, or MyControlSurface, or my_control_surface, change it to something more descriptive to suite your needs


# TODO: Change the name of the device to something more descriptive
from controller.control_surface import MyControlSurface


my_control_surface = MyControlSurface("my_control_surface")


def OnInit():
    my_control_surface.OnInit()


def OnMidiMsg(event):
    my_control_surface.OnMidiMsg(event)


def OnMidiOutMsg(event):
    pass
    # print(event)


def OnRefresh(event):
    my_control_surface.OnRefresh(event)


def OnIdle():
    my_control_surface.OnIdle()


def OnUpdateMeters():
    my_control_surface.OnUpdateMeters()


def OnDeInit():
    my_control_surface.OnDeInit()


def OnUpdateBeatIndicator(event):
    my_control_surface.OnUpdateBeatIndicator(event)


def OnProjectLoad(status: int):
    my_control_surface.OnProjectLoad(status)


def OnDoFullRefresh():
    my_control_surface.OnDoFullRefresh()


def OnDisplayZone():
    my_control_surface.OnDisplayZone()


def OnUpdateLiveMode(lastTrack: int):
    my_control_surface.OnUpdateLiveMode(lastTrack)


def OnDirtyMixerTrack(index: int):
    my_control_surface.OnDirtyMixerTrack(index)


def OnDirtyChannel(index: int, flag: int):
    my_control_surface.OnDirtyChannel(index, flag)


def OnFirstConnect():
    my_control_surface.OnFirstConnect()


def OnWaitingForInput():
    my_control_surface.OnWaitingForInput()


def OnSendTempMsg(message: str, duration: int):
    my_control_surface.OnSendTempMsg(message, duration)
