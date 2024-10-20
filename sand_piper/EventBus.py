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
        return "{} {} {}".format(super().toStr(), self.key_number, self.pressed)


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
        self._keyDownHandlers = []
        self._keyUpHandlers = []
        self._encSwitchDownHandlers = []
        self._encSwitchUpHandlers = []
        self._encChangeHandlers = []
        self._onKeyDown = self._noOp
        self._onKeyUp = self._noOp
        self._onEncSwitchDown = self._noOp
        self._onEncSwitchUp = self._noOp
        self._onEncChange = self._noOp

    def _noOp(self, event: HidEvent):
        pass

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

    def _callHandlers(self, event, handlers):
        for handler in handlers:
            if callable(handler):
                handler(event)

    def _appendHandler(self, list, handler):
        list.append(handler)
        index = len(list) - 1

        def removeHandler():
            list[index] = None
            return None

        return removeHandler

    def addEventListener(self, type, handler):
        if type == "key_down":
            return self._appendHandler(self._keyDownHandlers, handler)
        elif type == "key_up":
            return self._appendHandler(self._keyUpHandlers, handler)
        elif type == "enc_down":
            return self._appendHandler(self._encSwitchDownHandlers, handler)
        elif type == "enc_up":
            return self._appendHandler(self._encSwitchUpHandlers, handler)
        elif type == "enc_change":
            return self._appendHandler(self._encChangeHandlers, handler)

    def update(self):
        self._getKeyEvents()
        self._getEncoderSwitchEvent()
        self._getEncoderEvent()
        for event in self.events:
            if event.type == "key":
                if event.pressed:
                    self._onKeyDown(event)
                    self._callHandlers(event, self._keyDownHandlers)
                else:
                    self._onKeyUp(event)
                    self._callHandlers(event, self._keyUpHandlers)
            elif event.type == "enc_sw":
                if event.pressed:
                    self._onEncSwitchDown(event)
                    self._callHandlers(event, self._encSwitchDownHandlers)
                else:
                    self._onEncSwitchUp(event)
                    self._callHandlers(event, self._encSwitchUpHandlers)
            elif event.type == "enc":
                self._onEncChange(event)
                self._callHandlers(event, self._encChangeHandlers)
        self.events = []

    def setOnKeyDown(self, cb: function[KeyEvent, None] | None):
        if cb == None:
            self._onKeyDown = self._noOp
        self._onKeyDown = cb

    def setOnEncChange(self, cb: function[EncoderEvent, None] | None):
        if cb == None:
            self._onEncChange = self._noOp
        self._onEncChange = cb

    def setOnEncSwitchDown(self, cb: function[EncoderSwitchEvent, None] | None):
        if cb == None:
            self._onEncSwitchDown = self._noOp
        self._onEncSwitchDown = cb
