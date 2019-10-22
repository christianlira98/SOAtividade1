from bean.Sector import Sector


class Track:

    def __init__(self, identifier, number_of_sectors=63):
        self.identifier = identifier
        self.sectors = []
        self.number_of_sectors = number_of_sectors
        for sector_index in range(number_of_sectors):
            self.sectors.append( Sector(sector_index) )
