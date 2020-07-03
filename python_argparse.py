import argparse

parser = argparse.ArgumentParser(description='Enter server name ...')


parser.add_argument("--ip")
ip = parser.parse_args().ip

print(ip)
