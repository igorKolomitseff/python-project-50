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
