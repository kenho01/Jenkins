# Python Fire is a libary for automatically generating CLI from simple python codes
import fire

def hello(name="World"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)