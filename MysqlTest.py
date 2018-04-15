
# coding=UTF-8
'''
本次测试采用的是MySqldb模块， python环境：2.7.8，见不少网友说python3 不再支持该模块，所以使用python3的可用pymysql代替，两者的操作并没有太大区别。
'''
import MySQLdb


def testInsert(Cursor):
    try:
        # test后无具体字段，表示添加全部字段，等价于test(id,name,age,sex),()中为全部字段名
        # sql = 'insert into test values(2,"小明",19,"男")' #添加单条记录
        # 非添加所有字段时，要将所有添加字段名写上
        #sql = 'insert into test(id,name,age) values(3,"小虎",17)'
        # 添加多条记录方法
        ids = [1, 2, 3, 4]
        names = ['小白', '小黄', '小花', '小草']
        ages = [12, 13, 14, 15]
        sexs = ['男', '男', '女', '女']
        for i in range(4):
            #             sql = 'insert into test values(' +str(ids[i]) + ',"' + names[i] + '",' + str(ages[i]) + ',"' + sex[i] + '"'')'            
            #             sql = 'insert into test values({},"{}",{},"{}")'.format(ids[i], names[i], ages[i], sexs[i])          
            sql = 'insert into test values(%d,"%s",%d,"%s")' % (ids[i], names[i], ages[i], sexs[i])
            print sql
            Cursor.execute(sql)
            print '添加成功'
    except Exception, e:
        print '添加失败', e


def testDelete(Cursor, id):
    try:
        # sql = 'delete from test where id=4' #给定id具体值
        sql = 'delete from test where id =%d' % id  # id值由外面传入
        Cursor.execute(sql)
        print '删除成功'
    except Exception, e:
        print '发生异常:', e


def testUpdate(Cursor, name, id):
    try:
        sql = 'update test set name="更改",age=3,sex="未知" where id=2'  # 直接给值
        sql = 'update test set name="{}" where id={}'.format(name, id)  # 由外部传值
        Cursor.execute(sql)
        print '修改成功'
    except Exception, e:
        print '发生异常:', e


def testSelect(cursor, id):
    try:
        # sql = 'select * from test where id=2'  # 查询单条记录，直接给值
        sql = 'select * from test where id=%d' % id  # 查询单条记录,外部传值
        # sql = 'select * from test'  # 查询所有记录
        cursor.execute(sql)
        data = cursor.fetchone()  # 从结果集中取得单条数据
        print type(data)  # 验证返回类型
        for d in data:
            print d,

#         data = cursor.fetchall()  # 获取结果集的所有数据
#         print type(data)  # 验证返回类型
#         for r in data: #先取得每条记录的元组对象
#             for d in r:
#                 print d,

        # 在con.cursor()中加上参数 MySQLdb.cursors.DictCursor后,查询返回一个字典对象，可通过字段名取值
#         data = cursor.fetchall()
#         print type(data)  # 验证返回类型
#         print '按字段名取值测试成功:'
#         for d in data:
#             print 'id:', d['id'], 'name:', d['name'], 'age:', d['age'], 'sex:',
#             d['sex']
    except Exception, e:
        print '发生异常:', e


def testCounts(cursor):
    try:
        sql = 'select count(*) from test'
        cursor.execute(sql)
        length = cursor.fetchone()
        print length[0]
    except Exception, e:
        print '发生异常', e


if __name__ == '__main__':
    try:
        con = MySQLdb.connect('localhost', 'root', 'root', 'python', charset='utf8')
        # 加入编码，防止表中乱码，切记，是 utf8 ！！！不是utf-8!
        cursor = con.cursor()  # 查询返回一个元组对象
        # cursor = con.cursor(MySQLdb.cursors.DictCursor)  # 加上该参数后，查询返回一个字典对象
        # testInsert(cursor)  # 测试插入方法
        # testDelete(cursor, 1)  # 测试删除方法
        # testUpdate(cursor, '我又改名了', 2)  # 测试修改方法
        # testSelect(cursor, 2)  # 测试查询方法
        testCounts(cursor)  # 测试获取记录数方法
        con.commit()  # 记得提交，不然没有效果
    except Exception, e:
        print '连接数据库失败', e
        con.rollback()  # 错误时回滚
    finally:
        cursor.close()
        con.close()  # 关闭数据库连接
