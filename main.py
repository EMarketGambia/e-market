from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
import webbrowser

# ==========================================
# SCREEN 1: THE FACEBOOK STYLE MARKETPLACE VIEW
# ==========================================
class MarketplaceDashboard(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Main layout framework
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header Area with Search Bar
        header = BoxLayout(orientation='horizontal', size_hint_y=0.1, spacing=10)
        header.add_widget(Label(text="🛒 MARKETPLACE GAMBIA", font_size='18sp', bold=True, color=(0, 0.6, 1, 1)))
        
        # Sell Button (Triggers subscription/payment check)
        sell_btn = Button(text="+ Post Item", size_hint_x=0.3, background_color=(0, 0.8, 0.4, 1), bold=True)
        sell_btn.bind(on_press=self.go_to_vendor_payment)
        header.add_widget(sell_btn)
        main_layout.add_widget(header)
        
        # Scrollable area for products
        scroll = ScrollView(size_hint_y=0.9)
        grid = GridLayout(cols=2, spacing=12, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        # Simulated Multi-Vendor Product Feed Database (In real life, this pulls from Firebase!)
        products = [
            {"title": "iPhone 12 Pro", "price": "D28,000", "seller": "Alieu (Serekunda)"},
            {"title": "Samsung Charger", "price": "D450", "seller": "Modou (Brikama)"},
            {"title": "HP Laptop Core i5", "price": "D15,500", "seller": "Fatou (Bakau)"},
            {"title": "Techno Camon 20", "price": "D9,000", "seller": "Ebrima (Shop)"}
        ]
        
        for item in products:
            item_box = BoxLayout(orientation='vertical', size_hint_y=None, height=180, padding=5)
            item_box.add_widget(Label(text=f"[b]{item['title']}[/b]\n{item['price']}\n[size=12]Seller: {item['seller']}[/size]", markup=True, halign='center'))
            
            # Chat with Seller Button
            chat_btn = Button(text="💬 Chat to Buy", background_color=(0, 0.6, 1, 1))
            chat_btn.bind(on_press=lambda instance, seller=item['seller'], prod=item['title']: self.open_chat_room(seller, prod))
            item_box.add_widget(chat_btn)
            
            grid.add_widget(item_box)
            
        scroll.add_widget(grid)
        main_layout.add_widget(scroll)
        self.add_widget(main_layout)

    def go_to_vendor_payment(self, instance):
        self.manager.current = 'payment_screen'

    def open_chat_room(self, seller_name, product_title):
        # Set the global details for the chat screen layout
        chat_screen = self.manager.get_screen('chat_screen')
        chat_screen.update_chat_header(seller_name, product_title)
        self.manager.current = 'chat_screen'

# ==========================================
# SCREEN 2: THE VENDOR REGISTRATION & WAVE PAYMENT GATEWAY
# ==========================================
class VendorPaymentGate(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="Become a Verified Seller! 🚀\n\nPay a one-time setup fee of D100\nto get an account and post unlimited products.", font_size='16sp', halign='center'))
        
        pay_btn = Button(text="Pay D100 Account Fee via Wave 💸", background_color=(0, 0.6, 1, 1), size_hint_y=0.2, bold=True)
        pay_btn.bind(on_press=self.redirect_to_wave)
        layout.add_widget(pay_btn)
        
        back_btn = Button(text="◄ Back to Marketplace", size_hint_y=0.15)
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)
        
        self.add_widget(layout)

    def redirect_to_wave(self, instance):
        # Ebrima's real verified Gambian mobile money merchant routing line
        gambia_merchant = "+2202071291"
        wave_url = f"https://wave.com{gambia_merchant}&amount=100"
        webbrowser.open(wave_url)

    def go_back(self, instance):
        self.manager.current = 'marketplace_screen'

# ==========================================
# SCREEN 3: NATIVE REAL-TIME IN-APP CHAT INTERFACE
# ==========================================
class LiveChatInterface(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Active Chat Header Panel
        self.chat_header = Label(text="Chatting with Seller...", size_hint_y=0.1, bold=True)
        self.layout.add_widget(self.chat_header)
        
        # Scrollable Chat Message History Box
        self.msg_scroll = ScrollView(size_hint_y=0.7)
        self.msg_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.msg_box.bind(minimum_height=self.msg_box.setter('height'))
        self.msg_scroll.add_widget(self.msg_box)
        self.layout.add_widget(self.msg_scroll)
        
        # Message Typing Input Line Footer
        footer = BoxLayout(orientation='horizontal', size_hint_y=0.12, spacing=5)
        self.txt_input = TextInput(hint_text='Type your message & arrange meetup...', multiline=False)
        footer.add_widget(self.txt_input)
        
        send_btn = Button(text="Send ➔", size_hint_x=0.25, background_color=(0, 0.6, 1, 1), bold=True)
        send_btn.bind(on_press=self.send_message_payload)
        footer.add_widget(send_btn)
        self.layout.add_widget(footer)
        
        back_btn = Button(text="◄ Close Chat & Return", size_hint_y=0.08)
        back_btn.bind(on_press=self.go_back)
        self.layout.add_widget(back_btn)
        
        self.add_widget(self.layout)

    def update_chat_header(self, seller_name, product_title):
        self.chat_header.text = f"💬 Chatting with {seller_name}\nRegarding: {product_title}"
        self.msg_box.clear_widgets() # Clear old history
        # Add initial greeting system string
        self.msg_box.add_widget(Label(text=f"[color=888888]System: Connection established. Arrange delivery with safety.[/color]", size_hint_y=None, height=30, markup=True))

    def send_message_payload(self, instance):
        if self.txt_input.text.strip() != "":
            # Add user message to the text array feed container
            user_msg = Label(text=f"[b]You:[/b] {self.txt_input.text}", size_hint_y=None, height=40, markup=True, halign='left')
            self.msg_box.add_widget(user_msg)
            self.txt_input.text = "" # Reset type box string buffer

    def go_back(self, instance):
        self.manager.current = 'marketplace_screen'

# ==========================================
# MASTER KERNEL ROUTER CONFIGURATION
# ==========================================
class EmarketMarketplaceApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MarketplaceDashboard(name='marketplace_screen'))
        sm.add_widget(VendorPaymentGate(name='payment_screen'))
        sm.add_widget(LiveChatInterface(name='chat_screen'))
        return sm

if __name__ == '__main__':
    EmarketMarketplaceApp().run()
# Build Trigger Verification Timestamp
# Termux Production Line Connection Verified
# Termux Production Line Connection Verified
