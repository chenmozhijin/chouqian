import sqlite3


class Data:
    def __init__(self):
        self.db_version = 1
        self.cfg = {
            "draw_animation": True,
            "reduce_duplication": True,
            "groups_count": 7,
            "default_list": None
        }  # 配置数据
        self.cfg_keys = self.cfg.keys()
        self.cfg_boolkeys = [key for key, value in self.cfg.items() if isinstance(value, bool)]
        self.cfg_intkeys = [key for key, value in self.cfg.items() if isinstance(value, int)]
        self.cfg_strkeys = [key for key, value in self.cfg.items() if isinstance(value, str)]
        self.list_names = []
        self.islistsAvailable = False
        self.conn = sqlite3.connect('chouqiandata.db')
        self.init_db()
        self.read_lists()
        self.read_settings()

    def init_db(self):
        c = self.conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS db_info(version INTEGER)""")
        c.execute("""CREATE TABLE IF NOT EXISTS settings(
                      ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       item TEXT NOT NULL,
                      value INTEGER)""")
        c.execute("""CREATE TABLE IF NOT EXISTS lists(
                      ID INTEGER PRIMARY KEY AUTOINCREMENT,
                      list_name TEXT,
                      item TEXT)""")
        c.execute("""CREATE TABLE IF NOT EXISTS records(
                      ID INTEGER PRIMARY KEY AUTOINCREMENT,
                      list_name TEXT,
                      item TEXT,
                      time INTEGER)""")

    def read_settings(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM settings")
        for setting in c.fetchall():
            if setting[1] == "default_list" and setting[2] not in self.list_names:
                continue
            if setting[1] in self.cfg_boolkeys:
                if setting[2] == 1:
                    self.cfg[setting[1]] = True
                elif setting[2] == 0:
                    self.cfg[setting[1]] = False
                else:
                    raise ValueError(f"Invalid value for {setting[1]}")
            else:
                self.cfg[setting[1]] = setting[2]

    def write_settings(self, item: str, value):
        self.cfg[item] = value
        if value in [True, False]:
            value = 1 if value else 0
        c = self.conn.cursor()
        c.execute("SELECT * FROM settings WHERE item=?", (item,))
        if c.fetchone() is None:
            c.execute("INSERT INTO settings(item, value) VALUES (?, ?)", (item, value))
        else:
            c.execute("UPDATE settings SET value=? WHERE item=?", (value, item))
        self.conn.commit()

    def read_lists(self):
        """获取列表名字"""
        c = self.conn.cursor()
        c.execute("SELECT * FROM lists")
        for list_name in c.fetchall():
            if list_name[1] not in self.list_names:
                self.list_names.append(list_name[1])

    def read_list(self, list_name: str):
        """获取列表内容"""
        return_list = []
        c = self.conn.cursor()
        c.execute("SELECT * FROM lists WHERE list_name=?", (list_name,))
        for item in c.fetchall():
            return_list.append(item[2])
        return return_list

    def write_lists(self, lists: dict):
        """写入列表"""
        c = self.conn.cursor()
        # 清空列表数据
        self.list_names.clear()
        c.execute("DELETE FROM lists")
        self.conn.commit()
        # 写入列表
        for list_name, list_content in lists.items():
            for item in list_content:
                c.execute("INSERT INTO lists(list_name, item) VALUES (?, ?)", (list_name, item))
                if list_name not in self.list_names:
                    self.list_names.append(list_name)

        # 删除records表中不属于lists的项
        # 删除records表中list_name不属于self.list_names的项
        c.execute("DELETE FROM records WHERE list_name NOT IN ({})".format(','.join(['?'] * len(self.list_names))), tuple(self.list_names))
        for list_name in self.list_names:
            # 获取指定list_name的所有ID与item
            c.execute("SELECT id, item FROM records WHERE list_name=?", (list_name,))
            items = c.fetchall()
            # 检查item是否存在与lists[list_name]中,不存在则删除
            for item in items:
                if item[1] not in lists[list_name]:
                    c.execute("DELETE FROM records WHERE id=?", (item[0],))

        self.conn.commit()

    def read_records(self, list_name, start_time, end_time):
        """获取记录"""
        records = {}
        c = self.conn.cursor()
        # 使用SELECT语句查询指定列表在指定时间范围内每个item的个数
        if start_time and end_time:
            c.execute("SELECT item, COUNT(*) FROM records WHERE list_name=? AND time>=? AND time<=? GROUP BY item", (list_name, start_time, end_time))
        elif start_time:
            c.execute("SELECT item, COUNT(*) FROM records WHERE list_name=? AND time>=? GROUP BY item", (list_name, start_time))
        elif end_time:
            c.execute("SELECT item, COUNT(*) FROM records WHERE list_name=? AND time<=? GROUP BY item", (list_name, end_time))
        else:
            c.execute("SELECT item, COUNT(*) FROM records WHERE list_name=? GROUP BY item", (list_name,))
        for record in c.fetchall():
            records[record[0]] = {"count": record[1]}
        if list_name == "小组抽签":
            list_data = []
            for i in range(1, self.cfg["groups_count"] + 1):
                list_data.append("第" + str(i) + "组")
        else:
            list_data = self.read_list(list_name)
        for item in list_data:
            if item not in records:
                records[item] = {"count": 0}
        # 查询指定列表中每个item最后被抽到的时间
        c.execute("SELECT item, MAX(time) FROM records WHERE list_name=? GROUP BY item", (list_name,))
        for record in c.fetchall():
            records[record[0]]["last_time"] = record[1]
        for key, item in records.items():
            if "last_time" not in item:
                records[key]["last_time"] = None
        return records

    def read_last_records(self, list_name, num):
        """获取最近num条记录"""
        records = []
        c = self.conn.cursor()
        c.execute("SELECT item, time FROM records WHERE list_name=? ORDER BY time DESC LIMIT ?", (list_name, num))
        for record in c.fetchall():
            records.append(record[0])
        return records

    def write_record(self, list_name, item, time):
        """写入记录"""
        c = self.conn.cursor()
        c.execute("INSERT INTO records(list_name, item, time) VALUES (?, ?, ?)", (list_name, item, time))
        self.conn.commit()

    def del_group_record(self):
        group_list = []
        c = self.conn.cursor()
        for i in range(1, self.cfg["groups_count"] + 1):
            group_list.append("第" + str(i) + "组")
        c.execute("SELECT id, item FROM records WHERE list_name=?", ("小组抽签",))
        items = c.fetchall()
        for item in items:
            if item[1] not in group_list:
                c.execute("DELETE FROM records WHERE id=?", (item[0],))
