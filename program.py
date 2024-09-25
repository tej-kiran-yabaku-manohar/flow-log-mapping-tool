import csv
from pathlib import Path
from collections import defaultdict

def get_programFiles_path():
    home = Path.home()
    desktop_path = home / 'Desktop'
    project_path = desktop_path / 'Illumio'
    return project_path


def parse_lookup_table(file_path):
    lookup_dict = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            dstport, protocol, tag = row
            key = (dstport, protocol)
            lookup_dict[key] = tag
    return lookup_dict


def parse_flow_logs(file_path):
    flow_logs = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split(' ')
            dst_port = parts[6]
            protocol = parts[7]
            flow_logs.append((dst_port, protocol))
    return flow_logs


def map_logs_to_tags(flow_logs, lookup_dict):
    tag_counts = {}
    port_protocol_counts = defaultdict(int)
    untagged_count = 0
    protocols = {'6': 'tcp', '17': 'udp', '1': 'icmp'}
    
    for dst_port, protocol in flow_logs:
        key = (dst_port, protocols.get(protocol))
        if key in lookup_dict:
            tag = lookup_dict[key]
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
        else:
            untagged_count += 1
        
        port_protocol_counts[key] += 1
    
    return tag_counts, port_protocol_counts, untagged_count


def write_output(file_path, tag_counts, port_protocol_counts, untagged_count):
    with open(file_path, 'w') as file:
        file.write("Tag Counts:\nTag,Count\n")
        for tag, count in tag_counts.items():
            file.write(f"{tag},{count}\n")
        file.write(f"Untagged,{untagged_count}\n\n")
        

        file.write("Port/Protocol Combination Counts:\nPort,Protocol,Count\n")
        for (port, protocol), count in port_protocol_counts.items():
            file.write(f"{port},{protocol},{count}\n")


def main():

    projectFolder_path = get_programFiles_path()
    flow_logs = parse_flow_logs(projectFolder_path / 'flow_logs.txt')
    lookup_dict = parse_lookup_table(projectFolder_path / 'lookup_table.csv')
   

    print(flow_logs)
    print(lookup_dict)
    
    tag_counts, port_protocol_counts, untagged_count = map_logs_to_tags(flow_logs, lookup_dict)
    
    write_output(projectFolder_path / 'output.txt', tag_counts, port_protocol_counts, untagged_count)
    print(f"Output written to {projectFolder_path / 'output.txt'}")

if __name__ == "__main__":
    main()
