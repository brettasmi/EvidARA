#! /bin/bash
IA_APP_ENV=$IA_APP_ENV \
PSEV_API_KEY=$PSEV_API_KEY \
NEO4J_SPOKE_USER=$NEO4J_SPOKE_USER \
NEO4J_SPOKE_PASSWORD=$NEO4J_SPOKE_PASSWORD \
NEO4J_SPOKE_URI=$NEO4J_SPOKE_URI \
docker-compose up web
