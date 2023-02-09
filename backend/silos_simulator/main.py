from models.silos import Silos, Size
from simulator import Simulator


simulators = [
    Simulator(Silos("silos1", Size(10, 3))),
    Simulator(Silos("silos2", Size(10, 4)))
]

if __name__ == '__main__':
    for simulator in simulators:
        simulator.start()

    while simulators[0].is_alive() or simulators[1].is_alive():
        pass
