from collections import defaultdict

def load_lookup_table(filename):
    lookup_table = {}
    with open(filename, mode="r") as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split(",")
            # dstport = parts[0], protocol = parts[1], tag = parts[2]
            key = (int(parts[0]), parts[1].lower())
            lookup_table[key] = parts[2]
    return lookup_table


def parse_flow_logs(log_filename, lookup_table):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)

    with open(log_filename, mode="r") as file:
        for line in file:
            parts = line.split()
            dstport = int(parts[6])
            protocol = (
                "tcp" if parts[7] == "6" else "udp" if parts[7] == "17" else "icmp"
            )
            key = (dstport, protocol)

            port_protocol_counts[key] += 1
            
            if key in lookup_table:
                tag = lookup_table[key]
            else:
                tag = "Untagged"
            tag_counts[tag] += 1

    return tag_counts, port_protocol_counts


def write_output(tag_counts, port_protocol_counts, tag_output_file, pp_output_file):
    with open(tag_output_file, mode="w") as file:
        file.write("Tag,Count\n")
        for tag, count in sorted(tag_counts.items()):
            file.write(f"{tag},{count}\n")

    with open(pp_output_file, mode="w") as file:
        file.write("Port,Protocol,Count\n")
        for (port, protocol), count in sorted(port_protocol_counts.items()):
            file.write(f"{port},{protocol},{count}\n")


def main():
    LOOKUPADDR = "testcase1/lookup.csv"
    FLOWLOGADDR = "testcase1/flow_logs.txt"
    lookup_table = load_lookup_table(LOOKUPADDR)
    tag_counts, port_protocol_counts = parse_flow_logs(
       FLOWLOGADDR, lookup_table
    )
    write_output(
        tag_counts, port_protocol_counts, "tag_counts.csv", "port_protocol_counts.csv"
    )


if __name__ == "__main__":
    main()
