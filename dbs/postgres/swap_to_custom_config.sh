#!/usr/bin/env bash

cat /tmp/custom_config.conf > /var/lib/postgresql/data/postgresql.conf
cat /tmp/custom_pg_hba.conf > /var/lib/postgresql/data/pg_hba.conf
