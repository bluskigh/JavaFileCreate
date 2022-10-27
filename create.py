import sys


def run():
    program_name = sys.argv[1]
    with open(f'{program_name}.java', 'w') as f:
        f.write(f"public class {program_name}" + " {\n\tpublic static void main(String[] args) {\n\t}\n}")

if __name__ == "__main__":
    run()

