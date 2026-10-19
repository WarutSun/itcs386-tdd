## 1. Tests and production code

In Part A I ended with 9 tests in test_kitchen.py (I wrote 10 in total, but
deleted test_multiplication_by_two in A3 because its job was done). The final
kitchen.py has 41 non-blank lines, and test_kitchen.py has 36 non-blank,
non-comment lines. The ratio of test code to production code is therefore
about 36 : 41, or roughly 0.9 : 1. The test code is almost as large as the
production code, even though each test is only a few lines, because every
behaviour was specified by its own test before it was implemented.