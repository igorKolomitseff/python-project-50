install:
		poetry install

patch:
		poetry version patch

minor:
		poetry version minor

major:
		poetry version major

build: check
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

package-reinstall:
		python3 -m pip install --user --force-reinstall dist/*.whl

lint:
		poetry run flake8

test:
		poetry run pytest

test-coverage:
		poetry run pytest --cov=gendiff --cov-report xml

selfcheck:
		poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build