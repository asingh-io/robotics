from NexusConstant import *


def percentage_to_value(percentage_value, min_actual_value, max_actual_value):
    negative = False
    if percentage_value < 0:
        negative = True
    percentage_value = abs(percentage_value)
    if percentage_value < 0:
        percentage_value = 0
    if percentage_value > 100:
        percentage_value = 100

    speed_mmsec = min_actual_value + (percentage_value / 100) * (
        max_actual_value - min_actual_value
    )
    if negative == True:
        return speed_mmsec * -1
    else:
        return speed_mmsec


def get_speed_mmsec(percentage_value):
    return percentage_to_value(
        percentage_value, DEFAULT_MIN_SPEED_MMSEC, DEFAULT_MAX_SPEED_MMSEC
    )


def get_acceleration_mmsec2(percentage_value):
    return percentage_to_value(
        percentage_value,
        DEFAULT_MIN_ACCELERATION_MMSEC,
        DEFAULT_MAX_ACCELERATION_MMSEC,
    )


def get_turn_rate_degsec(percentage_value):
    return percentage_to_value(
        percentage_value, DEFAULT_MIN_TURN_RATE_DEGSEC, DEFAULT_MAX_TURN_RATE_DEGSEC
    )


def get_turn_acceleration_degsec2(percentage_value):
    return percentage_to_value(
        percentage_value,
        DEFAULT_MIN_TURN_ACCELERATION_DEGSEC2,
        DEFAULT_MAX_TURN_ACCELERATION_DEGSEC2,
    )


