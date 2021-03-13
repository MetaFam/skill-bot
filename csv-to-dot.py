import argparse
import skillgraph as sg

"""
Script to read data from CSV files, and output a .dot (GraphViz) file.

Example usage:
  python3 csv-to-dot.py --input-csv-dir data/simple --output-dot-file tmp/simple.dot

The .dot can then be converted to an image, for example with:
  $dot -Tpng tmp/simple.dot -o tmp/simple.png
"""

def main():
    all_args = argparse.ArgumentParser()

    all_args.add_argument("--input-csv-dir", required=True,
    help="Path of directory containing CSV inputs")
    all_args.add_argument("--output-dot-file", required=True,
    help="Output DOT file path")

    args = vars(all_args.parse_args())

    graph = sg.SkillGraph()

    sg.helpers.load_from_csv_directory(graph, args['input_csv_dir'])
    sg.helpers.export_as_dotfile(graph, args['output_dot_file'])


if __name__ == "__main__":
    main()
