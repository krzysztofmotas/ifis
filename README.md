# IFIS (*Interval-Valued Inference System based on Simpful*)
The motivation of creating a library for the application of interval-valued fuzzy inference was the fact, 
that the methods for classifying uncertain data are important in many applications.

Interval-Valued Inference System (IFIS) is implemented in the Python 3 programming language. 
It is an extension of the Simpful library [1] and the dependencies are Numpy  and Scipy. 
The latest version of IFIS currently supports the following features:
1. Definition of polygonal (e.g., vertex-based) and functional (e.g., sigmoidal, Gaussian, custom shaped) membership 
functions.
2. Definition of interval-valued fuzzy rules as strings of text written in natural language.
3. Definition of arbitrarily complex fuzzy rules built with the logic operators AND, OR (adequate interval-valued 
fuzzy operations built by minimum and maximum, respectively), or  NOT (interval fuzzy negation) or arbitrary 
interval-valued aggregations.
4. Mamdani and Takagi-Sugeno inference methods.

By providing the input values for the antecedents, IFIS  can perform an interval-valued fuzzy inference and eventually 
provides the final output values.

The elements of our system are present in the next points:

I. *Preparation data - 2 fuzzyfication*. Defining the interval fuzzy sets connected later with linguistic variables

Data preparation takes place in the following two paths:

a. The data is input as real values. Then, the interval-valued fuzzy set is defined by the membership function that 
describes it. Within the library, standard types of membership functions are defined, e.g. triangular, trapezoidal, 
sigmoidal, Gaussian, etc. It is also possible to define  membership functions based on the function or by specifying 
characteristic points  of this function. To define interval-valued fuzzy sets, it is required to provide two provisions 
of the membership function, describing, respectively, the beginning and the end of the interval set onto.

b. The data is input as real value intervals. Then it is  possible to describe a fuzzy set with one membership function.

The obtained interval data for both paths will meet the assumption:

{[a1, a2]:  a1 <= a2,  a1, a2 belongs to [0.1]}.

II. *Inference Process. Rules*

The construction of an inference system based on the interval extension of the Simpful library consists in:

a. Defining the parameters to interval-valued fuzzy sets (parameters functions built as objects of an abstract class, 
extending FuzzySet object) used to connect with linguistic variables. Moreover, we give the boundaries of the universe 
for each variable/attribute (except in the case of building a function based on points, where the minimum and maximum 
values determine the limit values) helpful in their graphic representation.

b. Determining interval linguistic variables based on the defined interval-valued fuzzy sets - creating objects by 
extending LinguisticVariable objects. Depending on the selected inference type, ie Mamdani or Takagi-Sugeno, an 
appropriate representation of the inferring system output is defined.

c. Providing a set of inference rules based on the defined interval linguistic variables and fuzzy sets. As part of 
the rules for premises and output values, you can use the logical operators AND, OR, NOT, and chosen interval-valued 
aggregation functions, which have also been specified in the interval form.

d. Launches the inference process according to the defined types, i.e., Mamdani or Takagi-Sugeno with given values of 
variables. For the Takagi-Sugeno system, we also need to define the output functions along with their identification 
for rule definitions.

e. The inference results take into account the appropriate defuzzification: centroid (Mamdani) or weighted mean 
(Takagi-Sugeno) method and eventually decision thresholds.

## Installation
To be able to use our library you need to download its sources. Earlier you must install the Simpful library from 
https://github.com/aresio/simpful

## Citing IFIS
If you find  IFIS useful for your research, please cite our work as follows:

[1] Spolaor S., Fuchs C., Cazzaniga P., Kaymak U., Besozzi D., Nobile M.S.: Simpful: a user-friendly Python library for 
fuzzy logic, International Journal of Computational Intelligence Systems, 13(1):1687–1698, 2020 
[DOI:10.2991/ijcis.d.201012.002].

[2] Grochowalski P.,  Kosior D., Gil D., Kozioł W., Pękala B., Dyczkowski K., Python library for interval-valued fuzzy 
inference, to appear.

## Illustrative Examples
In this section, we provide  examples, together with their corresponding Python code, to show the potential and the 
usage of IFIS. To show the usefulness and possibility of IFIS we provide two practical applications. They are using 
the definition of a Mamdani and Takagi-Sugeno IFIS for the tipping problem (presented here), and a more complex problem 
which is posture diagnostics used in fall detection based on the analysis of images from Kinect cameras (presented in 
[2]).

### Tipping problem
The tipping problem consists in computing a fair tip (in terms of percentage of the overall bill), taking into account 
a restaurant’s services. Listings 1 show example of IFIS code to define a interval inference system that calculates 
the tipping amount on the basis of two input variables, describing food and serving staff quality.

Listing 1 illustrates a range inference system whose task is to determine the value of the tip for the waiter 
(as a percentage of the total order value) based on the evaluation of the service in an example restaurant. 
To determine the size of the tip, two inputs are taken into account: food quality and service quality. 
The considered example is to illustrate how to define an inference system based on interval fuzzy sets. The basis for 
the created library, which has already been mentioned, is the Simpful library supporting the creation of fuzzy 
inference systems.

