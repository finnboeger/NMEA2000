from typing import NamedTuple, List, Optional

from n2k.device_information import DeviceInformation
from n2k.n2k import PGN
from n2k.message import Message
from n2k.types import N2kTimeSource, N2kAISRepeat, N2kAISTransceiverInformation, N2kMOBStatus, N2kMOBPositionSource, \
    N2kHeadingReference, N2kMOBEmitterBatteryStatus, N2kOnOff, N2kSteeringMode, N2kTurnMode, N2kRudderDirectionOrder, \
    ProductInformation, ConfigurationInformation, N2kWindReference
from n2k.constants import *
from n2k.utils import IntRef


# System Date/Time (PGN 126992)
class SystemTime(Message):
    sid: int
    system_date: int
    system_time: float
    time_source: N2kTimeSource

    def __init__(self):
        super().__init__()
        self.pgn = PGN.SystemDateTime
        self.priority = 3

    @classmethod
    def from_values(cls, sid: int, system_date: int, system_time: float,
                    time_source: N2kTimeSource = N2kTimeSource.GPS) -> 'SystemTime':
        """
        Generate NMEA2000 message containing specified System Date/Time (PGN 126992). System Time is in UTC.

        :param sid: Sequence ID. If your device provides e.g. boat speed and heading at same time, you can set the same SID
            different messages to indicate that they are measured at same time
        :param system_date: Days since 1970-01-01
        :param system_time: seconds since midnight
        :param time_source: Time source, see :py:class:`n2k_types.N2kTimeSource`
        :return: NMEA2000 message ready to be sent.
        """
        msg = cls()
        msg.add_byte_uint(sid)
        msg.add_byte_uint((time_source & 0x0f) | 0xf0)
        msg.add_2_byte_uint(system_date)
        msg.add_4_byte_double(system_time, 1e-4)
        return msg
        
    @classmethod
    def from_can(cls, buf: bytearray) -> 'SystemTime':
        """
        Parse current system time from a PGN 126992 message

        :param buf: data bytes (already combined if sent via multiple frames)
        :return: SystemTime Message Object containing the parsed information
        """
        msg = cls()
        msg.data = buf
        index = IntRef(0)
        msg.sid = msg.get_byte_uint(index)
        msg.time_source = N2kTimeSource(msg.get_byte_uint(index) & 0x0f)
        msg.system_date = msg.get_2_byte_uint(index)
        msg.system_date = msg.get_4_byte_udouble(0.0001, index)
        return msg


# AIS Safety Related Broadcast Message (PGN 129802)
def set_n2k_ais_related_broadcast_msg(message_id: int, repeat: N2kAISRepeat, source_id: int,
                                      ais_transceiver_information: N2kAISTransceiverInformation,
                                      safety_related_text: str) -> Message:
    """
    Generate NMEA2000 message containing AIS Safety Related Broadcast Message. (PGN 129802)
    
    :param message_id: Message Type. Identifier for AIS Safety Related Broadcast Message aka Message 14; always 14.
    :param repeat: Repeat indicator. Used by the repeater to indicate how many times a message has been repeated.
        0-3; 0 = default; 3 = do not repeat anymore
    :param source_id: MMSI number of source station of message
    :param ais_transceiver_information: see :py:class:`n2k_types.N2kAISTransceiverInformation`
    :param safety_related_text: Maximum 121 bytes. Encoded as 6-bit ASCII
    :return: NMEA2000 message ready to be sent.
    """
    print("NotImplemented, set_n2k_ais_related_broadcast_msg")


class AISSafetyRelatedBroadcast(NamedTuple):
    message_id: int
    repeat: N2kAISRepeat
    source_id: int
    ais_transceiver_information: N2kAISTransceiverInformation
    safety_related_text: str


def parse_n2k_ais_related_broadcast_msg(msg: Message) -> AISSafetyRelatedBroadcast:
    """
    Parse current system time from a PGN 126992 message
    
    :param msg: NMEA2000 Message with PGN 126992
    :return: Dictionary containing the parsed information.
    """
    print("NotImplemented, parse_n2k_ais_related_broadcast_msg")


