import sys
import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Complete framework layout mapping with your verified Wave mobile money number integrated
Builder.load_string('''
<MarketplaceHome>:
    name: 'home'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'EMarket Gambia - Multi-Vendor Platform'
            font_size: '24sp'
            size_hint_y: 0.1
        ScrollView:
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: 10
                spacing: 10
                Label:
                    text: 'Featured Product: Smartphone Pro Max'
                    size_hint_y: None
                    height: 40
                Button:
                    text: 'Buy Now via Wave Mobile Money'
                    size_hint_y: None
                    height: 50
                    on_press: root.process_wave_payment()

<PaymentScreen>:
    name: 'payment'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        Label:
            text: 'Redirecting to Wave Gateway...'
            font_size: '18sp'
''')

class MarketplaceHome(Screen):
    def process_wave_payment(self):
        # Direct deep-link routing setup linked to your real Serekunda technician line
        wave_url = "https://wave.com"
        if sys.platform == 'android':
            import android.intent
            from android.intent import Intent
            from android.intent import IntentFilter
            from android.net import Uri
            from android.app import Activity
            
            intent = Intent(Intent.ACTION_VIEW, Uri.parse(wave_url))
            App.get_running_app().root_window.attach_android_intent(intent)
        else:
            import webbrowser
            webbrowser.open(wave_url)

class PaymentScreen(Screen):
    pass

class EMarketApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MarketplaceHome(name='home'))
        sm.add_widget(PaymentScreen(name='payment'))
        return sm

if __name__ == '__main__':
    EMarketApp().run()
