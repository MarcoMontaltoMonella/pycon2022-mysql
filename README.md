![Meta PyCon Banner](https://github.com/MarcoMontaltoMonella/pycon2022-mysql/blob/main/meta-pycon-header-transparent.png#gh-light-mode-only)
![Meta PyCon Banner](https://github.com/MarcoMontaltoMonella/pycon2022-mysql/blob/main/meta-pycon-header-dark.png#gh-dark-mode-only)

![Discord](https://img.shields.io/discord/964334241875914792?label=Discord%20Server&logo=Discord&logoColor=%235865F2&style=plastic) | ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/_/python/3.8?color=3294DF&label=Python%203.8&logo=Docker&logoColor=232496ED&style=plastic) ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/mysql/mysql-server/8.0.28?color=3294DF&label=MySQL%208&logo=Docker&logoColor=232496ED&style=plastic)

Learn how Meta scaled MySQL automation and fleet management using Python and how you can reuse similar design and techniques to scale your DBMS.

As [Production Engineers](https://engineering.fb.com/category/production-engineering/) at Meta, we strive to build and maintain our production services *reliable*, *scalable*, *performant*, and *secure*.

How Python has been leveraged to automate tasks, such as replication lag monitoring, replica promotion, and backup and restore, to name a few that in the past would have been missing or manually executed by DBAs.

The workshop will have follow-along examples to give you insights and make you learn skills you could reuse at your company.

## Prerequisites 🚚
1. Install Docker [[MacOS](https://runnable.com/docker/install-docker-on-macos)] [[Linux](https://runnable.com/docker/install-docker-on-linux)]
2. Make sure you're able to run the followings (*version I'm using*):
   1. `docker --version` (*Docker version 20.10.13, build a224086*)
   2. `docker-compose --version` (*Docker Compose version v2.3.3*)
3. Join the Discord channel for communication between us by following this link: https://fb.me/pycon22-mysql-discord
   1. Troubleshooting channel: [here](https://discord.com/channels/964334241875914792/964589394751283240)

## Get started 🚀
1. Clone this repo (`git clone git@github.com:MarcoMontaltoMonella/pycon2022-mysql.git`)
   1. The initial state of the system can be seen in [here](https://github.com/MarcoMontaltoMonella/pycon2022-mysql/blob/main/initial-state-diagram.png)
2. From within the repo, run `docker-compose up --build`
   1. You should be seeing a front-end page at http://0.0.0.0:8000
3. Follow along the workshop, where we will cover the following (*#Discord channel*):
   1. **Automating periodic backups** (*[#ex1-backup](https://discord.com/channels/964334241875914792/964589613593272361)*)
   2. **Automating healthcheck monitoring** (*[#ex2-healthcheck](https://discord.com/channels/964334241875914792/965504119148273685)*)

### Automating periodic backups 🗳
Discord channel: (*[#ex1-backup](https://discord.com/channels/964334241875914792/964589613593272361)*)

In this first example we will setup a job for creating backups of our MySQL databases.
The high level idea is to have an external agent that will periodically run the following steps:
- Run `mysqldump` against our databases
- Compress the generated backup
  - useful lib: [zstd](https://pypi.org/project/zstd/)
- Upload the backup to a storage location

### Automating healthcheck monitoring 🚨
Discord channel: (*[#ex2-healthcheck](https://discord.com/channels/964334241875914792/965504119148273685)*)

This second example will see us creating a job for periodically check for any sign of database corruption, and notify us in case that happens.
The high level idea for this code is the follow:
- Run `mysqlcheck` against our databases
- Analyze the output
- Alert us if database is not healthy
  - useful lib: [notifiers](https://pypi.org/project/notifiers/)


## Thank you for attending 🙏

![Meta PyCon Banner](https://github.com/MarcoMontaltoMonella/pycon2022-mysql/blob/main/meta-pycon-banner-transparent.png#gh-light-mode-only)
![Meta PyCon Banner](https://github.com/MarcoMontaltoMonella/pycon2022-mysql/blob/main/meta-pycon-banner-dark.png#gh-dark-mode-only)
