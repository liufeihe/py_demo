import yaml

def parseYml():
  path = './test.yml'
  f = open(path)
  c = yaml.load(f)
  print(c['types'])
  print(c['scene_tc_map'][10001])

def writeYml():
  data = {
    "name": '储物货柜配置',
    "run": True,
    "list": [
      {
        "id": 1,
        "tc": 4,
      },
      {
        "id": 2,
        "tc": 4,
      }
    ]
  }
  f = open('./test_w.yml', 'w')
  yaml.safe_dump(data, f, encoding='utf-8',allow_unicode=True)

  f = open('./test_w.yml')
  data2 = yaml.safe_load(f)
  print(data2.get('list'))

class Test:
  def __init__(self, a):
    self.a = a

if __name__ == "__main__":
  # tList = []
  # tList.append(Test(2))
  # tList.append(Test(3))
  # t = None
  # for _, v in enumerate(tList):
  #   if v.a==2:
  #     t = v
  #     break
  # # t = tList[0]
  # print(t.a)
  # t.a = 3
  # print(t.a)
  # print(tList[0].a)
  # parseYml()
  writeYml()