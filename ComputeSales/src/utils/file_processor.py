def process_file(file_path):
    if not file_path:
        file_path = 'ComputeStatistics/data/test_file.txt'
        
    with open(file_path, 'r') as file:
        items = file.readlines()
    return [item.strip() for item in items]