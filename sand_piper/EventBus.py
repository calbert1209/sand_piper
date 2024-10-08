from adafruit_macropad import MacroPad
from supervisor import ticks_ms


class EventBus:
    def __init__(self, macroPad: MacroPad):
        self.macroPad = macroPad
        self.events = []
        self.lastEncoderSwitch = False

    def _getKeyEvents(self):
        k_event = self.macroPad.keys.events.get()
        while k_event:
            self.events.append({
                "type": "key",
                "payload": k_event
            })
            k_event = self.macroPad.keys.events.get()

    def _getEncoderSwitchEvent(self):
        enc_switch = self.macroPad.encoder_switch
        if enc_switch != self.lastEncoderSwitch:
            self.events.append({
                "type": "enc_sw",
                "payload": {
                    "timestamp": ticks_ms(),
                    "pressed": enc_switch,
                    "released": not enc_switch
                }
            })
            self.lastEncoderSwitch = enc_switch

    def update(self):
        self._getKeyEvents()
        self._getEncoderSwitchEvent()

    def toString(self, event):
        type = event["type"]
        payload = event["payload"]
        if type == "key":
            return "{} {} {} {}".format(
                payload.timestamp, type, payload.key_number, payload.pressed)
        if type == "enc_sw":
            return "{} {} {}".format(payload["timestamp"], type, payload["pressed"])
