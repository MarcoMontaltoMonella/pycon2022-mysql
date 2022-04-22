import os
import sys
import time


# The following would be stored in a config/secrets file and service discovery
INITIAL_OFFSET = 55  # seconds
DB_HOST = "db1"
DB_PORT = "3306"
DBS_TO_MONITOR = [os.getenv("MYSQL_DATABASE")]


def do_healthcheck(current_time: str) -> None:
    print("Healthcheck initiated \N{speech balloon}")
    # mysqlcheck -h 127.0.0.1 -P 1441 -u root --protocol=tcp --password=pycon --analyze <db-name>


def offset_healthcheck_start() -> None:
    # to make sure dbs are up and running
    print(
        f"Waiting {INITIAL_OFFSET} seconds before starting healthcheck...\N{sleeping face}"
    )
    time.sleep(INITIAL_OFFSET)


def periodic_healthcheck() -> None:
    healthcheck_periodicity = int(sys.argv[1])

    offset_healthcheck_start()

    while True:
        current_time = time.ctime()
        print(f"Healthcheck time: {current_time} \N{stopwatch}")
        do_healthcheck(current_time)
        time.sleep(healthcheck_periodicity)


if __name__ == "__main__":
    periodic_healthcheck()
