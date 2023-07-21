import pymysql
"""
PyMySQL==0.9.3

安装命令 pip install PyMySQL==0.9.3
"""

#配置信息
dbinfo = {
    "host":"124.70.221.221",
    "user":"root",
    "password":"yoyo123456",
    "port":3309,
    "database":"apps"
}

class DbConnet():

    def __init__(self, dbinfo=dbinfo):
        self.db = pymysql.connect(cursorclass=pymysql.cursors.DictCursor,
                        **dbinfo,)

        self.cursor = self.db.cursor()

    """  查询  """
    def select(self, sql):
        #查询数据
        #sql = '查询语句'

        self.cursor.execute(sql)

        result = self.cursor.fetchall()
        return result

    """ 新增、修改、删除  """
    def execute(self, sql2):
        # 修改数据
        # sql2 = '修改语句'

        try:
            self.cursor.execute(sql2)
            print("成功")
            self.db.commit()
            rr = self.cursor.fetchall()
            return rr
        except:
            # 捕获异常 回滚
            self.db.rollback()

    def close(self):
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
        db = DbConnet(dbinfo)

        ## 查询
        sql1 = "SELECT * from apiapp_goods WHERE id=2"
        result = db.select(sql1)
        print(result)

        ##修改
        sql2 = 'UPDATE apiapp_goods set goodsname="《selenium》" WHERE id=12;'
        db.execute(sql2)

        # 更新后查询
        sql = "SELECT * from apiapp_goods WHERE id=12"
        result = db.select(sql)
        print(result)

        # 调用关闭游标
        db.close()
