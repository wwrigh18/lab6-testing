import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    
    assert sample_run_anonymizer('My name is Bond.', 'PERSON', 0.8, 11, 15).text == "My name is BIP."
    
    pass