import datetime
import sys
import json

def filter_file(input_filename, rule):
    if input_filename is None:
        print("Error: No file provided!")
        sys.exit(1)

    output_filename = input_filename + ".csv"

    try:
        # Open the input JSON file
        with open(input_filename, "r") as file_input:
            data = json.load(file_input)

        # Open the output CSV file for writing
        with open(output_filename, "w") as output_file:
            # Add timestamp and header
            timestamp = datetime.datetime.now().isoformat()
            output_file.write(f"Generated on: {timestamp}\n")
            output_file.write("Name, Rule,Message,Location,Line,Column\n")

            results_found = False

            # Check if 'runs' exists and is a list
            if 'runs' in data and isinstance(data['runs'], list):
                for run in data['runs']:
                    if 'results' in run and isinstance(run['results'], list):
                        for result in run['results']:
                            rule_id = result.get('ruleId', 'N/A')

                            if rule_id == rule:
                                name = result.get('name', {}).get('text', 'N/A')
                                message = result.get('message', {}).get('text', 'N/A')
                                location = result.get('locations', [{}])[0].get('physicalLocation', {}).get('artifactLocation', {}).get('uri', 'N/A')
                                region = result.get('locations', [{}])[0].get('physicalLocation', {}).get('region', {})
                                startline = region.get('startLine', 'N/A')
                                endcolumn = region.get('endColumn', 'N/A')

                                # Write filtered result to CSV
                                output_file.write(f"{rule_id},{message},{location},{startline},{endcolumn}\n")
                                results_found = True

            if not results_found:
                output_file.write(f"No results found for rule: {rule}\n")

        print(f"Filtered data saved to {output_filename}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python filter.py <filename> <rule>")
        sys.exit(1)

    input_filename = sys.argv[1]
    rule = sys.argv[2]

    if not input_filename:
        print("Error: Filename is empty or None!")
        sys.exit(1)

    filter_file(input_filename, rule)

