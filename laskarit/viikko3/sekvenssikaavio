main->*machine: Machine(self)
main->+machine: self.__init__
machine->*fuel tank: FuelTank(self)
machine->+fuel tank: self._tank.fill(40)
fuel tank->-machine: self.fuel_contents = 40
machine->*engine: Engine(self._tank)
machine-->-main: 
main->+machine: self.drive
machine->+engine: self._engine.start()
engine->+fuel tank: self._fuel_tank.consume(5)
fuel tank->-engine: self.fuel_contents = 35
engine-->-machine:
machine->+engine: self._engine.is_running
engine->-machine: True
machine->+engine: self._engine.use_energy
engine->+fuel tank: self._fuel_tank.consume(10)
fuel tank->-engine: self.fuel_contents = 25
engine-->-machine:
machine-->-main:
