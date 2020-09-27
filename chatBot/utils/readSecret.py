class reader():
    def readSecret(self,path):
        secret = {}
        with open(path,'r') as f:
            for line in f.readlines():
                  splitLine = line.split("=")
                  if len(splitLine) >= 2:
                      key = splitLine[0].strip()
                      value = "=".join(splitLine[1:]).strip()
                      secret[key] = value
        return secret
