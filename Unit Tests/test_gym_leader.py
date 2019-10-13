from unittest import TestCase
from gym_leader import GymLeader

import inspect


class TestGymLeader(TestCase):
    ''' Unit Tests for Gym Leader Class '''
    # Test parameters
    ID_PARAMETER = 0
    NAME_PARAMETER = 'Brock'
    POKEMON_TEAM_PARAMETER = {
        'Golem': {55},
        'Rellcanth': {54},
        'Omastar': {56},
        'Kabutops': {55},
        'Onix': {61},
        'Ramparods': {57}
    }
    LOCATION_PARAMETER = 'Kanto'
    POKECOIN_PARAMETER = 6840
    BADGE_PARAMETER = 'Boulder'
    ELEMENT_PARAMETER = 'Rock'
    PRIZE_PARAMETER = 'HM10'

    TEST_INT_PARAMETER = 0
    EMPTY_PARAMETER = ''
    UNDEFINED_PARAMETER = None

    def setUp(self):
        '''Sets up test GymLeader class'''
        self.logGymLeader()
        self.gym_leader = GymLeader(TestGymLeader.ID_PARAMETER,
                                    TestGymLeader.NAME_PARAMETER,
                                    TestGymLeader.POKEMON_TEAM_PARAMETER,
                                    GymLeader.TRAINER_CLASS,
                                    TestGymLeader.POKECOIN_PARAMETER,
                                    TestGymLeader.LOCATION_PARAMETER,
                                    TestGymLeader.BADGE_PARAMETER,
                                    TestGymLeader.ELEMENT_PARAMETER,
                                    TestGymLeader.PRIZE_PARAMETER
                                    )
        self.assertIsNotNone(self.gym_leader)

    def teardown(self):
        '''Tears down test GymLeader class'''
        self.logGymLeader()

    def logGymLeader(self):
        '''Creates log info inside console'''
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_valid_init(self):
        '''Tests valid parameters for GymLeader constructor'''
        self.gym_leader = GymLeader(TestGymLeader.ID_PARAMETER,
                                    TestGymLeader.NAME_PARAMETER,
                                    TestGymLeader.POKEMON_TEAM_PARAMETER,
                                    GymLeader.TRAINER_CLASS,
                                    TestGymLeader.POKECOIN_PARAMETER,
                                    TestGymLeader.LOCATION_PARAMETER,
                                    TestGymLeader.BADGE_PARAMETER,
                                    TestGymLeader.ELEMENT_PARAMETER,
                                    TestGymLeader.PRIZE_PARAMETER
                                    )
        self.assertIsNotNone(self.gym_leader)

    def test_invalid_parameter_init(self):
        '''Tests invalid parameters for GymLeader constructor'''
        # Testing Badge parameter
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should be a string',
                               TestGymLeader.ID_PARAMETER,
                               TestGymLeader.NAME_PARAMETER,
                               TestGymLeader.POKEMON_TEAM_PARAMETER,
                               GymLeader.TRAINER_CLASS,
                               TestGymLeader.POKECOIN_PARAMETER,
                               TestGymLeader.LOCATION_PARAMETER,
                               TestGymLeader.EMPTY_PARAMETER,
                               TestGymLeader.ELEMENT_PARAMETER,
                               TestGymLeader.PRIZE_PARAMETER)
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should be a string',
                               TestGymLeader.ID_PARAMETER,
                               TestGymLeader.NAME_PARAMETER,
                               TestGymLeader.POKEMON_TEAM_PARAMETER,
                               GymLeader.TRAINER_CLASS,
                               TestGymLeader.POKECOIN_PARAMETER,
                               TestGymLeader.LOCATION_PARAMETER,
                               TestGymLeader.UNDEFINED_PARAMETER,
                               TestGymLeader.ELEMENT_PARAMETER,
                               TestGymLeader.PRIZE_PARAMETER)
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should be a string',
                               TestGymLeader.ID_PARAMETER,
                               TestGymLeader.NAME_PARAMETER,
                               TestGymLeader.POKEMON_TEAM_PARAMETER,
                               GymLeader.TRAINER_CLASS,
                               TestGymLeader.POKECOIN_PARAMETER,
                               TestGymLeader.LOCATION_PARAMETER,
                               TestGymLeader.TEST_INT_PARAMETER,
                               TestGymLeader.ELEMENT_PARAMETER,
                               TestGymLeader.PRIZE_PARAMETER)

        # Testing Element Parameter
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should be a string',
                               TestGymLeader.ID_PARAMETER,
                               TestGymLeader.NAME_PARAMETER,
                               TestGymLeader.POKEMON_TEAM_PARAMETER,
                               GymLeader.TRAINER_CLASS,
                               TestGymLeader.POKECOIN_PARAMETER,
                               TestGymLeader.LOCATION_PARAMETER,
                               TestGymLeader.BADGE_PARAMETER,
                               TestGymLeader.EMPTY_PARAMETER,
                               TestGymLeader.PRIZE_PARAMETER)
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should be a string',
                               TestGymLeader.ID_PARAMETER,
                               TestGymLeader.NAME_PARAMETER,
                               TestGymLeader.POKEMON_TEAM_PARAMETER,
                               GymLeader.TRAINER_CLASS,
                               TestGymLeader.POKECOIN_PARAMETER,
                               TestGymLeader.LOCATION_PARAMETER,
                               TestGymLeader.BADGE_PARAMETER,
                               TestGymLeader.UNDEFINED_PARAMETER,
                               TestGymLeader.PRIZE_PARAMETER)
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should be a string',
                               TestGymLeader.ID_PARAMETER,
                               TestGymLeader.NAME_PARAMETER,
                               TestGymLeader.POKEMON_TEAM_PARAMETER,
                               GymLeader.TRAINER_CLASS,
                               TestGymLeader.POKECOIN_PARAMETER,
                               TestGymLeader.LOCATION_PARAMETER,
                               TestGymLeader.BADGE_PARAMETER,
                               TestGymLeader.TEST_INT_PARAMETER,
                               TestGymLeader.PRIZE_PARAMETER)

        # Testing Prize Parameter
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should be a string',
                               TestGymLeader.ID_PARAMETER,
                               TestGymLeader.NAME_PARAMETER,
                               TestGymLeader.POKEMON_TEAM_PARAMETER,
                               GymLeader.TRAINER_CLASS,
                               TestGymLeader.POKECOIN_PARAMETER,
                               TestGymLeader.LOCATION_PARAMETER,
                               TestGymLeader.BADGE_PARAMETER,
                               TestGymLeader.ELEMENT_PARAMETER,
                               TestGymLeader.EMPTY_PARAMETER)
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should be a string',
                               TestGymLeader.ID_PARAMETER,
                               TestGymLeader.NAME_PARAMETER,
                               TestGymLeader.POKEMON_TEAM_PARAMETER,
                               GymLeader.TRAINER_CLASS,
                               TestGymLeader.POKECOIN_PARAMETER,
                               TestGymLeader.LOCATION_PARAMETER,
                               TestGymLeader.BADGE_PARAMETER,
                               TestGymLeader.ELEMENT_PARAMETER,
                               TestGymLeader.UNDEFINED_PARAMETER)
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should be a string',
                               TestGymLeader.ID_PARAMETER,
                               TestGymLeader.NAME_PARAMETER,
                               TestGymLeader.POKEMON_TEAM_PARAMETER,
                               GymLeader.TRAINER_CLASS,
                               TestGymLeader.POKECOIN_PARAMETER,
                               TestGymLeader.LOCATION_PARAMETER,
                               TestGymLeader.BADGE_PARAMETER,
                               TestGymLeader.ELEMENT_PARAMETER,
                               TestGymLeader.TEST_INT_PARAMETER)

    def test_get_type(self):
        '''Tests if get_type() returns correct value'''
        self.assertEqual('Gym Leader', self.gym_leader.get_type())

    def test_get_badge(self):
        '''Tests if get_badge() returns correct value'''
        self.assertEqual('Boulder Badge', self.gym_leader.get_badge())

    def test_get_element(self):
        '''Tests if get_element() returns correct value'''
        self.assertEqual('Rock Type', self.gym_leader.get_element())

    def test_get_prize(self):
        '''Tests if get_prize() returns correct value'''
        self.assertEqual('HM10', self.gym_leader.get_prize())