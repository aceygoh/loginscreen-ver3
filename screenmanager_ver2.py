from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition

screen_helper = """
ScreenManager:
    LoginScreen:
    MenuScreen:
    ProfileScreen:
    MonitoringScreen:
    Jenny:
    John:
    Jerry:
    Benny:

<LoginScreen>:
    name: 'login'

    MDTextField:       
        hint_text: "Enter username"
        helper_text: "all in lower case"
        helper_text_mode: "on_focus"
        icon_right: "language-python"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:300 
    MDTextField:
        hint_text: "Enter password"
        helper_text: "all in lower case"
        helper_text_mode: "on_focus"
        icon_right: "language-python"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:300 
    MDRectangleFlatButton:
        text: "Enter"
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'menu'



<MenuScreen>:
    name: 'menu'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Mobile GUI'
                        left_action_items: [["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation :8

                    Widget:

                  
                BoxLayout
                    orientation: 'vertical'
                    spacing: '75dp'
                    padding: '75dp'
                    MDRectangleFlatIconButton:
                        icon: 'close'
                        text: 'Officer Jenny'
                        line_color: 0, 0, 0, 1
                        text_color: 0, 0, 0, 1
                        pos_hint: {'center_x':0.5,'center_y':0.3}
                        on_press: root.manager.current = 'jenny'
                    MDRectangleFlatIconButton:
                        icon: 'close'
                        text: 'Officer John'
                        line_color: 0, 0, 0, 1
                        text_color: 0, 0, 0, 1
                        pos_hint: {'center_x':0.5,'center_y':0.4}
                        on_press: root.manager.current = 'john'
                    MDRectangleFlatIconButton:
                        icon: 'check'
                        text: 'Officer Jerry'
                        line_color: 0, 168/255.0, 0, 1
                        text_color: 0, 168/255.0, 0, 1
                        pos_hint: {'center_x':0.5,'center_y':0.5}
                        on_press: root.manager.current = 'jerry'
                    MDRectangleFlatIconButton:
                        icon: 'check'
                        text: 'Officer Benny'
                        line_color: 0, 168/255.0, 0, 1
                        text_color: 0, 168/255.0, 0, 1
                        pos_hint: {'center_x':0.5,'center_y':0.6}
                        on_press: root.manager.current = 'benny'

                        


        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing:'8dp'
                padding:'8dp'
                Image:
                    source: 'stickman.png'
                MDLabel:
                    text: ' Tester'
                    front_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: ' tester123@ntu.edu.sg'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            on_press: root.manager.current = 'profile'
                            IconLeftWidget:
                                icon: 'face-profile-woman'
                        OneLineIconListItem:
                            text: 'Monitoring'
                            on_press: root.manager.current = 'monitor'
                            IconLeftWidget:
                                icon: 'file-upload'
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon: 'logout'   

<ProfileScreen>:
    name: 'profile'
    Image:
        source: 'stickman.png'
        size_hint: (0.25,0.25)
        pos_hint: {'center_x':0.5,'center_y':0.8}
    MDLabel:
        text: 'Name: Major Ahmad'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.6}
    MDLabel:
        text: 'Age: 50  Gender: Male'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.5}
    MDLabel:
        text: 'Years of Service: 30'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.4}
    MDLabel:
        text: 'Focus Period: NA'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.3}
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

<MonitoringScreen>:
    name: 'monitor'
    BoxLayout
        orientation: 'horizontal'
        MDRectangleFlatButton:
            text: 'User1'
            halign: 'center'
        MDRectangleFlatButton:
            text: 'User2'
            halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'


    
<Jenny>:
    name: 'jenny'
    Image:
        source: 'Jenny.png'
        size_hint: (0.25,0.25)
        pos_hint: {'center_x':0.5,'center_y':0.8}
    MDLabel:
        text: 'Name: Officer Jenny'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.6}
    MDLabel:
        text: 'Age: 30  Gender: Female'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.5}
    MDLabel:
        text: 'Years of Service: 10'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.4}
    MDLabel:
        text: 'Peak Focus Period: 1000-1200'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.3}
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

<John>:
    name: 'john'
    Image:
        source: 'John.png'
        size_hint: (0.25,0.25)
        pos_hint: {'center_x':0.5,'center_y':0.8}
    MDLabel:
        text: 'Name: Officer John'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.6}
    MDLabel:
        text: 'Age: 44  Gender: Male'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.5}
    MDLabel:
        text: 'Years of Service: 21'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.4}
    MDLabel:
        text: 'Peak Focus Period: 1500-1800'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.3}
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

<Jerry>:
    name: 'jerry'
    Image:
        source: 'Jerry.png'
        size_hint: (0.25,0.25)
        pos_hint: {'center_x':0.5,'center_y':0.8}
    MDLabel:
        text: 'Name: Officer Jerry'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.6}
    MDLabel:
        text: 'Age: 25  Gender: Male'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.5}
    MDLabel:
        text: 'Years of Service: 3'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.4}
    MDLabel:
        text: 'Peak Focus Period: 1700-2000'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.3}
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

<Benny>:
    name: 'benny'
    Image:
        source: 'Benny.png'
        size_hint: (0.25,0.25)
        pos_hint: {'center_x':0.5,'center_y':0.8}
    MDLabel:
        text: 'Name: Officer Benny'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.6}
    MDLabel:
        text: 'Age: 33  Gender: Female'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.5}
    MDLabel:
        text: 'Years of Service: 11'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.4}
    MDLabel:
        text: 'Peak Focus Period: 0800-1200'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.3}
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

"""


class LoginScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class MonitoringScreen(Screen):
    pass


class Jenny(Screen):
    pass


class John(Screen):
    pass


class Jerry(Screen):
    pass


class Benny(Screen):
    pass


# Create the screen manager
sm = ScreenManager(transition=SwapTransition())
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(MonitoringScreen(name='monitor'))
sm.add_widget(Jenny(name='jenny'))
sm.add_widget(John(name='john'))
sm.add_widget(Jerry(name='jerry'))
sm.add_widget(Benny(name='benny'))


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'
        screen = Builder.load_string(screen_helper)

        return screen


DemoApp().run()
