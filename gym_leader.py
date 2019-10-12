from abstract_trainer import AbstractTrainer


class GymLeader(AbstractTrainer):
    """ GymLeader class (derived from AbstractTrainer) """

    TRAINER_TYPE = 'Gym Leader'
    TRAINER_CLASS = 'Gym Leader'


    def __init___(self, id, pokemon_team, trainer_class, pokecoins, location, badge, element, prize):
        """ Constructor - Initializes the main attributes of GymLeader """
        super().__init__(id, name, pokemon_team, GymLeader.TRAINER_CLASS, pokecoins, location)
        self._badge = badge
        self._element = element
        self._prize = prize

    def get_type(self):
        """ Returns the trainer type """
        return GymLeader.TRAINER_TYPE

    def get_badge(self):
        """ Returns the badge """
        return self._badge

    def get_element(self):
        """ Returns the element """
        return self._element

    def get_prize(self):
        """ Returns the prize """
        return self._prize

    @staticmethod
    def _str_validator(arg):
        """ Validator for string input """
        if arg is None or type(arg) != str:
            return ValueError('Incorrect value: input should be a string')
