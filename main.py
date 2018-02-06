import collections
import utils

unacceptable_venue = collections.namedtuple('unacceptable_venue', ['venue_name', 'reason', 'person_name'])
acceptable_venue = collections.namedtuple('acceptable_venue', ['venue_name'])


def _parse_venues(venues, users):
    acceptable_venues = []
    unacceptable_venues = []

    for user in users:
        user_drink_set_multi = set(user['drinks'])
        user_wont_eat_set_multi = set(user['wont_eat'])

        for venue in venues:
            venue_drink_set = set(venue['drinks'])
            venue_food_set = set(venue['food'])

            if user_drink_set_multi.intersection(venue_drink_set):
                pass
            else:
                unacceptable_venues.append(unacceptable_venue(venue['name'], 'no_drink', user['name']))

            if user_wont_eat_set_multi.intersection(venue_food_set):
                unacceptable_venues.append(unacceptable_venue(venue['name'], 'no_food', user['name']))

            acceptable_venues.append(acceptable_venue(venue['name']))

    return acceptable_venues, unacceptable_venues


def _find_acceptable_venues(acceptable_venues, unacceptable_venues):
    return set(
        [f.venue_name for f in unacceptable_venues]
    ).symmetric_difference(
        set([f.venue_name for f in acceptable_venues]))

def _output_acceptable_venues(acceptable_venues):
    print('Places to go:')
    for venue in acceptable_venues:
        print(venue)


def _output_unacceptable_venues(parsed_unacceptable_venues):
    print('Places to avoid:')
    for venue in parsed_unacceptable_venues:
        print('Venue: {}, reason: {}, for person {}'.format(venue[0], venue[1], venue[2]))


def main():
    """
    Barebones, I would like to add proper inputs etc,

    """
    # load input files
    venues = utils.load_input('./input/venues.json')
    users = utils.load_input('./input/users.json')

    # input for further down
    parsed_acceptable_venues, parsed_unacceptable_venues = _parse_venues(venues, users)

    # find un/acceptable venues
    acceptable_venues = _find_acceptable_venues(parsed_acceptable_venues, parsed_unacceptable_venues)

    # output acceptable events
    _output_acceptable_venues(acceptable_venues)

    # output unacceptable events
    _output_unacceptable_venues(parsed_unacceptable_venues)


if __name__ == "__main__":
    main()
