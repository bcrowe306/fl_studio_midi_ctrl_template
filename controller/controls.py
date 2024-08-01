# In this file, we define the controls for the controller you're implementing.
# This should be where you define buttons, faders, knobs, etc. and how they interact with FL Studio via midi.
# I usually like to to keep all my controls attached to a single Control class, but you can do it however you like.
# There are examples already in the file, so you can just copy and paste them and modify them to your needs.
 
from fl_controller_framework.controls.button import ButtonControl
from fl_controller_framework.controls.fader import FaderControl
from fl_controller_framework.controls.knob import KnobControl
from fl_controller_framework.controls.encoder import EncoderControl

from fl_controller_framework.util.midi import MIDI_STATUS


class Controls:
    my_button_control: ButtonControl = ButtonControl("my_button_control", 0, 45, playable=False, status=MIDI_STATUS.NOTE_ON_STATUS)
    my_fader_control: FaderControl = FaderControl("my_fader_control", 0, 46, status=MIDI_STATUS.CC_STATUS)
    my_knob_control: KnobControl = KnobControl("my_knob_control", 0, 47, status=MIDI_STATUS.CC_STATUS)
    my_encoder_control: EncoderControl = EncoderControl("my_encoder_control", 0, 48, status=MIDI_STATUS.CC_STATUS)