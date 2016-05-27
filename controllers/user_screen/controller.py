#!/usr/bin/env python3
# -*- coding: utf8 -*-

from smutils import smpacket

from stepmania_controller import StepmaniaController

import models

class UserStatusController(StepmaniaController):
    command = smpacket.SMClientCommand.NSSCSMS

    def handle(self):
        if not self.active_users:
            return

        status_mapping = {
            1: models.UserStatus.music_selection,
            3: models.UserStatus.option,
            5: models.UserStatus.evaluation,
            7: models.UserStatus.room_selection
        }

        if self.packet["action"] == 7:
            self.send(models.Room.smo_list(self.session))

        for user in self.active_users:
            user.status = status_mapping.get(self.packet["action"], models.UserStatus.unknown).value

 
