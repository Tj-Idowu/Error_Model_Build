import os

def merge_files(source_directory, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for root, _, files in os.walk(source_directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                with open(file_path, 'r') as input_file:
                    output_file.write(input_file.read())

if __name__ == "__main__":
    source_directory = "path/to/ncbi-genomes-2023-08-15"  # Path to input directory
    output_file_path = "path/to/reference/ncbi_sequence.fna"    # Path to output file name

    merge_files(source_directory, output_file_path)
    print("Done merging files to", output_file_path)
