import parser
import graphs

class Test:
    __var = 'sky'
def menu():

    print('Choice your option\n'
          '1: Start parsing prices\n'
          '2: Build graphs\n'
          'other: end\n')

    choice = input()
    if choice == "1":
        parser.start_pars()
    elif choice == "2":
        graphs.build_graph()
    else:
        pass




if __name__ == "__main__":

    # menu()
    test_list = [[1,2], [3,4], [5,6]]
    print(test_list[-1] > 5)
    pass
