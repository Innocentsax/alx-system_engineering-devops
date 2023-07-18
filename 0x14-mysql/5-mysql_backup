#!/usr/bin/env bash
# This script generates a MySQL dump and creates a compressed archive  of it

mysqldump -uroot -p"$1" --all-databases > backup.sql
tar -czf $(date +%d-%m-%Y).tar.gz backup.sql
