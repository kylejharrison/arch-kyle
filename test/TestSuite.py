__author__ = 'Kyle Harrison'

import unittest
import subprocess
import paramiko

VAGRANT_EXIT_CODE = None

def run_process(run_command):
    process = subprocess.Popen(run_command, cwd='..', stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    out, err = process.communicate()
    exit_code = process.returncode
    return out, err, exit_code


def setUpModule():
    """Launch Vagrant VM"""
    global VAGRANT_EXIT_CODE
    command = ['vagrant', 'up']
    out, err, VAGRANT_EXIT_CODE = run_process(command)
    print 'stdout: ' + out
    print 'stderr: ' + err



def tearDownModule():
    """Destroy Vagrant VM"""
    command = ['vagrant', 'destroy', '-f']
    out, err, exit_code = run_process(command)
    print 'stdout: ' + out
    print 'stderr: ' + err


class BasicTests(unittest.TestCase):

    def setUp(self):
        self.vm_client = paramiko.SSHClient()
        self.vm_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.vm_client.connect('localhost', port=2222, username='vagrant', password='vagrant')
        except (paramiko.BadAuthenticationType, paramiko.AuthenticationException, paramiko.SSHException) as e:
            raise e

    def tearDown(self):
        self.vm_client.close()

    def test_vagrant_up_exit_code_is_0(self):
        self.assertEquals(VAGRANT_EXIT_CODE, 0)

    def test_can_ssh_to_vm_and_run_a_simple_command(self):
        stdin, stdout, stderr = self.vm_client.exec_command('echo ok')
        self.assertRegexpMatches(stdout.read(), '^ok', msg='stdout: ' + stdout.read())
        self.assertEquals(stdout.channel.recv_exit_status(), 0)


if __name__ == '__main__':
    unittest.main()




