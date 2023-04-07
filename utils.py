def parse_form_data(form_data):
    parsed_data = {}
    for key, value in form_data.items():
        if key != 'name':
            try:
                parsed_value = float(value.split(' ')[-1][1:-1])
                parsed_data[key] = parsed_value
            except:
                parsed_data[key] = 0
    return parsed_data