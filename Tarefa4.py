import Classes
import Parts


# O código abaixo é uma forma bem rudimentar de conseguir um setup otimizado, consistindo basicamente de encontrar
# partes de um setup com o maior teamscore e juntando tudo em um só setup A forma que decidi encontrar o melhor setup
# possível é ordenando as arrays que contém todas as peças, declarado no arquivo Parts, e colocando tudo em uma
# classe Setup_T4

# Para as partes do carro e o motorista, decidi ordenar por teamscore

Brake_Best = max(Parts.Brakes, key=lambda temp: temp.teamscore)
Gbox_Best = max(Parts.Gboxes, key=lambda temp: temp.teamscore)
Bwing_Best = max(Parts.Bwings, key=lambda temp: temp.teamscore)
Fwing_Best = max(Parts.Fwings, key=lambda temp: temp.teamscore)
Engine_Best = max(Parts.Engines, key=lambda temp: temp.teamscore)
Suspension_Best = max(Parts.Suspensions, key=lambda temp: temp.teamscore)
Driver_Best = max(Parts.Drivers, key=lambda temp: temp.teamscore)

# Para as garrafas, decidi  basear a melhor card no speed e cornering delas, visto que esses atributos parecem mais
# importantes que os outros, além de claro, o teamscore

Bottle_Best = max(Parts.Bottles, key=lambda temp: (temp.speed, temp.cornering, temp.teamscore))


Setup_Best = Classes.Setup_T4(Brake_Best, Engine_Best, Suspension_Best, Fwing_Best, Bwing_Best, Gbox_Best, Driver_Best, Bottle_Best, 'Melhor Setup')

print('Cards do Melhor setup: (Brake = {}, Gbox = {}, Bwing = {}, Fwing = {}, Engine = {}, Suspension = {}, '
      'Driver = {}, Bottle = {})'.format(Brake_Best.name, Gbox_Best.name, Bwing_Best.name, Fwing_Best.name,
                                         Engine_Best.name, Suspension_Best.name, Driver_Best.name,Bottle_Best.name))
