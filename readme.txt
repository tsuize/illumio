README

Program Assumptions:
-The program supports only the default log format, not custom formats.
-Both lookup.csv and flow_logs.txt must contain data and should not be empty.
-The "port" referenced in port_protocol_counts.csv corresponds to dstport.
-The protocol is limited to three types: tcp, icmp, and udp. Expanding support to all protocols would require mapping approximately 150 different protocol numbers.
-The lookup.csv and flow_logs.txt files are expected to follow the format provided in the sample and should not contain any erroneous rows.
-Tags are handled in a case-insensitive manner (e.g., "SV_P3" and "sv_p3" are treated as equivalent).
-The program minimizes the use of external libraries or packages to facilitate easy review.

Instructions:
1.Ensure that the LOOKUPADDR and FLOWLOGADDR variables in the script are correctly set to the paths of your lookup.csv and flow_logs.txt files.
2.Run the script using Python:
    python app.py
3.The output files tag_counts.csv and port_protocol_counts.csv will be generated in the script's directory.

Dependencies:
    Python 3.x

Testing:
The program has been tested with various flow logs and lookup files. All test cases are documented in the testcase folder.

Space and Time Complexity:
-Space complexity: O(n + m)
-Time complexity: O(n + m)
    Where n is the number of lines in the lookup file, and m is the number of lines in the flow log file.
