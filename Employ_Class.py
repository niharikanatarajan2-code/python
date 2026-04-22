class Employee:
    def __init__(self):
        print('Employee created')
    def __del__(self):
            print("Destructor called")
def create_obj():
                print('Making Object')
                obj=Employee()
                print('function end...')
                return obj
print('Calling Create_obj()function...')
obj=create_obj()
print('Program End...')