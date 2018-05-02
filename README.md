# A-FRONTEND-API-FOR-TEST-PROCEDURES-IN-EMBEDDED-SYSTEMS

## ABSTRACT

Who polices the police? This is a question many educated people have already made. For the countries that
conform to the code of law, the answer lies on the checks and balances that are inscribed in the law and govern
the separation of powers of the branches of state. From a more philosophical but also practical perspective the
question one is looking to answer is how to assert something is correct without entering and infinite regression
of checks?
The question "who polices the police?" finds also key relevance in the field of software, embedded systems and
cyber-physical systems testing. These days, testing, as performed in efficient organisations, is mainly automated.
Manual testing still exists, because some test procedures are hard, if not impossible to automate in a practical
way, but for the most part tests are implemented by automated test procedures. But automated test procedures,
at least those that matter for this discussion, are not generated automatically, they are coded by someone. The
question is then, if automated test procedures are used to test the correct functioning of a SW application or of
a system, are they less prone to errors or somehow more reliable than the SW or system under test? The short
answer is "no"; in general, there is no good justification to claim that the source code of an automated test
procedure is more reliable than the SW being tested. Rather often one could claim the exact opposite instead,
at least for developers own unit tests.
The case that we build here is that, in general, source code of test procedures can be no more error prone than
the source code of the SW application being tested. Or better saying, for source code of equivalent complexity
one should expect an equivalent error rate. And from here we reach to the following key challenge that we formulate out of first-hand experience: testing complex systems often involves test scripts nearly as complex, or
sometimes more complex, than the system being tested.
A potential way around this conundrum is to develop test procedures atop of simple test APIs, strictly enforce
complexity limitation conventions, use simple special purpose test languages, or a combination of these. The
question that we set at the core of this thesis proposal, is whether there is a practical way to test complex
systems without having complex test procedures and without creating the illusion of simplicity by hiding complexity in draconian test libraries.
The proposed case study takes a satellite control application as system under test and entails extending a simple
simulator for the system component this application interacts with. Atop of these shall be developed test procedures to study whether there are practical limitations of using simple procedures to test complex interactions
between the satellite control application and its simulated environment.
