python_test_utils(
    name="test_utils"
)

python_sources()

python_tests(
    name="tests",
    dependencies=[
        "//:req",
        "config:config",  # For settings.py.
    ],
    sources=[
        "**/tests/**/test_*.py"
    ]
)
