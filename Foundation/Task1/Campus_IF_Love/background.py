class character:
    talk_list1 = {"你是新来的吧？画画过吗？":["其实我更擅长写代码，但我愿意试试画画。", "画画？那种小孩子的东西我可没兴趣。"]}
    talk_list2 = {}
    talk_list3 = {}

    def __init__(self, name : str, role : str, appearance : str, personality : str, affinity : int):
        self.name = name
        self.role = role
        self.appearance = appearance
        self.personality = personality
        self.affinity = affinity
