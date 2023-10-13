class Brake:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time, name):
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.name = name
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)


class Engine:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time, name):
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.name = name
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)


class Suspension:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time, name):
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.name = name
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)


class Fwing:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time, name):
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.name = name
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)


class Bwing:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time, name):
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.name = name
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)


class Gbox:
    def __init__(self, speed, cornering, power_unit, reliability, pit_time, name):
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.pit_time = pit_time
        self.name = name
        self.teamscore = (self.speed + self.cornering + self.power_unit + self.reliability + (self.pit_time) / 0.02)


class Bottle:
    def __init__(self, Speed, Cornering, Power_Unit, Reliability, Pit_Stop, Overtaking, Defending, Race_start,
                 tyre_management, name):
        self.speed = Speed
        self.cornering = Cornering
        self.power_unit = Power_Unit
        self.reliability = Reliability
        self.pit_stop = Pit_Stop
        self.overtaking = Overtaking
        self.defending = Defending
        self.race_start = Race_start
        self.tyre_management = tyre_management
        self.name = name
        self.teamscore = Speed + Cornering + Power_Unit + Reliability + Pit_Stop + Overtaking + Defending + Race_start + tyre_management


class Setup:
    def __init__(self, Brake, Engine, Suspension, Fwing, Bwing, Gbox, n):
        self.Brake = Brake
        self.Engine = Engine
        self.Suspension = Suspension
        self.Fwing = Fwing
        self.Bwing = Bwing
        self.Gbox = Gbox
        self.n = n
        self.teamscore = Brake.teamscore + Engine.teamscore + Suspension.teamscore + Fwing.teamscore + Bwing.teamscore + Gbox.teamscore
