from fl_controller_framework.control_surface import ControlSurface
from .controls import Controls

class MyControlSurface(ControlSurface):
    def __init__(self, name: str, meters: bool = False, *a, **k):
        super(ControlSurface, self).__init__(name, meters, *a, **k)

        # Example of adding directly to the control surface. In most cases, you wont do this. You should instead add your controls to a component, and add the compoenent to the control surface.
        # But you can also add directly to the control surface like this:
        self.my_button_control = Controls.my_button_control
        self.my_fader_control = Controls.my_fader_control
        self.my_knob_control = Controls.my_knob_control
        self.my_encoder_control = Controls.my_encoder_control
        
