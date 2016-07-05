#coding:utf8
import MySQLdb

class HtmlOutputer(object):
    """docstring for HtmlOutputer"""
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
    
    #输出为html
    def output_html(self):
        fout = open("output.html",'w')

        fout.write("<html>")
        
        fout.write('<meta charset="UTF-8">')
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'].encode('utf-8'))
            fout.write("<td>%s</td>"%data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()
    
    #输出到数据库
    def output_db(self):
        
        sql = ''
        
        conn = MySQLdb.connect(
                               host = 'localhost',
                               port = 3306,
                               user = 'root',
                               passwd = '123456',
                               db = 'test',
                               charset = 'utf8'
                               )
        cur = conn.cursor()
        
        id = 0
        
        for data in self.datas:            
            cur.execute(
                        'insert into practice values(%s, %s, %s, %s)'
                        ,(id, 
                          data['url'], 
                          data['title'].encode('utf-8'), 
                          data['summary'].encode('utf-8')
                        )
                        )
            id += 1
        
        print 'output finished!'
        
        cur.close()
        conn.commit()
        conn.close()
    
    #查询现有数据库中的最大id    
#     def getId(self):
#         sql = 'select max(id) from practice'
#         cur.execute(sql)
#         row = cur.fetchone()
#         id = row[0] + 1
        
        
        
        
        
        