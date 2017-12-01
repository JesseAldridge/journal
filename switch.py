import glob, getpass, os, subprocess

def switch(should_unlock):
  in_dir = 'decrypted'
  out_dir = 'encrypted'

  if should_unlock:
    in_dir, out_dir = out_dir, in_dir

  if not os.path.exists(out_dir):
    os.mkdir(out_dir)

  if not os.path.exists(in_dir):
    os.mkdir(in_dir)

  password = getpass.getpass('Enter hash password:')

  for in_path in glob.glob('{}/*.txt'.format(in_dir)):
    out_path = in_path.replace(in_dir, out_dir, 1)

    print 'in_path:', in_path
    print 'out_path:', out_path

    encrypt_command = [
      'openssl', 'enc', '-in', in_path, '-out', out_path, '-{}'.format(out_dir[0]), '-aes256',
      '-pass', 'pass:{}'.format(password)
    ]
    subprocess.call(encrypt_command)
