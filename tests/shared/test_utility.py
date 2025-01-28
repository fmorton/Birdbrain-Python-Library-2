from birdbrain_utility import BirdbrainUtility

def test_flatten():
    flattened = BirdbrainUtility.flatten_string([ "something", "1", [ "A", "B" ], "2", "else", 99, [ 99 ]])

    assert flattened == "something/1/A/B/2/else/99/99"

def test_flatten_tuple():
    flattened = BirdbrainUtility.flatten_string( ("something", "1", [ "A", "B" ], "2", "else", 99, [ 99 ]) )

    assert flattened == "something/1/A/B/2/else/99/99"

def test_is_none_or_empty():
    assert BirdbrainUtility.is_none_or_empty(None)
    assert BirdbrainUtility.is_none_or_empty('')
    assert not BirdbrainUtility.is_none_or_empty('something')

