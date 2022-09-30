class Sort_string():
    
    def __init__(self, input_string):
        self.input_string = input_string

    def sortString(self):
        self.output_string = "".join(sorted(self.input_string))
        return self.output_string

if __name__ == "__main__":
    test1 = Sort_string("aguacate")
    print(test1.sortString())
