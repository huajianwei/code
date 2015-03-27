__author__ = 'huajw'
#coding = utf-8

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


    def print_score(self):
        print '%s: %s' % (self.name, self.score)


    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "C"
        else:
            return "Unpassed"

    def Run(self):
        print "Student is running"


class TiyuSheng(Student):
    def Run(self):
        print  "TiyuSheng run faster than others "
class WuDaoSheng(Student):
    def Run(self):
        print  " wudaosheng run not faster than others "

bart = Student('Bart Simpson', 90)

#bart.print_score()
#print bart.get_grade()
#print bart.score
lisa = Student('Lisa Simpson', 87)
print lisa.score
print lisa.Run()
xiaowang = TiyuSheng("liujia", 59.5 )

xiaowang.Run()
lei = WuDaoSheng("xiaolei",88)
lei.Run()


#多态,在函数中定义一个方法,当我们在父类中修改后,在子类中,也会改变.
#对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，
# 就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，
# 由运行时该对象的确切类型决定，这就是多态真正的威力：
# 调用方只管调用，不管细节，而当我们新增一种Animal的子类时，
# 只要确保run()方法编写正确，不用管原来的代码是如何调用的。
# 这就是著名的“开闭”原则：这样就不必重零做起，子类只需要新增自己特有的方法，
# 也可以把父类不适合的方法覆盖重写；在调用类实例方法的时候，尽量把变量视作父类类型

def runtwice(Student):
    Student.Run()
    Student.Run()

lisa.Run()

runtwice(lisa)

xiaowang.Run()
runtwice(xiaowang)

lei.Run()

runtwice(lei)

#获取对象的信息,我们来判断对象类型，使用type()函数：
# 基本类型,变量指向类或者函数,可以使用type().
#
#Python把每种type类型都定义好了常量，放在types模块里，使用之前，需要先导入：
#能用type()判断的基本类型也可以用isinstance()判断：
#并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是str或者unicode：
#isinstance('a', (str, unicode))