An exemplary implementation of an inference system based on the Takagi-Sugeno method:

```
from simpful import *
from interval_simpful.interval_fuzzy_sets import *
from interval_simpful.interval_fuzzy_system import *
from interval_simpful.interval_linguistic_variable import *

# A simple interval fuzzy inference system for the tipping problem
# Create interval fuzzy system object
iFS = IntervalFuzzySystem()

# Define interval fuzzy sets and interval linguistic variables
S_1 = IntervalFuzzySet(function_start=Triangular_MF(a=0, b=0, c=5), function_end=Trapezoidal_MF(a=1, b=1, c=1, d=6), term='poor')
S_2 = IntervalFuzzySet(function_start=Triangular_MF(a=0, b=5, c=10), function_end=Trapezoidal_MF(a=0, b=4, c=6, d=10), term='good')
S_3 = IntervalFuzzySet(function_start=Triangular_MF(a=5, b=10, c=10), function_end=Trapezoidal_MF(a=4, b=9, c=10, d=10), term='excellent')
iFS.add_linguistic_variable("Service", IntervalLinguisticVariable([S_1, S_2, S_3], concept="Service quality", universe_of_discourse=[0, 10]))

F_1 = IntervalFuzzySet(function_start=Triangular_MF(a=0, b=0, c=8), function_end=Trapezoidal_MF(a=1, b=1, c=2, d=10), term='rancid')
F_2 = IntervalFuzzySet(function_start=Triangular_MF(a=2, b=10, c=10), function_end=Trapezoidal_MF(a=0, b=8, c=10, d=10), term='delicious')
iFS.add_linguistic_variable("Food", IntervalLinguisticVariable([F_1, F_2], concept="Food quality", universe_of_discourse=[0, 10]))

# Define output crisp values
iFS.set_crisp_output_value("small", 5)
iFS.set_crisp_output_value("average", 15)

# Define function for generous tip (food score + service score + 5%)
iFS.set_output_function("generous", "Food+Service+5")

# Define fuzzy rules
R1 = "IF (Service IS poor) OR (Food IS rancid) THEN (Tip IS small)"
R2 = "IF (Service IS good) THEN (Tip IS average)"
R3 = "IF (Service IS excellent) OR (Food IS delicious) THEN (Tip IS generous)"
iFS.add_rules([R1, R2, R3])

# Set antecedents values
iFS.set_variable("Service", 4)
iFS.set_variable("Food", 8)

# Perform Sugeno interval inference and print output
print(iFS.Sugeno_interval_inference(["Tip"]))
```

In the first step, on line 8, a root object is created representing the inference system based on interval fuzzy sets. 
The resources of this object will be supplemented with individual elements of the system allowing for the implementation 
of fuzzy inference. In lines 11-18, interval fuzzy sets are created and attached to the appropriate interval linguistic 
variables. Each of the interval fuzzy sets is (in the current version of the library) described by two membership 
functions, i.e. one for the beginning of the interval and the other for its end. These functions can be defined by 
means of defined functions that perform typical membership functions, e.g. triangular, trapezoidal, etc. (taken from 
the Simpful library), by means of characteristic points that define them or their own function definitions. 
In the considered example, two input data (input linguistic variables) are considered: Service quality and Food quality. 
Service quality is described by three compartments fuzzy harvests "poor", "good", "excellent", and Food quality by two 
fuzzy harvests "rancid" and "delicious".

Between lines 21-25, the output of the inferring system is defined, the implementation of which depends on the selected 
inference method. In the inference system based on the Mamdani method, the output is defined in the form of an 
interval fuzzy set, and with the Takagi-Sugeno inference method, specific output functions are defined. In the example 
under consideration, two exact output values are given, corresponding to the tip value of 5% and 15% of the order value, 
and one value, which is derived from the relationship specified in line 25. Lines 27 - 30 define fuzzy inference rules, 
and lines 33 - 34 determine the real values of the input variables (two variables in the discussed example). The entire 
inference process is started on line 38, where the Takagi-Sugeno method of inference was used. For exemplary input 
data: rating for Service quality is equal to 4 and the rating for food quality (Food) is equal to 8 (for limits [0,10]), 
the result is a tip value defined by the range [14.1667%, 14.78143%]. It specifies the range in which the tip value may 
fluctuate as a percentage of the total order value.

## Further info
If you need further information, please write an e-mail at: pgrochowalski@ur.edu.pl

### References
[1] Spolaor S., Fuchs C., Cazzaniga P., Kaymak U., Besozzi D., Nobile M.S.: Simpful: a user-friendly Python library 
for fuzzy logic, International Journal of Computational Intelligence Systems, 13(1):1687–1698, 2020 
[DOI:10.2991/ijcis.d.201012.002]

[2] Grochowalski P.,  Kosior D., Gil D., Kozioł W., Pękala B., Dyczkowski K., Python library for interval-valued fuzzy 
inference, to appear

