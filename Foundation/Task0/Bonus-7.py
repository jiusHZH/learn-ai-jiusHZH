class good:
    def init(self, no, name, price, total):
        self.no = no
        self.name = name
        self.price = price
        self.total = total
        self.remain = total

    def display(self):
        print("商品序号：", self.no)
        print("商品名：  ", self.name)
        print("单价：    ", self.price)
        print("总数量：  ", self.total)
        print("剩余数量：", self.remain)

    def income(self):
        sold = self.total - self.remain
        return sold * self.price

    def setdata(self, name=None, price=None, total=None, remain=None):
        if name:
            self.name = name
        if price:
            self.price = price
        if total:
            self.total = total
        if remain:
            self.remain = remain

g = good()
g.init(1, "钢笔", 15.5, 100)
g.display()
print("当前销售额：", g.income())
print()
g.setdata(remain=70)
g.display()
print("当前销售额", g.income())
