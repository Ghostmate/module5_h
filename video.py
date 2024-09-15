class Video:
    """
    Класс описаний видео, содержащий атрибуты: название, длительность, текущее время просмотра, ограничение по возрасту
    """
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
