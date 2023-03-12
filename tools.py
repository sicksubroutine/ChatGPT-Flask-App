import string, random, uuid


def random_token() -> str:
  ran_token = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
  return ran_token

def get_IP_Address(request):
  ip_address = request.headers.get('X-Forwarded-For', '').split(',')[0].strip()
  return ip_address

def uuid_func():
  device_id = f"{uuid.uuid1()}"
  return device_id
