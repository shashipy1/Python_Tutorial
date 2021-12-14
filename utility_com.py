import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'dev':
        return args.x / args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'mod':
        return args.x % args.y
    else:
        return "something went to wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help = "Enter the first number: This is utility for calculation, Please contact to me")

    parser.add_argument('--y', type=float, default=3.0,
                        help = "Enter the second number: This is utility for calculation, Please contact to me")

    parser.add_argument('--o', type=str, default= "add",
                      help = "Enter the second number: This is utility for calculation, Please contact to me for more") # which types operation perform

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))