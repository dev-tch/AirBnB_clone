#!/usr/bin/python3
"""
module for purpose to test some behavior of class console
"""
from console import HBNBCommand
from unittest.mock import create_autospec
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from io import StringIO
import unittest
import sys


class TestConsole(unittest.TestCase):
    """implement class TestConsole"""

    def SetUp(self):
        """setting the mock_stdin and mock_stdout"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def test_Console(self, server=None):
        """" instantiates Console for HBNBCommand """
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_Quit(self):
        """tests quit method """

        cmd = HBNBCommand()
        self.assertRaises(SystemExit, quit)

    def test_docs(self):
        """tests docstrings"""
        self.assertTrue(HBNBCommand.__doc__)
        self.assertTrue(HBNBCommand.do_quit.__doc__)
        self.assertTrue(HBNBCommand.emptyline.__doc__)
        self.assertTrue(HBNBCommand.do_EOF.__doc__)
        self.assertTrue(HBNBCommand.do_help.__doc__)
        self.assertTrue(HBNBCommand.do_create.__doc__)
        self.assertTrue(HBNBCommand.do_show.__doc__)
        self.assertTrue(HBNBCommand.do_destroy.__doc__)
        self.assertTrue(HBNBCommand.do_all.__doc__)
        self.assertTrue(HBNBCommand.do_update.__doc__)
        self.assertTrue(HBNBCommand.do_count.__doc__)
        self.assertTrue(HBNBCommand.default.__doc__)

    """Test command interpreter outputs"""
    def test_emptyline(self):
        """test blank command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), '')

    def test_create(self):
        """test invalid syntax of command create"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create SomeClass")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())

    def test_show_id(self):
        """ test missing id of command show  """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show BaseModel')
            self.assertTrue(f.getvalue() == "** instance id missing **\n")

    def test_destroy_empty(self):
        """test missing class arg for cmd destroy """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy')
            self.assertTrue(f.getvalue() == "** class name missing **\n")

    def test_class_exist(self):
        """test class name valid and other not valid """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all NotFoundClass')
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")

    def test_all(self):
        """test cmd all"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all')
            self.assertTrue(len(f.getvalue()) > 0)

    def test_update(self):
        """test update cmd """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update BaseModel')
            self.assertTrue(f.getvalue() == "** instance id missing **\n")

    def test_alt_all(self):
        """test custom cmd : [class].all """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.all()')
            self.assertTrue(len(f.getvalue()) > 0)

    def test_count(self):
        """test cmd : [class].count """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.count()')
            self.assertTrue(int(f.getvalue()) >= 0)
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create User')
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('User.count()')
            self.assertTrue(int(v.getvalue()) >= 1)

    def test_user(self):
        """test some commands on User Object"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            printed_user_id = f.getvalue()
            self.assertTrue(printed_user_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show User')
            self.assertTrue(f.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all User')
            self.assertTrue(f.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            cmd_up = "update User " + printed_user_id + " name TCH"
            print(cmd_up)
            HBNBCommand().onecmd(cmd_up)
            HBNBCommand().onecmd("show User " + printed_user_id)
            self.assertTrue("TCH" in v.getvalue())
            HBNBCommand().onecmd("destroy User " + printed_user_id)
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("show User "+printed_user_id)
            self.assertEqual(v.getvalue(), "** no instance found **\n")


if __name__ == '__main__':
    unittest.main()
