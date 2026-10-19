# Reflection

## 1. Tests and production code

In Part A I ended with 9 tests in test_kitchen.py (I wrote 10 in total, but
deleted test_multiplication_by_two in A3 because its job was done). The final
kitchen.py has 41 non-blank lines, and test_kitchen.py has 36 non-blank,
non-comment lines. The ratio of test code to production code is therefore
about 36 : 41, or roughly 0.9 : 1. The test code is almost as large as the
production code, even though each test is only a few lines, because every
behaviour was specified by its own test before it was implemented.

## 2. Longest red bar

The longest red period was in A7, when I changed reduce(unit) into
reduce(converter, unit). Three tests failed at once (simple addition, same-unit
reduce and mixed addition) because I had changed the signature in some places
but not in Converter.reduce, and Converter had no `rates` dictionary yet. I
changed too many things in one step. A5 was also red for a while: adding the
`unit` field broke every old test that called Quantity(200). That one was
expected, and the failing tests showed exactly which lines to update. I also
lost time in A3 because I ran the tests several times before deleting
test_multiplication_by_two and saving the file, so I kept seeing the same
failure.

## 3. Fake It, Triangulate, Obvious Implementation

- **Fake It:** In A1, times() returned the constant 600, and in A6, plus()
  returned grams(500) and Converter.reduce returned its argument. This was a
  good choice. It proved the test setup worked and gave me a green bar to
  refactor from. The next test removed each fake value.
- **Triangulate:** In A2, a second test (200 x 2 = 400) forced me to replace 600
  with the real formula. This was right, because one example could not
  determine the formula. The cost was a test that I deleted later.
- **Obvious Implementation:** In A8, Sum.times was a short method that
  multiplies left and right, and it worked first time, so the choice was right.
  In A7, I made several changes at once (rate lookup, new signature,
  conversion), and it went wrong with three failing tests. That step was too
  big, and I should have used smaller steps.

## 4. Test list

Still open: `__hash__`. Defining __eq__ makes Quantity unhashable, so it cannot
go in a set or dictionary. Nothing in the program needs that, so I would delete
it as speculation unless a real use appears. If I had more time, I would add two
tests that are not on the list: converting between units when no rate has been
added (currently a KeyError), and comparing a Quantity with a Sum (currently an
AttributeError, which I saw in A6). I would implement these next, because they
describe behaviour that users could really trigger.

## 5. Quantity.reduce

If I had designed the system on paper first, I would not have written
Quantity.reduce as a method that returns itself. I would probably have written
one function that converts a quantity to a unit. The method exists because
Converter.reduce needs to treat Quantity and Sum in the same way, so both must
answer reduce(converter, unit). That polymorphism appeared from the tests, not
from a plan. In the end, the design is cleaner than what I would have guessed,
and Sum does not need to know anything about conversion rates.

## 6. Tests after code vs before code

In Part 0 the code already existed, so I wrote tests to check it. The work felt
like checking and hunting for bugs, and in shipping.py the tests found three
bugs at the boundaries (0 kg, 1 kg and started kilograms). The tests did not
change the design. In Part A the tests came first and they shaped the design.
The test in A3 showed that times() should return a new object (a value
object). In A4, writing assertions on .amount was awkward, so I added __eq__.
In A5, the first client of Quantity was the test suite, and it told me where
the change to add a unit would land. Part A was slower, but the commit history
shows each red and green step, and I always knew which change turned the bar
green.