Program Assumptions:
    -The program supports only the default log format, not custom formats.
    -Both lookup.csv and flow_logs.txt must contain data and should not be empty.
    -The "port" referenced in port_protocol_counts.csv corresponds to dstport.
    -The protocol is limited to three types: tcp, icmp, and udp. Expanding support to all protocols would require mapping approximately 150 different protocol numbers.
    -The lookup.csv and flow_logs.txt files are expected to follow the format provided in the sample and should not be empty or contain any erroneous rows.
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
The program has been tested with various flow logs and lookup files. All test cases are documented in the testcase folder. A script is used to generate lookup.csv and flow_logs.txt.
    testcase1:
        -flow_logs.txt has 99988 rows.
        -lookup.txt has 12 rows. 
    testcase2:
        -flow_logs.txt has 99990 rows.
        -lookup.csv has 10000 rows.
    testcase3:
        -flow_logs has 100000 rows
        -lookup.csv has 100 rows, each port assigned random number between 1 to 100. 
The program pass all testcases. 

Space and Time Complexity:
    -Space complexity: O(n + m)
    -Time complexity: O(n + m)
    Where n is the number of lines in the lookup file, and m is the number of lines in the flow log file.