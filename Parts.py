import Classes

#Aqui esta a lista dos freios

Wildcore = Classes.Brake(36, 23, 33, 22, 0.59)
Suspense = Classes.Brake(20,32,23,21,0.37)
The_Warden = Classes.Brake(26,28,27,25,0.43)
Axiom = Classes.Brake(14,34,18,15,0.67)
Crisis_SL = Classes.Brake(27,16,18,19,0.51)
Essence = Classes.Brake(14,13,12,25,0.76)
Onyx = Classes.Brake(26,23,25,50,0.49)
Starter_Brake = Classes.Brake(1,1,1,1,1)

# array com o teamscore de cada freio

Brakes_teamscore = [Wildcore.teamscore, Suspense.teamscore, The_Warden.teamscore, Axiom.teamscore,Crisis_SL.teamscore, Essence.teamscore, Onyx.teamscore,Starter_Brake.teamscore]

#Array com  cada Brake

Brakes = [Wildcore, Suspense, The_Warden, Axiom, Crisis_SL, Essence, Onyx, Starter_Brake]

#Aqui esta a lista das caixas de marcha

Voyage = Classes.Gbox(23,28,22,27,0)
Vector = Classes.Gbox(24,38,22,36,0.55)
Kick_Shift = Classes.Gbox(18,19,29,19,0.45)
Verdict = Classes.Gbox(33,18,20,30,0.63)
Spectrum = Classes.Gbox(20,25,21,23,0.53)
Swiftcharge = Classes.Gbox(14,23,22,16,0.71)
Switch_r_00 = Classes.Gbox(12,13,11,14,0.47)
Starter_Gbox = Classes.Gbox(1,1,1,1,1)

#array com o teamscore de cada Gbox

Gbox_teamscore = [Voyage.teamscore, Vector.teamscore, Kick_Shift.teamscore, Verdict.teamscore, Spectrum.teamscore, Swiftcharge.teamscore, Switch_r_00.teamscore, Starter_Gbox.teamscore]

#Array com cada Gbox

Gboxes = [Voyage, Vector, Kick_Shift, Verdict, Spectrum, Swiftcharge, Switch_r_00, Starter_Gbox]

#Aqui esta a lista dos Bwings

Typhoon = Classes.Bwing(50,27,26,23,0.53)
Transcendence = Classes.Bwing(24,22,36,37,0.53)
Freeflare = Classes.Bwing(21,33,20,22,0.37)
The_Patron = Classes.Bwing(23,21,19,37,0.61)
The_Wasp = Classes.Bwing(16,24,23,14,0.69)
The_Matador = Classes.Bwing(19,16,18,17,0.72)
Phantom_X = Classes.Bwing(26,15,12,11,0.76)
Starter_Bwing = Classes.Bwing(1,1,1,1,1)

#array com o teamscore de cada Bwing

Bwing_teamscore = [Typhoon.teamscore, Transcendence.teamscore, Freeflare.teamscore, The_Patron.teamscore, The_Wasp.teamscore, The_Matador.teamscore, Phantom_X.teamscore, Starter_Bwing.teamscore]

#Array com cada Bwing

Bwings = [Typhoon, Transcendence, Freeflare, The_Patron, The_Wasp, The_Matador, Phantom_X, Starter_Bwing]

#Aqui esta a lista dos Fwings

Virtue = Classes.Fwing(23,50,27,24,0.49)
Thunderclap = Classes.Fwing(35,23,21,33,0.55)
Trailblazer = Classes.Fwing(21,23,42,20,0.57)
Zeno = Classes.Fwing(25,23,22,26,0.53)
The_Vagabond = Classes.Fwing(31,20,23,21,0.35)
Feral_Punch = Classes.Fwing(13,15,22,21,0.73)
The_Scout = Classes.Fwing(13,27,15,14,0.73)
Starter_Fwing = Classes.Fwing(1,1,1,1,1)

#array com o teamscore de cada Fwing

Fwing_teamscore = [Virtue.teamscore,Thunderclap.teamscore,Trailblazer.teamscore,Zeno.teamscore,The_Vagabond.teamscore,Feral_Punch.teamscore,The_Scout.teamscore,Starter_Fwing.teamscore]

#Array co9m cada Fwing

Fwings = [Virtue, Thunderclap, Trailblazer, Zeno, The_Vagabond, Feral_Punch, The_Scout, Starter_Fwing]

#Aqui esta a lista das suspensoes

Sigma = Classes.Suspension(32,28,30,29,0.39)
Presence = Classes.Suspension(23,26,24,22,0.2)
Horizon = Classes.Suspension(22,36,24,37,0.53)
Radiance = Classes.Suspension(25,17,26,19,0.65)
Icon_V3 = Classes.Suspension(17,13,16,23,0.54)
Rodeo = Classes.Suspension(23,22,15,14,0.69)
The_Equator = Classes.Suspension(20,19,18,21,0.61)
Starter_Suspension = Classes.Suspension(1,1,1,1,1)

#Array com teamscore de cada suspensao

Suspension_teamscore = [Sigma.teamscore,Presence.teamscore,Horizon.teamscore,Radiance.teamscore,Icon_V3.teamscore,Rodeo.teamscore,The_Equator.teamscore,Starter_Suspension.teamscore]

#Array com cada suspensao

Suspensions = [Sigma, Presence, Horizon, Radiance, Icon_V3, Rodeo, The_Equator, Starter_Suspension]

#Aqui esta a lista dos Motores