# Man Overboard Notification (PGN 127233)
def set_n2k_mob_notification(sid: int, mob_emitter_id: int, mob_status: N2kMOBStatus, activation_time: float,
                             position_source: N2kMOBPositionSource, position_date: int, position_time: float,
                             latitude: float, longitude: float, cog_reference: N2kHeadingReference, cog: float,
                             sog: float, mmsi: int,
                             mob_emitter_battery_status: N2kMOBEmitterBatteryStatus) -> Message:
    """
    Generate NMEA2000 message containing Man Overboard Notification (PGN 127233)
    
    :param sid: Sequence ID. If your device provides e.g. boat speed and heading at same time, you can set the same SID
        for different messages to indicate that they are measured at same time.
    :param mob_emitter_id: Identifier for each MOB emitter, unique to the vessel
    :param mob_status: MOB Status, see :py:class:`n2k_types.N2kMOBStatus`
    :param activation_time: Time of day (UTC) in seconds when MOB was initially activated
    :param position_source: Position Source, see :py:class:`n2k_types.N2kMOBPositionSource`
    :param position_date: Date of MOB position in days since 1970-01-01 (UTC)
    :param position_time: Time of day of MOB position (UTC) in seconds
    :param latitude: Latitude in degrees
    :param longitude: Longitude in degrees
    :param cog_reference: True or Magnetic
    :param cog: Course Over Ground in radians with a resolution of 1x10E-4 rad
    :param sog: Speed Over Ground in m/s with a resolution of 1x10E-2 m/s
    :param mmsi: MMSI of vessel of Origin. Can be set to 2,147,483,647 if unknown
    :param mob_emitter_battery_status: see :py:class:`n2k_types.N2kMOBEmitterBatteryStatus`
    :return: NMEA2000 message ready to be sent.
    """
    print("NotImplemented, set_n2k_mob_notification")


class MOBNotification(NamedTuple):
    sid: int
    mob_emitter_id: int
    mob_status: N2kMOBStatus
    activation_time: float
    position_source: N2kMOBPositionSource
    position_date: int
    position_time: float
    latitude: float
    longitude: float
    cog_reference: N2kHeadingReference
    cog: float
    sog: float
    mmsi: int
    mob_emitter_battery_status: N2kMOBEmitterBatteryStatus
    
    
def parse_n2k_mob_notification(msg: Message) -> MOBNotification:
    """
    Parse Man Over Board Notification from a PGN 127233 message

    :param msg: NMEA2000 Message with PGN 127233
    :return: Dictionary containing the parsed information.
    """
    print("NotImplemented, parse_n2k_mob_notification")


# Heading/Track Control (PGN 127237)
def set_n2k_heading_track_control(rudder_limit_exceeded: N2kOnOff, off_heading_limit_exceeded: N2kOnOff,
                                  off_track_limit_exceeded: N2kOnOff, override: N2kOnOff,
                                  steering_mode: N2kSteeringMode, turn_mode: N2kTurnMode,
                                  heading_reference: N2kHeadingReference,
                                  commanded_rudder_direction: N2kRudderDirectionOrder,
                                  commanded_rudder_angle: float, heading_to_steer_course: float, track: float,
                                  rudder_limit: float, off_heading_limit: float, radius_of_turn_order: float,
                                  rate_of_turn_order: float, off_track_limit: float,
                                  vessel_heading: float) -> Message:
    """
    Generate NMEA2000 message containing Heading/Track Control information (PGN 127233)
    
    :param rudder_limit_exceeded: Yes/No
    :param off_heading_limit_exceeded: Yes/No
    :param off_track_limit_exceeded: Yes/No
    :param override: Yes/No
    :param steering_mode: Steering Mode
    :param turn_mode: Turn Mode
    :param heading_reference: True or Magnetic
    :param commanded_rudder_direction: Port or Starboard
    :param commanded_rudder_angle: In radians
    :param heading_to_steer_course: In radians
    :param track: In radians
    :param rudder_limit: In radians
    :param off_heading_limit: In radians
    :param radius_of_turn_order: In meters
    :param rate_of_turn_order: In radians/s
    :param off_track_limit: In meters
    :param vessel_heading: In radians
    :return: NMEA2000 message ready to be sent.
    """
    print("NotImplemented, set_n2k_heading_track_control")


