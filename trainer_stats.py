class TrainerStats:
    """ Trainer stats class """

    def __init__(self, num_trainers, num_gym_leader, num_regular_trainer, num_movement_type, num_have_partner, num_per_location):
        """ Constructor for trainer stats """
        self._num_trainers = num_trainers
        self._num_gym_leaders = num_gym_leader
        self._num_regular_trainer = num_regular_trainer
        self._num_movement_type = num_movement_type
        self._num_have_partner = num_have_partner
        self._num_per_location = num_per_location

    def get_num_trainers(self):
        """ """
        pass

    def get_num_gym_leader(self):
        """ """
        pass

    def get_num_regular_trainer(self):
        """ """
        pass

    def get_num_movement_type(self):
        """ """
        pass

    def get_num_trainer_have_partner(self):
        """ """
        pass

    def get_num_per_location(self):
        """ """
        pass

    @staticmethod
    def _str_validator(arg):
        """ validator for string input """
        if arg is None or type(arg) != str:
            return ValueError('Incorrect value: input should be a string')

    @staticmethod
    def _int_validator(arg):
        """ validator for integer input """
        if arg is None or type(arg) != int:
            return ValueError('Incorrect value: input should an int')

    @staticmethod
    def _float_validator(arg):
        """ validator for float input """
        if arg is None or type(arg) != float:
            return ValueError('Incorrect value: input should be a float')

    @staticmethod
    def _boolean_validator(arg):
        """ validator for boolean input """
        if arg is None or type(arg) != bool:
            return ValueError('Incorrect value: input should be boolean')