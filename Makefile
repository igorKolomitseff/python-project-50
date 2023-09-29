install:
		poetry install

patch:
		poetry version patch

minor:
		poetry version minor

major:
		poetry version major

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

package-reinstall:
		python3 -m pip install --user --force-reinstall dist/*.whl

lint:
		poetry run flake8 gendiff

test:
		poetry run pytest
