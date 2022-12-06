## **Restore the infrastructure**
`ansible-playbook infra.yaml` on local machine.

## **Restore MySQL data from the backup:**
Run on desired mysql machine from mysql servers group.
1. `sudo -u backup duplicity --no-encryption restore rsync://binary0ne@backup/mysql /home/backup/restore/mysql`
2. `sudo mysql agama < /home/backup/restore/mysql/agama.sql`

Main page of agama should indicate restored records.

## **Restore telegraf db**
Run on desired influxdb machine from influxdb group.
1. `sudo -u backup duplicity --no-encryption restore rsync://binary0ne@backup/influxdb /home/backup/restore/influxdb`
2. `sudo service telegraf stop`
3. `sudo influx -execute 'DROP DATABASE telegraf'`
4. `sudo influxd restore -portable -database telegraf /home/backup/restore/influxdb/`
5. `sudo service telegraf start`

To verify the correct restoration run: `sudo influx -execute 'SELECT first(*) FROM syslog' -database='telegraf'`
Check the time, if this record is earlier then the EVENT, then restoration is correct.