class HeadingTrackControl(NamedTuple):
    rudder_limit_exceeded: N2kOnOff
    off_heading_limit_exceeded: N2kOnOff
    off_track_limit_exceeded: N2kOnOff
    override: N2kOnOff
    steering_mode: N2kSteeringMode
    turn_mode: N2kTurnMode
    heading_reference: N2kHeadingReference
    commanded_rudder_direction: N2kRudderDirectionOrder
    commanded_rudder_angle: float
    heading_to_steer_course: float
    track: float
    rudder_limit: float
    off_heading_limit: float
    radius_of_turn_order: float
    rate_of_turn_order: float
    off_track_limit: float
    vessel_heading: float
    

def parse_n2k_heading_track_control(msg: Message) -> HeadingTrackControl:
    """
    Parse heading/track control information from a PGN 127237 message

    :param msg: NMEA2000 Message with PGN 127237
    :return: Dictionary containing the parsed information.
    """
    print("NotImplemented, parse_n2k_heading_track_control")


# Rudder (PGN 127245)
def set_n2k_rudder(rudder_position: float, instance: int = 0,
                   rudder_direction_order: N2kRudderDirectionOrder = N2kRudderDirectionOrder.NoDirectionOrder,
                   angle_order: float = N2K_DOUBLE_NA) -> Message:
    """
    Rudder
    
    :param rudder_position: Current rudder postion in radians.
    :param instance: Rudder instance.
    :param rudder_direction_order: Direction, where rudder should be turned.
    :param angle_order: Angle where rudder should be turned in radians.
    :return: NMEA2000 Message ready to be sent.
    """
    print("NotImplemented, set_n2k_rudder")


class Rudder(NamedTuple):
    rudder_position: float
    instance: int
    rudder_direction_order: N2kRudderDirectionOrder
    angle_order: float
    

def parse_n2k_rudder(msg: Message) -> Rudder:
    """
    Parse rudder control information from a PGN 127245 message
    
    :param msg: NMEA2000 Message with PGN 127245
    :return: Dictionary containing the parsed information
    """
    print("NotImplemented, parse_n2k_rudder")


# Vessel Heading (PGN 127250)
def set_n2k_heading(sid: int, heading: float, deviation: float = N2K_DOUBLE_NA, variation: float = N2K_DOUBLE_NA,
                    ref: N2kHeadingReference = N2kHeadingReference.true) -> Message:
    """
    Vessel Heading (PGN 127250).
    If the true heading is used, leave the deviation and variation undefined. Else if the magnetic heading is sent,
    specify the magnetic deviation and variation.
    
    :param sid: Sequence ID. If your device provides e.g. boat speed and heading at same time, you can set the same SID
        for different messages to indicate that they are measured at same time.
    :param heading: Heading in radians
    :param deviation: Magnetic deviation in radians. Use `N2K_DOUBLE_NA` for undefined value.
    :param variation: Magnetic variation in radians. Use `N2K_DOUBLE_NA` for undefined value.
    :param ref: Heading reference. Can be true or magnetic.
    :return: NMEA2000 message ready to be sent.
    """
    print("NotImplemented, set_n2k_heading")


class Heading(NamedTuple):
    sid: int
    heading: float
    deviation: float
    variation: float
    ref: N2kHeadingReference


def parse_n2k_heading(msg: Message) -> Heading:
    """
    Parse heading information from a PGN 127250 message
    
    :param msg: NMEA2000 Message with PGN 127250
    :return: Dictionary containing the parsed information
    """
    print("NotImplemented, parse_n2k_heading")


