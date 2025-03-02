"""This Python script computes the Longest Common Subsequence (LCS) between two sequences,
utilizing dynamic programming and a brute force approach with a timeout for proper utilization
of time and memory.The script ensures input data integrity by validating nucleotide characters
and handles sequence comparison through different functions. The output includes the LCS, the number
of comparisons, and computation time, written to a user-specified file."""

import time
import re

def lcs_dp(s1, s2):
    """Calculate the longest common subsequence using dynamic programming."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp_comparisons = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp_comparisons += 1
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs = []
    while m > 0 and n > 0:
        if s1[m - 1] == s2[n - 1]:
            lcs.append(s1[m - 1])
            m, n = m - 1, n - 1
        elif dp[m - 1][n] > dp[m][n - 1]:
            m -= 1
        else:
            n -= 1

    return ''.join(reversed(lcs)), dp_comparisons

def is_valid_sequence(sequence):
    """Check if the sequence contains only ATGC characters."""
    return not re.search(r'[^ATGC]', sequence.upper())

def read_input(input_filepath):
    """Read input file, validate and return a dictionary of uppercase DNA strings."""
    with open(input_filepath, 'r') as file:
        data = {}
        for line in file:
            if '=' in line:
                key, value = line.split('=', 1)
                value = value.strip().upper()  # Convert to uppercase
                if is_valid_sequence(value):  # Validate sequence
                    data[key.strip()] = value
                else:
                    print(f"Invalid sequence found for key {key.strip()}: {value}")
                    return {}
    print(f"Input file '{input_filepath}' read successfully with valid sequences.")
    return data


def generate_subsequences(s):
    """Generate all subsequences of the given string."""
    subsequences = ['']
    for char in s:
        subsequences += [char + subseq for subseq in subsequences]
    return subsequences

def is_subsequence(subseq, s2):
    """Check if subseq is a subsequence of s2."""
    it = iter(s2)
    return all(char in it for char in subseq)


def lcs_recursive(s1, s2, i, j, start_time, timeout, comparisons):
    current_time = time.time()
    if current_time - start_time > timeout:
        return "", comparisons  # Return empty LCS if timeout exceeded

    if i == 0 or j == 0:
        return "", comparisons

    comparisons += 1  # Increment comparison each time a recursive call is made
    if s1[i - 1] == s2[j - 1]:
        lcs, comparisons = lcs_recursive(s1, s2, i - 1, j - 1, start_time, timeout, comparisons)
        return lcs + s1[i - 1], comparisons
    else:
        left, comp_left = lcs_recursive(s1, s2, i, j - 1, start_time, timeout, comparisons)
        right, comp_right = lcs_recursive(s1, s2, i - 1, j, start_time, timeout, comparisons)
        if len(left) > len(right):
            return left, comp_left
        else:
            return right, comp_right


def lcs_brute_force(s1, s2, timeout=120):
    start_time = time.time()
    max_lcs, bf_comparisons = lcs_recursive(s1, s2, len(s1), len(s2), start_time, timeout, 0)
    elapsed_time = time.time() - start_time
    timed_out = elapsed_time > timeout
    return max_lcs, bf_comparisons, timed_out, elapsed_time


def compare_strings(strings):
    """Compare each string pair using dynamic programming."""
    keys = list(strings.keys())
    results = []
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            s1_key, s2_key = keys[i], keys[j]
            s1, s2 = strings[s1_key], strings[s2_key]

            start_time = time.time()
            lcs_result, comparisons = lcs_dp(s1, s2)
            duration = time.time() - start_time

            results.append({
                's1_key': s1_key, 's2_key': s2_key,
                's1': s1, 's2': s2,
                'lcs': lcs_result, 'time': duration, 'comparisons': comparisons
            })

    return results

def main():
    input_filepath = input("Enter the input file location: ")
    output_filepath = input("Enter the output file location: ")
    strings = read_input(input_filepath)

    if not strings:
        print("Invalid input sequences or no sequences to process.")
        return

    # First, open the file to write the dynamic programming results
    with open(output_filepath, 'w') as file:
        if not strings:
            file.write(f"Invalid input sequences or no sequences to process.")
        file.write("Dynamic Programming Results:\n")
        for s1_key, s1 in strings.items():
            for s2_key, s2 in strings.items():
                if s1_key != s2_key:
                    start_time = time.time()
                    lcs_result, comparisons = lcs_dp(s1, s2)
                    duration = time.time() - start_time
                    file.write(f"Between {s1_key} & {s2_key}:\n")
                    file.write("  Method: Dynamic Programming\n")
                    file.write(f"  Original Sequences: {s1_key}='{s1}', {s2_key}='{s2}'\n")
                    file.write(f"  LCS (DP): '{lcs_result}' Length={len(lcs_result)} Time Taken: {duration:.6f}s Comparisons={comparisons}\n")
                    file.write("\n")

    # Second, open the file to write brute force results
    with open(output_filepath, 'a') as file:
        file.write("\nBrute Force Results:\n")
        for s1_key, s1 in strings.items():
            for s2_key, s2 in strings.items():
                if s1_key != s2_key:
                    lcs_bf, bf_comparisons, timed_out, bf_time = lcs_brute_force(s1, s2)
                    file.write(f"Between {s1_key} & {s2_key}:\n")
                    file.write(f"  Original Sequences: {s1_key}='{s1}', {s2_key}='{s2}'\n")
                    if timed_out:
                        file.write("  Brute Force calculation exceeded the timeout of 120 seconds and was terminated.\n")
                    else:
                        file.write("  Method: Brute Force\n")
                        file.write(f"  LCS (BF): '{lcs_bf}' Length={len(lcs_bf)} Time={bf_time:.6f}s Comparisons={bf_comparisons}\n")
                    file.write("\n")

    print(f"Results written successfully to '{output_filepath}'.")

if __name__ == "__main__":
    main()


