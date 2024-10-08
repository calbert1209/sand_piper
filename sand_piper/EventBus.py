from adafruit_macropad import MacroPad
from supervisor import ticks_ms
from keypad import Event as KeypadEvent


class HidEvent:
    def __init__(self, type: str, timestamp: int):
        self.type = type
        self.timestamp = timestamp

    def toStr(self):
        return '{} {}'.format(self.timestamp, self.type)


class KeyEvent(HidEvent):
    def __init__(self, event: KeypadEvent):
        super().__init__("key", event.timestamp)
        self.pressed = event.pressed
        self.released = event.released
        self.key_number = event.key_number

    def toStr(self):
        return "{} {}".format(super().toStr(), self.key_number, self.pressed)


class EncoderEvent(HidEvent):
    def __init__(self, previous: int, current: int):
        super().__init__("enc", ticks_ms())
        self.previous = previous
        self.current = current
        self.delta = current - previous

    def toStr(self):
        return "{} ({})".format(super().toStr(), self.delta)


class EncoderSwitchEvent(HidEvent):
    def __init__(self, pressed: bool):
        super().__init__("enc_sw", ticks_ms())
        self.pressed = pressed
        self.released = not pressed

    def toStr(self):
        return "{} {}".format(super().toStr(), self.pressed)


class EventBus:
    def __init__(self, macroPad: MacroPad):
        self.macroPad = macroPad
        self.events: list[HidEvent] = []
        self.lastEncoderSwitch = False
        self.lastEncoder = 0
        self.listeners: list[(str, callable[[HidEvent], None])] = []

    def _getKeyEvents(self):
        k_event = self.macroPad.keys.events.get()
        while k_event:
            self.events.append(KeyEvent(k_event))
            k_event = self.macroPad.keys.events.get()

    def _getEncoderSwitchEvent(self):
        enc_switch = self.macroPad.encoder_switch
        if enc_switch != self.lastEncoderSwitch:
            self.events.append(EncoderSwitchEvent(pressed=enc_switch))
            self.lastEncoderSwitch = enc_switch

    def _getEncoderEvent(self):
        encoder = self.macroPad.encoder
        if encoder != self.lastEncoder:
            self.events.append(EncoderEvent(self.lastEncoder, encoder))
            self.lastEncoder = encoder

    def update(self):
        self._getKeyEvents()
        self._getEncoderSwitchEvent()
        self._getEncoderEvent()
