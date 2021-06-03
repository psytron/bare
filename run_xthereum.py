

import space
from agents import *
from matrix import MatrixModel

procs = [ PoolWatcher , TradeActor , PoolPrototypeV2 , Xthereum ] # Archivist --> Cass

actor1 = space.up( TradeActor , {} )

model = space.up( MatrixModel )
agents = space.up( procs )

