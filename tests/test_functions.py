# tests/test_functions.py

from tarotai.core import tarotAI_functions as tf

def test_tell_output_type():
    result = tf.tell("past-present-future")
    assert isinstance(result, str)

def test_help_contains_word_tarot():
    text = tf.help()
    assert "tarot" in text.lower()
