import Classes

# Aqui esta a lista dos freios

Wildcore = Classes.Brake(36, 23, 33, 22, 0.59, 'Wildcore')
Suspense = Classes.Brake(20, 32, 23, 21, 0.37, 'Suspense')
The_Warden = Classes.Brake(26, 28, 27, 25, 0.43, 'The Warden')
Axiom = Classes.Brake(14, 34, 18, 15, 0.67, 'Axiom')
Crisis_SL = Classes.Brake(27, 16, 18, 19, 0.51, 'Crisis SL')
Essence = Classes.Brake(14, 13, 12, 25, 0.76, 'Essence')
Onyx = Classes.Brake(26, 23, 25, 50, 0.49, 'Onyx')
Starter_Brake = Classes.Brake(1, 1, 1, 1, 1, 'Starter')

# array com o teamscore de cada freio

Brakes_teamscore = [Wildcore.teamscore, Suspense.teamscore, The_Warden.teamscore, Axiom.teamscore, Crisis_SL.teamscore,
                    Essence.teamscore, Onyx.teamscore, Starter_Brake.teamscore]

# Array com  cada Brake

Brakes = [Wildcore, Suspense, The_Warden, Axiom, Crisis_SL, Essence, Onyx, Starter_Brake]

# Aqui esta a lista das caixas de marcha

Voyage = Classes.Gbox(23, 28, 22, 27, 0, 'Voyage')
Vector = Classes.Gbox(24, 38, 22, 36, 0.55, 'Vector')
Kick_Shift = Classes.Gbox(18, 19, 29, 19, 0.45, 'Kick Shift')
Verdict = Classes.Gbox(33, 18, 20, 30, 0.63, 'Verdict')
Spectrum = Classes.Gbox(20, 25, 21, 23, 0.53, 'Spectrum')
Swiftcharge = Classes.Gbox(14, 23, 22, 16, 0.71, 'Swiftcharge')
Switch_r_00 = Classes.Gbox(12, 13, 11, 14, 0.47, 'Switch r 00')
Starter_Gbox = Classes.Gbox(1, 1, 1, 1, 1, 'Starter')

# array com o teamscore de cada Gbox

Gbox_teamscore = [Voyage.teamscore, Vector.teamscore, Kick_Shift.teamscore, Verdict.teamscore, Spectrum.teamscore,
                  Swiftcharge.teamscore, Switch_r_00.teamscore, Starter_Gbox.teamscore]

# Array com cada Gbox

Gboxes = [Voyage, Vector, Kick_Shift, Verdict, Spectrum, Swiftcharge, Switch_r_00, Starter_Gbox]

# Aqui esta a lista dos Bwings

Typhoon = Classes.Bwing(50, 27, 26, 23, 0.53, 'Typhoon')
Transcendence = Classes.Bwing(24, 22, 36, 37, 0.53, 'Transcendence')
Freeflare = Classes.Bwing(21, 33, 20, 22, 0.37, 'Freeflare')
The_Patron = Classes.Bwing(23, 21, 19, 37, 0.61, 'The Patron')
The_Wasp = Classes.Bwing(16, 24, 23, 14, 0.69, 'The Wasp')
The_Matador = Classes.Bwing(19, 16, 18, 17, 0.72, 'The Matador')
Phantom_X = Classes.Bwing(26, 15, 12, 11, 0.76, 'Phantom X')
Starter_Bwing = Classes.Bwing(1, 1, 1, 1, 1, 'Starter')

# array com o teamscore de cada Bwing

Bwing_teamscore = [Typhoon.teamscore, Transcendence.teamscore, Freeflare.teamscore, The_Patron.teamscore,
                   The_Wasp.teamscore, The_Matador.teamscore, Phantom_X.teamscore, Starter_Bwing.teamscore]

# Array com cada Bwing

Bwings = [Typhoon, Transcendence, Freeflare, The_Patron, The_Wasp, The_Matador, Phantom_X, Starter_Bwing]

# Aqui esta a lista dos Fwings

Virtue = Classes.Fwing(23, 50, 27, 24, 0.49, 'Virtue')
Thunderclap = Classes.Fwing(35, 23, 21, 33, 0.55, 'Thunderclap')
Trailblazer = Classes.Fwing(21, 23, 42, 20, 0.57, 'Trailblazer')
Zeno = Classes.Fwing(25, 23, 22, 26, 0.53, 'Zeno')
The_Vagabond = Classes.Fwing(31, 20, 23, 21, 0.35, 'The Vagabond')
Feral_Punch = Classes.Fwing(13, 15, 22, 21, 0.73, 'Feral Punch')
The_Scout = Classes.Fwing(13, 27, 15, 14, 0.73, 'The Scout')
Starter_Fwing = Classes.Fwing(1, 1, 1, 1, 1, 'Starter')

# array com o teamscore de cada Fwing

Fwing_teamscore = [Virtue.teamscore, Thunderclap.teamscore, Trailblazer.teamscore, Zeno.teamscore,
                   The_Vagabond.teamscore, Feral_Punch.teamscore, The_Scout.teamscore, Starter_Fwing.teamscore]

