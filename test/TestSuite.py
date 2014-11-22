__author__ = 'Kyle Harrison'

import unittest
import subprocess

def setUpModule():
    """Launch Vagrant VM"""
    vagrant_process = subprocess.Popen(['vagrant', 'up'], cwd='../', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = vagrant_process.communicate()
    print 'stdout: ' + out
    print 'stderr: ' + err

def tearDownModule():
    """Destroy Vagrant VM"""
    vagrant_process = subprocess.Popen(['vagrant', 'destroy', '-f'], cwd='../', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = vagrant_process.communicate()
    print 'stdout: ' + out
    print 'stderr: ' + err


class BasicTests(unittest.TestCase):

    def test_can_ssh_to_vm(self):
        print 'test'


if __name__ == '__main__':
    unittest.main()


