import argparse

# arguments
parser = argparse.ArgumentParser(description="Sort key-value pairs based on values.")
parser.add_argument("input_file", help="Input file")
parser.add_argument("output_file", help="Output file")
parser.add_argument(
    "-r", "--reverse", action="store_true", help="Reverse the sort order"
)
args = parser.parse_args()

with open(args.input_file, "r") as file:
    lines = file.readlines()
    data = [line.strip().split("\t") for line in lines]

sorted_data = sorted(data, key=lambda x: float(x[1]), reverse=args.reverse)

# sorted data
with open(args.output_file, "w") as file:
    for pair in sorted_data:
        file.write(f"{pair[0]}\t{pair[1]}\n")
