from unittest.mock import patch
from io import StringIO
import pytest
from backend import console

# Mocking the SQLAlchemy session for testing
@patch("console.db_session")
def test_create(mock_db_session):
    console = QuickSearchConsole()
    mock_db_session.add.return_value = None
    mock_db_session.commit.return_value = None
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("create Nanny")
    assert output.getvalue() == "New Nanny created with ID: None\n"

@patch("console.db_session")
def test_show(mock_db_session):
    console = QuickSearchConsole()
    instance = "Test Nanny"
    mock_db_session.query.return_value.filter_by.return_value.first.return_value = instance
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("show Nanny 1")
    assert output.getvalue() == instance + "\n"

@patch("console.db_session")
def test_all(mock_db_session):
    console = QuickSearchConsole()
    instances = ["Nanny 1", "Nanny 2", "Nanny 3"]
    mock_db_session.query.return_value.all.return_value = instances
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("all Nanny")
    assert output.getvalue() == str(instances) + "\n"

@patch("console.db_session")
def test_destroy(mock_db_session):
    console = QuickSearchConsole()
    instance = "Nanny 1"
    mock_db_session.query.return_value.filter_by.return_value.first.return_value = instance
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("destroy Nanny 1")
    assert output.getvalue() == "Nanny instance 1 deleted successfully\n"

@patch("console.db_session")
def test_update(mock_db_session):
    console = QuickSearchConsole()
    instance = "Nanny 1"
    mock_db_session.query.return_value.filter_by.return_value.first.return_value = instance
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("update Nanny 1 title 'Updated Title'")
    assert output.getvalue() == "title updated successfully for Nanny instance 1\n"

@patch("console.db_session")
def test_invalid_class_name(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("create InvalidClass")
    assert "*** Unknown class name ***" in output.getvalue()

@patch("console.db_session")
def test_emptyline(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("")  # Enter an empty line
    assert output.getvalue() == ""

@patch("console.db_session")
def test_quit(mock_db_session):
    console = QuickSearchConsole()
    assert console.do_quit("")  # Simulate quitting the console

@patch("console.db_session")
def test_EOF(mock_db_session):
    console = QuickSearchConsole()
    assert console.do_EOF("")  # Simulate reaching end of file (Ctrl+D)

@patch("console.db_session")
def test_default_invalid_syntax(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.default("invalid_syntax")
    assert "*** Unknown syntax: missing command ***" in output.getvalue()

@patch("console.db_session")
def test_default_invalid_class_name(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.default("InvalidClass")
    assert "*** Unknown syntax: invalid class name ***" in output.getvalue()

@patch("console.db_session")
def test_default_invalid_command(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.default("Nanny invalid_command")
    assert "*** Unknown syntax: invalid command ***" in output.getvalue()

# Additional test cases
@patch("console.db_session")
def test_invalid_instance_id(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("show Nanny")
    assert "*** Usage: show <class name> <instance id> ***" in output.getvalue()

@patch("console.db_session")
def test_update_no_value(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("update Nanny 1 title")
    assert "*** Usage: update <class name> <instance id> <attribute> <value> ***" in output.getvalue()

@patch("console.db_session")
def test_invalid_update(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("update Nanny 1 invalid_attribute value")
    assert "*** Unknown syntax: invalid command ***" in output.getvalue()

@patch("console.db_session")
def test_invalid_destroy(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("destroy Nanny")
    assert "*** Usage: destroy <class name> <instance id> ***" in output.getvalue()

@patch("console.db_session")
def test_invalid_show(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("show")
    assert "*** Usage: show <class name> <instance id> ***" in output.getvalue()

@patch("console.db_session")
def test_invalid_all(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("all")
    assert "*** Unknown class name ***" in output.getvalue()

