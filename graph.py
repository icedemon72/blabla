class Graph:
    def __init__(self, number, id, connected, max):
        self.number = number # The number of nodes the GraphInstance's node connects to
        self.id = id      # The node's relative id (0 -> 9)
        self.connected = connected 
        self.max = max

    def addNode(self, node):
        self.connected.append(node)

    def elemInConnected(self, e):
        return e in self.connected

    def getRes(self):
        return(self.connected)
    
    def getResArr(self):
        arr = [0 for x in range(self.max)]
        for i in self.connected:
            arr[i - 1] = 1
        return arr

    def getResString(self):
        arr = self.getResArr()
        string = ""
        for i in arr:
            string += (f' {i} ')
        return string

