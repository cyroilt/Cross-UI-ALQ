import time
def get_keys_by_value(d, target_value):
    keys = [key for key, value in d.items() if value == target_value]
    return keys
mouse_events={"left-click":"<Button-1>",
              "middle-click":"<Button-2>",
              "right-click":"<Button-3>",
              "double-left":"<Double-Button-1>",
              "double-middle":"<Double-Button-2>",
              "double-right":"<Double-Button-3>",
              "triple-left":"<Triple-Button-1>",
              "triple-middle":"<Triple-Button-2>",
              "triple-right":"<Triple-Button-3>",
              "mouse-press":"<ButtonPress>",
              "mouse-release":"<ButtonRelease>",
              "enter":"<Enter>",
              "leave":"<Leave>",
              "mouse-motion":"<Motion>",
              "left-motion":"<B1-Motion>",
              "middle-motion":"<B2-Motion>",
              "right-motion":"<B3-Motion>",
              "wheel":"<MouseWheel>",
              "enter":"<Enter>",
              "leave":"<Leave>"}
event_names={
    "click":"<Button-1>",
    "double_click":"<Double-1>",
    "right_click":"<Button-3>",
    "motion":"<B1-Motion>",
    "release":"<ButtonRelease-1>",
    "enter":"<Enter>",
    "leave":"<Leave>",
    "scroll_up":"<Button-4>",
    "scroll_down":"<Button-5>",
    "key_down":"<Key>",
    "key_up":"<KeyRelease>",
    "key_press":"<KeyPress>"
}
class Event():
    def __init__(self,widget,event_name,command):
        self.event_name=event_name
        self.widget=widget
        self.command=command
        if event_name in mouse_events.keys():
            self.type=MouseEvent
            self.typo=f"MouseEvent.{event_name}"
            self.association=mouse_events[event_name]
    def on_call(self,event):
        if self.type==MouseEvent:
            return self.command(MouseEvent(event,self.widget,self.typo))
class MouseEvent():
    def __init__(self,event,widget,type):
        self.event = event
        self.widget = widget
        self.time = time.time()
        self.type = type
        self.x=event.x
        self.y=event.y
    def __str__(self):
        return f"Mouse Event: {self.type} on Widget: {self.widget.__class__.__name__} at Time: {self.time}"
    def __repr__(self) -> str:
        return self.__str__()
    