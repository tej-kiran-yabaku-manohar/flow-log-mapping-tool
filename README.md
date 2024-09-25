# Flow Log Mapping Tool

This project parses AWS VPC flow log data and maps each log entry to a tag based on a predefined lookup table. The tool counts occurrences of each tag and port/protocol combination and generates summary reports.

## Features

- Parses AWS VPC flow logs in the default version 2 format. For more information on the flow log format, refer to the [AWS Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html#flow-logs-fields).
- Maps log entries to tags based on destination port and protocol using a CSV lookup table.
- Provides a summary of tag counts and port/protocol combination counts.
- Case-insensitive matching for tags and protocol types.

## Requirements

- Python 3.x (or higher)
- No external dependencies (uses only built-in Python libraries)
- The project folder should be located on the Desktop for the program to read input files and write the output file.

## Usage

1. **Clone the repository** to the Desktop:
   ```bash
   git clone https://github.com/tej-kiran-yabaku-manohar/flow-log-mapping-tool.git
2. Or download the zip file, and save it in the Desktop location.
3. Run the below script using Python 3: ```
   python3 program.py ```
6. The output will be saved as output.txt in the project folder on the Desktop.