# Rate of Turn (PGN 127251)
# TODO


# Attitude (PGN 127257)
# TODO


# Magnetic Variation (PGN 127258)
# TODO


# Engine parameters rapid (PGN 127488)
# TODO


# Engine parameters dynamic (PGN 127489)
# TODO


# Transmission parameters, dynamic (PGN 127493)
# TODO


# Trip Parameters, Engine (PGN 127497)
# TODO


N2kBinaryStatus = int


def n2k_get_status_on_binary_status(bank_status: N2kBinaryStatus, item_index: int = 1) -> N2kOnOff:
    """
    Get single status of full binary bank status returned by :py:func:`parse_n2k_binary_status`.
    
    :param bank_status: Full bank status read by :py:func:`parse_n2k_binary_status`
    :param item_index: Status item index 1-28
    :return: single status of full binary bank status
    """
    print("NotImplemented, n2k_get_status_on_binary_status")


def n2k_reset_binary_status(bank_status: N2kBinaryStatus) -> None:
    # TODO: can't pass int as reference in python so this doesn't make any sense
    print("NotImplemented, n2k_reset_binary_status")


def n2k_set_status_binary_on_status(bank_status: N2kBinaryStatus, item_status: N2kOnOff, item_index: int = 1) -> N2kBinaryStatus:
    """
    Set single status to full binary bank status.
    
    :param bank_status: Existing Bank Status
    :param item_status: New Item Status
    :param item_index: Index of Item to be changed
    :return: New Bank Status
    """
    print("NotImplemented, n2k_set_status_binary_on_status")


# Binary status report (PGN 127501)
# TODO


# Fluid level (PGN 127505)
# TODO


# DC Detailed Status (PGN 127506)
# TODO


# Charger Status (PGN 127507)
# TODO


# Battery Status (PGN 127508)
# TODO


# Battery Configuration Status (PGN 127513)
# TODO


# Leeway (PGN 128000)
# TODO


# Boat Speed (PGN 128259)
# TODO


# Water depth (PGN 128267)
# TODO


# Distance log (PGN 128275)
# TODO


# Anchor Windlass Control Status (PGN 128776)
# TODO


# Anchor Windlass Operating Status (PGN 128777)
# TODO


# Anchor Windlass Monitoring Status (PGN 128778)
# TODO


# Lat/lon rapid (PGN 129025)
# TODO


# COG SOG rapid (PGN 129026)
# TODO


# GNSS Position Data (PGN 129029)
# TODO


# Date,Time & Local offset (PGN 129033, see also PGN 126992)
# TODO


# AIS position reports for Class A (PGN 129038)
# TODO


# AIS position reports for Class B (PGN 129039)
# TODO


# AIS Aids to Navigation (AtoN) Report (PGN 129041)
# TODO


# Cross Track Error (PGN 129283)
# TODO


# Navigation info (PGN 129284)
# TODO


# Route/WP information (PGN 129285)
# TODO


# GNSS DOP data (PGN 129539)
# TODO


# GNSS Satellites in View (PGN 129540)
# TODO


# AIS static data class A (PGN 129794)
# TODO


# AIS static data class B part A (PGN 129809)
# TODO


# AIS static data class B part B (PGN 129810)
# TODO


# Waypoint list (PGN 130074)
# TODO


