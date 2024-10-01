from logic import *

rain = Symbol("rain")
heavy_traffic = Symbol("heavy traffic")
early_meeting = Symbol("early meeting")
strike = Symbol("strike")
appointment = Symbol("appointment")
road_construction = Symbol("road construction")
overslept = Symbol("overslept")

wfh = Symbol("wfh")
drive = Symbol("drive")
public_transport = Symbol("public transport")


knowledge_base = And(
    Implication((Or(rain, early_meeting)), wfh),
    Implication(And(Not(heavy_traffic), Not(rain)), drive),
    Implication(And(Not(strike), Not(rain)), public_transport),

    Implication(appointment, drive),
    Implication(And(overslept, Or(heavy_traffic, road_construction, rain), strike), wfh)
)

print(f"\nKnowledge base: {knowledge_base.formula()}")


def query(scenario, action):
    return Implication(scenario, action)

def suggestions(scenario):
    print(f"\nScenario: {scenario.formula()}")
    print(f"Work from home: {model_check(knowledge_base, query(scenario, wfh))}")
    print(f"Take public transport: {model_check(knowledge_base, query(scenario, public_transport))}")
    print(f"Drive: {model_check(knowledge_base, query(scenario, drive))}")


scenario_1 = And(rain, heavy_traffic)
scenario_2 = And(Not(rain), strike, Not(heavy_traffic))
scenario_3 = And(Not(rain), Not(heavy_traffic), Not(strike))

suggestions(scenario_1)
suggestions(scenario_2)
suggestions(scenario_3)


scenario_4 = And(appointment, rain, road_construction)
scenario_5 = And(road_construction, strike, overslept)

suggestions(scenario_4)
suggestions(scenario_5)
