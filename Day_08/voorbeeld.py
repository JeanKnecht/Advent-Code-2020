import argparse

def print1():
    print("hallo 1")

def print2():
    print("hallo 2")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='show arguments passed to main function')
    parser.add_argument('--print',  required=True,
                        help='the path to workspace')

    args = parser.parse_args()
    # print(args.print)
    if args.print == "1":
        print1()
    elif args.print == "2":
        print2()
    else:
        print("value outside range 1-2")

    #odel_schema(workspace=args.workspace, schema=args.schema, dem=args.dem) 