Cloudroar = Classes.Engine(26,24,50,27,0.55)
Avalanche = Classes.Engine(34,22,25,21,0.35)
The_Rover = Classes.Engine(27,25,28,24,0.53)
Twinburst = Classes.Engine(16,29,18,18,0.51)
Enigma = Classes.Engine(16,13,23,25,0.69)
Nova = Classes.Engine(31,13,15,16,0.71)
Brute_Force = Classes.Engine(21,19,36,18,0.63)
Starter_Engine = Classes.Engine(1,1,1,1,1)

#Array com teamscore de cada Engine

Engine_teamscore = [Cloudroar.teamscore,Avalanche.teamscore,The_Rover.teamscore,Twinburst.teamscore,Enigma.teamscore,Nova.teamscore,Brute_Force.teamscore,Starter_Engine.teamscore]

#Array com cada Engine

Engines = [Cloudroar, Avalanche, The_Rover, Twinburst, Enigma, Nova, Brute_Force, Starter_Engine]

#Aqui está a lista de garrafinhas

Tsar =          Classes.Bottle(0,15,0,0,0,0,10,0,25)
Frost =         Classes.Bottle(0,0,0,10,0,0,0,15,25)
Tulip =         Classes.Bottle(0,0,0,20,20,0,10,0,0)
Dragon =        Classes.Bottle(0,0,0,15,0,20,0,0,15)
Kawaii =        Classes.Bottle(0,0,0,0,15,0,0,15,20)
Pretzel =       Classes.Bottle(0,0,0,15,10,0,0,0,25)
Vice =          Classes.Bottle(10,0,15,25,0,0,0,0,0)
Schooner =      Classes.Bottle(0,0,0,25,15,0,10,0,0)
Djinn =         Classes.Bottle(0,0,15,20,0,0,15,0,0)
Oud =           Classes.Bottle(0,10,0,0,25,15,0,0,0)
Eternal_Flame = Classes.Bottle(0,0,0,15,0,25,0,0,10)
Eagle =         Classes.Bottle(0,0,0,15,0,0,0,15,20)
Iron_Force =    Classes.Bottle(0,0,20,20,0,0,0,0,10)
Lumberjack =    Classes.Bottle(0,0,0,25,0,0,15,0,10)
Cranberry =     Classes.Bottle(0,0,0,10,0,20,20,0,0)
Butterfly =     Classes.Bottle(0,0,25,0,5,0,0,0,20)
Tune_in =       Classes.Bottle(10,15,0,0,25,0,0,0,0)
Self_Control =  Classes.Bottle(0,0,5,5,0,0,0,0,5)
Warrior =       Classes.Bottle(10,0,0,0,0,5,5,0,0)
Ballast =       Classes.Bottle(0,10,0,0,10,0,0,5,0)
Instinct =      Classes.Bottle(0,0,15,5,0,0,0,10,0)
Downforce =     Classes.Bottle(0,5,0,0,0,0,15,0,15)
Hex =           Classes.Bottle(15,0,0,0,5,20,0,0,0)
Eggception =    Classes.Bottle(0,0,10,0,25,0,15,0,0)
Rooster =       Classes.Bottle(0,0,10,0,0,20,0,20,0)
Cuppa =         Classes.Bottle(0,20,0,0,0,10,0,20,0)
Street_Shark =  Classes.Bottle(15,0,0,0,0,10,0,25,0)
Herald =        Classes.Bottle(0,15,0,0,0,10,0,25,0)
Prince =        Classes.Bottle(0,20,0,0,0,0,10,20,0)
Unstoppable =   Classes.Bottle(15,0,10,0,25,0,0,0,0)
Dead_Fast =     Classes.Bottle(25,0,20,0,0,0,0,0,5)
Gladiator =     Classes.Bottle(0,0,10,0,0,0,25,15,0)
Taurus =        Classes.Bottle(20,0,25,0,0,5,0,0,0)
Merlion =       Classes.Bottle(15,25,0,0,10,0,0,0,0)
Samba =         Classes.Bottle(5,0,25,0,20,0,0,0,0)
Caveira =       Classes.Bottle(25,0,10,0,0,15,0,0,0)
Fogos =         Classes.Bottle(20,0,0,0,0,15,0,15,0)
Movember =      Classes.Bottle(0,25,0,0,0,0,15,0,10)
Palmeira =      Classes.Bottle(0,0,0,0,0,0,20,10,20)
Nazal =         Classes.Bottle(0,0,0,15,0,0,0,20,15)
Aderencia =     Classes.Bottle(0,25,0,15,0,0,0,10,0)
Arco_Iris =     Classes.Bottle(20,0,0,0,0,0,25,5,0)
Eclipse =       Classes.Bottle(25,0,0,0,10,15,0,0,0)
Rena =          Classes.Bottle(0,10,0,0,20,0,20,0,0)

Bottles = [Tsar, Frost, Tulip, Dragon, Kawaii, Pretzel, Vice, Schooner, Djinn, Oud, Eternal_Flame, Eagle, Iron_Force, Lumberjack, Cranberry, Butterfly, Tune_in, Self_Control, Warrior, Ballast, Instinct, Downforce, Hex, Eggception, Rooster
           , Cuppa, Street_Shark, Herald, Prince, Unstoppable, Dead_Fast, Gladiator, Taurus, Merlion, Samba, Caveira, Fogos, Movember, Palmeira, Nazal, Aderencia, Arco_Iris, Eclipse, Rena]