# Wind Speed (PGN 130306)
def set_n2k_wind_speed(sid: int, wind_speed: float, wind_angle: float, wind_reference: N2kWindReference) -> Message:
    """
    Wind Speed (PGN 130306)

    :param sid: Sequence ID. If your device provides e.g. boat speed and heading at same time, you can set the same SID
        for different messages to indicate that they are measured at same time.
    :param wind_speed: Wind Speed in meters per second
    :param wind_angle: Wind Angle in radians
    :param wind_reference: Can be e.g. Theoretical Wind using True North or Magnetic North,
        Apparent Wind as measured, ...\n
        See :py:class:`n2k.types.N2kWindReference`
    :return: NMEA2000 message ready to be sent.
    """
    msg = Message()
    msg.pgn = PGN.WindSpeed
    msg.priority = 2
    msg.add_byte_uint(sid)
    msg.add_2_byte_udouble(wind_speed, 0.01)
    msg.add_2_byte_udouble(wind_angle, 0.0001)
    msg.add_byte_uint(wind_reference)
    msg.add_byte_uint(0xff)  # Reserved
    msg.add_byte_uint(0xff)  # Reserved
    return msg


class WindSpeed(NamedTuple):
    sid: int
    heading: float
    deviation: float
    variation: float
    ref: N2kHeadingReference


def parse_n2k_wind_speed(msg: Message) -> WindSpeed:
    """
    Parse heading information from a PGN 127250 message

    :param msg: NMEA2000 Message with PGN 127250
    :return: Dictionary containing the parsed information
    """
    print("NotImplemented, parse_n2k_heading")


# Outside Environmental parameters (PGN 130310)
# TODO


# Environmental parameters (PGN 130311)
# TODO


# Temperature [deprecated] (PGN 130312)
# TODO


# Humidity (PGN 130313)
# TODO


# Pressure (PGN 130314)
# TODO


# Set pressure (PGN 130315)
# TODO


# Temperature (PGN 130316)
# TODO


# Meteorological Station Data (PGN 130323)
# TODO


# Small Craft Status (Trim Tab Position) (PGN 130576)
# TODO


# Direction Data (PGN 130577)
# TODO


# ISO Acknowledgement (PGN 59392)
def set_n2k_pgn_iso_acknowledgement(msg: Message, control: int, group_function: int, pgn: int) -> None:
    msg.pgn = PGN.IsoAcknowledgement
    msg.priority = 6
    msg.add_byte_uint(control)
    msg.add_byte_uint(group_function)
    msg.add_byte_uint(0xff)  # Reserved
    msg.add_byte_uint(0xff)  # Reserved
    msg.add_byte_uint(0xff)  # Reserved
    msg.add_3_byte_int(pgn)


# ISO Address Claim (PGN 60928)
def set_n2k_iso_address_claim(msg: Message, unique_number: int, manufacturer_code: int, device_function: int,
                              device_class: int, device_instance: int = 0, system_instance: int = 0,
                              industry_group: int = 4) -> None:
    device_information = DeviceInformation()
    device_information.unique_number = unique_number
    device_information.manufacturer_code = manufacturer_code
    device_information.device_function = device_function
    device_information.device_class = device_class
    device_information.device_instance = device_instance
    device_information.system_instance = system_instance
    device_information.industry_group = industry_group

    set_n2k_iso_address_claim_by_name(msg, device_information.name)


def set_n2k_iso_address_claim_by_name(msg: Message, name: int) -> None:
    msg.pgn = PGN.IsoAddressClaim
    msg.priority = 6
    msg.add_uint_64(name)


# Product Information (PGN 126996)
def set_n2k_product_information(msg: Message, n2k_version: int, product_code: int, model_id: str, sw_code: str,
                                model_version: str, model_serial_code: str, certification_level: int = 1,
                                load_equivalency: int = 1) -> None:
    msg.pgn = PGN.ProductInformation
    msg.priority = 6
    msg.add_2_byte_uint(n2k_version)
    msg.add_2_byte_uint(product_code)
    msg.add_str(model_id, MAX_N2K_MODEL_ID_LEN)
    msg.add_str(sw_code, MAX_N2K_SW_CODE_LEN)
    msg.add_str(model_version, MAX_N2K_MODEL_VERSION_LEN)
    msg.add_str(model_serial_code, MAX_N2K_MODEL_SERIAL_CODE_LEN)
    msg.add_byte_uint(certification_level)
    msg.add_byte_uint(load_equivalency)


