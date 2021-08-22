CSC CKAN
========

The built is based on CKAN 2.9.3. It enables ylchan87/ckanext-landdbcustomize and chunlaw/ckanext-oauth2.

# Preparation
Apply [Google OAuth2](https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred) in Google Cloud Console.
```
// Replace registered <CLIENT_ID> and <CLIENT_SECRET>
vi production.ini.patch 

// DANGEROUS, your development work may be lost 
docker volume rm docker_ckan_home docker_ckan_config
```

# Launch instance
```
cd contril/docker
docker-compose up -d --build
# or for dev
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build
```

Test your CKAN instance in localhost:5000

# Note
For OAuth2 testing, uncomment 'export OAUTHLIB_INSECURE_TRANSPORT=True' in `contril/docker/ckan-entrypoint.sh` if no https is possible.
