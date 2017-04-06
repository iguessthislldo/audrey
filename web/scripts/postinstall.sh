mkdir -p lib

# jQuery
cp node_modules/jquery/dist/jquery.min.js lib

# Bootstrap
cp -r node_modules/bootstrap/dist lib/bootstrap

# another-rest-client
cp node_modules/another-rest-client/rest-client.min.js lib

# fontawesome
mkdir -p lib/font-awesome/css
cp -r node_modules/font-awesome/fonts lib/font-awesome
cp -r node_modules/font-awesome/css/font-awesome.min.css lib/font-awesome/css

# select
mkdir -p lib/select
cp node_modules/select2/dist/js/select2.full.min.js lib/select
cp node_modules/select2/dist/css/select2.min.css lib/select
