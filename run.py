


#   contracts are getting deployed and confired live on target networks 

# space.live()  # returns list of running objects and 



from node_modules import  space
from agents import *
from matrix import MatrixModel

procs = [ PoolWatcher , TradeActor , PoolPrototypeV2 ] # Archivist --> Cass
actor1 = space.up( TradeActor , {} )
model = space.up( MatrixModel )
agents = space.up( procs )
