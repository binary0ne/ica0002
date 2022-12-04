## **Database servers**

The data is exported by mysql exporter and uploaded to the backup servers.

## **InfluxDB**

Data from monitoring is uploaded to database backup servers.

## **Ansible repository**

Backup for ansible repository is done through git. 
It is stored on github and additionally local branch is stored on the computer of an infrastructure engineer.
When some changes are done it is pushed to github.

## **Backup coverage**
Backup is covering the structure of this project, as well as data inserted to databases, except the data from prometheus.

## **RPO (recovery point objective)**
RPO is to keep the ability to restore the state of a data within 12 hours.

## **Versioning and retention**
Ansible GIT is stored from day 0 and till the last changes. Every change is stored as git commit and allows to reproduce the whole infrastructure from the scratch
Databases are backed up every 8 hours, at 8am, 16pm, and 12am (00:00).

## **Usability checks**
After backup is done the backups are tested on test server within the same infrastructure, if automatic tests are failed it is trying to make one another backup automatically and if test fails then, the system administrator is get informed


## **Restoration criteria**
Restoration should be done in the case of the Event. Event is described in the corporate policy. Event is classified by type and these types affect the strategy of restoration

## **RTO**
RTO is related to policy that the service should be available at least 90% of time. RTO in case of an Event should not exceed 2 hours.