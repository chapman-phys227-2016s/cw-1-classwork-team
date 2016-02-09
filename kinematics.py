#! /usr/bin/env python

"""
File: kinematics.py

Copyright (c) 2016 Taylor Patti

License: MIT

Two different constructions of simple velocity and acceleration approximations are featured
and their test functions included. A comparison test which takes a sample of a million runs
and outputs a comparative efficiency table for the two functions is also included.
"""   

import time

def kinematics1(x_list, t_list, i):
    """Computes approximage v and a for given x-coordinate and t value lists at a given
    index i. Note that for the approximation to work, i must not be the index of either
    the first or last measurement."""
    if len(x_list) != len(t_list):
        print '\n The lists are of different lengths. Please enter commensurate \
        data lists. \n'
        return None
    if (i<=0) or (i>=len(x_list)):
        print '\n Index outside of approximation bounds. Please see docstring. \n'
        return None
    v = (x_list[i + 1] - x_list[i - 1]) / (t_list[i + 1] - t_list[i - 1])
    a = 2*(((x_list[i + 1] - x_list[i]) / (t_list[i + 1] - t_list[i])) - ((x_list[i]-x_list[i - 1]) \
    / (t_list[i] - t_list[i - 1]))) / (t_list[i + 1] - t_list[i - 1])
    return v, a

def kinematics2(x_list, t_list, i):
    """Computes approximage v and a for given x-coordinate and t value lists at a given index i.
    Note that for the approximation to work, i must not be the index of either the first or last
    measurement."""
    if len(x_list) != len(t_list):
        print '\n The lists are of different lengths. Please enter commensurate data lists. \n'
        return None
    if (i<=0) or (i>=len(x_list)):
        print '\n Index outside of approximation bounds. Please see docstring. \n'
        return None
    t_twointerval = t_list[i + 1] - t_list[i - 1]
    t_intervalone = t_list[i + 1] - t_list[i]
    t_intervaltwo = t_list[i] - t_list[i - 1]
    x_twointerval = x_list[i + 1] - x_list[i - 1]
    x_intervalone = x_list[i + 1] - x_list[i]
    x_intervaltwo = x_list[i] - x_list[i - 1]
    v = x_twointerval / t_twointerval
    a = 2 * (x_intervalone / t_intervalone - x_intervaltwo / t_intervaltwo) / t_twointerval
    return v, a

def efficiency_comparison():
    data_tuples = []
    type_list = ['Constant V', 'Constant A']
    t_list = [0, 3, 5, 11]
    x_array = [[t*3 for t in t_list], [3*t + t**2 for t in t_list]]
    for x in range(len(x_array)):
        x_list = [t*3 for t in t_list]
        t_start = time.clock()
        for i in range(1000000):
            kinematics1(x_list, t_list, 1)
        t_middle = time.clock()
        for i in range(1000000):
            kinematics2(x_list, t_list, 1)
        t_end = time.clock()
        data_tuples.append((type_list[x], t_middle - t_start, t_end - t_middle))
    print '\n Efficiency Comparison in Seconds for a Million Runs \n'
    print '\n %18s %23s %19s \n' % ('Run Type', 'kinematics1', 'kinematics2')
    for i in data_tuples:
        print '%20s %20f %20f \n' % (i[0], i[1], i[2])

def test_constant_kinematics1():
    """Tests to ensure that the algorithms preform for constant velocity."""
    V = 2
    t_tests = [0, 0.5, 1.5, 2.2]
    x_tests = [t*V for t in t_tests]
    apt = (abs(kinematics1(x_tests, t_tests, 1)[0] - 2) < 1E-3) and (abs(kinematics1(x_tests, \
    t_tests, 1)[1]) < 1E-3)
    msg = 'Velocity and acceleration unindicative of one directional linear displacement.'
    assert apt, msg

def test_constant_kinematics2():
    """Tests to ensure that the algorithms preform for constant velocity."""
    V = 2
    t_tests = [0, 0.5, 1.5, 2.2]
    x_tests = [t*V for t in t_tests]
    apt = (abs(kinematics2(x_tests, t_tests, 1)[0] - 2) < 1E-3) and (abs(kinematics2(x_tests, \
    t_tests, 1)[1]) < 1E-3)
    msg = 'Velocity and acceleration unindicative of one directional linear displacement.'
    assert apt, msg

def test_acceleration_kinematics1():
    """Tests to ensure that constant acceleration is correctly calculated."""
    a = 2
    t_tests = [0, 0.5, 1.5, 2.2]
    x_tests = [(0.5) * t**2 * a for t in t_tests]
    apt = (abs(kinematics1(x_tests, t_tests, 1)[1] - 2) < 1E-3)
    msg = 'Acceleration not constant value of 2 as it should be.'
    assert apt, msg

def test_acceleration_kinematics2():
    """Tests to ensure that constant acceleration is correctly calculated."""
    a = 2
    t_tests = [0, 0.5, 1.5, 2.2]
    x_tests = [(0.5) * t**2 * a for t in t_tests]
    apt = (abs(kinematics2(x_tests, t_tests, 1)[1] - 2) < 1E-3)
    msg = 'Acceleration not constant value of 2 as it should be.'
    assert apt, msg