# Array co9m cada Fwing

Fwings = [Virtue, Thunderclap, Trailblazer, Zeno, The_Vagabond, Feral_Punch, The_Scout, Starter_Fwing]

# Aqui esta a lista das suspensoes

Sigma = Classes.Suspension(32, 28, 30, 29, 0.39, 'Sigma')
Presence = Classes.Suspension(23, 26, 24, 22, 0.2, 'Presence')
Horizon = Classes.Suspension(22, 36, 24, 37, 0.53, 'Horizon')
Radiance = Classes.Suspension(25, 17, 26, 19, 0.65, 'Radiance')
Icon_V3 = Classes.Suspension(17, 13, 16, 23, 0.54, 'Icon V3')
Rodeo = Classes.Suspension(23, 22, 15, 14, 0.69, 'Rodeo')
The_Equator = Classes.Suspension(20, 19, 18, 21, 0.61, 'The Equator')
Starter_Suspension = Classes.Suspension(1, 1, 1, 1, 1, 'Starter')

# Array com teamscore de cada suspensao

Suspension_teamscore = [Sigma.teamscore, Presence.teamscore, Horizon.teamscore, Radiance.teamscore, Icon_V3.teamscore,
                        Rodeo.teamscore, The_Equator.teamscore, Starter_Suspension.teamscore]

# Array com cada suspensao

Suspensions = [Sigma, Presence, Horizon, Radiance, Icon_V3, Rodeo, The_Equator, Starter_Suspension]

# Aqui esta a lista dos Motores

Cloudroar = Classes.Engine(26, 24, 50, 27, 0.55, 'Cloudroar')
Avalanche = Classes.Engine(34, 22, 25, 21, 0.35, 'Avalanche')
The_Rover = Classes.Engine(27, 25, 28, 24, 0.53, 'The Rover')
Twinburst = Classes.Engine(16, 29, 18, 18, 0.51, 'Twinburst')
Enigma = Classes.Engine(16, 13, 23, 25, 0.69, 'Enigma')
Nova = Classes.Engine(31, 13, 15, 16, 0.71, 'Nova')
Brute_Force = Classes.Engine(21, 19, 36, 18, 0.63, 'Brute Force')
Starter_Engine = Classes.Engine(1, 1, 1, 1, 1, 'Starter')

# Array com teamscore de cada Engine

Engine_teamscore = [Cloudroar.teamscore, Avalanche.teamscore, The_Rover.teamscore, Twinburst.teamscore,
                    Enigma.teamscore, Nova.teamscore, Brute_Force.teamscore, Starter_Engine.teamscore]

# Array com cada Engine

Engines = [Cloudroar, Avalanche, The_Rover, Twinburst, Enigma, Nova, Brute_Force, Starter_Engine]

# Aqui está a lista de garrafinhas

