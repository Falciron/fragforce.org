""" Donations """
from .base import DonorDriveBase
from collections import namedtuple
from urllib.parse import urljoin
from .log import root_logger

mod_logger = root_logger.getChild('donors')
Donation = namedtuple('Donation',
                      [
                          'avatarImageURL',
                          'createdDateUTC',
                          'amount',
                          'displayName',
                          'donorID',  # aka donation id - string value!
                          'participantID',
                          'teamID',
                          'message',
                          'raw',
                      ],
                      rename=True,
                      )


class Donations(DonorDriveBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def sub_by_pid(self, participantID):
        return urljoin('participants', str(participantID), 'donations')

    def sub_by_tid(self, teamID):
        return urljoin('teams', str(teamID), 'donations')

    @classmethod
    def _d_to_d(cls, data):
        kws = {}
        for f in Donation._fields:
            if f == 'raw':
                kws[f] = data
            else:
                kws[f] = data.get(f, None)
        return Donation(**kws)

    def donations_for_participants(self, participantID):
        """ Get all donations for the given participant """
        fresp = self.fetch(sub_url=self.sub_by_pid(participantID))
        return self._d_to_d(fresp)

    def donations_for_team(self, teamID):
        """ Get all donations for the given team """
        fresp = self.fetch(sub_url=self.sub_by_tid(teamID))
        return self._d_to_d(fresp)
