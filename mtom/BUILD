python_test_utils(
    name="test_utils"
)

python_sources(
    sources=['*.py', '**/*.py',  "!**/test_*.py", "!**/conftest.py", '!conftest.py']
)

python_tests(
    name="mtom_tests",
    dependencies=["//:req", 'config'],
    sources=["**/tests/**/test_*.py"]
)
