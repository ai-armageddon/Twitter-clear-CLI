from os.path import exists

# value_if_true if condition else value_if_false
env = 'development' if exists('./temp_creds.py') else 'production'

# dev vs. deploy env creds
def get_creds(env=env, msg=True):
  if env == 'development':
    print('Running in: ', env) if msg == True else ""
    return env
  elif env == 'production':
    print('Running in: ', env) if msg == True else ""
    return env
