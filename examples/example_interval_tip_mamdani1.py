from simpful import *

from ifis.interval_fuzzy_sets import *
from ifis.interval_fuzzy_system import *
from ifis.interval_linguistic_variable import *
# A simple fuzzy inference system for the tipping problem
# Create a fuzzy system object

iFS = IntervalFuzzySystem()

# Define fuzzy sets and linguistic variables
S_1 = IntervalFuzzySet(function_start=Triangular_MF(a=0, b=0, c=5), function_end=Trapezoidal_MF(a=1, b=1, c=1, d=6), term='poor')
S_2 = IntervalFuzzySet(function_start=Triangular_MF(a=0, b=5, c=10), function_end=Trapezoidal_MF(a=0, b=4, c=6, d=10), term='good')
S_3 = IntervalFuzzySet(function_start=Trapezoidal_MF(a=4, b=9, c=10, d=10), function_end=Triangular_MF(a=5, b=10, c=10), term='excellent')
# iFS.add_linguistic_variable("Service", LinguisticVariable([S_1, S_2, S_3], concept="Service quality", universe_of_discourse=[0,10]))
iLV_1 = IntervalLinguisticVariable([S_1, S_2, S_3], concept="Service quality", universe_of_discourse=[0, 10])
iLV_1.plot()
iFS.add_linguistic_variable("Service", iLV_1)

F_1 = IntervalFuzzySet(function_start=Triangular_MF(a=0, b=0, c=8), function_end=Trapezoidal_MF(a=1, b=1, c=2, d=10), term='rancid')
F_2 = IntervalFuzzySet(function_start=Trapezoidal_MF(a=0, b=8, c=10, d=10), function_end=Triangular_MF(a=2, b=10, c=10), term='delicious')
# iFS.add_linguistic_variable("Food", LinguisticVariable([F_1, F_2], concept="Food quality", universe_of_discourse=[0,10]))
iLV_2 = IntervalLinguisticVariable([F_1, F_2], concept="Food quality", universe_of_discourse=[0, 10])
iLV_2.plot()
iFS.add_linguistic_variable("Food", iLV_2)


# Define output fuzzy sets and linguistic variable
T_1 = IntervalFuzzySet(function_start=Trapezoidal_MF(a=0, b=0, c=1, d=9), function_end=Trapezoidal_MF(a=0, b=0, c=1, d=11), term="small")
T_2 = IntervalFuzzySet(function_start=Triangular_MF(a=0, b=10, c=18), function_end=Triangular_MF(a=2, b=10, c=22), term="average")
T_3 = IntervalFuzzySet(function_start=Trapezoidal_MF(a=8, b=18, c=25, d=25), function_end=Trapezoidal_MF(a=12, b=18, c=25, d=25), term="generous")
# iFS.add_linguistic_variable("Tip", LinguisticVariable([T_1, T_2, T_3], universe_of_discourse=[0,25]))
iLV3 = IntervalLinguisticVariable([T_1, T_2, T_3], concept="Tip", universe_of_discourse=[0, 25])
iLV3.plot()
iFS.add_linguistic_variable("Tip", iLV3)

# Define fuzzy rules
R1 = "IF (Service IS poor) OR (Food IS rancid) THEN (Tip IS small)"
R2 = "IF (Service IS good) THEN (Tip IS average)"
R3 = "IF (Service IS excellent) OR (Food IS delicious) THEN (Tip IS generous)"
iFS.add_rules([R1, R2, R3])

# Set antecedents values
iFS.set_variable("Service", 4)
iFS.set_variable("Food", 8)

# Perform Mamdani inference and print output
print(iFS.Mamdani_interval_inference(["Tip"]))
