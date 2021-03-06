from reverse_dict import reverse_input_dict
from unittest import TestCase
from io import StringIO
from unittest.mock import patch

output_value = reverse_input_dict()
output_value_answer = {
  'I': {
    'deserve': {
      'to': {
         'be': 'hired'
      }
    }
  }
}
TestCase().assertEqual(output_value, output_value_answer)