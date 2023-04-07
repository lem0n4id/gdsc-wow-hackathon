def parse_form_data(form_data):
    parsed_data = {}
    for key, value in form_data.items():
        if key != 'name':
            parsed_value = float(value.split(' ')[-1][1:-1])
            parsed_data[key] = parsed_value
    return parsed_data