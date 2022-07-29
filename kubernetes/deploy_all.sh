#!/bin/bash
set -ex

/bin/bash deploy_backend.sh
/bin/bash deploy_frontend.sh
/bin/bash deploy_database.sh