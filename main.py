from kivy.config import Config
Config.set('graphics', 'width',370)
Config.set('graphics', 'height',  770)
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
Builder.load_file("kv/solar_tracker.kv")
from kivy3dgui.layout3d import Layout3D,Node
from kivy.properties import NumericProperty,ListProperty,DictProperty
from joystick import Joystick
from kivy.clock import Clock
class Lay3D(Layout3D):
    pass
class SolarTracker(FloatLayout):
    pad_y=NumericProperty(0)
    pad_x=NumericProperty(0)
    def __init__(self,*args,**kwargs):
        super(SolarTracker,self).__init__(*args,**kwargs)
        Clock.schedule_interval(self.timer,.01)
    def timer(self,dt):
        self.pad_y-=self.ids.joy1.pad_y
        self.pad_x+=self.ids.joy.pad_x
        if self.pad_y>90:
            self.pad_y=90
        if self.pad_y<-90:
            self.pad_y=-90
        if self.pad_y>-90 and self.pad_y<90:
            self.ids.sol.rotate=(180+90+self.pad_y,1,0,0)

class MyApp(App):
    def build(self):
        return SolarTracker()
if __name__=="__main__":
    MyApp().run()
