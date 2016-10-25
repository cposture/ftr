#!/usr/bin/env python
#coding=utf-8
import os, sys
import traceback
import pexpect

g_ip = []
g_passwd = ''
g_cmd = 'scp'
g_transfile = ''
g_path = ''

# ��������м������ӡ��ʾ��Ϣ���˳�
def exit_with_usage():
    print globals()['__doc__']
    os._exit(1)


def main():
    for ip in g_ip:
       remote = 'root@' + ip
       command = g_cmd + ' -rp ' + g_transfile + ' ' + remote + ':' + g_path
       print command
       # Ϊ��������������������һ�� pexpect �� spawn ���ӳ���Ķ���.
       p = pexpect.spawn(command)
       p.logfile_read = sys.stdout
       #i = p.expect(remote+"'s password:")
       i = p.expect(["^The authenticity of host.+", "^root", ".+"])
       print i
       if i == 1:
           p.sendline(g_passwd)
           p.expect(pexpect.EOF)
       else:
           p.sendline('yes')
           p.sendline(g_passwd)
           p.expect(pexpect.EOF)
    return 0

if __name__ == "__main__":
    try:
        main()
    except SystemExit, e:
        raise e
    except Exception, e:
        print "ERROR"
        print str(e)
        traceback.print_exc()
        os._exit(1)
