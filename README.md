# Longest Common Subsequence (LCS) Calculation Programming Project 03

This LCS Calculation Project involves a script for computing the longest common subsequence between two sequences using both dynamic programming and brute force methods. It includes a timeout feature for the brute force method to prevent excessively long computation times.

## Features

- Accepts DNA sequences from a specified input file.
- Utilizes two methods for LCS computation: dynamic programming and brute force with a timeout.
- Outputs the results, method used, including the LCS, number of comparisons, and computation time.
- Supports validating sequence content to ensure compatibility.
- Ensures only A,T,G,C nucleotides are in the input file , and converts the small letters to capital letters. 
- An Error message is displayed in the terminal along with, in which sequence there is an error, in case of Invalid input sequences or if there are no sequences in the input file.

## Requirements

- Python 3.x
## File Organization

- **Code File**: `DynamicProgramming.py`
- **Input Files**:
  - `DynamicLab2Input.txt` - Contains test sequences from the lab handout for basic functionality testing.
  - `Input_longsequences.txt` - Contains longer sequences for performance testing.
  - `Input_shortsequences.txt` - Contains shorter sequences to check brute force.
  -  `error.txt`- contains sequences with error
- **Output Files**:
  - `DynamicLab2Output.txt` - Outputs results for tests run with `DynamicLab2Input.txt`.
  - `Output_longsequences.txt` - Outputs results for tests run with `Input_longsequences.txt`.
  - `Output_shortsequence.txt` - Outputs results for tests run with `Input_shortsequences.txt`.
  -  `error_output.txt`- Output results from `error.txt`, it is an empty file because no results were generated. 

## Usage

1. **Prepare the Input File**: Create an input text file containing sequences formatted as `key=value`, one sequence per line.
2. **Run the Script**: Execute the script from the command line. When prompted, enter the paths to the input and desired output file locations.
3. **Review the Output**: Open the output file to review the results, including the LCS, method used, number of comparisons made, and the execution time for each method.

## Functions

### `lcs_dp(s1, s2)`
- **Purpose**: Computes the longest common subsequence using dynamic programming, which is efficient and optimal for most cases.
- **Parameters**:
  - `s1`, `s2`: The sequences to compare.
- **Returns**: A tuple containing the LCS and the number of comparisons made.

### `lcs_brute_force(s1, s2, timeout)`
- **Purpose**: Attempts to find the LCS using a brute force method, with a timeout to abort excessively long computations.
- **Parameters**:
  - `s1`, `s2`: The sequences to compare.
  - `timeout`: Maximum allowed time in seconds before aborting the computation.
- **Returns**: A tuple containing the LCS, number of comparisons made, a boolean indicating if the computation was timed out, and the elapsed time.

### `read_input(input_filepath)`
- **Purpose**: Reads and validates sequences from an input file, ensuring they contain only valid characters (e.g., ATGC for DNA sequences).
- **Parameters**:
  - `input_filepath`: Path to the input file.
- **Returns**: A dictionary with sequences keyed by their identifiers.

### `compare_strings(strings)`
- **Purpose**: Compares each pair of strings using the specified LCS computation methods.
- **Parameters**:
  - `strings`: A dictionary of string identifiers to sequences.
- **Returns**: A list of results, including details for each comparison.

## Implementation Details

- **Dynamic Programming**: The dynamic programming approach provides an efficient solution to the LCS problem by building a matrix that helps trace back the longest subsequence. This method is significantly faster and uses less memory than Brute force.
- **Brute Force with Timeout**: This method explores all possible subsequences recursively. Given the exponential growth of possibilities, a timeout parameter was used to avoid long computation times, making the script practical even for larger sequences.

## Execution

The script prompts user for input and output file locations and runs the LCS computation for configured sequences. The results, including the LCS and associated statistics, are written to the output file.For a better use of system memory a termination has been added to the brute force method.

## Note

This LCS computation project provides a detailed analysis of sequence comparison efficiencies. It is particularly useful in bioinformatics for comparing DNA, RNA, or protein sequences.

## Author
Rishitha Pulakhandam <br>
rpulakh1@jh.edu

