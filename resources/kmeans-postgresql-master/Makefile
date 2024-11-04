# contrib/kmeans/Makefile

# Define the module name
MODULES = kmeans
# Set the extension to the module name
EXTENSION = $(MODULES)
# Define the extension version
EXTVERSION = 1.1.0
# Construct the SQL file name for the extension
EXTSQL = $(MODULES)--$(EXTVERSION).sql

# Specify the SQL file that is built from source
DATA_built = $(MODULES).sql
# Specify the SQL file for uninstalling the module
DATA = uninstall_$(MODULES).sql
# Specify the documentation file
DOCS = doc/$(MODULES).md
# Specify the regression tests directory
REGRESS = $(MODULES)

# Specify the input SQL file
SQL_IN = $(MODULES).sql.in
# Specify additional files to clean during make clean
EXTRA_CLEAN = sql/$(MODULES).sql expected/$(MODULES).out

# Determine if the PostgreSQL version supports extensions
USE_EXTENSION = $(shell pg_config --version | grep -qE " 8\.|9\.0" && echo no || echo yes)

# Conditional block that checks if extensions are supported
ifeq ($(USE_EXTENSION),yes)
all: $(EXTSQL)  # Default target depends on the extension SQL file

$(EXTSQL): $(EXTENSION).sql
	cp $< $@  # Copy the source SQL file to the target SQL file
DATA = $(EXTSQL)  # Set DATA to the extension SQL file
EXTRA_CLEAN += $(EXTSQL)  # Add the extension SQL file to the clean list
endif

# Define the path to the pg_config utility
PG_CONFIG = pg_config
# Use pg_config to determine the path to the PostgreSQL extensions makefile
PGXS := $(shell $(PG_CONFIG) --pgxs)
# Include the PostgreSQL extensions makefile
include $(PGXS)
