import subprocess
import time

def run(step, command):
    print(f"\n Running: {step}")
    start = time.time()

    result = subprocess.run(command, shell=True)

    end = time.time()
    print(f"Finished {step} in {round(end - start, 2)} sec")

    if result.returncode != 0:
        print(f" Error in {step}")
        exit(1)

if __name__ == "__main__":

    run("STAGING LOAD", "python3 scripts/load_staging.py")

    run("DIMENSIONS BUILD", "python3 scripts/build_dimensions.py")

    run("FACT TABLE BUILD", "python3 scripts/build_fact.py")

    run("EXPORT TO POWER BI", "python3 scripts/export_powerbi.py")
    
    print("\n ETL PIPELINE COMPLETED SUCCESSFULLY ")
    