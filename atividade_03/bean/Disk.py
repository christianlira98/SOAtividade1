from bean.Track import Track


class Disk:

    def __init__(self, identifier, number_of_tracks=1024):
        self.identifier = identifier
        self.tracks = []
        self.number_of_tracks = number_of_tracks
        for track_identifier in range(number_of_tracks):
            self.tracks.append( Track(track_identifier) )
