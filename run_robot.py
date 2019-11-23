import os
import robot


def run_robot(root):
    args = {
        'variable': ['ROOTDIR:' + root],
        'variablefile': root + '/' + "env.py",
        'suite': 'robot_tests',
        'noncritical': 'noncritical'
    }
    robot.run(root, **args)


def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    run_robot(root_dir)


if __name__ == '__main__':
    main()
