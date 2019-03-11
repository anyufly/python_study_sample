from datetime import date


class Field:

    @property
    def values(self):
        return self._values


class IntField(Field):

    def __init__(self, db_column=None, min_value=None, max_value=None, positive=None):
        self.db_column = db_column

        if min_value is not None:
            if not isinstance(min_value, int):
                raise ValueError('min_value必须为int类型')
            elif min_value < 0:
                raise ValueError('min_value必须为正数')
        if max_value is not None:
            if not isinstance(max_value, int):
                raise ValueError('max_value')
            elif max_value < 0:
                raise ValueError('max_value必须为正数')
        if min_value is not None and max_value is not None:
            if min_value > max_value:
                min_value, max_value = max_value, min_value
                print('min_value的值大于max_value的值，已将其交换')

        self.min_value = min_value
        self.max_value = max_value
        self.positive = positive
        self._values = {}

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("属性值只能是int类型")
        if self.positive and value < 0:
            raise ValueError("属性值只能为正数")
        if self.min_value is not None and value < self.min_value:
            raise ValueError("传入的值比允许传入的最小值还小")
        if self.max_value is not None and value > self.max_value:
            raise ValueError("传入的值比允许传入的最大值还大")
        self._values[id(instance)] = value

    def __get__(self, instance, owner):
        return self._values[id(instance)]

    def __delete__(self, instance):
        del self._values[id(instance)]


class CharField(Field):

    def __init__(self, db_column=None, max_length=None):
        self.db_column = db_column
        if max_length is None:
            raise ValueError("必须传入max_length")
        elif max_length <= 0:
            raise ValueError("max_length必须大于0")
        self.max_length = max_length
        self._values = {}

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("属性值只能是str类型")
        if len(value) > self.max_length:
            raise ValueError("传入的字符串超出最大长度限制")
        self._values[id(instance)] = value

    def __get__(self, instance, owner):
        return self._values[id(instance)]

    def __delete__(self, instance):
        del self._values[id(instance)]


class DateField(Field):

    def __init__(self, db_column=None):
        self.db_column = db_column
        self._values = {}

    def __set__(self, instance, value):
        if not isinstance(value, date):
            raise ValueError("属性值只能是date类型")
        self._values[id(instance)] = str(value.year) + '-' + str(value.month) + '-' + str(value.day)

    def __get__(self, instance, owner):
        return self._values[id(instance)]

    def __delete__(self, instance):
        del self._values[id(instance)]


class MetaClassSample(type):
    def __new__(mcs, name, base, attrs, **kwargs):
        if name == 'BaseModel':
            return super().__new__(mcs, name, base, attrs, **kwargs)

        db_table = attrs['Meta'].db_table or name.lower()
        fields = {}

        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
        attrs['db_table'] = db_table
        attrs['fields'] = fields
        del attrs['Meta']
        return super().__new__(mcs, name, base, attrs, **kwargs)


class BaseModel(metaclass=MetaClassSample):
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            raise RuntimeError("只能传入keyword参数")

        for key, value in kwargs.items():
            setattr(self, key, value)
        pass

    def save(self):
        cur_id = id(self)
        columns = []
        values = []
        for name, field in self.fields.items():
            for obj_id, value in field.values.items():
                if obj_id == cur_id:
                    if isinstance(value, str):
                        value = "'" + value + "'"
                    values.append(str(value))
            column_name = field.db_column or name.lower()
            columns.append(column_name)

        sql = 'insert into {tb_name}({columns}) values({values}) '.format(
            tb_name=self.db_table, columns=', '.join(["'" + column + "'" for column in columns]), values=', '.join(
                values))
        print(sql)


class Student(BaseModel):
    name = CharField(max_length=100, db_column='student_name')
    height = IntField(positive=True)
    birthday = DateField()

    class Meta:
        db_table = ''

    def __str__(self):
        return 'name：{name}\theight：{height}\tbirthday：{birthday}'.format(
            name=self.name, height=self.height, birthday=self.birthday)


if __name__ == '__main__':
    # student = Student('Jeff', 175 , date(1993, 9, 24))
    student = Student(name='Jeff', height=175, birthday=date(1993, 9, 24))
    student1 = Student(name='Rose', height=185, birthday=date(1991, 9, 24))
    # print(student)
    # print(student1)
    student.save()
    student1.save()
