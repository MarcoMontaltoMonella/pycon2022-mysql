import os
import sys
import time

# The following would be stored in a config/secrets file and service discovery
INITIAL_OFFSET = 60  # seconds
DB_HOST = "db1"
DB_PORT = "3306"
BACKUP_DESTINATION = "/backup/backup_storage"


def do_backup(current_time: str) -> None:
    print("Backup initiated \N{speech balloon}")
    # mysqldump --all-databases --single-transaction --host=db1 --port=3306 --user=root --password=pycon --protocol=tcp


def offset_backup_start() -> None:
    # to make sure dbs are up and running
    print(
        f"Waiting {INITIAL_OFFSET} seconds before starting backups...\N{sleeping face}"
    )
    time.sleep(INITIAL_OFFSET)


def periodic_backup() -> None:
    backup_periodicity = int(sys.argv[1])

    offset_backup_start()

    while True:
        current_time = time.ctime()
        print(f"Backup time: {current_time} \N{stopwatch}")
        do_backup(current_time)
        time.sleep(backup_periodicity)


if __name__ == "__main__":
    periodic_backup()
