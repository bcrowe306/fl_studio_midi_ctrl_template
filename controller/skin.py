# This file will hold the code to draw the skin for the controller you're implementing.
# A skin is the visual representation of the controller. It is how you light up buttons, faders, knobs, pads, etc. on the controller.
# This allows you to implement the visual feedback for the controller, according to the specifications of the controller.
# 
# A skin is defined as a class with, member objects called "colors" that contain a draw method. 
# The draw method is called by the controller framework to draw a "color" to the controller, and takes in the control as an argument.
# For example, I may have a button on my controller that has a backlit LED. This LED may have three states, off, on, and blinking. 
# In MIDI, these states may be represented by different MIDI CC messages, 0, 1, and 2.
# I would define a color for each of these states, and then implement a draw method for each of these states like so:

from fl_controller_framework.util.midi import MIDI_STATUS
import device

# Color definitions
class ThreeStateButtonColor:
    def __init__(self, color: int):
        self.color = color

    def draw(self, control):
        # Notice we're using the control's value to determine the parameters of the midi message. This is common practice among controller implementations.
        device.midiOutMsg(MIDI_STATUS.CC_STATUS, control.channel, control.identifier, self.value)

# Skin definition:

class ThreeStateButton:
    # Make sure to provide an OFF, ON, and DEFAULT color for each control. The framework will use the DEFAULT color if no color is specified, and will use the ON color if the control is active.
    OFF = ThreeStateButtonColor(0)
    ON = ThreeStateButtonColor(1)
    DEFAULT = ThreeStateButtonColor(1)
    BLINK = ThreeStateButtonColor(2)