# TODO: parser
def parse_n2k_pgn_product_information(msg: Message) -> ProductInformation:
    assert msg.pgn == PGN.ProductInformation

    index = IntRef(0)
    return ProductInformation(
        n2k_version=msg.get_2_byte_uint(index),
        product_code=msg.get_2_byte_uint(index),
        n2k_model_id=msg.get_str(MAX_N2K_MODEL_ID_LEN, index),
        n2k_sw_code=msg.get_str(MAX_N2K_SW_CODE_LEN, index),
        n2k_model_version=msg.get_str(MAX_N2K_MODEL_VERSION_LEN, index),
        n2k_model_serial_code=msg.get_str(MAX_N2K_MODEL_SERIAL_CODE_LEN, index),
        certification_level=msg.get_byte_uint(index),
        load_equivalency=msg.get_byte_uint(index),
    )


# Configuration Information (PGN: 126998)
def set_n2k_configuration_information(msg: Message, manufacturer_information: str, installation_description1: str,
                                      installation_description2: str) -> None:
    total_len = 0
    max_len = msg.max_data_len - 6  # each field has 2 extra bytes
    man_info_len = min(len(manufacturer_information), Max_N2K_CONFIGURATION_INFO_FIELD_LEN)
    inst_desc1_len = min(len(installation_description1), Max_N2K_CONFIGURATION_INFO_FIELD_LEN)
    inst_desc2_len = min(len(installation_description2), Max_N2K_CONFIGURATION_INFO_FIELD_LEN)

    if total_len + man_info_len > max_len:
        man_info_len = max_len - total_len
    total_len += man_info_len
    if total_len + inst_desc1_len > max_len:
        inst_desc1_len = max_len - total_len
    total_len += inst_desc1_len
    if total_len + inst_desc2_len > max_len:
        inst_desc2_len = max_len - total_len
    total_len += inst_desc2_len

    msg.pgn = PGN.ConfigurationInformation
    msg.priority = 6

    # Installation Description 1
    msg.add_byte_uint(inst_desc1_len + 2)
    msg.add_byte_uint(0x01)
    msg.add_str(installation_description1, inst_desc1_len)

    # Installation Description 2
    msg.add_byte_uint(inst_desc2_len + 2)
    msg.add_byte_uint(0x01)
    msg.add_str(installation_description2, inst_desc1_len)

    # Manufacturer Information
    msg.add_byte_uint(man_info_len + 2)
    msg.add_byte_uint(0x01)
    msg.add_str(manufacturer_information, man_info_len)


# TODO: parser
def parse_n2k_pgn_configuration_information(msg: Message) -> ConfigurationInformation:
    assert msg.pgn == PGN.ConfigurationInformation
    index = IntRef(0)

    return ConfigurationInformation(
        installation_description1=msg.get_var_str(index) or "",
        installation_description2=msg.get_var_str(index) or "",
        manufacturer_information=msg.get_var_str(index) or "",
    )


# ISO Request (PGN 59904)
def set_n2k_pgn_iso_request(msg: Message, destination: int, requested_pgn: int) -> None:
    msg.pgn = PGN.IsoRequest
    msg.destination = destination
    msg.priority = 6
    msg.add_3_byte_int(requested_pgn)


def parse_n2k_pgn_iso_request(msg: Message) -> Optional[int]:
    if 3 <= msg.data_len <= 8:
        return msg.get_3_byte_uint(IntRef(0))
    return None

# enum tN2kPGNList {N2kpgnl_transmit=0, N2kpgnl_receive=1 };


# PGN List (Transmit and Receive)
def set_n2k_pgn_transmit_list(msg: Message, destination: int, pgns: List[int]):
    print("NotImplemented set_n2k_pgn_transmit_list")


# Heartbeat (PGN: 126993)
# time_interval_ms: between 10 and 655'320ms
def set_heartbeat(msg: Message, time_interval_ms: int, status_byte: int) -> None:
    print("NotImplemented set_heartbeat")
