# Assuming user logged in to Docker Hub
#   and docker / docker-compose is installed.
# Also 'export DATABASE_URI=<remote database credentials>'
# Bypasses:
#          DOCKER_HUB_CREDS = credentials('DOCKER_HUB_CREDS')
#          DATABASE_URI = credentials("DATABASE_URI")
echo "Test stage"

echo "create virtual environment"
python3 -m venv venv
source venv/bin/activate

echo "Install pytest"
pip3 install pytest pytest-cov flask_testing
pip3 install -r frontend/requirements.txt
pip3 install -r backend/requirements.txt

mkdir test_reports

echo "Run pyest"
python3 -m pytest frontend \
    --cov=frontend/application \
    --cov-report term-missing \
    --cov-report xml:test_reports/frontend_coverage.xml \
    --junitxml=test_reports/frontend_junit_report.xml

python3 -m pytest backend \
    --cov=backend/application \
    --cov-report term-missing \
    --cov-report xml:test_reports/backend_coverage.xml \
    --junitxml=test_reports/backend_junit_report.xml

deactivate

rm -rf venv

# Now build docker, push, deploy
