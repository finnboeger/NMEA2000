import time
from math import radians

import can

import n2k
from n2k.messages import WindSpeed

bus = can.Bus("can0", interface="socketcan")
notifier = can.Notifier(bus, [])
device_information = n2k.DeviceInformation(
    unique_number=1,
    manufacturer_code=2046,
    device_function=130,
    device_class=25,
    industry_group=4,
)
n2k_node = n2k.Node(bus, device_information)
n2k_node.set_product_information("Test", "0.0.1", "Dev", "00000000001", 2)
n2k_node.set_configuration_information()

# n2k.set_log_level(logging.DEBUG)


class Handler(n2k.MessageHandler):
    def __init__(self, node: n2k.Node) -> None:
        super().__init__(0, node)

    def handle_msg(self, msg: n2k.Message) -> None:
        if msg.pgn not in (n2k.PGN.WindSpeed, n2k.PGN.VesselHeading):
            return
        if msg.pgn == n2k.PGN.WindSpeed:
            print(msg)
            wind_data = n2k.messages.parse_n2k_wind_speed(msg)
            print(wind_data)
        else:
            print(n2k.messages.parse_n2k_heading(msg))


handler = Handler(n2k_node)
n2k_node.attach_msg_handler(handler)

# notifier.add_listener(print)
notifier.add_listener(n2k_node)

while True:
    time.sleep(0.2)
    msg = n2k.messages.create_n2k_wind_speed_message(
        WindSpeed(
            wind_speed=10,
            wind_angle=radians(340),
            wind_reference=n2k.types.N2kWindReference.TrueNorth,
            sid=0,
        ),
    )
    n2k_node.send_msg(msg)
