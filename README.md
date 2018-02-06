# Timeout Tech Test

### Unfinished

I didn't get a chance to fully complete this to the standards I would like,
The main problem has been "solved", but the supporting infrastructure around
the code hasn't been finished to where I would like it to be.

* Test suite not fully completed, I didn't manage to test the main task,
only the utilities around it.
* main.py is a bit overcrowded, I would want to possibly move some of the functions
into their own files, and also the namedtuple possibly replaced by a class.
* Error handling, there are not enough exception handling, for example if you
pass in a bunk json file the program would crash
* output; no logging and the final output for the venues is a bit messy
* duplication, there is a couple of functions that could be made a bit
more generic (output and parsing) that have special code paths depending on
if it's an unacceptable or acceptable venue, I could move that into one function
```    return set(
        [f.venue_name for f in unacceptable_venues]
    ).symmetric_difference(
        set([f.venue_name for f in acceptable_venues]))
```
* this could be a lot nicer ^^^^
* I brute force my way through some of the set theory
* I would of liked to have customised input locations, and also the inputs themselves
are a bit flaky.

### Running

```python main.py```

```python -m unittest discover tests```



