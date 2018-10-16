import sys
import importlib
importlib.reload(sys)
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

# 解析PDF保存到txt文件中
path = r'./test2.pdf'
def parse():
    fp = open(path,'rb') #二进制读模式打开
    #创建pdf文档分析器
    praser = PDFParser(fp)
    #创建一个pdf文档
    doc = PDFDocument()

    #连接分析器 与文档对象
    praser.set_document(doc)
    doc.set_parser(praser)

    #提供初始化密码，没有密码则创建一个空字符串
    doc.initialize()

    #检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        #创建PDF资源管理器 共享资源
        rsrcmgr = PDFResourceManager()
        #创建PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr,laparams=laparams)
        #创建PDF解释器
        interpreter = PDFPageInterpreter(rsrcmgr,device)

        #循环遍历，每次处理一Page内容
        for page in doc.get_pages(): #doc.get_pages()获取pag列表
            interpreter.process_page(page)
            #接受页面的LTPage对象,这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
            layout = device.get_result()
            for x in layout:
                    with open(r'./2.txt','a',encoding="UTF-8") as f:
                        if (isinstance(x, LTTextBoxHorizontal)):
                            results = x.get_text()
                            print(results)
                            f.write(results+'\n')
# if __name == '__main__':
parse()

