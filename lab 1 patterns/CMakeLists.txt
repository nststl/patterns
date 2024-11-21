cmake_minimum_required(VERSION 3.29)
project(lab_1_patterns)

set(CMAKE_CXX_STANDARD 20)

add_executable(lab_1_patterns main.cpp
        bill.h
        bill.cpp
        operator.h
        operator.cpp
        customer.cpp
        customer.h)
