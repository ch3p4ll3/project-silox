from models.silos import Silos, Size
from simulator import Simulator
from models.sensors import TempSensor, LevelSensor


sensors = [
    TempSensor('Internal Temperature', 30, 20, "int_temp"),
    TempSensor('External Temperature', 30, 20, "ext_temp"),
]

level_sensors = [
    LevelSensor('Level Sensor 1', 10, 0, 'level_1'),
    LevelSensor('Level Sensor 2', 10, 0, 'level_2')
]

silos1 = Silos("silos1", Size(10, 3), sensors, level_sensors)
silos2 = Silos("silos2", Size(10, 4), sensors, level_sensors)


simulators = [
    Simulator(silos1),
    Simulator(silos2)
]

if __name__ == '__main__':
    for simulator in simulators:
        simulator.start()

    for simulator in simulators:
        simulator.join()
