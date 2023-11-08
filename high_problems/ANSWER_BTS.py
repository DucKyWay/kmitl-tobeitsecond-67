EXCEED_CONDITIONS = [
    ('N', 24),
    ('E', 23),
    ('S', 12),
    ('W', 1),
]

BTS_FARE = {
    0: 17,
    1: 17,
    2: 25,
    3: 28,
    4: 32,
    5: 35,
    6: 40,
    7: 43,
    8: 47,
}
BTS_OPERATED_STATIONS = [
    ('N', 8),
    ('E', 9),
    ('S', 8),
    ('W', 1),
]

BMA_FARE = 15
BMA_FREE_FARE = 0


def organize_station(origin: str, dest: str):
    '''Organize station id'''

    # Check if origin and/or destination is at Siam
    if origin == 'CEN':
        if dest[0] == 'N':
            origin = 'N0'
        elif dest[0] == 'E':
            origin = 'E0'
        elif dest[0] == 'W':
            origin = 'W0'
        elif dest[0] == 'S':
            origin = 'S0'
        else:
            origin = 'E0'

    if dest == 'CEN':
        if origin[0] == 'N':
            dest = 'N0'
        elif origin[0] == 'E':
            dest = 'E0'
        elif origin[0] == 'W':
            dest = 'W0'
        elif origin[0] == 'S':
            dest = 'S0'
        else:
            dest = 'E0'

    origin_side = origin[0]
    dest_side = dest[0]

    origin_stations = int(origin[1:])
    dest_stations = int(dest[1:])

    return origin_side, dest_side, origin_stations, dest_stations


def is_station_exceed(origin: str, dest: str):
    '''Check that station is exceeded'''

    origin_side, dest_side, origin_stations, dest_stations = organize_station(
        origin, dest)

    if 'N6' in (origin, dest):
        return True

    # Check if station ID is exceed
    for side, station in EXCEED_CONDITIONS:
        if origin_side == side and origin_stations > station:
            return True

        if dest_side == side and dest_stations > station:
            return True

    return False


def calculate_bma_free_fare(origin: str, dest: str):
    '''Calculate BMA free fare, if user travelled between BMA free fare'''

    origin_side, dest_side, origin_stations, dest_stations = organize_station(
        origin, dest)

    travel_between_mochit_khokhot = 'N' == origin_side and 'N' == dest_side \
        and 8 <= origin_stations <= 24 and 8 <= dest_stations <= 24
    travel_between_bearing_kheha = 'E' == origin_side and 'E' == dest_side \
        and 14 <= origin_stations <= 23 and 14 <= dest_stations <= 23

    return any([
        travel_between_mochit_khokhot,
        travel_between_bearing_kheha
    ])


def calculate_bma_paid_fare(origin: str, dest: str):
    '''Calculate BMA paid fare, if user travelled between BMA paid fare'''

    origin_side, dest_side, origin_stations, dest_stations = organize_station(
        origin, dest)

    travel_between_wwyai_bangwa = 'S' == origin_side and 'S' == dest_side \
        and 8 <= origin_stations <= 12 and 8 <= dest_stations <= 12
    travel_between_onnut_bearing = 'E' == origin_side and 'E' == dest_side \
        and 9 <= origin_stations <= 14 and 9 <= dest_stations <= 14
    travel_between_onnut_kheha = 'E' == origin_side and 'E' == dest_side \
        and 9 <= origin_stations <= 23 and 9 <= dest_stations <= 23

    return any([
        travel_between_wwyai_bangwa,
        travel_between_onnut_bearing,
        travel_between_onnut_kheha
    ])


def is_pass_bma_paid_section(origin: str, dest: str):
    '''Check if user travelled pass in BMA paid section'''

    origin_side, dest_side, origin_stations, dest_stations = organize_station(
        origin, dest)

    is_come_from_bangwa = (
        origin_side == 'S' and 12 <= origin_stations <= 9
    ) or (
        dest_side == 'S' and 12 <= dest_stations <= 9
    )
    is_go_to_wongwianyai = (
        origin_side == 'S' and 12 >= origin_stations >= 9
    ) or (
        dest_side == 'S' and 12 >= dest_stations >= 9
    )

    is_come_from_bearing = (
        origin_side == 'E' and 9 <= origin_stations <= 23
    ) or (
        dest_side == 'E' and 9 <= dest_stations <= 23
    )
    is_go_to_onnut = (
        origin_side == 'E' and 9 >= origin_stations >= 23
    ) or (
        dest_side == 'E' and 9 >= dest_stations >= 23
    )

    return any([
        is_come_from_bangwa,
        is_go_to_wongwianyai,
        is_come_from_bearing,
        is_go_to_onnut
    ])


def calculate_bts_fare(origin: str, dest: str):
    '''Calculate BTS fare (all section)'''

    origin_side, dest_side, origin_stations, dest_stations = organize_station(
        origin, dest)

    bts_origin_stations = origin_stations
    bts_dest_stations = dest_stations

    for side, stations in BTS_OPERATED_STATIONS:
        if origin_side == side and origin_stations > stations:
            bts_origin_stations = stations

        if dest_side == side and dest_stations > stations:
            bts_dest_stations = stations

    fare = 0

    if calculate_bma_free_fare(origin, dest):
        return BMA_FREE_FARE

    elif calculate_bma_paid_fare(origin, dest):
        return BMA_FARE

    # Check if destination pass Siam (CEN)
    if origin_side is not dest_side:
        bts_total_stations = bts_origin_stations + bts_dest_stations
    else:
        bts_total_stations = abs(bts_origin_stations - bts_dest_stations)

    if is_pass_bma_paid_section(origin, dest):
        fare += BMA_FARE

    fare += BTS_FARE.get(bts_total_stations) or 47

    return fare


def main() -> None:
    '''This is main function'''

    origin = input()
    dest = input()

    if is_station_exceed(origin, dest):
        return print('Error')

    total_fare = calculate_bts_fare(origin, dest)

    print(total_fare)


main()
