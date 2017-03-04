class StreetCorrector:
    CORRECTIONS = {
        'вул.в/ч': 'в/ч',
        'в.ч.': 'в/ч',
        'Військова частина': 'в/ч',
        'військова частина': 'в/ч',
        'Житловий масив': 'ж/м',
        'Військове містечко': 'в/ч',
        'військове містечко': 'в/ч',
    }

    TYPES_CORRECTIONS = {
        'кв': 'кв-л',
        'квартал': 'кв-л',
        'квар': 'кв-л',
        'ж/кв': 'кв-л',
        '3-провулок': 'пров',
        'провулок': 'пров',
        'мікрорайон': 'мкр-н',
        'мкрн': 'мкр-н',
        'мкр': 'мкр-н',
        'м-р': 'мкр-н',
        'м-н': 'мкр-н',
        'проспект': 'просп',
        'пр-т': 'просп',
        'пр': 'просп',
        'узвіз': 'узв',
        'тупик': 'туп',
        'тупік': 'тупик',
        'житмасив': 'ж/м',
        'жилмасив': 'ж/м',
        'жилмістечко': 'ж/м',
        'масив': 'ж/м',
        'м-в': 'ж/м',
        'кілометр': 'км',
        'в\ч': 'в/ч',
        'в/городок': 'в/ч',
        'вч': 'в/ч',
        'бульвар': 'бульв',
        'буд': 'будка',
        'проєзд': 'проїзд',
        'ур': 'урочище',
        'в’їзд': "в'їзд",

        'о': 'острів',
        # city
        'хут': 'х',
        'хутір': 'x',
        'сел': 'с',
        'селище': 'с-ще',
    }

    @classmethod
    def correct_full_str(cls, node_text):
        for corr in cls.CORRECTIONS:
            node_text = node_text.replace(corr, cls.CORRECTIONS[corr])
        return node_text

    @classmethod
    def correct_type(cls, _type):
        if _type in cls.TYPES_CORRECTIONS:
            _type = cls.TYPES_CORRECTIONS[_type]
        return _type
