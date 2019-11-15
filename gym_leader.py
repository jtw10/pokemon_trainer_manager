from abstract_trainer import AbstractTrainer


class GymLeader(AbstractTrainer):
    """ GymLeader class (derived from AbstractTrainer) """

    TRAINER_TYPE = 'Gym Leader'
    TRAINER_CLASS = 'Gym Leader'

    def __init__(self, name, pokemon_team, trainer_class, pokecoins, location,
                 badge, element, prize):
        """ Constructor - Initializes the main attributes of GymLeader """
        super().__init__(name, pokemon_team, GymLeader.TRAINER_CLASS,
                         pokecoins, location)
        GymLeader._str_validator(badge)
        self._badge = badge
        GymLeader._str_validator(element)
        self._element = element
        GymLeader._str_validator(prize)
        self._prize = prize

    def get_type(self):
        """ Returns the trainer type """
        return GymLeader.TRAINER_TYPE

    def get_details(self):
        """ Return the trainer details """
        return ('{0} {1} {2} from {3} has {4} pokemon(s)').format(
            self._element, GymLeader.TRAINER_CLASS, self._name, self._location,
            len(self._pokemon_team))

    def get_badge(self):
        """ Returns the badge """
        return self._badge

    def get_element(self):
        """ Returns the trainer element """
        return self._element

    def get_prize(self):
        """ Returns the prize """
        return self._prize

    def to_dict(self):
        """ Returns Python dictionary representation of GymLeader """
        dict = {}

        dict['id'] = self._id
        dict['name'] = self._name
        dict['pokemon_team'] = self._pokemon_team
        dict['trainer_class'] = self._trainer_class
        dict['pokecoins'] = self._pokecoins
        dict['location'] = self._location
        dict['badge'] = self._badge
        dict['element'] = self._element
        dict['prize'] = self._prize

        return dict

    @staticmethod
    def _str_validator(arg):
        """ Validator for string input """
        if arg is None or arg == '' or type(arg) != str:
            raise ValueError('Incorrect value: input should be a string')
