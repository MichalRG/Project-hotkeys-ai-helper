import keyboard

from events.EventManager import EventManager

event_manager = EventManager()

keyboard.add_hotkey('ctrl+alt+1', event_manager.translate_event)

keyboard.wait('ctrl+alt+num 0') 