Tsar = Classes.Bottle(0, 15, 0, 0, 0, 0, 10, 0, 25, 'Tsar')
Frost = Classes.Bottle(0, 0, 0, 10, 0, 0, 0, 15, 25, 'Frost')
Tulip = Classes.Bottle(0, 0, 0, 20, 20, 0, 10, 0, 0, 'Tulip')
Dragon = Classes.Bottle(0, 0, 0, 15, 0, 20, 0, 0, 15, 'Dragon')
Kawaii = Classes.Bottle(0, 0, 0, 0, 15, 0, 0, 15, 20, 'Kawaii')
Pretzel = Classes.Bottle(0, 0, 0, 15, 10, 0, 0, 0, 25, 'Pretzel')
Vice = Classes.Bottle(10, 0, 15, 25, 0, 0, 0, 0, 0, 'Vice')
Schooner = Classes.Bottle(0, 0, 0, 25, 15, 0, 10, 0, 0, 'Schooner')
Djinn = Classes.Bottle(0, 0, 15, 20, 0, 0, 15, 0, 0, 'Djinn')
Oud = Classes.Bottle(0, 10, 0, 0, 25, 15, 0, 0, 0, 'Oud')
Eternal_Flame = Classes.Bottle(0, 0, 0, 15, 0, 25, 0, 0, 10, 'Eternal Flame')
Eagle = Classes.Bottle(0, 0, 0, 15, 0, 0, 0, 15, 20, 'Eagle')
Iron_Force = Classes.Bottle(0, 0, 20, 20, 0, 0, 0, 0, 10, 'Iron Force')
Lumberjack = Classes.Bottle(0, 0, 0, 25, 0, 0, 15, 0, 10, 'Lumberjack')
Cranberry = Classes.Bottle(0, 0, 0, 10, 0, 20, 20, 0, 0, 'Cranberry')
Butterfly = Classes.Bottle(0, 0, 25, 0, 5, 0, 0, 0, 20, 'Butterfly')
Tune_in = Classes.Bottle(10, 15, 0, 0, 25, 0, 0, 0, 0, 'Tune in')
Self_Control = Classes.Bottle(0, 0, 5, 5, 0, 0, 0, 0, 5, 'Self Control')
Warrior = Classes.Bottle(10, 0, 0, 0, 0, 5, 5, 0, 0, 'Warrior')
Ballast = Classes.Bottle(0, 10, 0, 0, 10, 0, 0, 5, 0, 'Ballast')
Instinct = Classes.Bottle(0, 0, 15, 5, 0, 0, 0, 10, 0, 'Instinct')
Downforce = Classes.Bottle(0, 5, 0, 0, 0, 0, 15, 0, 15, 'Downforce')
Hex = Classes.Bottle(15, 0, 0, 0, 5, 20, 0, 0, 0, 'Hex')
Eggception = Classes.Bottle(0, 0, 10, 0, 25, 0, 15, 0, 0, 'Eggception')
Rooster = Classes.Bottle(0, 0, 10, 0, 0, 20, 0, 20, 0, 'Rooster')
Cuppa = Classes.Bottle(0, 20, 0, 0, 0, 10, 0, 20, 0, 'Cuppa')
Street_Shark = Classes.Bottle(15, 0, 0, 0, 0, 10, 0, 25, 0, 'Street Shark')
Herald = Classes.Bottle(0, 15, 0, 0, 0, 10, 0, 25, 0, 'Herald')
Prince = Classes.Bottle(0, 20, 0, 0, 0, 0, 10, 20, 0, 'Prince')
Unstoppable = Classes.Bottle(15, 0, 10, 0, 25, 0, 0, 0, 0, 'Unstoppable')
Dead_Fast = Classes.Bottle(25, 0, 20, 0, 0, 0, 0, 0, 5, 'Dead Fast')
Gladiator = Classes.Bottle(0, 0, 10, 0, 0, 0, 25, 15, 0, 'Gladiator')
Taurus = Classes.Bottle(20, 0, 25, 0, 0, 5, 0, 0, 0, 'Taurus')
Merlion = Classes.Bottle(15, 25, 0, 0, 10, 0, 0, 0, 0, 'Merlion')
Samba = Classes.Bottle(5, 0, 25, 0, 20, 0, 0, 0, 0, 'Samba')
Caveira = Classes.Bottle(25, 0, 10, 0, 0, 15, 0, 0, 0, 'Caveira')
Fogos = Classes.Bottle(20, 0, 0, 0, 0, 15, 0, 15, 0, 'Fogos')
Movember = Classes.Bottle(0, 25, 0, 0, 0, 0, 15, 0, 10, 'Movember')
Palmeira = Classes.Bottle(0, 0, 0, 0, 0, 0, 20, 10, 20, 'Palmeira')
Nazal = Classes.Bottle(0, 0, 0, 15, 0, 0, 0, 20, 15, 'Nazal')
Aderencia = Classes.Bottle(0, 25, 0, 15, 0, 0, 0, 10, 0, 'Aderencia')
Arco_Iris = Classes.Bottle(20, 0, 0, 0, 0, 0, 25, 5, 0, 'Arco Iris')
Eclipse = Classes.Bottle(25, 0, 0, 0, 10, 15, 0, 0, 0, 'Eclipse')
Rena = Classes.Bottle(0, 10, 0, 0, 20, 0, 20, 0, 0, 'Rena')

Bottles = [Tsar, Frost, Tulip, Dragon, Kawaii, Pretzel, Vice, Schooner, Djinn, Oud, Eternal_Flame, Eagle, Iron_Force,
           Lumberjack, Cranberry, Butterfly, Tune_in, Self_Control, Warrior, Ballast, Instinct, Downforce, Hex,
           Eggception, Rooster, Cuppa, Street_Shark, Herald, Prince, Unstoppable, Dead_Fast, Gladiator, Taurus, Merlion, Samba, Caveira, Fogos,
           Movember, Palmeira, Nazal, Aderencia, Arco_Iris, Eclipse, Rena]


# Aqui segue a lista dos motoristas

Verstappen = Classes.Driver(97, 86, 99, 89, 94, 'Verstappen')
Leclerc = Classes.Driver(93, 99, 97, 87, 89, 'Leclerc')
Alonso = Classes.Driver(99, 92, 89, 97, 88, 'Alonso')
Hamilton = Classes.Driver(81, 86, 89, 94, 90, 'Hamilton')
Norris = Classes.Driver(99, 95, 99, 99, 99, 'Norris')
Russell = Classes.Driver(95, 90, 91, 83, 86, 'Russell')
Perez = Classes.Driver(85, 96, 89, 91, 84, 'Perez')
Sainz = Classes.Driver(84, 85, 95, 90, 91, 'Sainz')
Stroll = Classes.Driver(92, 83, 87, 94, 89, 'Stroll')
Gasly = Classes.Driver(88, 93, 83, 85, 96, 'Gasly')

Drivers = [Verstappen, Leclerc, Alonso, Hamilton, Norris, Russell, Perez, Sainz, Stroll, Gasly]