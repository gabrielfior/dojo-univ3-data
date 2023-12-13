
from dojo.environments import UniV3Env
from dateutil import parser as dateparser
from dojo.dataloaders import univ3_loader, UniV3Loader
from dojo.agents import BaseAgent, DummyAgent
from decimal import Decimal

print("start")
pools = ["USDC/WETH-0.3"]
sim_start = dateparser.parse("2023-04-29 00:00:00 UTC")
sim_end = dateparser.parse("2023-04-30 00:00:00 UTC")

#agent = BaseAgent(initial_portfolio={"USDC": Decimal(10_000)})
agent = DummyAgent()
env = UniV3Env(
    agents=[agent],  # Of course, you'd want an agent here to actually do things
    date_range=(sim_start, sim_end),
    pools=pools,
    market_impact="replay",  # defaults to "replay", simply replaying history
)

loader = UniV3Loader(env, (sim_start, sim_end), ['a.txt'])
result = loader.load()
print ('loader', result)

print("finish")