class Brake:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time):
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)
class Engine:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time):
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)

class Suspension:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time):
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)
class Fwing:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time):
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)
class Bwing:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time):
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)
class Gbox:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time):
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)

class Setup:
    def __init__(self,Brake,Engine,Suspension,Fwing,Bwing,Gbox):
        self.Brake = Brake.teamscore
        self.Engine = Engine.teamscore
        self.Suspension = Suspension.teamscore
        self.Fwing = Fwing.teamscore
        self.Bwing = Bwing.teamscore
        self.Gbox = Gbox.teamscore
        self.teamscore = Brake.teamscore + Engine.teamscore + Suspension.teamscore + Fwing.teamscore + Bwing.teamscore + Gbox.teamscore

