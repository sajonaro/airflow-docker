FROM postgres:14.5

#seed DB
COPY init.sql /docker-entrypoint-initdb.d/books_shop_schema.sql

# Add custom config files
COPY custom_config.conf  /tmp/custom_config.conf
COPY custom_pg_hba.conf  /tmp/custom_pg_hba.conf

# Add the '_' symbol to make it run before any other script in the directory
COPY swap_to_custom_config.sh /docker-entrypoint-initdb.d/_swap_to_custom_config.sh


