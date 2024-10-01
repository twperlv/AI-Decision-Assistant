from logic import *

# Events
rain = Symbol("rain")
heavy_traffic = Symbol("heavy traffic")
early_meeting = Symbol("early meeting")
strike = Symbol("strike")
appointment = Symbol("appointment")
road_construction = Symbol("road construction")
overslept = Symbol("overslept")

# Possible actions
wfh = Symbol("wfh")
drive = Symbol("drive")
public_transport = Symbol("public transport")


knowledge_base = And(
    # If it's raining or there’s an early meeting, you should work from home
    Implication((Or(rain, early_meeting)), wfh),

    # If it’s not raining and there’s no heavy traffic, you should drive
    Implication(And(Not(heavy_traffic), Not(rain)), drive),

    # If there’s no strike and it’s not raining, you should take public transport
    Implication(And(Not(strike), Not(rain)), public_transport),

    # If there is an appointment, you should drive
    Implication(appointment, drive),
    
    # If you overslept and there is any problem on the way to work, you should work at home
    Implication(And(overslept, Or(heavy_traffic, road_construction, rain), strike), wfh)
)

print(f"\nKnowledge base: {knowledge_base.formula()}")


def query(scenario, action):
    '''
    Defines a query given a specific scenario and the action to be considered. 
    '''
    return Implication(scenario, action)

def suggestions(scenario):
    '''
    Prints out the output for each possible action in the given scenario.
    '''
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
