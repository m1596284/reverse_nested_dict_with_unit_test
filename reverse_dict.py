# Input:
input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}

def reverse_input_dict():
    # deform the nested dict
    input_list = []
    for key, val in input_value.items():
        input_list.append(key)
        for key2, val2 in val.items():
            input_list.append(key2)
            for key3, val3 in val2.items():
                input_list.append(key3)
                for key4, val4 in val3.items():
                    input_list.append(key4)
                    input_list.append(val4)
    #create output_value
    output_value = {
        input_list.pop():{
            input_list.pop():{
                input_list.pop():{
                    input_list.pop():input_list.pop()
                }
            }
        }
    }
    return output_value

if __name__ == "__main__":
    reverse_input_dict()
